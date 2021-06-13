import networkx as nx
import matplotlib.pyplot as plt
import copy
import random

# ----------------------------------------------------CLASS--------------------------------------------------------------
class Tree:
    def __init__(self, addr, branches, is_leaf=False, is_rcv=False):
        self.addr = addr
        self.branches = branches
        self.is_leaf = is_leaf # is_leaf imply is_rcv
        self.is_rcv = is_rcv

    def get_addr(self):
        return self.addr

    def set_is_leaf(self, val):
        self.is_leaf = val

    def set_is_rcv(self, val):
        self.is_rcv = val

    def n_branch(self):
        return len(self.branches)

    def add_branch(self, tree):
        self.branches.append(tree)

# Represent a packet (after encapsulation) with a Bit String and a payload
class Packet:
    def __init__(self, bit_string, payload):
        self.bit_string = bit_string
        self.payload = payload

    def copy_payload(self):
        return copy.deepcopy(self.payload)

# --------------------------------------------------FUNCTIONS------------------------------------------------------------

# Simulate the process of an incoming packet inside a BIER network. (graph = network)
def ingress_process(graph, ingress_node, pkt, dst, print_info=False, print_tree=False, return_tree=False):
    if len(dst)>128:
        print("Too many destination!!!\n This BIER model only support max 128 different destinations")
        exit(1)
    dst.sort() # ordering list
    if print_info:
        print('\n',ingress_node)# source
        print(dst)              # destination
    packet = encapsulate_pkt(graph, ingress_node, pkt, dst, print_info)
    entire_tree = process_packet(graph, ingress_node, packet, print_info)
    if print_tree:
        print("\n ENTIRE TREE: ")
        printTree(entire_tree)
        print()
    if return_tree:
        return entire_tree

# Return an encapluled packet with the BitString on the top and a payload which
# contains the paquet pkt given as argument form a list dst of ddestinations.
def encapsulate_pkt(graph, curr_node, pkt, dst, print_info=False):
    bit_string = 0
    for node in dst:
        node_bit_string = graph.nodes[curr_node]['match_table'][node]
        bit_string |= node_bit_string
    if print_info:
        print("\n BIT STRING: ")
        print(format(bit_string, 'b'))
        print()
    return Packet(bit_string, pkt)

# Simulate the process of a packet inside a BIER network. (graph = network)
# return the entire_tree where packets pass throught.
def process_packet(graph, curr_node, packet, print_info=False):
    tree = Tree(curr_node, [])
    if packet.bit_string == 0:
        print("ERROR!!! -> Empty BitString")
    bit_string = packet.bit_string
    if 'match_table' in graph.nodes[curr_node]: # If curr_node is a Ingress/Egress node
        if bit_string & graph.nodes[curr_node]['match_table'][curr_node] != 0: # If curr_node is a destination,
            tree.set_is_rcv(True)
            process_payload(curr_node, packet.payload, print_info)              # process the payload and
            bit_string ^= graph.nodes[curr_node]['match_table'][curr_node]     # remove curr_node from the destination.
            if bit_string == 0:
                tree.set_is_leaf(True)
                return tree

    bift = graph.nodes[curr_node]['BIFT'] # get the 'bit indexing forwarding table' of curr_node.
    for n_hop in bift:                    # Check all F-BM in the Forwarding table
        new_bit_string = bit_string & bift[n_hop]
        if new_bit_string != 0:           # If destinations pass throught n_hop
            new_packet = Packet(new_bit_string, packet.copy_payload())
            branch = send_packet(graph, n_hop, new_packet, print_info)
            tree.add_branch(branch)
            bit_string &= ~bift[n_hop]    # remove the F-BM of the BitString
            if bit_string == 0:
                return tree
    if print_info:
        print("WARNING !!! -> BitString non empty after BIFT\n----Source cannot reach all destinations-----")
        print("\n BIT STRING LEFT: ")
        print(format(bit_string, 'b'))
        print()
        dest_left = []
        s = format(bit_string, 'b')
        s = list(s)
        s.reverse()
        count = 1
        for e in s:
            n = int(e)
            if n == 1:
                dest_left.append(count)
            count += 1
        print("Unreached destination:", dest_left)
    return tree

# Simulate the sending and the process of a packet
# (which is done instantly in this case). <- Assume a perfect link (not necessarily direct) between the sender and the receiver.
def send_packet(graph, dest_node, packet, print_info=False):
    return process_packet(graph, dest_node, packet, print_info)

# Simulate the processing of the payload after recover it from the paquet.
# (Simple print() statement in this case)
def process_payload(curr_node, payload, print_info=False):
    if print_info:
        print("The node:", curr_node,"receive:", payload)
#----------------------------------------- INTERACTION FUNCTION -----------------------------------------

# ADD
# -> Manualy add the node to the list of destination and run again ingress_process() with the updated list of destinations.
# 
"""# Add the node to the BitString.
def add_to_BS(bit_string, node):
    if node < 1 or 128 < node:
        print("The node:", node, "is not an Egress node!!!")
        return
    bit = 2**(node-1)
    if (bit_string & bit) == 0:# Add it only if not already in the BitString
        bit_string |= bit"""

