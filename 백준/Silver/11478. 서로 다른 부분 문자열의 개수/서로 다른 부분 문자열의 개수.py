from sys import stdin

input = stdin.readline

a = input().rstrip()

b = []

for i in range(len(a)):
    for j in range(i + 1, len(a) + 1):
        b.append(a[i:j])

print(len(set(b)))
