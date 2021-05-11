from queue import PriorityQueue


def dijkstra(graph, source):
    queue = PriorityQueue()
    graph.nodes[source]['distance'] = 0

    for node, data in graph.nodes(data=True):
        data['parent'] = None
        data['visited'] = None
        if node != source:
            data['distance'] = float("inf")
        queue.put((data['distance'], node))

    while not queue.empty():
        current = queue.get()[1]
        graph.nodes[current]['visited'] = True
        for edge in graph.edges([current], data=True):
            if not graph.nodes[edge[1]]['visited']:
                c = graph.nodes[current]['distance']
                w = edge[2]['weight']
                d = graph.nodes[edge[1]]['distance']
                if d > (c + w):
                    graph.nodes[edge[1]]['distance'] = c + w
                    graph.nodes[edge[1]]['parent'] = current
                    graph.nodes[edge[1]]['visited'] = True
