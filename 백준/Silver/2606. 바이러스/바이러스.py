from collections import defaultdict


def dfs(graph, start, visited):
    stack = [start]
    count = 0

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            count += 1
            stack.extend(graph[node])

    return count


def main():
    n = int(input()) 
    m = int(input())  

    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    result = dfs(graph, 1, visited)

    print(result - 1)


if __name__ == "__main__":
    main()
