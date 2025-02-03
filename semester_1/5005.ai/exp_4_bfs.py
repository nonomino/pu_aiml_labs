# Implement BFS (Breadth First Search) algorithm to find the shortest path
# between two nodes in a graph.

def bfs(graph, start, end):
    visited = []
    queue = [[start]]
    if start == end:
        return "Start = End"
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                print(f"Updated path is {new_path}")
                queue.append(new_path)
                if neighbour == end:
                    return new_path
            visited.append(node)
            print(f"Visited nodes currently: {visited}")
    return "Unreachable"


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    graph2 = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': []
    }
    print(bfs(graph2, '5', '8'))
    # print(bfs(graph, 'A', 'D'))
    # print(bfs(graph, 'A', 'A'))
    # print(bfs(graph, 'A', 'Z'))
