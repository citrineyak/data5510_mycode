import networkx as nx

def count(graph):
    return graph.number_of_nodes()

G = nx.Graph()

G.add_edges_from([(1,2), (2,3), (3,4),(4,5)])

print(count(G))