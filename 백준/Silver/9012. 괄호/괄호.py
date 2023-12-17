from sys import stdin

input = stdin.readline

n = int(input())

a = [input().strip() for _ in range(n)]

for b in a:
    d = 0
    for i, c in enumerate(b):
        if c == "(":
            d += 1
        elif c == ")":
            d -= 1

        if d < 0:
            print("NO")
            break
    else:
        if d == 0:
            print("YES")
        else:
            print("NO")
