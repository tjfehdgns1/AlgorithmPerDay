from sys import stdin
input = stdin.readline

n = int(input())
a = input().rstrip()
sum = 0

for i, c in enumerate(a):
    sum += (ord(c) - 96) * (31 ** i)

print(sum%1234567891)