# REMOVE
# -> Manualy remove the node from the list of destination and run again ingress_process() with the updated list of destinations.
#
"""# -> Remove the node from the BitString.
def remove_from_BS(bit_string, node):
    if node < 1 or 128 < node:
        print("The node:", node, "is not an Egress node!!!")
        return
    bit = 2**(node-1)
    if (bit_string & bit) != 0:# Remove it only if in the BitString
        bit_string &= ~bit"""

# FAILURE
# Remove the node from the graph and return his information (in case of recovery) without the 'table' attribute.
# Also perform the IGP and update the tables of all nodes in the graph.
def failure(graph, node):
    if str(type(node))=="<class 'list'>":
        return failure_list(graph, node)
    if node not in graph.nodes:
        print("The node:", node, "is not in the network!")
        return -1
    # Get the node informations
    info = graph.nodes[node]
    info.pop('table')
    info.pop('BIFT')
    if 1 <= node and node <= 128:
        info.pop('match_table')
                               #                        edge(node, 8)       edge(node, 9)       edge(node, 2)
    node_adj = graph.adj[node] # info: node -> adj    e.g  {8: {'weight': 1.0}, 9: {'weight': 1.0}, 2: {'weight': 1.0}}

                               #                        edge(8, node)       edge(8, node)       edge(2, node)
    adj_node = {}              # info:  adj -> node   e.g  {8: {'weight': 1.0}, 9: {'weight': 1.0}, 2: {'weight': 1.0}}
    for adj in node_adj:
        adj_node[adj] = graph.adj[adj][node]
    if len(node_adj) != len(adj_node):
        print("WARNING !!! Error in edges information.")
    node_info = {'node': node, 'node_adj': node_adj, 'adj_node': adj_node, 'info': info}
    # Remove the node
    graph.remove_node(node)

    # Update 'table'
    list_nodes = list(graph.nodes)
    for u_node in list_nodes:
        table = nx.single_source_dijkstra_path(graph, u_node) # for weighed graphs
        graph.nodes[u_node]['table'] = table
    # Update 'BIFT' and 'match_table'
    match_table = {}
    ingress_egress = []
    for node_e in list_nodes:
        if 1 <= node_e and node_e <= 128:
            ingress_egress.append(node_e)
    for ie_node in ingress_egress:
        match_table[ie_node] = 2**(ie_node-1)
    for _node in list_nodes:
        if _node in ingress_egress: # if ingress/egress
            graph.nodes[_node]['match_table'] = match_table
        bift = {}
        for e in graph.adj[_node]:
            bift[e] = 0
        for e in ingress_egress:
            if e != _node:
                if e in graph.nodes[_node]['table']:
                    n_hop = graph.nodes[_node]['table'][e][1]
                    bift[n_hop] |= match_table[e]
        graph.nodes[_node]['BIFT'] = bift

    return node_info

# Failure simulation for a list of nodes.
def failure_list(graph, nodes):
    nodes_info = []
    for node in nodes:
        if node not in graph.nodes:
            print("The node:", node, "is not in the network!")
            continue
        # Get the node informations
        info = graph.nodes[node]
        info.pop('table')
        info.pop('BIFT')
        if 1 <= node and node <= 128:
            info.pop('match_table')
                                   #                        edge(node, 8)       edge(node, 9)       edge(node, 2)
        node_adj = graph.adj[node] # info: node -> adj    e.g  {8: {'weight': 1.0}, 9: {'weight': 1.0}, 2: {'weight': 1.0}}

                                   #                        edge(8, node)       edge(8, node)       edge(2, node)
        adj_node = {}              # info:  adj -> node   e.g  {8: {'weight': 1.0}, 9: {'weight': 1.0}, 2: {'weight': 1.0}}
        for adj in node_adj:
            adj_node[adj] = graph.adj[adj][node]
        if len(node_adj) != len(adj_node):
            print("WARNING !!! Error in edges information.")
        node_info = {'node': node, 'node_adj': node_adj, 'adj_node': adj_node, 'info': info}
        nodes_info.append(node_info)
        # Remove the node
        graph.remove_node(node)

    # Update 'table'
    list_nodes = list(graph.nodes)
    for u_node in list_nodes:
        table = nx.single_source_dijkstra_path(graph, u_node) # for weighed graphs
        graph.nodes[u_node]['table'] = table
    # Update 'BIFT' and 'match_table'
    match_table = {}
    ingress_egress = []
    for node_e in list_nodes:
        if 1 <= node_e and node_e <= 128:
            ingress_egress.append(node_e)
    for ie_node in ingress_egress:
        match_table[ie_node] = 2**(ie_node-1)
    for _node in list_nodes:
        if _node in ingress_egress: # if ingress/egress
            graph.nodes[_node]['match_table'] = match_table
        bift = {}
        for e in graph.adj[_node]:
            bift[e] = 0
        for e in ingress_egress:
            if e != _node:
                if e in graph.nodes[_node]['table']:
                    n_hop = graph.nodes[_node]['table'][e][1]
                    bift[n_hop] |= match_table[e]
        graph.nodes[_node]['BIFT'] = bift

    return nodes_info

