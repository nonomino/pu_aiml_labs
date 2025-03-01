from functools import lru_cache

def tsp_f(graph):
    @lru_cache(None)
    def visit(mask, pos):
        if mask == (1 << len(graph)) - 1:
            return graph[pos][0]
        return min(graph[pos][i] + visit(mask | (1 << i), i) for i in range(len(graph)) if not mask & (1 << i))

    return visit(1, 0)

n = int(input("Enter number of cities: "))
print("Enter adjacency matrix row by row:")
graph = [list(map(int, input().split())) for _ in range(n)]

print(f"Minimum TSP cost: {tsp_f(tuple(map(tuple, graph)))}")