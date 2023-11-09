from sys import stdin

input = stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
print(round(sum(arr) / n))
print(arr[n // 2])

dic = {}
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
m = max(dic.values())
c = []

for j in list(dic.keys()):
	if dic[j] == m:
		c.append(j)

if len(c) > 1:
	print(c[1])
else:
	print(c[0])

print(max(arr) - min(arr))