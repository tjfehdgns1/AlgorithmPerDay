### 깊이 우선 탐색(DFS)
*Depth First Search*

![DFS](https://github.com/tjfehdgns1/AlgorithmPerDay/blob/main/image/DFS.gif?raw=true)


'''python
def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end=' ')
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)
'''
