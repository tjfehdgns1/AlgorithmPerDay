import sys


def sol(n, m, stack, visited, nums, used):
    if len(stack) == m:
        print(*stack)
        return

    for i in range(n):
        if not visited[i] and (i == 0 or nums[i] != nums[i - 1] or visited[i - 1]):
            visited[i] = True
            stack.append(nums[i])
            sol(n, m, stack, visited, nums, used)
            visited[i] = False
            stack.pop()


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    nums = sorted(map(int, input().split()))
    visited = [False] * n
    stack = []

    sol(n, m, stack, visited, nums, used=None)


if __name__ == "__main__":
    main()
