from collections import deque

N, K = map(int, input().split())

result = []

circle = deque(range(1, N + 1))

def josephus(circle, K):
    circle.rotate(-K + 1)
    removed_person = circle.popleft()
    return removed_person

while circle:
    removed_person = josephus(circle, K)
    result.append(removed_person)

print("<" + ", ".join(map(str, result)) + ">")
