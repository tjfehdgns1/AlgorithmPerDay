from collections import deque


n = int(input())

for _ in range(n):
    l, i = map(int, input().split())
    a = deque(map(int, input().split()))
    count = 0
    while a:
        m = max(a)
        f = a.popleft()
        i -= 1

        if f >= m:
            count += 1
            if i < 0:
                print(count)
                break
        else:
            a.append(f)
            if i < 0:
                i = len(a) - 1
