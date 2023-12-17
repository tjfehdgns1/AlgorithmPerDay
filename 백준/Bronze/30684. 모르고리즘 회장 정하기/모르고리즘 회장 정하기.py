import sys


input = sys.stdin.readline
n = int(input())
a = []
for _ in range(n):
    i = input().rstrip()
    if len(i) == 3:
        a.append(i)
a.sort()
print(a[0])
