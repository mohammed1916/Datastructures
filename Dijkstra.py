import heapq
from tabulate import tabulate

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = [(0, start)]
    previous = {node: [] for node in graph}  # Initialize previous dictionary
    visited = set()

    """iteration = 1
    table = []

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue


        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            row = [iteration, weight, current_node, neighbor, distance, queue, distances, previous]
            table.append(row)

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = [current_node]  # Update previous dictionary
                heapq.heappush(queue, (distance, neighbor))

            headers = ["Iteration",     "Weight", "Current Node", "Neighbor", "Distance", "Queue", "Distances", "Previous"]
            print(tabulate(table, headers, tablefmt="grid"))
            iteration += 1


    return distances, previous"""

    iteration = 1
    table = []

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue
        if current_node in visited:
            continue
        visited.add(current_node)

        row = [iteration, current_node, current_distance, queue, distances, previous]
        table.append(row)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = [current_node]  # Update previous dictionary
                heapq.heappush(queue, (distance, neighbor))

        headers = ["Iteration", "Current Node", "Current Distance", "Queue", "Distances", "Previous"]
        print(tabulate(table, headers, tablefmt="grid"))
        iteration += 1


    return distances, previous

# graph = {
#     'A': {'B': 5, 'C': 2},
#     'B': {'A': 5, 'C': 1, 'D': 3},
#     'C': {'A': 2, 'B': 1, 'D': 2},
#     'D': {'B': 3, 'C': 2}
# }
graph = {
    'A': {'B': 6, 'C': 4},
    'B': {'A': 6, 'D': 1, 'E': 7},
    'C': {'A': 4, 'D': 8},
    'D': {'B': 1, 'C': 8, 'E': 3},
    'E': {'B': 7, 'D': 3}
}

start_node = 'A'
distances, previous = dijkstra(graph, start_node)
print("Shortest distances from source A:\n", distances)
print("Previous nodes:\n", previous)
