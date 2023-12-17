import sys


def back_track(stack, given, start, n, m):
    if len(stack) == m:
        print(" ".join(map(str, stack)))
        return

    for i in range(n):
        if given[i] not in stack:
            stack.append(given[i])
            back_track(stack, given, i + 1, n, m)
            stack.pop()


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    given = sorted(map(int, input().split()))
    stack = []

    back_track(stack, given, 0, n, m)


if __name__ == "__main__":
    main()
