import sys


def sol(stack, given, start, m):
    if len(stack) == m:
        print(" ".join(map(str, stack)))
        return

    for i in range(start, len(given)):
        stack.append(given[i])
        sol(stack, given, i, m)
        stack.pop()


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    given = sorted(set(map(int, input().split())))
    stack = []

    sol(stack, given, 0, m)


if __name__ == "__main__":
    main()
