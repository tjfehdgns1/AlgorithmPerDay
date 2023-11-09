from sys import stdin


def solution(command: str, num=None):
    global s

    match command:
        case "add":
            if 1 <= num <= 20 and num not in s:
                s.add(num)
        case "remove":
            if 1 <= num <= 20 and num in s:
                s.remove(num)
        case "check":
            print(1 if num in s else 0)
        case "toggle":
            if 1 <= num <= 20:
                if num in s:
                    s.remove(num)
                else:
                    s.add(num)
        case "all":
            s = set(range(1, 21))
        case "empty":
            s = set()


input = stdin.readline
s = set()
n = int(input())

for _ in range(n):
    given = input().split()
    command = given[0]
    num = int(given[1]) if len(given) > 1 else None
    solution(command, num)
