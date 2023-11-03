from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())

a = list(map(int, input().split()))
b = deque()
i = 1

while a:
    if a[0] == i:
        a.pop(0)
        i += 1
    else:
        b.appendleft(a.pop(0))

    while b:
        if b[0] == i:
            b.popleft()
            i += 1
        else:
            break
        
    
if not b:
    print('Nice')
else:
    print('Sad')
                