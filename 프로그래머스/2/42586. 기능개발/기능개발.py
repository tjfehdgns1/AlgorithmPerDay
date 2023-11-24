from collections import deque


def solution(progresses, speeds):
    answer = []
    q = deque()
    for a, b in zip(progresses, speeds):
        q.append((100 - a) // b + ((100 - a) % b > 0))

    print(*q)
    front = 0
    for i in range(len(q)):
        if q[front] < q[i]:
            answer.append(i - front)
            front = i

    answer.append(len(q) - front)

    return answer
