import sys


input = sys.stdin.readline

s = [0]
a = 0
l, c = map(int, input().split())
g = list(map(int, input().split()))
for i in range(l):
    a += g[i]
    s.append(a)
    
for _ in range(c):
    start, end = map(int, input().split())
    print(s[end] - s[start - 1])
    

    
    
    
    