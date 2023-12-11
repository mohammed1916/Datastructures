import heapq

def prims(G):
    distances = {vertex: float('infinity') for vertex in G}
    start_vertex = list(G.keys())[0]
    distances[start_vertex] = 0
    pq = [(0, start_vertex)]
    visited = set()
    mst = []
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        mst.append((current_distance, current_vertex))
        for neighbor, weight in G[current_vertex].items():
            if neighbor not in visited:
                heapq.heappush(pq, (weight, neighbor))
    return mst

G = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1}
}

print(prims(G))
print("weight: ", sum([i[0] for i in prims(G)]))