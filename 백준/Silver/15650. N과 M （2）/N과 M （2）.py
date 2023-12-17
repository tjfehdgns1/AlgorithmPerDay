def backtracking(N, M, result, visited, start):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return

    for i in range(start, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            backtracking(N, M, result, visited, i + 1)
            visited[i] = False
            result.pop()


def main():
    N, M = map(int, input().split())
    visited = [False] * (N + 1)
    result = []

    backtracking(N, M, result, visited, 1)


if __name__ == "__main__":
    main()
