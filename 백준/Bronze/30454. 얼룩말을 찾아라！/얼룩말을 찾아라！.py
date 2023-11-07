from sys import stdin
input = stdin.readline

n, l = map(int, input().split())
dict = {}
for _ in range(n):
    a = input().strip()
    pre = '0'
    b = 0
    w = 0
    for c in a:
        if pre == '0' and c == '1':
            b += 1
        elif pre == '1' and c == '0':
            w += 1
        pre = c

    if b >= w:
        if b not in dict:
            dict[b] = 1
        else:
            dict[b] += 1

max_key = max(dict.keys())
print(max_key, end=' ')
print(dict[max_key])