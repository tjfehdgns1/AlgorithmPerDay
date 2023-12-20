import sys


def bag_problem(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
                
    return dp[n][capacity]

input = sys.stdin.readline
n, k = map(int, input().split())
weights = []
values = []

for _ in range(n):
    a, b = map(int, input().split())
    weights.append(a)
    values.append(b)
    
result = bag_problem(weights, values, k)
print(result)