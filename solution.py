import sys


def solution(grid: list, position: list):
    


    pass
        
if __name__ == "__main__":
    input = sys.stdin.readline
    n, t = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(n)]
    for row in grid:
        print(row)

    for _ in range(t):
        position = list(map(int ,input().split()))
        print(position)
        solution(grid, position)

    

    
        