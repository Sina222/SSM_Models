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

# Represent a packet (after encapsulation) with a list of SID and a payload
class Packet:
    def __init__(self, group, payload):
        self.group = group
        self.payload = payload

    def copy_payload(self):
        return copy.deepcopy(self.payload)

# --------------------------------------------------FUNCTIONS------------------------------------------------------------

# Simulate the process of an incoming packet inside a network. (graph = network)
def ingress_process(graph, ingress_node, pkt, group, print_info=False, print_tree=False, return_tree=False):
    if ingress_node != group[0]:
        print(f"ERROR -> the node {ingress_node} is not allowed to send packets associated to group: ({group[0]}, {group[1]})")
        return
    if print_info:
        print('\n',ingress_node)# source
        print(group)            # group
    packet = encapsulate_pkt(pkt, group)
    entire_tree = process_packet(graph, ingress_node, packet, print_info)
    if print_tree:
        print("\n ENTIRE TREE: ")
        printTree(entire_tree)
        print()
    if return_tree:
        return entire_tree

# Return an encapluled packet with the group on the top and a payload which
# contains the paquet pkt given as argument form a list dst of ddestinations.
def encapsulate_pkt(pkt, group):
    return Packet(group, pkt)

# Simulate the process of a packet inside a network. (graph = network)
def process_packet(graph, curr_node, packet, print_info=False):
    tree = Tree(curr_node, [])
    if 'Sub_table' in graph.nodes[curr_node]: # If curr_node have a Subscription table
        if packet.group in graph.nodes[curr_node]['Sub_table']: # If curr_node is subscribed to the group of the packet
            tree.set_is_rcv(True)
            process_payload(curr_node, packet.payload, print_info)
    if 'F_table' in graph.nodes[curr_node]:    # If curr_node have a Forwarding table
        if packet.group in graph.nodes[curr_node]['F_table']: # If curr_node should forward the group of the packet
            for node in graph.nodes[curr_node]['F_table'][packet.group]:
                new_packet = Packet(packet.group, packet.copy_payload())
                branch = send_packet(graph, node, new_packet, print_info)
                tree.add_branch(branch)
            return tree
        else:
            tree.set_is_leaf(True)
            return tree
    else:
        tree.set_is_leaf(True)
        return tree

# Subscribe the current node to the group.
def subscribe_to(graph, node, group, print_info=True):
    if group[0] not in graph.nodes[node]['table']:
        if print_info:
            print("\n!!! The node'", node,"'cannot subscribe to the group '", group, "' (no path between node and src)!!!")
        return
    if 'Sub_table' in graph.nodes[node]: # If curr_node have already a Subscription table
        if group in graph.nodes[node]['Sub_table']: # If already subscribed to the group
            if print_info:
                print("Node '", node, "' already subscibed to group '", group, "'.")
            return
        graph.nodes[node]['Sub_table'][group] = 'subscription'
    else:
        graph.nodes[node]['Sub_table'] = {group: 'subscription'} # Create a Subscription table
    if node != group[0]: # If curr_node is not the source of the group
        # Transit the subscription to next node
        next_node = graph.nodes[node]['table'][group[0]][1]
        transit_sub(graph, next_node, group, node)

# Transit a subscription to the group (create the tree).
def transit_sub(graph, curr_node, group, n_hop):
    if 'F_table' in graph.nodes[curr_node]: # If curr_node already have a Forwarding table
        if group in graph.nodes[curr_node]['F_table']: # If already know this group
            if n_hop not in graph.nodes[curr_node]['F_table'][group]: # If n_hop is not already in the forwarding list for this group
                graph.nodes[curr_node]['F_table'][group].add(n_hop)
        else:
            graph.nodes[curr_node]['F_table'][group] = {n_hop} # Create the group in the Forwarding table
    else:
        graph.nodes[curr_node]['F_table'] = {group: {n_hop}} # Create Forwarding table

    if curr_node != group[0]: # If curr_node is not the source of the group
        next_node = graph.nodes[curr_node]['table'][group[0]][1]
        transit_sub(graph, next_node, group, curr_node)

# Unsubscribe the current node from the group.
def unsubscribe_from(graph, node, group):
    if 'Sub_table' in graph.nodes[node]: # If node has a Subscription table
        if group in graph.nodes[node]['Sub_table']: # If node is realy subscribed to the group
            graph.nodes[node]['Sub_table'].pop(group)
            if 'F_table' not in graph.nodes[node] or group not in graph.nodes[node]['F_table']:# If node don't have the group in his Forwarding table
                # Transit the unsubscription to next node
                next_node = graph.nodes[node]['table'][group[0]][1]
                transit_unsub(graph, next_node, group, node)
        else:
            print("The node '", node, "' is not subscibed to the group '", group, "' -> cannot unsubscribe.")
    else:
        print("The node '", node, "' do not have a Subcription table.")

