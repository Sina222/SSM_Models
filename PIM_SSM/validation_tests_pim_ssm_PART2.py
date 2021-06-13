from pim_ssm_logic import ingress_process, subscribe_to, unsubscribe_from, failure, draw_graph, generate_random_dst, validate_tree
from validation_tests_graph1_PIM_SSM import network as network_1

#------------------------- GRAPHS DEFINITION --------------------------
graph_test_1 = network_1
# -----------------------------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------TESTS--------------------------------------------------------------
print("BEGIN TESTS VALIDATION Part2 PIM-SSM MODELISATION...\n")
count_test = 0
n_test = 13
# TEST 1 __________________________________________________________________________________________
#Test ADD and REMOVE
for node in [1,10,9]:
    subscribe_to(graph_test_1, node, (0,0), False)# Add [1,10,9] to (0,0)
for node in [4,11,0]:
    subscribe_to(graph_test_1, node, (5,0), False)# Add [4,11,0] to (5,0)

tree = ingress_process(graph_test_1, 0, "test", (0,0), return_tree=True)
v_tree = (0, False, [(1, True, [(2, False, [(3, False, [(7, False, [(8, False, [(9, True, [])])]), (6, False, [(10, True, [])])])])])])
if validate_tree(tree, v_tree):
    print("\tTEST add-remove.1: VALID")
    count_test += 1
else:
    print("\tTEST add-remove.1: FAILURE !")

tree = ingress_process(graph_test_1, 5, "test", (5,0), return_tree=True)
v_tree = (5, False, [(6, False, [(11, True, [])]), (3, False, [(4, True, []), (2, False, [(1, False, [(0, True, [])])])])])
if validate_tree(tree, v_tree):
    print("\tTEST add-remove.2: VALID")
    count_test += 1
else:
    print("\tTEST add-remove.2: FAILURE !")

for node in [0,4,11,3]:
    subscribe_to(graph_test_1, node, (0,0), False)# Add [0,4,11,3] to (0,0)
for node in [5,10,9]:
    subscribe_to(graph_test_1, node, (5,0), False)# Add [5,10,9] to (5,0)

tree = ingress_process(graph_test_1, 0, "test", (0,0), return_tree=True)
v_tree = (0, True, [(1, True, [(2, False, [(3, True, [(4, True, []), (7, False, [(8, False, [(9, True, [])])]), (6, False, [(10, True, []), (11, True, [])])])])])])
if validate_tree(tree, v_tree):
    print("\tTEST add-remove.3: VALID")
    count_test += 1
else:
    print("\tTEST add-remove.3: FAILURE !")

tree = ingress_process(graph_test_1, 5, "test", (5,0), return_tree=True)
v_tree = (5, True, [(6, False, [(10, True, []), (11, True, [])]), (3, False, [(2, False, [(1, False, [(0, True, [])])]), (4, True, []), (7, False, [(8, False, [(9, True, [])])])])])
if validate_tree(tree, v_tree):
    print("\tTEST add-remove.4: VALID")
    count_test += 1
else:
    print("\tTEST add-remove.4: FAILURE !")

for node in [1,10,9]:
    unsubscribe_from(graph_test_1, node, (0,0))# Remove [1,10,9] from (0,0)

tree = ingress_process(graph_test_1, 0, "test", (0,0), return_tree=True)
v_tree = (0, True, [(1, False, [(2, False, [(3, True, [(4, True, []), (6, False, [(11, True, [])])])])])])
if validate_tree(tree, v_tree):
    print("\tTEST add-remove.5: VALID")
    count_test += 1
else:
    print("\tTEST add-remove.5: FAILURE !")

for node in [1,10,9]:
    subscribe_to(graph_test_1, node, (0,1), False)# Add [1,10,9] to (1,0)

