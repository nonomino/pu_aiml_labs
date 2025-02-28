# Implement using OOP approach the a_star search algorithm with a graph
# and a heuristic function

import heapq
import math


class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def neighbors(self, node):
        return self.edges[node]

    def cost(self, from_node, to_node):
        return self.weights[(from_node, to_node)]


class AStar:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic

    def search(self, start, goal):
        frontier = []
        heapq.heappush(frontier, (0, start))
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while frontier:
            current = heapq.heappop(frontier)[1]

            if current == goal:
                break

            for next in self.graph.neighbors(current):
                new_cost = cost_so_far[current] + self.graph.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(goal, next)
                    heapq.heappush(frontier, (priority, next))
                    came_from[next] = current

        return came_from, cost_so_far


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


graph = Graph()

graph.edges = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

graph.weights = {
    ('A', 'B'): 1,
    ('A', 'C'): 2,
    ('B', 'D'): 3,
    ('B', 'E'): 4,
    ('C', 'F'): 5,
    ('E', 'F'): 6
}

a_star = AStar(graph, heuristic)
start = 'A'
goal = 'F'
came_from, cost_so_far = a_star.search(start, goal)
current = goal
path = []
while current != start:
    path.append(current)
    current = came_from[current]
    path.append(start)
    path.reverse()
print(path)
print(cost_so_far)
