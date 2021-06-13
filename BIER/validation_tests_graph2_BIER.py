import networkx as nx
#network = nx.Graph()   #undirected graph
network = nx.DiGraph() #directed graph
network.add_nodes_from([
(0, {'label': '0',
	  'received_msg': []
}),
(1, {'label': '1',
	  'received_msg': []
}),
(2, {'label': '2',
	  'received_msg': []
}),
(3, {'label': '3',
	  'received_msg': []
}),
(4, {'label': '4',
	  'received_msg': []
}),
])
network.add_edges_from([
(0, 1, {
	'weight': 1,
	'label': '0'
}),
(1, 0, {
	'weight': 1,
	'label': '1'
}),
(1, 2, {
	'weight': 2,
	'label': '2'
}),
(2, 1, {
	'weight': 2,
	'label': '3'
}),
(2, 3, {
	'weight': 2,
	'label': '4'
}),
(3, 2, {
	'weight': 2,
	'label': '5'
}),
(3, 4, {
	'weight': 2,
	'label': '6'
}),
(4, 3, {
	'weight': 2,
	'label': '7'
}),
(1, 4, {
	'weight': 1,
	'label': '8'
}),
(4, 1, {
	'weight': 10,
	'label': '9'
}),
])

list_nodes = list(network.nodes)
for src in list_nodes:
    #table = nx.single_source_shortest_path(network, src)  # for unweighted graphs
    table = nx.single_source_dijkstra_path(network, src) # for weighed graphs
    network.nodes[src]['table'] = table


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
