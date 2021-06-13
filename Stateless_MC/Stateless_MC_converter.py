import sys

#  example command: $python {THIS_FILE} Cogentco.graph     ->  will create 'Cogentco.py'

graph_file = sys.argv[1]# must be '.graph' type file
if graph_file[-6:] != ".graph":
    print("file not '.graph' type")
    exit(-1)
networkX_file = graph_file.split(".graph")[0]
networkX_file += ".py"

f = open(graph_file)
f_py = open(networkX_file, "w")

f_py.writelines([
    "import networkx as nx\n",
    "from math import sqrt\n",
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
                                                #     |------Mandatory-----|
edge_attr = f.readline().split(" ")             #    ['label', 'src', 'dest', 'weight', 'bw', 'delay\n']
edge_attr[len(edge_attr)-1] = edge_attr[len(edge_attr)-1][:-1]                # (remove the last '\n' char)

count = 0
for line in f:
    attr = line.split(" ")
    if attr[len(attr)-1][-1:] == '\n':
        attr[len(attr)-1] = attr[len(attr)-1][:-1]  #    ['edge_42', '10', '11', '40', '1000000', '803']
    f_py.write(
        "("+attr[1]+", "+attr[2]+", {\n",    #(10, 11, {
    )
    for i in range(3, len(edge_attr)):
        f_py.write("\t'"+edge_attr[i]+"': "+attr[i]+",\n") # 'weight': 40,
                                                           # 'bw': 1000000,
                                                           # 'delay': 803,
    f_py.writelines([
        "\t'"+edge_attr[0]+"': '"+attr[0]+"'\n",          # 'label': 'edge_42'
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
n_nodes = network.number_of_nodes()
list_nodes = list(network.nodes)
for src in list_nodes:
    #table = nx.single_source_shortest_path(network, src)  # for unweighted graphs
    table = nx.single_source_dijkstra_path(network, src) # for weighed graphs
    network.nodes[src]['table'] = table
"""
)

#              Other shortest path strategies:   (WARNING: following functions are not implemented for them 'failure', 'failure_list', 'recover' )
#
#f_py.write(
#"""
## Shortest path on: DELAY
#for src in list_nodes:
#    table_d = nx.single_source_dijkstra_path(network, src, weight='delay')
#    network.nodes[src]['table_d'] = table_d
#
## Shortest path on: #HOP
#for src in list_nodes:
#    table_h = nx.single_source_shortest_path(network, src)
#    network.nodes[src]['table_h'] = table_h
#
## Shortest path on: BANDWIDTH
#for src in list_nodes:
#    table_b = nx.single_source_dijkstra_path(network, src, weight='bw')
#    network.nodes[src]['table_b'] = table_b
#
## Shortest path on: PHYSICAL DISTANCE
#for e in network.edges:
#	# physical distance = sqrt( (x1-x2)**2 + (y1-y2)**2 )
#	#               ((         x1             -          x2            )**2+(            y1           -           y2          )**2)
#	phys_dist = round(sqrt((network.nodes[e[0]]['x']-network.nodes[e[1]]['x'])**2+(network.nodes[e[0]]['y']-network.nodes[e[1]]['y'])**2), 3)
#	network.edges[e]['phys_dist'] = phys_dist
#for src in list_nodes:
#    table_phys = nx.single_source_dijkstra_path(network, src, weight='phys_dist')
#    network.nodes[src]['table_phys'] = table_phys
#"""
#)

f_py.close()
