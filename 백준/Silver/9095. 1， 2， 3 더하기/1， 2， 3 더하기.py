import sys


input = sys.stdin.readline


def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        if i - 3 >= 0:
            dp[i] += dp[i - 3]

    return dp[n]


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        result = solution(int(input()))
        print(result)