tree = ingress_process(graph_test_1, 0, "test", (0,1), return_tree=True)
v_tree = (0, False, [(1, True, [(2, False, [(3, False, [(7, False, [(8, False, [(9, True, [])])]), (6, False, [(10, True, [])])])])])])
if validate_tree(tree, v_tree):
    print("\tTEST add-remove.6: VALID")
    count_test += 1
else:
    print("\tTEST add-remove.6: FAILURE !")

for node in [5,10,4,11,0]:
    unsubscribe_from(graph_test_1, node, (5,0))# Remove [5,10,4,11,0] from (5,0)
for node in [1,9]:
    unsubscribe_from(graph_test_1, node, (0,1))# Remove [1,9] from (0,1)

tree = ingress_process(graph_test_1, 5, "test", (5,0), return_tree=True)
v_tree = (5, False, [(3, False, [(7, False, [(8, False, [(9, True, [])])])])])
if validate_tree(tree, v_tree):
    print("\tTEST add-remove.7: VALID")
    count_test += 1
else:
    print("\tTEST add-remove.7: FAILURE !")

tree = ingress_process(graph_test_1, 0, "test", (0,1), return_tree=True)
v_tree = (0, False, [(1, False, [(2, False, [(3, False, [(6, False, [(10, True, [])])])])])])
if validate_tree(tree, v_tree):
    print("\tTEST add-remove.8: VALID")
    count_test += 1
else:
    print("\tTEST add-remove.8: FAILURE !")

#Tests FAILURE
print()
subscribe_to(graph_test_1, 6, (0,1), False)# Add [6] to (0,1)

failure(graph_test_1, 3, False) # Failure 3

tree = ingress_process(graph_test_1, 0, "test", (0,0), return_tree=True)
v_tree = (0, True, [(1, False, [(2, False, [(4, True, [(5, False, [(6, False, [(11, True, [])])])])])])])
if validate_tree(tree, v_tree):
    print("\tTEST failure.1: VALID")
    count_test += 1
else:
    print("\tTEST failure.1: FAILURE !")

tree = ingress_process(graph_test_1, 0, "test", (0,1), return_tree=True)
v_tree = (0, False, [(1, False, [(2, False, [(4, False, [(5, False, [(6, True, [(10, True, [])])])])])])])
if validate_tree(tree, v_tree):
    print("\tTEST failure.2: VALID")
    count_test += 1
else:
    print("\tTEST failure.2: FAILURE !")

tree = ingress_process(graph_test_1, 5, "test", (5,0), return_tree=True)
v_tree = (5, False, [(4, False, [(2, False, [(1, False, [(9, True, [])])])])])
if validate_tree(tree, v_tree):
    print("\tTEST failure.3: VALID")
    count_test += 1
else:
    print("\tTEST failure.3: FAILURE !")

for node in [8,7]:
    subscribe_to(graph_test_1, node, (0,1))# Add [8,7] to (0,1)

tree = ingress_process(graph_test_1, 0, "test", (0,1), return_tree=True)
v_tree = (0, False, [(1, False, [(9, False, [(8, True, [])]), (2, False, [(7, True, []), (4, False, [(5, False, [(6, True, [(10, True, [])])])])])])])
if validate_tree(tree, v_tree):
    print("\tTEST failure.4: VALID")
    count_test += 1
else:
    print("\tTEST failure.4: FAILURE !")

failure(graph_test_1, 5, False) # Failure 5
# Check Forwarding table of 4
print("\nCheck Forwarding table of 4:", "OK! (empty)" if not graph_test_1.nodes[4]['F_table'] else "Not OK! (not empty)")
#print(graph_test_1.nodes[4]['F_table'])
#

tree = ingress_process(graph_test_1, 0, "test", (0,1), return_tree=True)
v_tree = (0, False, [(1, False,[(9, False, [(8, True, [])]), (2, False, [(7, True, [])])])])
if validate_tree(tree, v_tree):
    print("\tTEST failure.5: VALID")
    count_test += 1
else:
    print("\tTEST failure.5: FAILURE !")

print("\nTESTS RESULT: Pass", count_test,"tests over", n_test)