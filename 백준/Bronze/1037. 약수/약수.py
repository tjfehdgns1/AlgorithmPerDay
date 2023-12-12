import sys


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arg = sorted(map(int, input().split()))
    
    if len(arg) == 1:
        print(arg[0] * arg[0])
    else: 
        print(arg[0] * arg[-1])