from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())

a = deque(enumerate(map(int, input().split())))
b = []

while a:
    i, p = a.popleft()
    b.append(i + 1)

    if p > 0:
        a.rotate(-p + 1)
    elif p < 0:
        a.rotate(-p)

print(' '.join(map(str, b)))