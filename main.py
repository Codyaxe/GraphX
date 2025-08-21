import networkx as nx
import math as m
import matplotlib.pyplot as pl


def binary_tree_factory(size):
    return ((m.ceil(i / 2), i + 1) for i in range(1, size))


edges = binary_tree_factory(200)


graph = nx.Graph()

graph.add_edges_from(edges)


def hierarchy_layout(G, root=1, width=2.0, vert_gap=1.0):
    """
    Compute a hierarchical/tree layout for a binary tree.
    """
    pos = {}

    def _hierarchy_pos(G, node, left, right, vert=0, parent=None):
        pos[node] = ((left + right) / 2, -vert)
        children = [n for n in G.neighbors(node) if n != parent]

        if children:
            if len(children) == 2:
                _hierarchy_pos(
                    G, children[0], left, (left + right) / 2, vert + vert_gap, node
                )
                _hierarchy_pos(
                    G, children[1], (left + right) / 2, right, vert + vert_gap, node
                )
            elif len(children) == 1:
                _hierarchy_pos(G, children[0], left, right, vert + vert_gap, node)

    _hierarchy_pos(G, root, 0, width)
    return pos


pos = hierarchy_layout(graph)

nx.draw(graph, pos, with_labels=True)
nx.drawing.layout
pl.show()
