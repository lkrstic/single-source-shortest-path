def bellmanford(graph, source):
    graph.nodes[source]['distance'] = 0

    for node, data in graph.nodes(data=True):
        data['parent'] = None
        if node != source:
            data['distance'] = float("inf")

    for i in range(graph.number_of_nodes() - 1):
        for edge in graph.edges(data=True):
            c = graph.nodes[edge[0]]['distance']
            w = edge[2]['weight']
            d = graph.nodes[edge[1]]['distance']
            if d > (c + w):
                graph.nodes[edge[1]]['distance'] = c + w
                graph.nodes[edge[1]]['parent'] = edge[0]
