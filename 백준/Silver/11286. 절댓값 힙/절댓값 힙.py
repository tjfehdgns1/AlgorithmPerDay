import sys
import heapq


input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    a = int(input())
    
    if a != 0:
        heapq.heappush(heap, (abs(a), a))
    else:
        if not heap:
            print(0)
        else:
            _, value = heapq.heappop(heap)
            print(value)
            