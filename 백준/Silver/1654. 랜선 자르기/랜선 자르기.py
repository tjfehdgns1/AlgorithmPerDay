import sys

input = sys.stdin.readline
k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
l, r = 1, sum(arr) // n

while l <= r:
    mid = (l + r) // 2
    count = sum(a // mid for a in arr)

    if count >= n:
        l = mid + 1
    else:
        r = mid - 1
print(r)
