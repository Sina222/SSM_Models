import time
import sys

#  example command: $python {THIS_FILE} {topo.ntf}

graph_file = sys.argv[1]# must be '.ntf' type file
if graph_file[-4:] != ".ntf":
    print("file not '.ntf' type")
    exit(-1)
formated_file = graph_file.split("_")[0]
formated_file += ".ntf"

f = open(graph_file)
f_f = open(formated_file, "w")

l = f.readline()                  #NODES 650
f_f.write(l)
n_nodes = int(l.split(" ")[1])
l = f.readline()                  #label
f_f.write(l)
dic = {}
count = 0
for line in f:
    f_f.write(line)
    l = line[:-1]
    _str = str(count)
    dic[l] = _str
    count+=1
    if count >= n_nodes:
        break

l = f.readline()                 #
f_f.write(l)
l = f.readline()                 #EDGES 2300
f_f.write(l)
n_edges = int(l.split(" ")[1])
l = f.readline()                 #src dst weight
f_f.write(l)
count = 0
for line in f:
    attr = line.split(" ")       #['src', 'dst', 'weight', ...]
    src = dic[attr[0]]
    dst = dic[attr[1]]
    f_f.write(src+" "+dst)
    for i in range(2, len(attr)):
        f_f.write(" "+attr[i])
    count+=1
    if count >= n_edges:
        break

f.close()

f_f.close()
