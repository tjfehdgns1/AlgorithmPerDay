### 너브 우선 탐색(BFS)
*Breadth First Search* 

![BFS](https://github.com/tjfehdgns1/AlgorithmPerDay/blob/70fd23e0e913b810f8a24c4b5e66e9f384eb57e7/image/BFS.gif)

***

큐 자료구조를 이용한다

```python
from collections import deque

def bfs(graph, start, visited) :
    queue = deque([start])
    visited[start] = True

    while queue :
        v = queue.popleft()
        print(v, end='')
        for i in graph[v]
            if not visited[i]
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * 9
result = bfs(graph, 1, visited) # 1 2 3 8 7 4 5 6
```

![graph](https://github.com/tjfehdgns1/AlgorithmPerDay/blob/ce0940c6cb4b26b35ff27a5b1e783f71902eff1d/image/graph.png)

***