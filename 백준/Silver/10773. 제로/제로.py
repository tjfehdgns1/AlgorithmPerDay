from sys import stdin

input = stdin.readline

n = int(input())
b = []
for _ in range(n):
    a = int(input())
    if a != 0:
        b.append(a)
    else:
        b.pop()

if b:
    print(sum(b))
else:
    print(0)
