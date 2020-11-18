import networkx as nx
import numpy
G = nx.read_edgelist("facebook_combined.txt")

n = list(G.nodes())

spll = []

for u in n:
  for v in n:
    if u != v:
      l = nx.shortest_path_length(G,u,v)
      print("Shortest path between ",u," and ",v," is of lenth ",l)
      spll.append(l)

min_spl = min(spll)
max_spl = max(spll)
avg_spl = numpy.average(spll)

print("Minimum shortest path length : ",min_spl)
print("Maximum shortest path length : ",max_spl)
print("Average shortest path length : ",avg_spl)
