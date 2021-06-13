#Compare the maximum count-end obtained in 100 random experiement with the diameter
# Performed on all networks in the '2016TopologyZooUCL' folder
# 2016TopologyZooUCL files can be found at "https://github.com/svissicchio/Repetita/tree/master/data/2016TopologyZooUCL_unary"
import time
import math
import importlib
import sys
from os import walk
import random
import networkx as nx
from Stateless_MC.Stateless_MC_stat import tree_size, tree_height
from Stateless_MC.Stateless_MC_logic import ingress_process, generate_random_dst
networks = []
for folder in ["2016TopologyZooUCL"]:
    for _, _, files in walk(folder):
        for filename in files:
            if filename[-3:] != ".py":
                continue
            full_module_name = folder+"."+filename[:-3]
            mymodule = importlib.import_module(full_module_name)
            networks.append((mymodule.network, filename[:-3]))

print("Network Max_count_end Diameter")
for net in networks:
    spl = {}
    list_nodes = list(net[0].nodes)
    for src in list_nodes:
        path = nx.single_source_dijkstra_path(net[0], src)
        paths_length = {}
        for e in path:
            paths_length[e] = len(path[e])-1
        spl[src] = paths_length
    e = nx.eccentricity(net[0], sp=spl)
    max_h = 0
    n_dest = round((net[0].number_of_nodes()/100.0)*80)
    for _ in range(100):
        src = random.randint(0, net[0].number_of_nodes()-1)
        dst = generate_random_dst(n_dest, 0, net[0].number_of_nodes()-1)
        tree = ingress_process(net[0], src, "", dst, return_tree=True)
        h = tree_height(tree)
        if h > max_h:
            max_h = h
    net_diameter = nx.diameter(net[0], e)
    print(f"{net[1]} {max_h-1} {net_diameter}")
    if max_h-1 > net_diameter:
        print("property violated")
