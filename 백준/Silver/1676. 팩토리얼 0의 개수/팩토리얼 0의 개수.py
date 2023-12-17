from sys import stdin

input = stdin.readline

n = int(input())


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


a = str(factorial(n))
result = 0
for i in a[::-1]:
    if i == "0":
        result += 1
    else:
        break

print(result)
