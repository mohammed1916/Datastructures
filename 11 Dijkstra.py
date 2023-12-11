# def printSolution(graph,v):
#     print("Vertex \t Distance from Source")
#     for node in range(v):
#         print(node, "\t\t", graph[node])

# def minDistance(dist, sptSet,V):
#     min = 1e+7
#     for v in range(V):
#         if dist[v] < min and sptSet[v] == False:
#             min = dist[v]
#             min_index = v
#     return min_index
# def dijkstra(src,m):
#     dist = [1e7] * m
#     dist[src] = 0
#     sptSet = [False] * m
#     for cout in range(m):
#         u = minDistance(dist, sptSet,m)
#         sptSet[u] = True
#     for v in range(m):
#         if (graph[u][v] > 0 and
#             sptSet[v] == False and dist[v] > dist[u] + graph[u][v]):
#             dist[v] = dist[u] + graph[u][v]
#     printSolution(dist,m)
# v=5
# graph = [[0,6,4,0,0],[6,0,0,1,7],[4,0,0,8,0],[0,1,8,0,3],[0,7,0,3,0]]
# dijkstra(0,v)