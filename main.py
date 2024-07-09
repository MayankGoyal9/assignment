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

