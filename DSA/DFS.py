def dfs(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        print (visited)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Example graph as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()
dfs(graph, 'A', visited)
