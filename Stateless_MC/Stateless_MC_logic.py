import networkx as nx
import matplotlib.pyplot as plt
import copy
import random
import time
import math

Log_file = "SID_log.txt"
# ----------------------------------------------------CLASS--------------------------------------------------------------
class Tree:
    def __init__(self, addr, branches, is_leaf=False, is_rcv=False):
        self.addr = addr
        self.branches = branches
        self.is_leaf = is_leaf # is_leaf imply is_rcv
        self.is_rcv = is_rcv
        self.count_end = -1

    def branches(self):
        return self.branches

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

# Represent a Segment id
class SID:
    # LOC:FUNC:ARG       LOC->...->114bits   FUNC->6bits      ARG->...->8bits
    #                          addr          = 0 => Leaf     => end_count
    #                          addr          = 1 => Tree     => 0
    #                          addr          = 2 => Tree_rcv => 0
    def __init__(self, loc, func, arg):
        self.loc = loc
        self.func = func
        self.arg = arg

    def __str__(self):
        res = ""
        if self.func == 0:
            res = str(self.loc)+"-end: "+str(self.arg)         # '2-end: 4'
        elif self.func == 1:
            res = "T"+str(self.loc)+"(b="+str(self.arg)+")"    # 'T2(b=3)'
        else:
            res = "T"+str(self.loc)+"_rcv(b="+str(self.arg)+")"# 'T2_rcv(b=3)'
        return res

# Represent a packet (after encapsulation) with a list of SID and a payload
class Packet:
    def __init__(self, list_SID, payload):
        self.list_SID = list_SID
        self.payload = payload

    def copy_payload(self):
        return copy.deepcopy(self.payload)

# --------------------------------------------------FUNCTIONS------------------------------------------------------------

# Simulate the process of an incoming packet inside a network. (graph = network)
def ingress_process(graph, ingress_node, pkt, dst, print_info=False, print_tree=False, return_tree=False, print_time=False, table='table', log=False):
    dst.sort() # ordering to create each time the same tree for the same destinations.
               # (ordering don't "change" the builded tree, but can swap sub-trees on the same
               # level on the rendering and thus change the Segment List (don't increase it))
    if print_info:
        print('\n',ingress_node)# source
        print(dst)              # destination
    packet, _ = encapsulate_pkt(graph, ingress_node, pkt, dst, print_info, print_time, table=table)
    entire_tree = process_packet(graph, ingress_node, packet, print_info, table=table, log=log)

    # Log list SID
    if log:
        log_SID = open(Log_file, "a")
        log_SID.write(f"""@ END INGRESS PROCESS\n""")
        log_SID.close()

    if print_tree:
        print("\n ENTIRE TREE: ")
        printTree(entire_tree)
        print()
    if return_tree:
        return entire_tree

# !!!! ONLY FOR: TIME building Segment List measurment !!!!
def ingress_process_SL(graph, ingress_node, pkt, dst):
    packet, times_SL = encapsulate_pkt(graph, ingress_node, pkt, dst)
    entire_tree = process_packet(graph, ingress_node, packet)
    return entire_tree, times_SL

# Return an encapluled packet with the list of SID on the top and a payload which
# contains the paquet pkt given as argument form a list dst of destinations.
def encapsulate_pkt(graph, curr_node, pkt, dst, print_info=False, print_time=False, table='table'):
    startTime = time.perf_counter() # start time
    tree = build_tree(graph, curr_node, dst, print_info, table=table)
    #t = time.perf_counter()#KKK
    #print(f"Time build_tree: \t{(t-startTime)*1000}")#KKK
    place_count_end(tree, 0)
    #t2 = time.perf_counter()#KKK
    #print(f"Time place_counts: \t{(t2-t)*1000}")#KKK
    segments = []
    build_segments(segments, tree)
    endTime = time.perf_counter()   #   end time
    #print(f"Time build_segment: \t{(endTime-t2)*1000}")#KKK
    times = endTime - startTime
    if print_time:
        max_count_end = tree_max_count_end(tree)
        print(f"\nMax COUNT-END = {max_count_end}\n")
        print("\n TIME TO BUILD SEGMENTS LIST: ")
        print("* Execution time:\t", str(times))
        print()
    if print_info:
        print("\n BUILDED TREE: ")
        printTree(tree)
        print()
    if print_info:
        print(" BUILDED LIST OF SID: ")
        print_list_SID(segments)
        print("----------------------------------------------\n")
    return Packet(segments, pkt), times

