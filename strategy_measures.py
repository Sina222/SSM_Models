import random
import time
from Stateless_MC.Stateless_MC_logic import generate_random_dst

from Stateless_MC.Stateless_MC_stat import strategy_measurements, strategy_measurementsV2

#from Stateless_MC.rf1239 import n_nodes as size_rf1239
#from Stateless_MC.Cogentco import n_nodes as size_Cogentco
from Stateless_MC.rf1239_copy import n_nodes as size_rf1239
from Stateless_MC.Cogentco_copy import n_nodes as size_Cogentco
#-------------------------------------------------------------------------------
networks = [("Cogentco", size_Cogentco), ("rf1239", size_rf1239)]
percentages = [2,20,40,60,80]
strategies = ["table", "table_b", "table_h", "table_phys", "table_d"]# "table"-> weight; "table_d"-> delay; "table_h"-> #hop;
                                                                     # "table_b"-> bandwidth;
                                                                     # (only for Cogentco: "table_phys"-> physical distance)
number_of_experiments = 2000
data_file = "strategy_measurement_data.txt"


def strat_measure_in_data_file():
    start_time = time.perf_counter()
    f = open(data_file, 'w')
    f.write("Network %Dest #Dest Strategy #Nodes #Leaves Height Avg_branch_factor\n")
    f.close()
    for network in networks:
        print(f"TIME: {round(time.perf_counter()-start_time, 3)} sec")
        print("______________________________________________________________________________________\n")
        print("     -------- ", network[0], " --------")
        for perc in percentages:
            n_dest = round((network[1]/100.0)*perc)
            exp = []
            for _ in range(number_of_experiments):
                src = random.randint(0, network[1]-1)
                dst = generate_random_dst(n_dest, 0, network[1]-1)
                exp.append((src, dst))
            for strat in strategies:
                if strat == "table_phys" and network[0]!="Cogentco":# only Cogentco support physical distance strategy
                    continue
                strategy_measurementsV2(data_file, exp, network[0], perc, n_dest, strat)
    print(f"TOTAL TIME: {round(time.perf_counter()-start_time, 3)} sec")

def strat_measure_latexTab():
    for network in networks:
        print("______________________________________________________________________________________\n")
        print("     -------- ", network[0], " --------")
        for perc in percentages:
            n_dest = round((network[1]/100.0)*perc)
            n_row = 10 if network[0]=="Cogentco" else 8
            print(f"\multirow{{{n_row}}}{{*}}{{{n_dest} ({perc}\%)}}")
            exp = []
            for _ in range(number_of_experiments):
                src = random.randint(0, network[1]-1)
                dst = generate_random_dst(n_dest, 0, network[1]-1)
                exp.append((src, dst))
            i = 0
            for strat in strategies:
                i += 1
                if strat == "table_phys" and network[0]!="Cogentco":# only Cogentco support physical distance strategy
                    continue
                strategy_measurements(perc, network[0], exp, strat)
                if i < len(strategies):
                    print("\cline{2-7}")
            print("\n\hline")
#----------------------------------------------------------------------------------------------------------------------------------
strat_measure_in_data_file()