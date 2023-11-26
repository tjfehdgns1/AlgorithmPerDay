import sys
from collections import deque


def bfs_tomato(m, n, grid):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    que = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                que.append((i, j, 0))

    while que:
        x, y, day = que.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                grid[nx][ny] = 1
                que.append((nx, ny, day + 1))


    for row in grid:
        if 0 in row:
            return -1


    return day

def main():
    input = sys.stdin.readline
    m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    result = bfs_tomato(m, n, grid)
    print(result)

if __name__ == "__main__":
    main()