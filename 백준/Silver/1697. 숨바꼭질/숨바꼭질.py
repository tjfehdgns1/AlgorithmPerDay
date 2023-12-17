from collections import deque

def bfs(start, end):
    visited = [False] * 100001
    queue = deque([(start, 0)])

    while queue:
        current, time = queue.popleft()

        if current == end:
            return time

        next_positions = [current - 1, current + 1, 2 * current]

        for next_pos in next_positions:
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

N, K = map(int, input().split())

result = bfs(N, K)
print(result)
