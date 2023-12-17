from sys import stdin

input = stdin.readline


def binomial(a, b):
    if b == 0 or a == b:
        return 1
    return binomial(a - 1, b) + binomial(a - 1, b - 1)


x, y = map(int, input().split())
print(binomial(x, y))