# return a pointer to a tree structure representing the tree-multicast
# path to the list of destination dst from the source src
# (ignoring non-branch-point and non-destination nodes).
# (Assume dst has no duplicate)
def build_tree(graph, src, dst, print_info=False, table='table'):
    # dst = list(dict.fromkeys(dest)) # <- remove duplicates from the list dst (MUST CHANGE THE NAME OF THE ARG 'dst' TO 'dest' !!!)
    tree = Tree(src, [])
    if src in dst:
        tree.set_is_rcv(True)
        dst.remove(src)
    if not dst:                # if the list dst is empty
        tree.set_is_leaf(True)
        return tree
    index = set()
    packets = {}
    list_next_hop = set()
    # Regarde sa table, regroupe tt les même next-hop des dest en paquets.
    # (obtient des listes des destinations à envoyer sur le même next-hop)
    for d in dst:
        if d not in graph.nodes[src][table]:
            if print_info:
                print("\nWARNING!!! The source'", src,"'cannot reach the destination '", d, "' (no path between)!!!")
            continue
        n_hop = graph.nodes[src][table][d][1]
        if n_hop not in list_next_hop:
            list_next_hop.add(n_hop)
            packets[n_hop] = [d]
        else:
            packets[n_hop].append(d)
    # Pour chaque packet: Regarde le +long unicast possible avant duplication
    #                     du packet (embranchement)
    for hop in packets:
        tab = {}
        # Compute the unicast path for this hop
        unicast_path = graph.nodes[src][table][packets[hop][0]]
        for e in packets[hop]:
            tab[e] = graph.nodes[src][table][e].copy()
            unicast_path = occur_lists(unicast_path, graph.nodes[src][table][e])
        unicast_dest = unicast_path[len(unicast_path)-1]
        arrange_table(tab, len(unicast_path))

        # build the branch and add it to the tree
        branch = build_tree_AUX(unicast_dest, tab, packets[hop])
        tree.add_branch(branch)
    return tree

# Auxiliar function, used in order to build the tree with informations in the table of the SOURCE node only.
def build_tree_AUX(curr_node, tab, dst):
    tree = Tree(curr_node, [])
    if curr_node in dst:
        tree.set_is_rcv(True)
        dst.remove(curr_node)
    if not dst:                # if the list dst is empty
        tree.set_is_leaf(True)
        return tree
    index = set()
    packets = {}
    list_next_hop = set()
    # Regarde sa table, regroupe tt les même next-hop des dest en paquets.
    # (obtient des listes des destinations à envoyer sur le même next-hop)
    for d in dst:
        n_hop = tab[d][1]
        if n_hop not in list_next_hop:
            list_next_hop.add(n_hop)
            packets[n_hop] = [d]
        else:
            packets[n_hop].append(d)
    # Pour chaque packet: Regarde le +long unicast possible avant duplication
    #                     du packet (embranchement)
    for hop in packets:
        new_table = {}
        # Compute the unicast path for this hop
        unicast_path = tab[packets[hop][0]]
        for e in packets[hop]:
            new_table[e] = tab[e].copy()
            unicast_path = occur_lists(unicast_path, tab[e])
        unicast_dest = unicast_path[len(unicast_path)-1]
        arrange_table(new_table, len(unicast_path))

        # build the branch and add it to the tree
        branch = build_tree_AUX(unicast_dest, new_table, packets[hop])
        tree.add_branch(branch)
    return tree

