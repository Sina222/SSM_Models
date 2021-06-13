import random
from numpy import mean, std
from bier_logic import ingress_process, failure, draw_graph, generate_random_dst

#------------------------- GRAPH DEFINITION --------------------------
from ISP1_BIER import network as network_ISP1 # 650 nodes, 2300 edges
from rf1239_BIER import network as network_rf1239 # 315 nodes, 1944 edges
from Cogentco_BIER import network as network_Cogentco # 197 nodes, 490 edges

network_list = [("Cogentco", network_Cogentco), ("rf1239", network_rf1239), ("ISP1", network_ISP1)]
# --------------------------------------------------------------------


#------------------- MEASUREMENT FUNCTION DEFINITION -----------------

# Return the number of node in the tree.
def tree_size(tree):
    size = 1
    if tree.n_branch() > 0:
        for i in range(tree.n_branch()):
            size += tree_size(tree.branches[i])
    return size

# Return the number of non-leaf node in the tree.
def tree_size_noleaf(tree):
    size = 0
    if tree.n_branch() > 0:
        size = 1
        for i in range(tree.n_branch()):
            size += tree_size_noleaf(tree.branches[i])
    return size

# Return the number of leaf in the tree.
def tree_n_leaf(tree):
    n_leaf = 0
    if tree.n_branch() > 0:
        for i in range(tree.n_branch()):
            n_leaf += tree_n_leaf(tree.branches[i])
    else:
        n_leaf = 1
    return n_leaf

# Return the height of the tree.
def tree_height(tree):
    height = 0
    if tree.n_branch() > 0:
        for i in range(tree.n_branch()):
            h = tree_height_AUX(tree.branches[i], 1)
            if h > height:
                height = h
    return height
def tree_height_AUX(tree, height):
    sub_height = height
    next_h = height + 1
    if tree.n_branch() > 0:
        for i in range(tree.n_branch()):
            h = tree_height_AUX(tree.branches[i], next_h)
            if h > sub_height:
                sub_height = h
    return sub_height

# Return the average branching factor.
def tree_av_branch_fact(tree):
    size = tree_size_noleaf(tree)
    count = av_branch_fact_AUX(tree)
    return count/size
def av_branch_fact_AUX(tree):
    count = tree.n_branch()
    if count > 0:
        for i in range(tree.n_branch()):
            count += av_branch_fact_AUX(tree.branches[i])
    return count

# Return the average branching factor 
# (taking the number of non-leaf node in argument).
def tree_av_branch_fact2(tree, n_non_leaf):
    size = n_non_leaf
    count = av_branch_fact_AUX(tree)
    return count/size
# --------------------------------------------------------------------
#--------------------------- MEASUREMENTS ----------------------------
E_NUM = 50

def protocol_measurements(perc_dest, e_num=E_NUM):
    print(
    f"""
    __________________BIER___________________
    Measurement of {len(network_list)} network
    Number of experiment per network = {e_num}."""
    )
    for i in range(len(network_list)):
        measures = {"#node": {}, "#leaf": {}, "height": {}, "Av_B_Fact": {}}
        network = network_list[i][1]
        n_node_val = []
        n_leaf_val = []
        height_val = []
        av_b_f_val = []
        n_dest = round((network.number_of_nodes()/100.0)*perc_dest)
        for j in range(e_num):
            src = random.randint(1, min(128, network.number_of_nodes()-1)) # with limit to 128 ingress/egress nodes
            dst = generate_random_dst(n_dest, 1, min(128, network.number_of_nodes()-1), []) # with limit to 128 ingress/egress nodes
            tree = ingress_process(network, src, "512bytes", dst, return_tree=True)
            n_node = tree_size(tree)
            n_leaf = tree_n_leaf(tree)
            height = tree_height(tree)
            av_b_f = tree_av_branch_fact2(tree, (n_node-n_leaf))
            n_node_val.append(n_node)
            n_leaf_val.append(n_leaf)
            height_val.append(height)
            av_b_f_val.append(av_b_f)
        if len(n_node_val)!= e_num or len(n_leaf_val)!= e_num or len(height_val)!= e_num or len(av_b_f_val)!= e_num:
            print("ERRRRRRRRRROOOOOOOOOOOOR! -> Number of values not right in the mesurement.")
            exit(1)
        measures["#node"]["Mean"] = mean(n_node_val)
        measures["#node"]["Std"] = std(n_node_val)
        measures["#leaf"]["Mean"] = mean(n_leaf_val)
        measures["#leaf"]["Std"] = std(n_leaf_val)
        measures["height"]["Mean"] = mean(height_val)
        measures["height"]["Std"] = std(height_val)
        measures["Av_B_Fact"]["Mean"] = mean(av_b_f_val)
        measures["Av_B_Fact"]["Std"] = std(av_b_f_val)
        print("\n---------", network_list[i][0], f"{n_dest} dest. ({perc_dest}%)----------")
        #for e in measures:
        #    print("   ", e+":\t", measures[e])
        #print()
        print(
            f"""
            \multirow{{2}}{{*}}{{BIER}} &\\vc Average &\\vc {round(measures["#node"]["Mean"], 5)} &\\vc {round(measures["#leaf"]["Mean"], 5)} &\\vc {round(measures["height"]["Mean"], 5)} &\\vc {round(measures["Av_B_Fact"]["Mean"], 5)}\\\ \cline{{3-7}}
                                              &&\\bc Stand. Dev. &\\bc {round(measures["#node"]["Std"], 5)} &\\bc {round(measures["#leaf"]["Std"], 5)} &\\bc {round(measures["height"]["Std"], 5)} &\\bc {round(measures["Av_B_Fact"]["Std"], 5)}\\\ 
            """
        )

#----------------------------------------------------------------
protocol_measurements(2, 200)


