import sys
from collections import deque


def bfs(root, tree):
    q = deque([1])
    
    while q:
        curr = q.popleft()
        for nxt in tree[curr]:
            if root[nxt] == 0:
                root[nxt] = curr
                q.append(nxt)
    
    
def main():
    input = sys.stdin.readline
    n = int(input())
    root = [0] * (n + 1)
    
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
        
    bfs(root, tree)
    
    for i in root[2:]:
        print(i)
        
if __name__ == "__main__":
    main()