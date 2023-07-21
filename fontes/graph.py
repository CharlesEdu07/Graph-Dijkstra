import graphviz
import sys

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = {'neighbors': []}

    def add_edge(self, node1, node2, weight):
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            self.adjacency_list[node1]['neighbors'].append((node2, weight))

    def dijkstra(self, source):
        dist = {}
        prev = {}
        Q = set()

        for node in self.adjacency_list:
            dist[node] = float('inf')
            prev[node] = None

            Q.add(node)

        dist[source] = 0

        while Q:
            current = min(Q, key=lambda node: dist[node])
            Q.remove(current)

            for neighbor, weight in self.adjacency_list[current]['neighbors']:
                alt = dist[current] + weight

                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prev[neighbor] = current

        return dist, prev

    def print_graph(self):
        for node in self.adjacency_list:
            edges = []

            for neighbor in self.adjacency_list[node]['neighbors']:
                edges.append(f"{neighbor[0]} (weight: {neighbor[1]})")

            print(node, "->", " -> ".join(edges))

    def print_graph_dot(self):
        dot = graphviz.Digraph()

        for node in self.adjacency_list:
            edges = []

            for neighbor in self.adjacency_list[node]['neighbors']:
                edges.append(f"{neighbor[0]} (weight: {neighbor[1]})")

            dot.node(str(node))

            for neighbor in self.adjacency_list[node]['neighbors']:
                dot.edge(str(node), str(neighbor[0]), label=f"weight: {neighbor[1]}")

        dot.render('graph', format='png')

graph = Graph()

for i in range(1, 26, 1):
    graph.add_node(i)

graph.add_edge(1, 6, 71)
graph.add_edge(1, 2, 33)
graph.add_edge(2, 1, 45)
graph.add_edge(2, 7, 42)
graph.add_edge(2, 3, 65)
graph.add_edge(3, 2, 100)
graph.add_edge(3, 8, 80)
graph.add_edge(3, 4, 17)
graph.add_edge(4, 3, 91)
graph.add_edge(4, 5, 22)
graph.add_edge(5, 4, 90)
graph.add_edge(5, 10, 24)
graph.add_edge(6, 1, 50)
graph.add_edge(6, 11, 89)
graph.add_edge(6, 7, 23)
graph.add_edge(7, 2, 71)
graph.add_edge(7, 6, 81)
graph.add_edge(7, 8, 58)
graph.add_edge(8, 3, 43)
graph.add_edge(8, 7, 28)
graph.add_edge(10, 5, 29)
graph.add_edge(10, 15, 48)
graph.add_edge(11, 6, 13)
graph.add_edge(11, 16, 52)
graph.add_edge(15, 10, 20)
graph.add_edge(15, 20, 52)
graph.add_edge(16, 11, 75)
graph.add_edge(16, 21, 50)
graph.add_edge(18, 23, 46)
graph.add_edge(18, 19, 35)
graph.add_edge(19, 18, 73)
graph.add_edge(19, 24, 16)
graph.add_edge(19, 20, 2)
graph.add_edge(20, 15, 0)
graph.add_edge(20, 19, 17)
graph.add_edge(20, 25, 13)
graph.add_edge(21, 16, 16)
graph.add_edge(21, 22, 24)
graph.add_edge(22, 21, 4)
graph.add_edge(22, 23, 19)
graph.add_edge(23, 18, 21)
graph.add_edge(23, 22, 43)
graph.add_edge(23, 24, 78)
graph.add_edge(24, 19, 4)
graph.add_edge(24, 23, 58)
graph.add_edge(24, 25, 36)
graph.add_edge(25, 20, 63)
graph.add_edge(25, 24, 39)

print("\n")

graph.print_graph()
graph.print_graph_dot()

print("\n")

distances, predecessors = graph.dijkstra(1)

print("Distances:")
for node, distance in distances.items():
    predecessor = predecessors[node]

    print(f"Node {node}: Min Distance = {distance}, Previous = {predecessor}")
