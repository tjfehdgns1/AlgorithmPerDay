from sys import stdin

input = stdin.readline
n, m, b = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

time = float("inf")
height = 0

for i in range(257):
    use = 0
    take = 0
    for x in range(n):
        for y in range(m):
            if grid[x][y] > i:
                take += grid[x][y] - i
            else:
                use += i - grid[x][y]

    if use > take + b:
        continue

    t = take * 2 + use

    if t <= time:
        time = t
        height = i

print(time, height, sep=" ")
