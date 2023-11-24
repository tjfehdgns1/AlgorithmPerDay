import sys


input = sys.stdin.readline
n, k = map(int, input().split())

a = sorted((int(input()) for _ in range(n)), reverse=True)
count = 0
for i in a:
    if k >= i:
        count += k // i
        k %= i
print(count)
