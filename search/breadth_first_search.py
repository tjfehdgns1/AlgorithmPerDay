from collections import deque


def bfs(graph, start):
    visited = set()  # 방문한 노드를 기록하기 위한 집합
    queue = deque([start])  # 큐를 사용하여 탐색할 노드를 관리

    while queue:
        node = queue.popleft()  # 큐에서 노드를 하나 꺼낸다
        if node not in visited:
            print(node, end=" ")  # 노드를 방문한 것으로 표시하고 출력
            visited.add(node)  # 방문한 노드를 집합에 추가
            queue.extend(graph[node] - visited)  # 방문하지 않은 이웃 노드들을 큐에 추가
