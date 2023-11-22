import sys

def solution(grid, x, y, N):
    color = grid[x][y]
    result = [0, 0]

    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != grid[i][j]:
                # Accumulate results from recursive calls
                result[0] += solution(grid, x, y, N//2)[0] + solution(grid, x, y + N//2, N//2)[0]
                result[1] += solution(grid, x, y, N//2)[1] + solution(grid, x, y + N//2, N//2)[1]
                result[0] += solution(grid, x + N//2, y, N//2)[0] + solution(grid, x + N//2, y + N//2, N//2)[0]
                result[1] += solution(grid, x + N//2, y, N//2)[1] + solution(grid, x + N//2, y + N//2, N//2)[1]
                return result

    if color == 0:
        result[0] += 1
    else:
        result[1] += 1
    
    return result

def main():
    input_func = sys.stdin.readline
    n = int(input_func())
    grid = []

    for i in range(n):
        grid.append(list(map(int, input_func().split())))

    zero, one = solution(grid, 0, 0, n)

    print(zero)
    print(one)

if __name__ == "__main__":
    main()