# For each key of the dictionnary 'table':
# If the lenght of the list in the dictionnary 'table' is <= than length remove this key of the dictionnary,
# otherwise, remove the length-1 first element of the list in the dictionnary 'table'
def arrange_table(table, length):
    keys = list(table)
    for key in keys:
        if len(table[key])<=length:
            table.pop(key)
        else:
            table[key] = table[key][length-1:]

# Place the counter end at all leaf of the tree.
def place_count_end(tree, level):
    if tree.is_leaf:
        if tree.count_end == -1:
            tree.count_end = level
    else:
        if tree.n_branch() < 1:
            print("ERROR in 'place_count_end()': expected Tree, receive Leaf")
        for i in range(tree.n_branch()):
            transit_count_end(tree.branches[i], level)
        for i in range(tree.n_branch()):
            place_count_end(tree.branches[i], level+1)

def transit_count_end(tree, level):
    if tree.is_leaf:
        if tree.count_end == -1:
            tree.count_end = level
            return
    else:
        if tree.n_branch() < 1:
            print("ERROR in 'transit_count_end()': expected Tree, receive Leaf")
        transit_count_end(tree.branches[tree.n_branch()-1], level)

# Add segments to the list_SID according to the current tree (and count_end if is_leaf).
def build_segments(list_SID, tree):
    # Append the corresponding type of SID
    if tree.is_leaf:
        list_SID.append(SID(tree.get_addr(), 0, tree.count_end))  # append a Leaf-segment
        return                                                    # nothing left after a leaf (no remaining branch)
    if tree.is_rcv:
        list_SID.append(SID(tree.get_addr(), 2, tree.n_branch())) # append a Tree-segment which is a destination.
    else:
        list_SID.append(SID(tree.get_addr(), 1, tree.n_branch())) # append a Tree-segment.
    branches = tree.branches
    # Append the SID of the n branches (recursively from left to right)
    for i in range(len(branches)):
        build_segments(list_SID, branches[i])

# Simulate the process of a packet inside a network. (graph = network)
# return the entire_tree where packets pass throught.
def process_packet(graph, curr_node, packet, print_info=False, table='table', log=False):
    #print_list_SID('\n', packet.list_SID) <- Used to see changes of the list of SID throught the network.
    # VERIFICATION--------
    if len(packet.list_SID) == 0:
        print("ERROR!!! -> Empty list of SID")
    # END VERIFICATION----

    # Log list SID
    if log:
        log_SID = open(Log_file, "a")
        log_SID.write(f"""{len(packet.list_SID)}\n""")
        log_SID.close()

    if curr_node != packet.list_SID[0].loc:
        # Forward to the next hop according to the SID
        branch = process_packet(graph, graph.nodes[curr_node][table][packet.list_SID[0].loc][1], packet, print_info, log=log)
        tree = Tree(curr_node, [])
        tree.add_branch(branch)
        return tree
    if packet.list_SID[0].func == 0:  # Leaf
        if len(packet.list_SID) != 1:
            print("WARNING! -> Bad list of SID, there should be only 1 left! Current length:", len(packet.list_SID))
            print("<---")
            print_list_SID(packet.list_SID)
            print("--->")
        # The current node is a destination. 
        # It decapsulates the packet and process the payload.
        process_payload(curr_node, packet.payload, print_info)
        return Tree(curr_node, [], True, True)
    elif packet.list_SID[0].func == 1:# Tree
        # Branch point.
        return process_packet_Tree(graph, curr_node, packet, print_info=print_info, table=table, log=log)
    elif packet.list_SID[0].func == 2:# Tree_rcv
        # Branch point and destination.
        process_payload(curr_node, packet.payload, print_info)
        return process_packet_Tree(graph, curr_node, packet, True, print_info=print_info, table=table, log=log)
    else:
        print("WARNING! -> Unknown function in the SID")

