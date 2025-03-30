def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=" ")  # Process the node
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(graph, neighbor, visited)

# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run DFS from node 'A'
dfs(graph, 'A')