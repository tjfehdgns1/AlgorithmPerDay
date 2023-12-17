import sys
import heapq


class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, value):
        heapq.heappush(self.heap, -value)
        
    def pop(self):
        if self.heap:
            return -heapq.heappop(self.heap)
        else:
            return 0
            
            
def main():
    input = sys.stdin.readline
    n = int(input())
    max_heap = MaxHeap()
    
    for _ in range(n):
        given = int(input())
        if given == 0:
            print(max_heap.pop())
        else:
            max_heap.push(given)
        
        
if __name__ == "__main__":
    main()