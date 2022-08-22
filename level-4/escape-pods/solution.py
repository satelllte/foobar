# Technique used:
# https://en.wikipedia.org/wiki/Ford-Fulkerson_algorithm

class Vertex:
    def __init__(self, id, source=False, sink=False):
        self.id = id
        self.source = source
        self.sink = sink

class Edge:
    def __init__(self, start, end, capacity):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.flow = 0
        self.return_edge = None

class FlowNetwork:
    def __init__(self):
        self.vertices = []
        self.network = {}

    def get_source(self):
        for vertex in self.vertices:
            if vertex.source == True:
                return vertex
        return None

    def get_sink(self):
        for vertex in self.vertices:
            if vertex.sink == True:
                return vertex
        return None

    def get_vertex(self, name):
        for vertex in self.vertices:
            if name == vertex.id:
                return vertex

    def add_vertex(self, id, source=False, sink=False):
        new_vertex = Vertex(id, source, sink)
        self.vertices.append(new_vertex)
        self.network[new_vertex.id] = []

    def add_edge(self, start, end, capacity):
        new_edge = Edge(start, end, capacity)
        return_edge = Edge(end, start, 0)
        new_edge.return_edge = return_edge
        return_edge.return_edge = new_edge
        vertex = self.get_vertex(start)
        self.network[vertex.id].append(new_edge)
        return_vertex = self.get_vertex(end)
        self.network[return_vertex.id].append(return_edge)

    def get_path(self, start, end, path):
        if start == end:
            return path
        for edge in self.network[start]:
            residual_capacity = edge.capacity - edge.flow
            if residual_capacity > 0 and not (edge, residual_capacity) in path:
                result = self.get_path(edge.end, end, path + [(edge, residual_capacity)])
                if result != None:
                    return result

    def calculate_max_flow(self):
        source = self.get_source()
        sink = self.get_sink()
        path = self.get_path(source.id, sink.id, [])
        while path != None:
            flow = min(edge[1] for edge in path)
            for edge, res in path:
                edge.flow += flow
                edge.return_edge.flow -= flow
            path = self.get_path(source.id, sink.id, [])
        return sum(edge.flow for edge in self.network[source.id])

def solution(entrances, exits, path):
    INFINITY = float('inf')
    SOURCE = -1
    SINK = len(path)

    network = FlowNetwork()
    network.add_vertex(SOURCE, True, False)
    network.add_vertex(SINK, False, True)
    map(network.add_vertex, range(len(path)))
    for entrance in entrances:
        network.add_edge(SOURCE, entrance, sum(path[entrance]))
    for i in range(len(path)):
        for j in range(len(path)):
            if path[i][j] > 0:
                network.add_edge(i, j, path[i][j])
    for exit in exits:
        network.add_edge(exit, SINK, INFINITY)

    return network.calculate_max_flow()
