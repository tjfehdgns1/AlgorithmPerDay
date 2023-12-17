import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n = int(sys.stdin.readline())

if a1 * n + a0 > c * n or c < a1:
    print(0)
else:
    print(1)
