from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def bfsTraversal(self, vertex):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(vertex)
        visited[vertex] = True
        while queue:
            vertex = queue.pop(0)
            print (vertex, end = " ")
            for i in self.graph[vertex]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def DFS_helper(self, u, visited):
        visited.add(u)
        print(u, end = " ")
        for v in self.graph[u]:
            if(v not in visited):
                self.DFS_helper(v, visited)
    def DFS(self, u):
        visited=set()
        self.DFS_helper(u,visited)

graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(2, 1)
graph.addEdge(2, 5)
graph.addEdge(3, 6)

print ("The BFS Traversal from node 1 is: ")
graph.bfsTraversal(1)

print("\nThe DFS traversal from node 0 is:")
graph.DFS(0)

