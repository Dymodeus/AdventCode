import sys

from config import input_path
import os
import numpy as np

# lines = [line.rstrip() for line in open(os.path.join(input_path, "input17.txt"))]
# print(lines)

test = True
if test:
    lines = ["2413432311323", "3215453535623", "3255245654254", "3446585845452", "4546657867536", "1438598798454",
             "4457876987766", "3637877979653", "4654967986887", "4564679986453", "1224686865563", "2546548887735",
             "4322674655533"]
else:
    lines = [line.rstrip() for line in open(os.path.join(input_path, "input17.txt"))]

lines_array = np.array([list(line) for line in lines], dtype=int)
print(lines_array)


class Graph:
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    @staticmethod
    def construct_graph(nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if not graph[adjacent_node].get(node, False):
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        return self.nodes

    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False):
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    shortest_path = {}
    previous_nodes = {}
    previous_dirs = {}
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if not current_min_node:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if neighbor < current_min_node:
                direction = "N"
            elif neighbor == current_min_node + 1:
                direction = "E"
            else:
                direction = "S"
            if len(previous_nodes[])
            if tentative_value < shortest_path[neighbor] and :



nodes = list(range(lines_array.size))
row_size = lines_array.shape[0]
col_size = lines_array.shape[1]

# print(nodes)

init_graph = {}
for node in nodes:
    init_graph[node] = {}
    if node < len(nodes) - row_size:
        init_graph[node][node + row_size] = lines_array[node // row_size + 1][node % row_size]
    if node % row_size < row_size - 1:
        init_graph[node][node + 1] = lines_array[node // row_size][node % row_size + 1]
    if node > row_size:
        init_graph[node][node - row_size] = lines_array[node // row_size - 1][node % row_size]

city_graph = Graph(nodes, init_graph)


