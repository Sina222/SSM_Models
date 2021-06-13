import random
import time
from Stateless_MC.Stateless_MC_logic import generate_random_dst

from Stateless_MC.Stateless_MC_stat import protocol_measurements as m_Stateless, protocol_measurementsV2 as m_StatelessV2
from PIM_SSM.pim_ssm_stat import protocol_measurements as m_pim_ssm, protocol_measurementsV2 as m_pim_ssmV2
from BIER.bier_stat_unlimited import protocol_measurements as m_bier, protocol_measurementsV2 as m_bierV2

from Stateless_MC.ISP1 import n_nodes as size_ISP1
from Stateless_MC.rf1239 import n_nodes as size_rf1239
from Stateless_MC.Cogentco import n_nodes as size_Cogentco

#-------------------------------------------------------------------------------
networks = [("ISP1", size_ISP1), ("rf1239", size_rf1239), ("Cogentco", size_Cogentco)]
percentages = [2, 30, 60]
percentagesV2 = [2,20,40,60,80]
protocols = ["s", "b", "p"] # s->Stateless; p->PIM_SSM; b->BIER
number_of_experiments = 1000

data_file = "protocol_measurement_data.txt"

def protocol_measure_in_data_file():
    start_time = time.perf_counter()
    f = open(data_file, 'w')
    f.write("Network %Dest #Dest Protocol #Nodes #Leaves Height AvgBranchFact\n")
    f.close()
    count_pim = 0
    for network in networks:
        print(f"TIME: {round(time.perf_counter()-start_time, 3)} sec")
        print("______________________________________________________________________________________\n")
        print("     -------- ", network[0], " --------")
        for perc in percentagesV2:
            n_dest = round((network[1]/100.0)*perc)
            exp = []
            for _ in range(number_of_experiments):
                src = random.randint(0, network[1]-1)
                dst = generate_random_dst(n_dest, 0, network[1]-1)
                exp.append((src, dst))
            for protocol in protocols:
                if protocol == "s":
                    m_StatelessV2(data_file, exp, network[0], perc, n_dest)
                elif protocol == "p":
                    count_pim = m_pim_ssmV2(count_pim, data_file, exp, network[0], perc, n_dest)
                elif protocol == "b":
                    m_bierV2(data_file, exp, network[0], perc, n_dest)
                else:
                    print("unknow protocol")
                    exit(1)
    print(f"TOTAL TIME: {round(time.perf_counter()-start_time, 3)} sec")

def protocol_measure_latexTab():
    count_pim = 0
    for network in networks:
        print("______________________________________________________________________________________\n")
        print("     -------- ", network[0], " --------")
        for perc in percentages:
            n_dest = round((network[1]/100.0)*perc)
            exp = []
            for _ in range(number_of_experiments):
                src = random.randint(0, network[1]-1)
                dst = generate_random_dst(n_dest, 0, network[1]-1)
                exp.append((src, dst))
            for protocol in protocols:
                if protocol == "s":
                    m_Stateless(perc, network[0], exp)
                elif protocol == "p":
                    count_pim = m_pim_ssm(count_pim, network[0], exp)
                elif protocol == "b":
                    m_bier(network[0], exp)
                else:
                    print("unknow protocol")
                    exit(1)
#----------------------------------------------------------------------------------------------------------------------------------
protocol_measure_in_data_file()
