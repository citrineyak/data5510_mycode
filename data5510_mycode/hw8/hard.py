import networkx as nx

def count_nodes(graph):
    count = 0

# How do I get it to count degreest that are greater than 5?
    for node in graph.nodes():
        if graph.degree(node) > 5:
            count += 1

    return count

G = nx.Graph()

G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
    (2, 3), (3, 4)])

print(count_nodes(G))