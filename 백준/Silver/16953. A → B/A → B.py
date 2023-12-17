import sys
from collections import deque


def bfs(start, target):
    q = deque([(start, 1)])
    while q:
        current, count = q.popleft()

        if current == target:
            print(count)
            return

        if current * 2 <= target:
            q.append((current * 2, count + 1))

        if current * 10 + 1 <= target:
            q.append((current * 10 + 1, count + 1))
    print(-1)


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    bfs(n, m)


if __name__ == "__main__":
    main()
