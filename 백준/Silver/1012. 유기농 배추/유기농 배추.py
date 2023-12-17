import sys

sys.setrecursionlimit(10000)


input = sys.stdin.readline


def dfs(x, y, field, visited):
    if x < 0 or x >= M or y < 0 or y >= N or field[y][x] == 0 or visited[y][x]:
        return 0

    visited[y][x] = True

    dfs(x + 1, y, field, visited)
    dfs(x - 1, y, field, visited)
    dfs(x, y + 1, field, visited)
    dfs(x, y - 1, field, visited)

    return 1


def count_worms(field):
    worms = 0
    visited = [[False] * M for _ in range(N)]

    for y in range(N):
        for x in range(M):
            if field[y][x] == 1 and not visited[y][x]:
                worms += dfs(x, y, field, visited)

    return worms


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    cabbage_field = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        cabbage_field[Y][X] = 1

    print(count_worms(cabbage_field))
