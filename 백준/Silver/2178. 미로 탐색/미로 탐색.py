import sys
from collections import deque


input = sys.stdin.readline
n, m = map(int, input().split())
grid = []
visited = [[False] * m for _ in range(n)]

for row in range(n):
    grid.append(list(map(int, input().rstrip())))

que = deque([(0, 0)])
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

visited[0][0] = True

while que:
    x, y = que.popleft()

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and grid[nx][ny] == 1:
                que.append((nx, ny))
                visited[nx][ny] = True
                grid[nx][ny] = grid[x][y] + 1

print(grid[-1][-1])
