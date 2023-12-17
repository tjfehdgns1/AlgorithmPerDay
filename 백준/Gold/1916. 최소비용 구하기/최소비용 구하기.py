import heapq
import sys


def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances[end]

def main():
    input = sys.stdin.readline
    N = int(input())
    M = int(input())

    graph = {i: {} for i in range(1, N + 1)}

    for _ in range(M):
        start, end, cost = map(int, input().split())
        if end not in graph[start] or cost < graph[start][end]:
            graph[start][end] = cost

    start_city, end_city = map(int, input().split())

    result = dijkstra(graph, start_city, end_city)
    print(result)

if __name__ == "__main__":
    main()
