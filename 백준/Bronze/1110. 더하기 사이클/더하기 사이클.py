def cycle(n: int) -> int:
    num = n
    cnt = 0

    while True:
        a = num // 10
        b = num % 10
        c = (a + b) % 10
        num = (b * 10) + c

        cnt += 1
        if num == n:
            break

    return cnt


n = int(input())
result = cycle(n)
print(result)
