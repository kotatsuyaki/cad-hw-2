from typing import Union
from dataclasses import dataclass

def to_str(num: int) -> str:
    return '{}'.format(num)

@dataclass
class NodeData:
    delay: int
    preds: list[str]
    longest_delay: int = -1
    shortest_delay: int = 1000000
    longest_pred: Union[str, None] = None
    shortest_pred: Union[str, None] = None


graph: dict[str, NodeData] = {
    'A': NodeData(2, ['S']),
    'B': NodeData(1, ['A', 'F']),
    'C': NodeData(4, ['B']),
    'D': NodeData(2, ['C']),
    'F': NodeData(3, ['S']),
    'G': NodeData(1, ['F']),
    'H': NodeData(4, ['B', 'G']),
    'I': NodeData(3, ['H', 'K']),
    'J': NodeData(3, ['C', 'I']),
    'K': NodeData(1, ['A', 'S']),
    'L': NodeData(2, ['G', 'K']),
    'M': NodeData(5, ['D', 'L']),
    'N': NodeData(3, ['D']),
    'S': NodeData(0, [], 0, 0),
    'E': NodeData(0, ['N', 'J', 'M'])
}
names = ['S', 'A', 'F', 'B', 'G', 'K', 'C', 'H', 'L', 'D', 'I', 'N', 'J', 'M', 'E']

# Validate the topological order of names
for name, data in graph.items():
    assert all(names.index(pred) < names.index(name) for pred in data.preds)

for name in names[1:]:
    long_candidates = [graph[pred].longest_delay + graph[pred].delay for pred in graph[name].preds]
    longest_delay = max(long_candidates)
    longest_pred = graph[name].preds[long_candidates.index(longest_delay)]
    print('$\\max({}) = {}$ ({})'.format(
          ','.join(map(to_str, long_candidates)),
          longest_delay,
          longest_pred))
    graph[name].longest_delay = longest_delay
    graph[name].longest_pred = longest_pred

print('=' * 40)
          
for name in names[1:]:
    short_candidates = [graph[pred].shortest_delay + graph[pred].delay for pred in graph[name].preds]
    shortest_delay = min(short_candidates)
    shortest_pred = graph[name].preds[short_candidates.index(shortest_delay)]
    print('$\\min({}) = {}$ ({})'.format(
          ','.join(map(to_str, short_candidates)),
          shortest_delay,
          shortest_pred))
    graph[name].shortest_delay = shortest_delay
    graph[name].shortest_pred = shortest_pred
