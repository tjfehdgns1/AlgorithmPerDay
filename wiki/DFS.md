### 깊이 우선 탐색(DFS)
*Depth First Search*

![DFS](https://github.com/tjfehdgns1/AlgorithmPerDay/blob/main/image/DFS.gif?raw=true)

***

스택 자료구조 혹은 재귀함수를 이용한다

```python
def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end=' ')
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

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
result = dfs(graph, 1, visited) # 1 2 7 6 8 3 4 5
```

