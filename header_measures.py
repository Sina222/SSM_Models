import random
import math
import time
import networkx as nx
from numpy import mean, std, sum, max

from Stateless_MC.Stateless_MC_logic import ingress_process, generate_random_dst, Log_file, ingress_process_SRH_limit, ingress_process_SRHs_limit, ingress_process_groupNear, ingress_process_SRHs_limit_groupNear

from Stateless_MC.ISP1 import network as network_ISP1
from Stateless_MC.rf1239 import network as network_rf1239
from Stateless_MC.Cogentco import network as network_Cogentco

networks = [("ISP1", network_ISP1), ("rf1239", network_rf1239), ("Cogentco", network_Cogentco)]
percentages = list(range(1, 81))
percentagesV2 = [2,20,40,60,80]
number_experiments = 500
data_file = "header_measurement_data.txt"
data_file_min = "header_measurement_min_data.txt"
minimisation = ["No_minimisation", "rm_prefix", "id_minimisation"]
data_stategy_file = "header_strategy_measurement_data.txt"
strategies = ["normal","SRH_limit","SRHs_limit","groupNear","Near_SRHsLimit"]
SRH_limit = 6      # limit to 6 destinations
SRHs_limit = 6     # limit to 6 destinations
#group_nearby_dist # Required max distance to be part of the same group ~ round_up(network_diameter/5)

def compute_val(file_name):
    f = open(file_name)
    exps_val = []
    exps_first = []
    val = []
    for line in f:
        l = line.split(" ")
        if l[0]=='@':
            f_val = val[0]
            average = mean(val)
            exps_val.append(average)# Append first size list SID
            exps_first.append(f_val)# Append average size in this experiment
            val = []
        else:
            v = int(l[0])
            val.append(v)
    if len(exps_val) != len(exps_first):
        print("ERROR")
    av_exp = round(mean(exps_val), 5)
    std_exp = round(std(exps_val), 5)
    av_first = round(mean(exps_first), 5)
    std_first = round(std(exps_first), 5)
    return {'avg_first': av_first, 'std_first': std_first, 'avg': av_exp, 'std': std_exp}

def compute_valV2(file_name):
    f = open(file_name)
    exps_val = []
    exps_first = []
    val = []
    for line in f:
        l = line.split(" ")
        if l[0]=='@':
            f_val = val[0]
            val = val[1:]
            average = mean(val)
            exps_val.append(average)# Append first size list SID
            exps_first.append(f_val)# Append average size in this experiment
            val = []
        else:
            v = int(l[0])
            val.append(v)
    if len(exps_val)!= 1 or len(exps_first)!=1:
        print("ERROR")
    return {'1st_header': exps_first[0], 'Avg_header': exps_val[0]}

def compute_valV2_strategy(file_name):
    # Return sizes in bytes ! (-> header_size = [nbr_segments*16 + 8])
    flag_first = True
    f = open(file_name)
    exps_use = []
    exps_fval = []
    for line in f:
        l = line.split(" ")
        if l[0]=='@':
            flag_first = True
        else:
            v = int(l[0]) # v represents the number of segments used in a header.
            if flag_first:
                flag_first = False
                exps_fval.append(v) # Append first size list SID
            else:
                exps_use.append(v)  # Append size list SID
    used_bytes = sum(exps_use)*16+8*len(exps_use)
    avg_header = mean(exps_use)*16+8
    avg_1st_header = mean(exps_fval)*16+8
    max_1st = int(max(exps_fval))*16+8
    return {'Max_1st_header': max_1st, 'Avg_1st_header': avg_1st_header, 'Avg_header': avg_header, 'Used_bytes': used_bytes}

def format_plot_data():
    for network in networks:
        _file = "plot/"+network[0]+"_Header_Size.data"
        f = open(_file, 'w')
        f.write("# 1[number of dest] 2[avg first header size (byte)] 3[std first header size] 4[avg header size (byte)] 5[std header size]\n")
        for perc in percentages:
            open(Log_file, 'w').close()   #clean log file
            n_dest = round((network[1].number_of_nodes()/100.0)*perc)
            for _ in range(number_experiments):
                src = random.randint(0, network[1].number_of_nodes()-1)
                dst = generate_random_dst(n_dest, 0, network[1].number_of_nodes()-1)
                ingress_process(network[1], src, "", dst, log=True)
            values = compute_val(Log_file)
            # segments are encoded on 16 bytes (1 segment == 16 bytes) + 8bytes header flags
            f.write(f"{n_dest} {values['avg_first']*16+8} {values['std_first']*16} {values['avg']*16+8} {values['std']*16}\n")
            print(f"Finish with {perc}%")
        f.close()

