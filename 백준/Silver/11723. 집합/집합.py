from sys import stdin


def solution(command: str, num=None):
    global s

    if command == "add":
        add(num)
    elif command == "remove":
        remove(num)
    elif command == "check":
        check(num)
    elif command == "toggle":
        toggle(num)
    elif command == "all":
        all_numbers()
    elif command == "empty":
        empty()


def add(num):
    if 1 <= num <= 20 and num not in s:
        s.add(num)


def remove(num):
    if 1 <= num <= 20 and num in s:
        s.remove(num)


def check(num):
    print(1 if num in s else 0)


def toggle(num):
    if 1 <= num <= 20:
        if num in s:
            s.remove(num)
        else:
            s.add(num)


def all_numbers():
    s.update(range(1, 21))


def empty():
    s.clear()


input = stdin.readline
s = set()
n = int(input())

for _ in range(n):
    given = input().split()
    command = given[0]
    num = int(given[1]) if len(given) > 1 else None
    solution(command, num)