# Simulate the process of a branch point (a Tree).
# In a list of SID, a SID with FUNC==0 and ARG==0 (leaf with the count-end equals to 0) represents
# an end-point of a nested list of SID inside the current list of SID. And it is used for the new paquet cloned from the current.
def process_packet_Tree(graph, curr_node, packet, is_rvc=False, print_info=False, table='table', log=False):
    tree = Tree(curr_node, [], is_rcv=True) if is_rvc else Tree(curr_node, [])
    segments = packet.list_SID
    if segments[len(segments)-1].arg != 0:
        print("ERROR!!! -> Bad list of SID, should finish with an leaf with 0 as ARG. Expected: 0, Receive:", segments[len(segments)-1].arg)
    list_SID = []
    # Process the list of SID
    for i in range(1, len(segments)):
        if segments[i].func == 0 and segments[i].arg == 0: # end-point, FUNC==0 and ARG==0 (leaf with the count-end equals to 0)
            list_SID.append(segments[i])
            # Create the new paquet with the new list of SID
            new_packet = Packet(list_SID, packet.copy_payload())
            # Forward to the next hop according to the SID
            branch = send_packet(graph, graph.nodes[curr_node][table][list_SID[0].loc][1], new_packet, print_info, log=log)
            tree.add_branch(branch)
            list_SID = [] # reset the list
        else:
            if segments[i].func == 0:
                # Decrement the count-end of the leaf SID
                segments[i].arg -= 1
            list_SID.append(segments[i])
    return tree

# Simulate the sending and the process of a packet
# (which is done instantly in this case). <- Assume a perfect link between the sender and the receiver.
def send_packet(graph, dest_node, packet, print_info=False, log=False):
    return process_packet(graph, dest_node, packet, print_info, log=log)

# Simulate the processing of the payload after recover it from the paquet.
# (Simple print() statement in this case)
def process_payload(curr_node, payload, print_info=False):
    if print_info:
        print("The node:", curr_node,"receive:", payload)

#----------------------------------------- INTERACTION FUNCTION -----------------------------------------
# To only obtain the list of SID, use:
#   'packet, _ = encapsulate_pkt(graph, curr_node, pkt, dst)'
#   'list_SID = packet.list_SID'
# and there you can process the same list SID as long as you want with:
#   'process_packet(graph, ingress_node, Packet(list_SID, [YOUR PAYLOAD HERE]))'


# ADD
# -> Manualy   add  the node  to  the list of destination and run again ingress_process() with the updated list of destinations.

# REMOVE
# -> Manualy remove the node from the list of destination and run again ingress_process() with the updated list of destinations.

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

    # Update tables
    list_nodes = list(graph.nodes)
    for u_node in list_nodes:
        table = nx.single_source_dijkstra_path(graph, u_node) # for weighed graphs
        graph.nodes[u_node]['table'] = table

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

    # Update tables
    startTime = time.perf_counter() # start time
    list_nodes = list(graph.nodes)
    for u_node in list_nodes:
        table = nx.single_source_dijkstra_path(graph, u_node) # for weighed graphs
        graph.nodes[u_node]['table'] = table
    endTime = time.perf_counter()   #   end time

    return nodes_info, endTime-startTime

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

    # Update tables
    list_nodes = list(graph.nodes)
    for u_node in list_nodes:
        table = nx.single_source_dijkstra_path(graph, u_node) # for weighed graphs
        graph.nodes[u_node]['table'] = table

#--------------------------------------------------------------------------------------------------------

# Print the list_SID (with the first element on the bottom)
def print_list_SID(list_SID):
    for i in range(len(list_SID)-1, -1, -1):
        print(list_SID[i])

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

# Return the maximum count_end number of a leaf in the tree
def tree_max_count_end(tree):
    res = -1
    if tree.n_branch() > 0:
        for i in range(tree.n_branch()):
            r = tree_max_count_end(tree.branches[i])
            if r > res:
                res = r
    else:
        if tree.count_end > res:
            res = tree.count_end
    return res
#-------------------------------------------------------------------------------------------------------------------------------------------
# Return the number of node in the tree.
def tree_size(tree):
    size = 1
    if tree.n_branch() > 0:
        for i in range(tree.n_branch()):
            size += tree_size(tree.branches[i])
    return size

