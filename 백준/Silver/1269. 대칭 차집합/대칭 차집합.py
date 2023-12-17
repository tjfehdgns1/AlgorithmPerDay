from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

a = set(input().split())
b = set(input().split())

print(len(a - b) + len(b - a))
