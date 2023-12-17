from sys import stdin

input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

dic = {}
for i in a:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

for num in b:
    if num in dic:
        print(dic[num], end=" ")
    else:
        print(0, end=" ")