# Return the worst network for Segment List computation
# for a number of destination. Return also a list with the id of the destination.
# Example for 8 destinations (destinations on leafs):
#
#   __(0)___
#  |        |
# (8)    __(1)___
#       |        |
#      (9)    __(2)___
#            |        |
#           (10)   __(3)___
#                 |        |
#                (11)   __(4)___
#                      |        |
#                     (12)   __(5)___
#                           |        |
#                          (13)   __(6)___
#                                |        |
#                               (14)     (7)
#
#
def create_worst_network(n_dest):
    network = nx.DiGraph()
    for i in range(0, n_dest):
        network.add_node(i)
    c = i+1
    for i in range(c, c+n_dest-1):
        network.add_node(i)
    for i in range(0, n_dest-1):
        j = i+1
        network.add_edge(i, j)
        network.add_edge(j, i)
        k = i+n_dest
        network.add_edge(i, k)
        network.add_edge(k, i)
    first = n_dest-1
    list_dest = list(range(first, first+n_dest))
    # Compute routing table
    list_nodes = list(network.nodes)
    for src in list_nodes:
        table = nx.single_source_shortest_path(network, src)  # for unweighted graphs
        network.nodes[src]['table'] = table
    return network, list_dest

# ---------------------------------------------------------- With Sending Strategy -----------------------------------------------------------------------------------

# Simulate the process of an incoming packet inside a network. (graph = network)
# Apply the SRH limit strategy
def ingress_process_SRH_limit(graph, ingress_node, pkt, dst, print_info=False, print_time=False, table='table', log=False, limit=5):
    dst.sort() # ordering to create each time the same tree for the same destinations.
               # (ordering don't "change" the builded tree, but can swap sub-trees on the same
               # level on the rendering and thus change the Segment List (don't increase it))
    if print_info:
        print('\n',ingress_node)# source
        print(dst)              # destination
    # Make a multicast tree limited to a number of destinations (in order to not create a large SRH)
    mc_dest = dst[:limit]
    packet, _ = encapsulate_pkt(graph, ingress_node, pkt, mc_dest, print_info, print_time, table=table)
    entire_tree = process_packet(graph, ingress_node, packet, print_info, table=table, log=log)
    # Log list SID
    if log:
        log_SID = open(Log_file, "a")
        log_SID.write(f"""@ END INGRESS PROCESS\n""")
        log_SID.close()
    # Unicast forwarding if destinations remain in the destination list
    if len(dst) > limit:
        u_dest = dst[limit:]
        for d in u_dest:
            unicast_dest = [d]
            packet, _ = encapsulate_pkt(graph, ingress_node, pkt, unicast_dest, print_info, print_time, table=table)
            entire_tree = process_packet(graph, ingress_node, packet, print_info, table=table, log=log)
            # Log list SID
            if log:
                log_SID = open(Log_file, "a")
                log_SID.write(f"""@ END INGRESS PROCESS\n""")
                log_SID.close()

# Simulate the process of an incoming packet inside a network. (graph = network)
# Apply the SRHs limit strategy (multiple multicast tree)
def ingress_process_SRHs_limit(graph, ingress_node, pkt, dst, print_info=False, print_time=False, table='table', log=False, limit=5):
    dst.sort() # ordering to create each time the same tree for the same destinations.
               # (ordering don't "change" the builded tree, but can swap sub-trees on the same
               # level on the rendering and thus change the Segment List (don't increase it))
    if print_info:
        print('\n',ingress_node)# source
        print(dst)              # destination

    i = 0
    j = limit if limit <= len(dst) else len(dst)
    while j <= len(dst):
        # Make a multicast tree limited to a number of destinations (in order to not create a large SRH)
        mc_dest = dst[i:j]
        packet, _ = encapsulate_pkt(graph, ingress_node, pkt, mc_dest, print_info, print_time, table=table)
        entire_tree = process_packet(graph, ingress_node, packet, print_info, table=table, log=log)
        # Log list SID
        if log:
            log_SID = open(Log_file, "a")
            log_SID.write(f"""@ END INGRESS PROCESS\n""")
            log_SID.close()
        
        if (j+1) > len(dst):
            break
        i = j
        j = j+limit if (j+limit) <= len(dst) else len(dst)

