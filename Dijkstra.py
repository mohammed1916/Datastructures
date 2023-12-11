import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = [(0, start)]
    previous = {node: [] for node in graph}  # Initialize previous dictionary

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = [current_node]  # Update previous dictionary
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous

graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 2},
    'D': {'B': 3, 'C': 2}
}

start_node = 'A'
distances, previous = dijkstra(graph, start_node)
print("Shortest distances from source A:\n", distances)
print("Previous nodes:\n", previous)
