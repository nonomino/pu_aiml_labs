from functools import lru_cache

def tsp_f(graph):
    n = len(graph)

    @lru_cache(None)
    def visit(mask, pos):
        if mask == (1 << n) - 1:
            return graph[pos][0]
        return min(graph[pos][i] + visit(mask | (1 << i), i) for i in range(n) if not mask & (1 << i))

    return visit(1, 0)

graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
print(tsp_f(graph))
