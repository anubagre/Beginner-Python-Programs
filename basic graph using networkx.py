import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
n=[1,2,3]
e=[(1,2),(2,3),(1,3)]
G.add_nodes_from(n)
G.add_edges_from(e)
nx.draw(G)
plt.show()