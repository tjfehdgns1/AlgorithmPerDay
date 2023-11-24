import sys
from collections import deque


input = sys.stdin.readline

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')

    for neighbor in sorted(graph[start]):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        print(current, end=' ')

        for neighbor in sorted(graph[current]):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

N, M, V = map(int, input().split())

graph = {i: set() for i in range(1, N + 1)}

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

visited_dfs = [False] * (N + 1)
dfs(graph, V, visited_dfs)
print()

visited_bfs = [False] * (N + 1)
bfs(graph, V, visited_bfs)
print()
