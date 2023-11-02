from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())

a = deque()

for i in range(n):
    b = input().split()
    match b[0]:
        case 'push':
            a.appendleft(int(b[1]))
        case 'pop':
            if a:
                print(a.pop())
            else:
                print(-1)
        case 'size':
            print(len(a))
        case 'empty':
            if a:
                print(0)
            else:
                print(1)
        case 'front':
            if a:
                print(a[-1])
            else:
                print(-1)
        case 'back':
            if a:
                print(a[0])
            else:
                print(-1)