# RECOVER
# Add the node to the graph and give it informations in the node_info.
# Also perform the IGP and update the tables of all nodes in the graph.
def recover(graph, node_info):
    node = node_info['node']
    if node in graph.nodes:
        print("The node:", node, "is already in the network!")
        return -1
    # Add the node to the graph
    graph.add_nodes_from([(node, node_info['info'])])
    # Add the directed edges to the graph
    for adj_node in node_info['node_adj']:
        if adj_node in graph.nodes: # If the adjacent node is in the graph
            graph.add_edges_from([(node, adj_node, node_info['node_adj'][adj_node])]) # add edge from node to adj_node
            graph.add_edges_from([(adj_node, node, node_info['adj_node'][adj_node])]) # add edge from adj_node to node

    # Update 'table'
    list_nodes = list(graph.nodes)
    for u_node in list_nodes:
        table = nx.single_source_dijkstra_path(graph, u_node) # for weighed graphs
        graph.nodes[u_node]['table'] = table
    # Update 'BIFT' and 'match_table'
    match_table = {}
    ingress_egress = []
    for node_e in list_nodes:
        if 1 <= node_e and node_e <= 128:
            ingress_egress.append(node_e)
    for ie_node in ingress_egress:
        match_table[ie_node] = 2**(ie_node-1)
    for _node in list_nodes:
        if _node in ingress_egress: # if ingress/egress
            graph.nodes[_node]['match_table'] = match_table
        bift = {}
        for e in graph.adj[_node]:
            bift[e] = 0
        for e in ingress_egress:
            if e != _node:
                if e in graph.nodes[_node]['table']:
                    n_hop = graph.nodes[_node]['table'][e][1]
                    bift[n_hop] |= match_table[e]
        graph.nodes[_node]['BIFT'] = bift

#--------------------------------------------------------------------------------------------------------

def draw_graph(graph):
        nx.draw(graph, with_labels=True, font_weight='bold')
        plt.show()

# Print the shortest paths between the node n and all the others node of the graph.
# (ASSUME ALL WEIGHT EQUALS)
def print_shortest_paths(graph, n):
        for i in range(1, n):
                print(nx.single_source_shortest_path(graph,i))

# return the longest occurrence from beginning between two lists.
def occur_lists(l1, l2):
        res = []
        l = min (len(l1), len(l2))
        for i in range(l):
                if l1[i] != l2[i]:
                        return res
                res.append(l1[i])
        return res

# From: https://simonhessner.de/python-3-recursively-print-structured-tree-including-hierarchy-markers-using-depth-first-search/
# -> Simon's blog <-
def printTree(root, markerStr="└──", levelMarkers=[]):
    emptyStr = " "*len(markerStr)
    connectionStr = "|" + emptyStr[:-1]

    level = len(levelMarkers)
    mapper = lambda draw: connectionStr if draw else emptyStr
    markers = "".join(map(mapper, levelMarkers[:-1]))
    markers += markerStr if level > 0 else ""
    print(f"{markers}{root.addr}")

    branches = root.branches.copy()
    branches.reverse()
    for i, child in enumerate(branches):
        isLast = i == len(branches) - 1
        printTree(child, markerStr, [*levelMarkers, not isLast])

# generate a random list of n different integer in the interval [min; max] not in _except
def generate_random_dst(n, min, max, _except=[]):
    dst = []
    ex = list(dict.fromkeys(_except))
    if n<=0 or max<min or max-min+1-len(ex)<n:
        print("Bad input in 'generate_random_dst'")
        return dst
    for i in range(n):
        found = False
        while not found:
            r = random.randint(min, max)
            if r not in ex and r not in dst:
                dst.append(r)
                found = True
    return dst

# @arg: tree: represent a Tree
# @arg: v_tree: represent the valid/correct form of the tree with a list like structure '(node, is_rcv, branch)' e.g.:
#       (1, True, [])   or    (1, False, [(2, True, []),(3, True, [(4, True, [])])])
#   
#           (1)         or                       .---(1)---.
#                                                |         |
#                                               (2)       (3)
#                                                          |
#                                                         (4)
# Verify that tree is equals to v_tree
def validate_tree(tree, v_tree):
    if tree.addr != v_tree[0] or tree.is_rcv != v_tree[1] or tree.n_branch() != len(v_tree[2]):
        return False
    if len(v_tree[2])==0:
        return tree.is_leaf
    l = {}
    for i in range(tree.n_branch()):
        l[tree.branches[i].addr] = i
    for i in range(len(v_tree[2])):
        if v_tree[2][i][0] not in l or not validate_tree(tree.branches[l[v_tree[2][i][0]]], v_tree[2][i]):
            return False
        l.pop(v_tree[2][i][0])
    return not l

#------------------------------------------------------------------------------------------------------------------------
