import sys


sys.setrecursionlimit(10**6)

def dfs(graph, visited, node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)
            
def count_connected_components(graph, n):
    visited = [False] * (n + 1)
    count = 0
    
    for node in range(1, n + 1):
        if not visited[node]:
            count += 1
            dfs(graph, visited, node)
            
    return count

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    graph = {i: [] for i in range(1, n + 1)}
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    result = count_connected_components(graph, n)
    print(result)
    
if __name__ == "__main__":
    main()