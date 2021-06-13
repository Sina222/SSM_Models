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
(5, {'label': '5',
	  'received_msg': []
}),
(6, {'label': '6',
	  'received_msg': []
}),
(7, {'label': '7',
	  'received_msg': []
}),
(8, {'label': '8',
	  'received_msg': []
}),
(9, {'label': '9',
	  'received_msg': []
}),
(10, {'label': '10',
	  'received_msg': []
}),
(11, {'label': '11',
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
	'weight': 1,
	'label': '2'
}),
(2, 1, {
	'weight': 1,
	'label': '3'
}),
(2, 3, {
	'weight': 1,
	'label': '4'
}),
(3, 2, {
	'weight': 1,
	'label': '5'
}),
(3, 6, {
	'weight': 1,
	'label': '6'
}),
(6, 3, {
	'weight': 1,
	'label': '7'
}),
(6, 10, {
	'weight': 1,
	'label': '8'
}),
(10, 6, {
	'weight': 1,
	'label': '9'
}),
(6, 11, {
	'weight': 1,
	'label': '10'
}),
(11, 6, {
	'weight': 1,
	'label': '11'
}),
(5, 6, {
	'weight': 1,
	'label': '12'
}),
(6, 5, {
	'weight': 1,
	'label': '13'
}),
(3, 5, {
	'weight': 1,
	'label': '14'
}),
(5, 3, {
	'weight': 1,
	'label': '15'
}),
(4, 5, {
	'weight': 5,
	'label': '16'
}),
(5, 4, {
	'weight': 5,
	'label': '17'
}),
(3, 4, {
	'weight': 1,
	'label': '18'
}),
(4, 3, {
	'weight': 1,
	'label': '19'
}),
(2, 4, {
	'weight': 5,
	'label': '20'
}),
(4, 2, {
	'weight': 5,
	'label': '21'
}),
(3, 7, {
	'weight': 1,
	'label': '22'
}),
(7, 3, {
	'weight': 1,
	'label': '23'
}),
(7, 8, {
	'weight': 1,
	'label': '24'
}),
(8, 7, {
	'weight': 1,
	'label': '25'
}),
(8, 9, {
	'weight': 1,
	'label': '26'
}),
(9, 8, {
	'weight': 1,
	'label': '27'
}),
(2, 7, {
	'weight': 8,
	'label': '28'
}),
(7, 2, {
	'weight': 8,
	'label': '29'
}),
(1, 9, {
	'weight': 8,
	'label': '30'
}),
(9, 1, {
	'weight': 8,
	'label': '31'
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
