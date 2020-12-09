import networkx as nx
import matplotlib.pyplot as plt
import random
import operator

g = nx.gnp_random_graph(10,0.5,directed=True)
nx.draw(g,with_labels=True)
plt.show()
x = random.choice([x for x in range(g.number_of_nodes())])
dict_counter = {}
for i in range(g.number_of_nodes()):
  dict_counter[i] = 0
dict_counter[x] += 1
for i in range(100000):
  list_n = list(g.neighbors(x))
  if(len(list_n)==0):
    x = random.choice([x for x in range(g.number_of_nodes())])
    dict_counter[x] += 1
  else:
    x=random.choice(list_n)
    dict_counter[x] += 1
p=nx.pagerank(g)
sorted_p = sorted(p.items(),key=operator.itemgetter(1))
sorted_rw = sorted(dict_counter.items(),key=operator.itemgetter(1))
print(sorted_p)
print(sorted_rw)