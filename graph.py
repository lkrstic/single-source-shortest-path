import random

import networkx as nx


def random_connected_graph(vertices, edges):
    # Generates a random graph with the following properties:
    # Directed, weighted, connected
    g1 = nx.DiGraph()
    g1.add_nodes_from(range(vertices))
    nlist = list(g1)
    edge_count = 0

    while edge_count < edges:
        # generate random edge,u,v
        u = random.choice(nlist)
        v = random.choice(nlist)
        if u == v or g1.has_edge(u, v) or g1.has_edge(v, u) or v == 0:
            continue
        else:
            g1.add_edge(u, v)
            edge_count = edge_count + 1

    # Check for nodes without edges, and add random ones
    for node in g1.nodes:
        if not g1.edges(node) and not g1.in_edges(node):
            v = random.choice(nlist)
            if v != node and v != 1:
                g1.add_edge(node, v)
            else:
                continue

    # Add random weights
    for (start, end) in g1.edges:
        g1.edges[start, end]['weight'] = random.randint(0, 10)
    return g1
