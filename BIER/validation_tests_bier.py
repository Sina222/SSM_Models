from bier_logic import ingress_process, failure, failure_list, recover, draw_graph, generate_random_dst, validate_tree
from validation_tests_graph1_BIER import network as network_1
from validation_tests_graph2_BIER import network as network_2

#------------------------- GRAPHS DEFINITION --------------------------
graph_test_1 = network_1
graph_test_2 = network_2
# -----------------------------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------TESTS--------------------------------------------------------------
print("BEGIN TESTS VALIDATION BIER MODELISATION...\n")
count_test = 0
n_test = 10
# TEST 1 __________________________________________________________________________________________
#Test ADD and REMOVE
src = 1
dst = [1,9,10]
tree = ingress_process(graph_test_1, src, "test", dst, return_tree=True)
v_tree = (1, True, [(2, False, [(3, False, [(6, False, [(10, True, [])]), (7, False, [(8, False, [(9, True, [])])])])])])
if validate_tree(tree, v_tree):
    print("\tTEST add-remove.1: VALID")
    count_test += 1
else:
    print("\tTEST add-remove.1: FAILURE !")

src = 5
dst = [4,1,11]
tree = ingress_process(graph_test_1, src, "test", dst, return_tree=True)
v_tree = (5, False, [(6, False, [(11, True, [])]), (3, False, [(4, True, []), (2, False, [(1, True, [])])])])
if validate_tree(tree, v_tree):
    print("\tTEST add-remove.2: VALID")
    count_test += 1
else:
    print("\tTEST add-remove.2: FAILURE !")

src = 1
dst = [1,10]
tree = ingress_process(graph_test_1, src, "test", dst, return_tree=True)
v_tree = (1, True, [(2, False, [(3, False, [(6, False, [(10, True, [])])])])])
if validate_tree(tree, v_tree):
    print("\tTEST add-remove.3: VALID")
    count_test += 1
else:
    print("\tTEST add-remove.3: FAILURE !")

src = 5
dst = [6,7,8,9,10]
tree = ingress_process(graph_test_1, src, "test", dst, return_tree=True)
v_tree = (5, False, [(3, False, [(7, True, [(8, True, [(9, True, [])])])]), (6, True, [(10, True, [])])])
if validate_tree(tree, v_tree):
    print("\tTEST add-remove.4: VALID")
    count_test += 1
else:
    print("\tTEST add-remove.4: FAILURE !")

src = 6
dst = [10,11,5,2]
tree = ingress_process(graph_test_1, src, "test", dst, return_tree=True)
v_tree = (6, False, [(10, True, []), (11, True, []), (3, False, [(2, True, [])]), (5, True, [])])
if validate_tree(tree, v_tree):
    print("\tTEST add-remove.5: VALID")
    count_test += 1
else:
    print("\tTEST add-remove.5: FAILURE !")

#Tests FAILURE
print()
failure(graph_test_1, 3) # Failure 3

src = 1
dst = [8,7,10]
tree = ingress_process(graph_test_1, src, "test", dst, return_tree=True)
v_tree = (1, False, [(2, False, [(4, False, [(5, False, [(6, False, [(10, True, [])])])]), (7, True, [])]), (9, False, [(8, True, [])])])
if validate_tree(tree, v_tree):
    print("\tTEST failure.1: VALID")
    count_test += 1
else:
    print("\tTEST failure.1: FAILURE !")

src = 5
dst = [9,7,11,6]
tree = ingress_process(graph_test_1, src, "test", dst, return_tree=True)
v_tree = (5, False, [(6, True, [(11, True, [])]), (4, False, [(2, False, [(7, True, []), (1, False, [(9, True, [])])])])])
if validate_tree(tree, v_tree):
    print("\tTEST failure.2: VALID")
    count_test += 1
else:
    print("\tTEST failure.2: FAILURE !")

failure(graph_test_1, 5) # Failure 5
src = 6
dst = [1,10]
tree = ingress_process(graph_test_1, src, "test", dst, return_tree=True)
v_tree = (6, False, [(10, True, [])])
if validate_tree(tree, v_tree):
    print("\tTEST failure.3: VALID")
    count_test += 1
else:
    print("\tTEST failure.3: FAILURE !")

src = 1
dst = [10,8]
tree = ingress_process(graph_test_1, src, "test", dst, return_tree=True)
v_tree = (1, False, [(9, False, [(8, True, [])])])
if validate_tree(tree, v_tree):
    print("\tTEST failure.4: VALID")
    count_test += 1
else:
    print("\tTEST failure.4: FAILURE !")

# TEST 2 -> routage from src to dest_______________________________________________________________
print()
src = 1
dst = [4]
tree = ingress_process(graph_test_2, src, "test", dst, return_tree=True)
v_tree = (1, False, [(4, True, [])])
if validate_tree(tree, v_tree):
    print("\tTEST -> ROUTAGE FROM SRC TO DEST: VALID")
    count_test += 1
else:
    print("\tTEST -> ROUTAGE FROM SRC TO DEST: FAILURE !")

print("\nTESTS RESULT: Pass", count_test,"tests over", n_test)