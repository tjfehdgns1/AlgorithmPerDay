def padovan_sequence(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    elif n == 4 or n == 5:
        return 2
    else:
        p = [0] * (n + 1)
        p[1] = p[2] = p[3] = 1
        p[4] = p[5] = 2
        for i in range(6, n + 1):
            p[i] = p[i - 1] + p[i - 5]
        return p[n]


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        result = padovan_sequence(N)
        print(result)
