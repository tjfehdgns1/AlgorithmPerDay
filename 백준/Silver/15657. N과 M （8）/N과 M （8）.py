import sys


def sol(stack, given, n, m, start):
    if len(stack) == m:
        print(" ".join(map(str, stack)))
        return

    for i in range(start, n):
        stack.append(given[i])
        sol(stack, given, n, m, i)
        stack.pop()


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    given = sorted(map(int, input().split()))

    stack = []
    sol(stack, given, n, m, 0)


if __name__ == "__main__":
    main()
