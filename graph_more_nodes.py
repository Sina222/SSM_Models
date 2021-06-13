import sys
from os import walk
# 2016TopologyZooUCL     2016RocketFuelUCL
res = []
_max = int(sys.argv[1])
for folder in ["2016TopologyZooUCL/", "2016RocketFuelUCL/"]:
    for _, _, files in walk(folder):
        for filename in files:
            if filename[-6:] != ".graph":
                continue
            f = open(folder+filename)
            n_nodes = int(f.readline().split(" ")[1])
            res.append((n_nodes, filename))
            res.sort()
            res = res[-_max:]
            f.close()

res .reverse()
for e in res:
    print(e)
