import sys


input = sys.stdin.readline
n, m = map(int, input().split())
dic = dict()
for _ in range(n):
    a, b = input().rstrip().split()
    dic[a] = b

for _ in range(m):
    print(dic[input().rstrip()])
