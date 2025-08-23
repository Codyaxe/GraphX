import networkx as nx
import math as m
import random as rand

# Define Graph


def create_graph(data):
    temp_graph = nx.DiGraph()
    temp_graph.add_edges_from(data)
    return temp_graph


# Define Probability Distribution and Data
data = (
    ("Math", "Physics", {"weight": 0.15}),
    ("Math", "Math", {"weight": 0.75}),
    ("Math", "Chemistry", {"weight": 0.05}),
    ("Math", "Biology", {"weight": 0.05}),
    ("Physics", "Math", {"weight": 0.55}),
    ("Physics", "Physics", {"weight": 0.35}),
    ("Physics", "Chemistry", {"weight": 0.05}),
    ("Physics", "Biology", {"weight": 0.05}),
    ("Chemistry", "Math", {"weight": 0.10}),
    ("Chemistry", "Physics", {"weight": 0.28}),
    ("Chemistry", "Biology", {"weight": 0.28}),
    ("Chemistry", "Chemistry", {"weight": 0.34}),
    ("Biology", "Chemistry", {"weight": 0.35}),
    ("Biology", "Physics", {"weight": 0.20}),
    ("Biology", "Math", {"weight": 0.20}),
    ("Biology", "Biology", {"weight": 0.25}),
)

# Create randomization and walk throughout the Graph.


def walk(graph: nx.DiGraph, walk_count: int):
    """
    start at node x
    find neighbors at x
    randomly walk through neighbors based on edges weights from x to neighbor node y
    """
    n = 0
    frequency = {"Physics": 0, "Math": 0, "Biology": 0, "Chemistry": 0}
    walk_pointer = list(graph.nodes())[0]  # Start at Math
    while n <= walk_count:
        neighbors = list(graph.neighbors(walk_pointer))
        weights = [graph[walk_pointer][neighbor]["weight"] for neighbor in neighbors]
        next_node = rand.choices(neighbors, weights=weights, k=1)[0]
        print(f"Moving from {walk_pointer} to {next_node}")
        walk_pointer = next_node
        frequency[next_node] += 1
        n = n + 1
    print(frequency)


def main():
    graph = create_graph(data)
    walk(graph, 100)


main()
