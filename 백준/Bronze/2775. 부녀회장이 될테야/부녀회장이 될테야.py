from sys import stdin
input = stdin.readline

n = int(input())

for _ in range(n):
    floor = int(input())
    room = int(input())
    f0 = [i for i in range(1,room+1)]
    for _ in range(floor):
        for j in range(1,room):
            f0[j] += f0[j-1]
    print(f0[-1])