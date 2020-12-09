import networkx as nx
import random
import matplotlib.pyplot as plt

def add_edges():
    nodes = list(G.nodes())

    for s in nodes:
        for t in nodes:
            if s != t:
                r = random.random()
                if r <= 0.5:
                    G.add_edge(s,t)
    return G

def assign_point(G):
    nodes = list(G.nodes())
    p = []
    for each in nodes:
        p.append(100)
    return p

def distribute_points(G,points):
    nodes = list(G.nodes())
    new_points = []
    for i in range(len(nodes)):
        new_points.append(0)
    for n in nodes:
        out = list(G.out_edges(n))
        if len(out) == 0:
            new_points[n] += points[n]
        else:
            share=points[n]/len(out)
            for (src,tar) in out:
                new_points[tar] = new_points[tar] + share
    return new_points

def keep_distributing(points,G):
    while(1):
        new_point = distribute_points(G,points)
        print(new_point)
        points = new_point
        stop = input("press # for stop or press anyother key for continue : ")
        if stop == "#":
            break
    return new_point

G = nx.DiGraph()
G.add_nodes_from([i for i in range(1,11)])
G = add_edges()
nx.draw(G,with_labels=True)
plt.show()

points = assign_point(G)
final_points = keep_distributing(points,G)