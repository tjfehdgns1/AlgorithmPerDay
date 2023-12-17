from sys import stdin

input = stdin.readline

n = int(input())
a = sorted(map(int, input().split()))
d = {}
for c in a:
    d[c] = 0

m = int(input())
b = list(map(int, input().split()))


for j in b:
    if j in d.keys():
        print(1)
    else:
        print(0)
