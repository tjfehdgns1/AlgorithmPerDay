from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())

a = deque()

for i in range(n):
    b = input().split()
    match b[0]:
        case '1':
            a.append(int(b[1]))
        case '2':
            a.appendleft(int(b[1]))
        case '3':
            if a:
                print(a.pop())
            else:
                print(-1)
        case '4':
            if a:
                print(a.popleft())
            else:
                print(-1)
        case '5':
            print(len(a))
        case '6':
            if a:
                print(0)
            else:
                print(1)
        case '7':
            if a:
                print(a[-1])
            else:
                print(-1)
        case '8':
            if a:
                print(a[0])
            else:
                print(-1)