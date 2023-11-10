import sys


input = sys.stdin.readline
n = int(input())
a = sorted(map(int, input().split()))
s = 0

for i in range(n):
    s += sum(a[: i + 1])

print(s)
