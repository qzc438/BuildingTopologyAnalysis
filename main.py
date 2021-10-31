from platform import python_version
print("python version: ", python_version())
print()

import os

from rdflib import Graph as RDFGraph
from rdflib.extras.external_graph_libs import rdflib_to_networkx_graph
import networkx as nx
import matplotlib.pyplot as plt

from tabulate import tabulate

# Mean
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

brick_model_names = []
brick_mean_degrees = []
brick_mean_diameters = []

haystack_model_names = []
haystack_mean_degrees = []
haystack_mean_diameters = []

path = "."
files = os.listdir(path)
for folders in files:
    if os.path.isdir(folders) and folders == "Brick":
        for file in os.listdir(path+"/"+folders+"/"):
            if file.endswith(".ttl"):

                print("FILE NAME")
                print("============")
                print(file)
                print()
                brick_model_names.append(file)

                print("LOAD ADN TRANSFER")
                print("============")
                rg = RDFGraph()
                # print("path: ", path + "/" + folders + "/" + file)
                rg.parse(path+"/"+folders+"/"+file, format='turtle')
                print("rdflib Graph loaded successfully with {} triples".format(len(rg)))
                G = rdflib_to_networkx_graph(rg)
                print("networkx Graph loaded successfully with length {}".format(len(G)))
                print()

                # Network size
                print("NETWORK SIZE")
                print("============")
                print("The network has {} nodes and {} edges".format(G.number_of_nodes(), G.number_of_edges()))
                print()

                # degree refers to number of properties
                print("DEGREE")
                print("============")
                degrees = []
                for n in G:
                    degrees.append(G.degree[n])
                print("The network mean number of degrees is {}".format("%.2f" % mean(degrees)))
                print()

                brick_mean_degrees.append(mean(degrees))

                # diameter refers to deeper hierarchy
                print("HIERARCHY")
                print("============")
                components = (G.subgraph(c).copy() for c in nx.connected_components(G))
                diameters = []
                for c in components:
                    diameters.append(nx.diameter(c))
                print("The network diameter is {}".format("%.2f" % mean(diameters)))
                print()

                brick_mean_diameters.append(mean(diameters))

    if os.path.isdir(folders) and folders == "Haystack":
        for file in os.listdir(path+"/"+folders+"/"):
            if file.endswith(".ttl"):

                print("FILE NAME")
                print("============")
                print(file)
                print()
                haystack_model_names.append(file)

                print("LOAD ADN TRANSFER")
                print("============")
                rg = RDFGraph()
                # print("path: ", path + "/" + folders + "/" + file)
                rg.parse(path+"/"+folders+"/"+file, format='turtle')
                print("rdflib Graph loaded successfully with {} triples".format(len(rg)))
                G = rdflib_to_networkx_graph(rg)
                print("networkx Graph loaded successfully with length {}".format(len(G)))
                print()

                # Network size
                print("NETWORK SIZE")
                print("============")
                print("The network has {} nodes and {} edges".format(G.number_of_nodes(), G.number_of_edges()))
                print()

                # degree refers to number of properties
                print("DEGREE")
                print("============")
                degrees = []
                for n in G:
                    degrees.append(G.degree[n])
                print("The network mean number of degrees is {}".format("%.2f" % mean(degrees)))
                print()

                haystack_mean_degrees.append(mean(degrees))

                # diameter refers to deeper hierarchy
                print("HIERARCHY")
                print("============")
                components = (G.subgraph(c).copy() for c in nx.connected_components(G))
                diameters = []
                for c in components:
                    diameters.append(nx.diameter(c))
                print("The network diameter is {}".format("%.2f" % mean(diameters)))
                print()

                haystack_mean_diameters.append(mean(diameters))

info = {'MODEL': brick_model_names, 'DEGREE': brick_mean_degrees, 'DIAMETER': brick_mean_diameters}
print(tabulate(info, headers='keys', tablefmt='fancy_grid', missingval='N/A', showindex=True))

info = {'MODEL': haystack_model_names, 'DEGREE': haystack_mean_degrees, 'DIAMETER': haystack_mean_diameters}
print(tabulate(info, headers='keys', tablefmt='fancy_grid', missingval='N/A', showindex=True))

plt.figure(figsize=(10,5))
plt.title('Topology Analysis',fontsize=20)
plt.xlabel('properties',fontsize=14)
plt.ylabel('hierarchy',fontsize=14)
plt.scatter(brick_mean_degrees, brick_mean_diameters, s=100, c='deeppink', marker='o')
plt.scatter(haystack_mean_degrees, haystack_mean_diameters, s=100, c='darkblue', marker='+')
plt.legend(['Brick Model', 'Project Haystack Model'])
plt.show()