# Transit an unsubscription to the group (create the tree).
def transit_unsub(graph, curr_node, group, n_hop):
    if 'F_table' in graph.nodes[curr_node]: # If curr_node have a Forwarding table
        if group in graph.nodes[curr_node]['F_table']: # If know this group
            if n_hop in graph.nodes[curr_node]['F_table'][group]: # If n_hop is in the forwarding list for this group
                graph.nodes[curr_node]['F_table'][group].remove(n_hop)
                if not graph.nodes[curr_node]['F_table'][group]: # if the forwarding list is empty for this group
                    graph.nodes[curr_node]['F_table'].pop(group) # remove the group from the Forwarding table
                    if 'Sub_table' in graph.nodes[curr_node] and group in graph.nodes[curr_node]['Sub_table']:# If the curr_node is subscribed to the group
                        return # Don't transit more
                    else:
                        if curr_node != group[0]: # If curr_node is not the source of the group
                            next_node = graph.nodes[curr_node]['table'][group[0]][1]
                            transit_unsub(graph, next_node, group, curr_node)
                else:
                    return # Don't transit more

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
# -> Subscribe the node to the group=(source, #) with 'subscribe_to(graph, node, group)'

# REMOVE
# -> Unsubscribe the node from the group=(source, #) with 'unsubscribe_from(graph, node, group)'

# FAILURE
# Remove the node from the graph.
# Also perform the IGP and update the tables of all nodes in the graph.
def failure(graph, node, print_info=True):
    if node not in graph.nodes:
        print("The node:", node, "is not in the network!")
        return -1
    # Get the node informations
    info = graph.nodes[node]
    info.pop('table')
    if 'Sub_table' in info:
        info.pop('Sub_table')
    if 'F_table' in info:
        info.pop('F_table')
                               #                        edge(node, 8)       edge(node, 9)       edge(node, 2)
    node_adj = graph.adj[node] # info: node -> adj    e.g  {8: {'weight': 1.0}, 9: {'weight': 1.0}, 2: {'weight': 1.0}}

                               #                        edge(8, node)       edge(8, node)       edge(2, node)
    adj_node = {}              # info:  adj -> node   e.g  {8: {'weight': 1.0}, 9: {'weight': 1.0}, 2: {'weight': 1.0}}
    for adj in node_adj:
        adj_node[adj] = graph.adj[adj][node]
    if len(node_adj) != len(adj_node):
        print("WARNING !!! Error in edges information.")
    node_info = {'node': node, 'node_adj': node_adj, 'adj_node': adj_node, 'info': info}

    # Adjacents nodes see that the node failed and forward information.
    re_sub = {}# List of subscriptions to redo after failure.
    for adj in node_adj:
        trans_down = {}
        trans_up = {}
        if 'F_table' in graph.nodes[adj]:# 'F_table'
            group_to_remove = set()
            sub_to_remove = set()
            for group in graph.nodes[adj]['F_table']:
                if adj != group[0] and graph.nodes[adj]['table'][group[0]][1] == node: # If the group pass througt failed node
                # Failed -> adj
                    if 'Sub_table' in graph.nodes[adj]:# 'F_table AND Sub_table'
                        if group in graph.nodes[adj]['Sub_table']:# If Subscribed to one of this group
                            if node != group[0]:# If the src of the group is not the failed node
                                if adj in re_sub:
                                    re_sub[adj].add(group)
                                else:
                                    re_sub[adj] = {group}
                            sub_to_remove.add(group)# Remove the group from Sub_table
                    for n_hop in graph.nodes[adj]['F_table'][group]:# Regroup which group with which next hop
                        if n_hop in trans_down:
                            trans_down[n_hop].add(group)
                        else:
                            trans_down[n_hop] = {group}
                    group_to_remove.add(group)# Remove the group from F_table
                elif node in graph.nodes[adj]['F_table'][group]:
                # Adj -> failed
                    graph.nodes[adj]['F_table'][group].remove(node)
                    if len(graph.nodes[adj]['F_table'][group]) == 0:
                        group_to_remove.add(group)# Remove the group from F_table
                        if adj != group[0] and ('Sub_table' not in graph.nodes[adj] or group not in graph.nodes[adj]['Sub_table']):
                            # Transit only if not the src of the group AND not Subscribed to the group.
                            up_node = graph.nodes[adj]['table'][group[0]][1]
                            if up_node in trans_up:
                                trans_up[up_node].add(group)
                            else:
                                trans_up[up_node] = {group}
            # Remove the groups from F_table
            for group in group_to_remove:
                graph.nodes[adj]['F_table'].pop(group)
            # Remove the group from Sub_table
            for group in sub_to_remove:
                graph.nodes[adj]['Sub_table'].pop(group)
            # Transit groups failure to all corresponding next hop.
            for n_hop in trans_up:
                transit_fail_up(graph, n_hop, adj, trans_up[n_hop])
            for n_hop in trans_down:
                transit_fail_info(graph, n_hop, node, trans_down[n_hop], re_sub)
        else:
            if 'Sub_table' in graph.nodes[adj]:# 'Sub_table'
                sub_to_remove = set()
                for group in graph.nodes[adj]['Sub_table']:
                    if graph.nodes[adj]['table'][group[0]][1] == node:# If a subscription pass throught failed node
                        sub_to_remove.add(group)
                        if adj in re_sub:
                            re_sub[adj].add(group)
                        else:
                            re_sub[adj] = {group}
                # Remove the groups from F_table
                for group in sub_to_remove:
                    graph.nodes[adj]['Sub_table'].pop(group)
                        
    # Remove the node
    graph.remove_node(node)
    # Update 'table'
    list_nodes = list(graph.nodes)
    for u_node in list_nodes:
        table = nx.single_source_dijkstra_path(graph, u_node) # for weighed graphs
        graph.nodes[u_node]['table'] = table

    # Re-subscribe nodes in re_sub
    for re_sub_node in re_sub:
        for group in re_sub[re_sub_node]:
            if group[0] in graph.nodes[re_sub_node]['table']:# If the src of the group is still reachable.
                subscribe_to(graph, re_sub_node, group, print_info)# Re-subscribe
    return node_info

