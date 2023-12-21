import sys


def ioi(string: str, n: int, m: int) -> int:
    front, back = 0, 0
    cnt = 0
    
    while back < m:
        if string[back:back + 3] == "IOI":
            back += 2
            if back - front == 2 * n:
                cnt += 1
                front += 2
        else:
            front = back = back + 1
    
    return cnt
if __name__ == "__main__":    
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    S = input().rstrip()    
    result = ioi(S, N, M)
    print(result)