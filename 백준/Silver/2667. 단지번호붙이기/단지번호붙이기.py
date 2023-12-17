import sys
from collections import deque


def bfs(grid, start):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    que = deque([start])
    n = len(grid)
    grid[start[0]][start[1]] = 0
    count = 1

    while que:
        x, y = que.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    que.append((nx, ny))
                    count += 1

    return count


def main():
    input = sys.stdin.readline
    n = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip())))

    results = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                result = bfs(grid, (i, j))
                results.append(result)

    print(len(results))
    for i in sorted(results):
        print(i)


if __name__ == "__main__":
    main()
