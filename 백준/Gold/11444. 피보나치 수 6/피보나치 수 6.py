def matrix_multiply(a, b, mod):
    return (
        (a[0] * b[0] + a[1] * b[2]) % mod,
        (a[0] * b[1] + a[1] * b[3]) % mod,
        (a[2] * b[0] + a[3] * b[2]) % mod,
        (a[2] * b[1] + a[3] * b[3]) % mod,
    )


def matrix_power(matrix, exp, mod):
    result = (1, 0, 0, 1)
    while exp > 0:
        if exp % 2 == 1:
            result = matrix_multiply(result, matrix, mod)
        matrix = matrix_multiply(matrix, matrix, mod)
        exp //= 2
    return result


def fibonacci(n, mod):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    base_matrix = (1, 1, 1, 0)
    result_matrix = matrix_power(base_matrix, n - 1, mod)
    return result_matrix[0]


n = int(input())
result = fibonacci(n, 1_000_000_007)
print(result)
