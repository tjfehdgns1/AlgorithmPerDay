from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())

a = deque(range(1, n+1))

while len(a) > 1:
    a.popleft()
    a.append(a.popleft())

print(a[0])