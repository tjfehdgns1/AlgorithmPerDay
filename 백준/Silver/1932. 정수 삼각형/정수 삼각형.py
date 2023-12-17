def find_max_path_sum(triangle):
    n = len(triangle)

    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    return triangle[0][0]


if __name__ == "__main__":
    n = int(input())
    triangle = [list(map(int, input().split())) for _ in range(n)]

    result = find_max_path_sum(triangle)
    print(result)
