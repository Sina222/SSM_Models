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
])
network.add_edges_from([
(0, 9, {
	'weight': 1,
	'label': '0'
}),
(9, 0, {
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
(2, 4, {
	'weight': 1,
	'label': '6'
}),
(4, 2, {
	'weight': 1,
	'label': '7'
}),
(2, 6, {
	'weight': 1,
	'label': '8'
}),
(6, 2, {
	'weight': 1,
	'label': '9'
}),
(6, 7, {
	'weight': 1,
	'label': '10'
}),
(7, 6, {
	'weight': 1,
	'label': '11'
}),
(7, 8, {
	'weight': 1,
	'label': '12'
}),
(8, 7, {
	'weight': 1,
	'label': '13'
}),
(1, 6, {
	'weight': 7,
	'label': '14'
}),
(6, 1, {
	'weight': 7,
	'label': '15'
}),
(1, 3, {
	'weight': 10,
	'label': '16'
}),
(3, 1, {
	'weight': 10,
	'label': '17'
}),
(4, 6, {
	'weight': 10,
	'label': '18'
}),
(6, 4, {
	'weight': 10,
	'label': '19'
}),
(4, 5, {
	'weight': 1,
	'label': '20'
}),
(5, 4, {
	'weight': 1,
	'label': '21'
}),
(9, 1, {
	'weight': 1,
	'label': '22'
}),
(1, 9, {
	'weight': 1,
	'label': '23'
}),
(0, 8, {
	'weight': 8,
	'label': '24'
}),
(8, 0, {
	'weight': 8,
	'label': '25'
}),
])

list_nodes = list(network.nodes)
for src in list_nodes:
    #table = nx.single_source_shortest_path(network, src)  # for unweighted graphs
    table = nx.single_source_dijkstra_path(network, src) # for weighed graphs
    network.nodes[src]['table'] = table
