import sys

input = sys.stdin.readline
N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = table[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]
    print(result)
