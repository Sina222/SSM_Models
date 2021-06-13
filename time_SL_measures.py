import random
import time
from copy import deepcopy
import networkx as nx
from numpy import mean, std

from Stateless_MC.Stateless_MC_logic import generate_random_dst, encapsulate_pkt, failure_list, create_worst_network

from Stateless_MC.ISP1 import network as network_ISP1
from Stateless_MC.rf1239 import network as network_rf1239
from Stateless_MC.Cogentco import network as network_Cogentco

networks = [("ISP1", network_ISP1), ("rf1239", network_rf1239), ("Cogentco", network_Cogentco)]
nbr_exp_SL = 500
nbr_exp_table = 50
nbr_exp_failure = 100
percentages = [2,30,60]
percentages_SL = [2,20,40,60,80]
percentages_failure = [1,10,20,30]
data_file = "time_SL_measurement_data.txt"
data_file_failure = "failure_measurement_data.txt"


def time_compute_seg_list_latex():
    for network in networks:
        print("______________________________________________________________________________________\n")
        print("     -------- ", network[0], " --------")
        for perc in percentages:
            n_dest = round((network[1].number_of_nodes()/100.0)*perc)
            val = []
            for _ in range(nbr_exp_SL):
                src = random.randint(0, network[1].number_of_nodes()-1)
                dst = generate_random_dst(n_dest, 0, network[1].number_of_nodes()-1)
                _, times = encapsulate_pkt(network[1], src, "", dst)
                times *= 1000
                val.append(times)
            avg = round(mean(val), 5)
            st_dev = round(std(val), 5)
            print(
f"""\multirow{{2}}{{*}}{{{n_dest} ({perc}\%)}}
&\\vc Average &\\vc {avg} \\\ \cline{{2-3}}
&\\bc Stand. Dev. &\\bc {st_dev} \\\ 
\hline"""
            )

def time_SL_measure_in_data_file():
    f = open(data_file, 'w')
    f.write(f"Network %Dest #Dest Time_SL(msec)\n")
    for network in networks:
        print("______________________________________________________________________________________\n")
        print("     -------- ", network[0], " --------")
        for perc in percentages_SL:
            n_dest = round((network[1].number_of_nodes()/100.0)*perc)
            worst_network, worst_dst = create_worst_network(n_dest)
            for _ in range(nbr_exp_SL):
                # Compute current network case times
                src = random.randint(0, network[1].number_of_nodes()-1)
                dst = generate_random_dst(n_dest, 0, network[1].number_of_nodes()-1)
                _, times = encapsulate_pkt(network[1], src, "payload", dst)
                times *= 1000
                f.write(f"{network[0]} {perc} {n_dest} {times}\n")
                # Compute worst case time for the same number of destination
                _, worst_time = encapsulate_pkt(worst_network, 0, "payload", worst_dst)
                worst_time *= 1000
                f.write(f"Worst_case X {n_dest} {worst_time}\n")
    f.close()

def time_compute_all_tables():
    for network in networks:
        print("______________________________________________________________________________________\n")
        print("     -------- ", network[0], " --------")
        val = []
        for _ in range(nbr_exp_table):
            startTime = time.perf_counter() # start time
            list_nodes = list(network[1].nodes)
            for src in list_nodes:
                table = nx.single_source_dijkstra_path(network[1], src) # for weighed graphs
                network[1].nodes[src]['table'] = table
            endTime = time.perf_counter()   #   end time
            times = endTime - startTime
            val.append(times)
        avg = round(mean(val), 5)
        st_dev = round(std(val), 5)
        print(f"""Average =\t{avg}\nStand.Dev =\t{st_dev}""")

def time_failures_latex():
    for i in range(len(networks)):
        print("______________________________________________________________________________________\n")
        print("     -------- ", networks[i][0], " --------")
        for perc_f in percentages_failure:
            val_t_rt = []
            n_fail = round((networks[i][1].number_of_nodes()/100.0)*perc_f)
            count = 0
            for _ in range(nbr_exp_failure):
                net_copy = deepcopy(networks[i][1])
                count += 1
                print(f"\t{count}")
                # Failures
                list_fail = generate_random_dst(n_fail, 0, net_copy.number_of_nodes()-1)
                _, time_rt = failure_list(net_copy, list_fail)
                val_t_rt.append(time_rt)
            avg_rt = round(mean(val_t_rt), 5)
            st_dev_rt = round(std(val_t_rt), 5)
            print(
f"""\multirow{{2}}{{*}}{{{n_fail} ({perc_f}\%)}}
&\\vc Average &\\vc {avg_rt} \\\ \cline{{2-3}}
&\\bc Stand. Dev. &\\bc {st_dev_rt} \\\ 
\hline"""
            )

def failure_measure_in_data_file():
    f = open(data_file_failure, 'w')
    s = "Failure"
    f.write(f"Network %{s} #Failures Time_comp_RT(sec)\n")
    for i in range(len(networks)):
        print("______________________________________________________________________________________\n")
        print("     -------- ", networks[i][0], " --------")
        for perc_f in percentages_failure:
            n_fail = round((networks[i][1].number_of_nodes()/100.0)*perc_f)
            for _ in range(nbr_exp_failure):
                net_copy = deepcopy(networks[i][1])
                # Failures
                list_fail = generate_random_dst(n_fail, 0, net_copy.number_of_nodes()-1)
                _, time_rt = failure_list(net_copy, list_fail)
                f.write(f"{networks[i][0]} {perc_f} {n_fail} {time_rt}\n")
    f.close()
#-----------------------------------------------------------------------------------------------------------


# Warning: ONLY MAKES ONE MEASUREMENT AT A TIME.

#time_compute_seg_list_latex()

#time_compute_all_tables()

#time_failures_latex()

#failure_measure_in_data_file()

time_SL_measure_in_data_file()


