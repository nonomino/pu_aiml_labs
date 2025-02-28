# Name: Anas Muhammmed Sahil
# Date: 21-01-2025
# Roll Number: 20242AIE0010

from typing import List


def a_star(start, stop):
    open_set, closed_set = {start}, set()
    g, parents = {start: 0}, {start: start}
    cost = 0
    while open_set:
        current = min(open_set, key=lambda node: g[node]
                      + H_dist.get(node, None))
        if current == stop or current not in graph_nodes:
            pass
        else:
            for neighbor, weight in graph_nodes.get(current, None):
                print(neighbor, end=', ')
                if neighbor not in open_set and neighbor not in closed_set:
                    open_set.add(neighbor)
                    parents[neighbor] = current
                    g[neighbor] = g[current] + weight
                    cost = g[neighbor] + H_dist.get(neighbor, None)
                elif g[neighbor] > g[current] + weight:
                    open_set.add(neighbor)
                    parents[neighbor] = current
                    g[neighbor] = g[current] + weight
                    closed_set.discard(neighbor)
                    cost = g[neighbor] + H_dist.get(neighbor, None)
            print()
        if not current:
            print('Path does not exist!')
            return
        if current == stop:
            path: List = []
            while parents[current] != current:
                path.append(current)
                current = parents[current]
            path.append(start)
            path.reverse()
            print('Path found:', path)
            print('Cost:', cost)
            return path
        open_set.remove(current)
        closed_set.add(current)
    print('Path does not exist!')
    return None


H_dist = {
    'A': 5,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 3,
    'F': 1,
    'G': 0,
}

graph_nodes = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3), ('C', 2)],
    'C': [('E', 5)],
    'D': [('G', 4), ('F', 2)],
    'E': [('G', 3)],
    'F': [('G', 1)],
}

# f(n) = g(n) + h(n)
a_star('A', 'G')
