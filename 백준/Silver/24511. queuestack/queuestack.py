import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))

r = deque()

for j in range(n):
    if a[j] == 0:
        r.appendleft(b[j])
        
for i in range(m):
    r.append(c[i])
    print(r.popleft(), end=' ')