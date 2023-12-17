from sys import stdin


input = stdin.readline
n = int(input())
if n == 0:
    print(0)
    exit()

a = sorted(int(input()) for _ in range(n))


def round5(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)


c = round5(n * 0.15)

b = a[c : n - c]

print(round5(sum(b) / len(b)))
