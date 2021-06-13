import time
import sys

#  example command: $python {THIS_FILE} {topo.ntf}

graph_file = sys.argv[1]# must be '.ntf' type file
if graph_file[-4:] != ".ntf":
    print("file not '.ntf' type")
    exit(-1)
networkX_file = graph_file.split(".ntf")[0]
networkX_file += "_BIER.py"

f = open(graph_file)
f_py = open(networkX_file, "w")

f_py.writelines([
    "import networkx as nx\n",
    "#network = nx.Graph()   #undirected graph\n",
    "network = nx.DiGraph() #directed graph\n",
    "network.add_nodes_from([\n"
])

# ADD NODES:
                                                # ex:
n_nodes = int(f.readline().split(" ")[1])       #    197
                                                #  |-Mandatory-|
node_attr = f.readline().split(" ")             #    ['label',  'x', 'y\n']
node_attr[len(node_attr)-1] = node_attr[len(node_attr)-1][:-1]                # (remove the last '\n' char)
count = 0
for line in f:
    attr = line.split(" ")
    attr[len(attr)-1] = attr[len(attr)-1][:-1]  #    ['42_Copenhagen', '12.56553', '55.67594']
    node_number = str(count)                    #    '42'
    node_name = attr[0]                         #    '42_Copenhagen'
    f_py.write(
        "("+node_number+", {'"+node_attr[0]+"': '"+node_name+"',\n", # (42, {'label': 'Copenhagen',
    )
    for i in range(1, len(node_attr)):
        f_py.write("\t  '"+node_attr[i]+"': "+attr[i]+",\n")         # 'x': 12.56553,
                                                                     # 'y': 55.67594
    f_py.writelines([
        "\t  'received_msg': []\n",                                 # 'received_msg': []
        "}),\n"                                                      # }),
    ])
    count+=1
    if count >= n_nodes:
        break
f_py.write(
    "])\n"
)
f.readline()

f_py.write(
    "network.add_edges_from([\n"
)
# ADD EDGES:
                                                # ex:
n_edges = int(f.readline().split(" ")[1])       #    490
                                                #    |--Mandatory--|
edge_attr = f.readline().split(" ")             #    ['src', 'dest', 'weight']
edge_attr[len(edge_attr)-1] = edge_attr[len(edge_attr)-1][:-1]                # (remove the last '\n' char)

count = 0
for line in f:
    label = str(count)
    attr = line.split(" ")
    if attr[len(attr)-1][-1:] == '\n':
        attr[len(attr)-1] = attr[len(attr)-1][:-1]  #    ['bttss', 'sttd', '40']
    f_py.write(
        "("+attr[0]+", "+attr[1]+", {\n",    #(10, 11, {
    )
    for i in range(2, len(edge_attr)):
        f_py.write("\t'"+edge_attr[i]+"': "+attr[i]+",\n") # 'weight': 40,
    f_py.writelines([
        "\t'label': '"+label+"'\n",          # 'label': '14'
        "}),\n"                                            # }),
    ])
    count+=1
    if count >= n_edges:
        break
f_py.write(
    "])\n"
)
f.close()

# COMPUTE TABLE (FOR EACH NODE)
#   nx.single_source_shortest_path(G, source) <- Shortest path algorithms for unweighted graphs
#   nx.single_source_dijkstra_path(G, source) <- Shortest path algorithms for weighed graphs.
f_py.write(
"""
list_nodes = list(network.nodes)
for src in list_nodes:
    #table = nx.single_source_shortest_path(network, src)  # for unweighted graphs
    table = nx.single_source_dijkstra_path(network, src) # for weighed graphs
    network.nodes[src]['table'] = table
"""
)

# COMPUTE TABLE 'match_table'(FOR INGRESS/EGRESS NODES)---------->{'node': BitString}
#               'BIFT'       (FOR FORWARDING NODES == all nodes)->{'n_hop': F-BM}      [F-BM = Forwarding-Bit Mask]
#                                                                                      [BIFT = Bit Indexing Forwarding Table]
# Use format() to print the binary representation of BitString and/or F-BM
# Ex: print(format(2**4, 'b'))           =>            "10000"
#     print(format(16, '#b'))            =>          "0b10000"   with '0b' prefix
#     print(format(16, 'b').zfill(16))   => "0000000000010000"   show 16bits
f_py.write(
"""

match_table = {}
count = 0
ingress_egress = list_nodes[1:129]
for node in ingress_egress:
    match_table[node] = 2**count
    count += 1

for node in list_nodes:
    if node in ingress_egress: # if ingress/egress
        network.nodes[node]['match_table'] = match_table
    
    bift = {}
    for e in network.adj[node]:
        bift[e] = 0
    for e in ingress_egress:
        if e != node:
            n_hop = network.nodes[node]['table'][e][1]
            bift[n_hop] |= match_table[e]
    network.nodes[node]['BIFT'] = bift
"""
)

f_py.close()
