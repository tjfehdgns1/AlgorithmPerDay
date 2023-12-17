import sys


input = sys.stdin.readline


def solution(given):
    result = 1
    for category in given:
        result *= len(given[category]) + 1

    return result - 1


def main():
    n = int(input())
    for _ in range(n):
        m = int(input())
        given = dict()
        for _ in range(m):
            v, k = input().rstrip().split()
            if k not in given:
                given[k] = [v]
            else:
                given[k].append(v)
        result = solution(given)
        print(result)


if __name__ == "__main__":
    main()