# Transit the fail node information. Unsubscribe the subscribed node in passing.
# @arg:list_groups: list of all groups that passed throught failed node
# @arg:re_sub: contain all the re-subscription caused by the failure of failed_node.
def transit_fail_info(graph, curr_node, failed_node, list_groups, re_sub):
    trans_down = {}
    for group in list_groups:
        if 'Sub_table' in graph.nodes[curr_node]:
            if group in graph.nodes[curr_node]['Sub_table']:# If Subscribed to one of this group
                if failed_node != group[0]:# If the src of the group is not the failed node
                    if curr_node in re_sub:
                        re_sub[curr_node].add(group)
                    else:
                        re_sub[curr_node] = {group}
                graph.nodes[curr_node]['Sub_table'].pop(group)# Remove the group from Sub_table
        if 'F_table' in graph.nodes[curr_node]:
            if group in graph.nodes[curr_node]['F_table']:# If group in the Forwarding table
                for n_hop in graph.nodes[curr_node]['F_table'][group]:# Regroup which group with which next hop
                    if n_hop in trans_down:
                        trans_down[n_hop].add(group)
                    else:
                        trans_down[n_hop] = {group}
                graph.nodes[curr_node]['F_table'].pop(group)# Remove the group from F_table
    # Transit groups failure to all corresponding next hop.
    for n_hop in trans_down:
        transit_fail_info(graph, n_hop, failed_node, trans_down[n_hop], re_sub)

# Transit the fail information to up nodes.
def transit_fail_up(graph, curr_node, down_node, list_groups):
    trans_up = {}
    if 'F_table' in graph.nodes[curr_node]:
        for group in list_groups:
            if down_node in graph.nodes[curr_node]['F_table'][group]:
                graph.nodes[curr_node]['F_table'][group].remove(down_node)
                if len(graph.nodes[curr_node]['F_table'][group]) == 0:# If no more n_hop for this group
                    graph.nodes[curr_node]['F_table'].pop(group)
                    if curr_node != group[0] and ('Sub_table' not in graph.nodes[curr_node] or group not in graph.nodes[curr_node]['Sub_table']):
                        # Transit only if not the src of the group AND not Subscribed to the group.
                        up_node = graph.nodes[curr_node]['table'][group[0]][1]
                        if up_node in trans_up:
                            trans_up[up_node].add(group)
                        else:
                            trans_up[up_node] = {group}
    # Transit groups failure to all corresponding next hop.
    for n_hop in trans_up:
                transit_fail_up(graph, n_hop, curr_node, trans_up[n_hop])

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
