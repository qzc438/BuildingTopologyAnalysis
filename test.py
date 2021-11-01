import networkx as nx
import statistics

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_node(4)
G.add_edge(3, 4)
G.add_edge(4, 5)

print("number of nodes", G.number_of_nodes())
print("number of edges", G.number_of_edges())

# Mean
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

# Degree centrality -- mean and stdev
dc = nx.degree_centrality(G)
degrees = []
for k, v in dc.items():
    print(k,v)
    degrees.append(v)
print("DEGREE CENTRALITY")
print("=================")
print("The mean degree centrality is {}, with stdev {}".format("%e" % mean(degrees),
                                                               "%e" % statistics.stdev(degrees)))
# print("The maximum node is {}, with value {}".format(max(dc, key=dc.get), max(dc.values())))
# print("The minimum node is {}, with value {}".format(min(dc, key=dc.get), min(dc.values())))
# histogram(dc)
print()

dl = nx.diameter(G)
print("diameter", dl)
dc = nx.radius(G)
print("radius", dc)

diameters = []
components = (G.subgraph(c).copy() for c in nx.connected_components(G))
for c in components:
    print("diameter in each subgraph", nx.diameter(c))
    diameters.append(nx.diameter(c))
print("max diameter in the graph", max(diameters))


