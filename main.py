
### 2. `main.py`

```python
"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""
from collections import deque

def longest_path(graph: list) -> int:
    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)

def topological_sort(graph):
    n = len(graph)
    in_degree = [0] * n
    for u in range(n):
        for v, w in graph[u]:
            in_degree[v] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for v, w in graph[node]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return topo_order

def calculate_longest_path(graph, topo_order):
    n = len(graph)
    dist = [-float('inf')] * n

    for node in topo_order:
        if dist[node] == -float('inf'):
            dist[node] = 0

        for v, w in graph[node]:
            if dist[v] < dist[node] + w:
                dist[v] = dist[node] + w

    return max(dist)