# Simulate the process of an incoming packet inside a network. (graph = network)
# Apply the group near destinations strategy
def ingress_process_groupNear(graph, ingress_node, pkt, dst, distances, print_info=False, print_time=False, table='table', log=False):
    dst.sort() # ordering to create each time the same tree for the same destinations.
               # (ordering don't "change" the builded tree, but can swap sub-trees on the same
               # level on the rendering and thus change the Segment List (don't increase it))
    if print_info:
        print('\n',ingress_node)# source
        print(dst)              # destination
# Managed in 'header_measures'
    #near_limit = math.ceil(nx.diameter(graph)/10)
    #distances = dict(nx.all_pairs_dijkstra_path_length(graph, cutoff=near_limit)) #<- (if we want to use weight) [NOT USABLE HERE]
    #distances = dict(nx.all_pairs_shortest_path_length(graph, cutoff=near_limit))  # distance per hop
#
    group_dst = group_near_dst(graph, dst, distances)
    for near_dest in group_dst:
        # Make a multicast tree limited to a number of destinations (in order to not create a large SRH)
        packet, _ = encapsulate_pkt(graph, ingress_node, pkt, near_dest, print_info, print_time, table=table)
        entire_tree = process_packet(graph, ingress_node, packet, print_info, table=table, log=log)
        # Log list SID
        if log:
            log_SID = open(Log_file, "a")
            log_SID.write(f"""@ END INGRESS PROCESS\n""")
            log_SID.close()

def group_near_dst(graph, dst, distances):
    groups = []
    for d in dst:
        placed = False
        for i in range(len(groups)):
            for e in groups[i]:
                if d in distances[e]:
                    groups[i].append(d)
                    placed = True
                    break
            if placed:
                break
        if not placed:
            groups.append([d])
    return groups

# Simulate the process of an incoming packet inside a network. (graph = network)
# Apply the group near destinations strategy
def ingress_process_SRHs_limit_groupNear(graph, ingress_node, pkt, dst, distances, print_info=False, print_time=False, table='table', log=False, limit=5):
    dst.sort() # ordering to create each time the same tree for the same destinations.
               # (ordering don't "change" the builded tree, but can swap sub-trees on the same
               # level on the rendering and thus change the Segment List (don't increase it))
    if print_info:
        print('\n',ingress_node)# source
        print(dst)              # destination
# Managed in 'header_measures'
    #near_limit = math.ceil(nx.diameter(graph)/10)
    #distances = dict(nx.all_pairs_dijkstra_path_length(graph, cutoff=near_limit)) #<- (if we want to use weight) [NOT USABLE HERE]
    #distances = dict(nx.all_pairs_shortest_path_length(graph, cutoff=near_limit))  # distance per hop
#
    group_dst = group_near_dst_limit(graph, dst, distances, limit)
    for near_dest in group_dst:
        # Make a multicast tree limited to a number of destinations (in order to not create a large SRH)
        packet, _ = encapsulate_pkt(graph, ingress_node, pkt, near_dest, print_info, print_time, table=table)
        entire_tree = process_packet(graph, ingress_node, packet, print_info, table=table, log=log)
        # Log list SID
        if log:
            log_SID = open(Log_file, "a")
            log_SID.write(f"""@ END INGRESS PROCESS\n""")
            log_SID.close()

def group_near_dst_limit(graph, dst, distances, limit):
    groups = []
    for d in dst:
        placed = False
        for i in range(len(groups)):
            if len(groups[i]) < limit:
                for e in groups[i]:
                    if d in distances[e]:
                        groups[i].append(d)
                        placed = True
                        break
                if placed:
                    break
        if not placed:
            groups.append([d])
    return groups