def header_measure_in_data_file():
    f = open(data_file, 'w')
    f.write("Network %Dest #Dest 1st_header Avg_header\n")
    for network in networks:
        for perc in percentagesV2:
            n_dest = round((network[1].number_of_nodes()/100.0)*perc)
            for _ in range(number_experiments):
                open(Log_file, 'w').close()   #clean log file
                src = random.randint(0, network[1].number_of_nodes()-1)
                dst = generate_random_dst(n_dest, 0, network[1].number_of_nodes()-1)
                ingress_process(network[1], src, "payload", dst, log=True)
                values = compute_valV2(Log_file)
                # segments are encoded on 16 bytes (1 segment == 16 bytes) + 8bytes header flags
                f.write(f"{network[0]} {perc} {n_dest} {values['1st_header']*16+8} {values['Avg_header']*16+8}\n")
    f.close()

def header_min_measure_in_data_file():
    f = open(data_file_min, 'w')
    f.write("Network %Dest #Dest Min_strat 1st_header Avg_header\n")
    for network in networks:
        #using a prefix /48
        if network[0]=="ISP1":
            val_min_prefix = 6.75 # 1 segment = 6.75 bytes
            val_min_id = 2        # 1 segment = 2 bytes
        elif network[0]=="rf1239":
            val_min_prefix = 6.75
            val_min_id = 1.875
        elif network[0]=="Cogentco":
            val_min_prefix = 6.875
            val_min_id = 1.875
        else:
            print("unknown network")
            val_min_id = 0
            val_min_prefix = 0
        for perc in percentagesV2:
            n_dest = round((network[1].number_of_nodes()/100.0)*perc)
            for _ in range(number_experiments):
                open(Log_file, 'w').close()   #clean log file
                src = random.randint(0, network[1].number_of_nodes()-1)
                dst = generate_random_dst(n_dest, 0, network[1].number_of_nodes()-1)
                ingress_process(network[1], src, "payload", dst, log=True)
                values = compute_valV2(Log_file)
                for min_strat in minimisation:
                    if min_strat == "No_minimisation":
                        f.write(f"{network[0]} {perc} {n_dest} {min_strat} {values['1st_header']*16+8} {values['Avg_header']*16+8}\n")
                    elif min_strat == "rm_prefix":
                        f.write(f"{network[0]} {perc} {n_dest} {min_strat} {values['1st_header']*val_min_prefix+8} {values['Avg_header']*val_min_prefix+8}\n")
                    elif min_strat == "id_minimisation":
                        f.write(f"{network[0]} {perc} {n_dest} {min_strat} {values['1st_header']*val_min_id+8} {values['Avg_header']*val_min_id+8}\n")
                    else:
                        print("unknown minimisation strategy")
    f.close()

def header_measure_strategies_in_data_file():
    f = open(data_stategy_file, 'w')
    f.write("Network %Dest #Dest Strategy Max_1st_header Avg_1st_header Avg_header Used_bytes\n")
    for network in networks:
        if "groupNear" in strategies:
            near_limit = math.ceil(nx.diameter(network[1])/5)
            distances = dict(nx.all_pairs_shortest_path_length(network[1], cutoff=near_limit))  # distance per hop
        for perc in percentagesV2:
            n_dest = round((network[1].number_of_nodes()/100.0)*perc)
            for _ in range(number_experiments):
                src = random.randint(0, network[1].number_of_nodes()-1)
                dst = generate_random_dst(n_dest, 0, network[1].number_of_nodes()-1)
                for strat in strategies:
                    open(Log_file, 'w').close() # clean log file
                    if strat == "normal": # no strategy->one multicast tree
                        ingress_process(network[1], src, "payload", dst, log=True)
                    elif strat == "SRH_limit": # one limited multicast tree + unicast forwarding
                        ingress_process_SRH_limit(network[1], src, "payload", dst, log=True, limit=SRH_limit)
                    elif strat == "SRHs_limit": # limited multicast trees
                        ingress_process_SRHs_limit(network[1], src, "payload", dst, log=True, limit=SRHs_limit)
                    elif strat == "groupNear": # group near destinations in a multicast tree
                        ingress_process_groupNear(network[1], src, "payload", dst, distances, log=True)
                    elif strat == "Near_SRHsLimit": # group near destinations in a limited multicast tree
                        ingress_process_SRHs_limit_groupNear(network[1], src, "payload", dst, distances, log=True, limit=SRHs_limit)
                    else:
                        print(f"Unknown strategy: '{strat}' .")
                    values = compute_valV2_strategy(Log_file)
                    f.write(f"{network[0]} {perc} {n_dest} {strat} {values['Max_1st_header']} {values['Avg_1st_header']} {values['Avg_header']} {values['Used_bytes']}\n")
    f.close()

#-------------------------------------------------------------------------
#header_measure_in_data_file()
#header_measure_strategies_in_data_file()
header_min_measure_in_data_file()
