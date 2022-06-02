from __future__ import annotations
import copy
from dataclasses import dataclass
from functools import reduce
from itertools import product
from random import randint

@dataclass
class Node:
    x: int
    y: int

    def dist(self, rhs: Node) -> int:
        return abs(self.x - rhs.x) + abs(self.y - rhs.y)


@dataclass
class Box:
    xmin: int = 100000
    xmax: int = -100000
    ymin: int = 100000
    ymax: int = -100000

    def xrange(self) -> range:
        return range(self.xmin, self.xmax + 1)

    def yrange(self) -> range:
        return range(self.ymin, self.ymax + 1)


def add_node(box: Box, node: Node) -> Box:
    box = copy.deepcopy(box)
    box.xmin = min(box.xmin, node.x)
    box.xmax = max(box.xmax, node.x)
    box.ymin = min(box.ymin, node.y)
    box.ymax = max(box.ymax, node.y)
    return box


def prim(nodes: list[Node]) -> list[tuple[int, int]]:
    size = len(nodes)
    start_node = randint(0, size - 1)

    pending_nodes = {*range(size)}

    selected_nodes = { start_node }
    pending_nodes.remove(start_node)

    edges = []
    while pending_nodes:
        candidate_edges = [*product(selected_nodes, pending_nodes)]
        edge_lengthes = [nodes[src].dist(nodes[dst]) for src, dst in candidate_edges]

        min_len = min(edge_lengthes)
        min_len_idx = edge_lengthes.index(min_len)

        min_len_edge = candidate_edges[min_len_idx]
        edges.append(min_len_edge)
        _, dst = min_len_edge
        selected_nodes.add(dst)
        pending_nodes.remove(dst)

    return normalize_edges(edges)


def normalize_edges(edges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    edges = [(src, dst) if src < dst else (dst, src) for src, dst in edges]
    return sorted(edges)


def cost(nodes: list[Node], edges: list[tuple[int, int]]) -> int:
    costs = [nodes[src].dist(nodes[dst]) for src, dst in edges]
    print(costs)
    return sum(costs)


def main():
    N = Node
    nodes = [
        N(2, 5),
        N(3, 8),
        N(6, 1),
        N(9, 3),
        N(5, 5),
    ]
    mst_edges = prim(nodes)
    mst_cost = cost(nodes, mst_edges)
    print('MST:', mst_cost, mst_edges)

    best_stei_cost = 1000000
    bbox = reduce(add_node, nodes, Box())
    for x, y in product(bbox.xrange(), bbox.yrange()):
        steiner_node = N(x, y)
        stei_nodes = nodes + [steiner_node]
        stei_edges = prim(stei_nodes)
        stei_cost = cost(stei_nodes, stei_edges)
        print('STI', (x, y), stei_cost, stei_edges)

        best_stei_cost = min(best_stei_cost, stei_cost)
    print('Best Steiner tree cost', best_stei_cost)

    print(cost(nodes, [*product(range(0, len(nodes)), range(0, len(nodes)))]))


if __name__ == '__main__':
    main()
