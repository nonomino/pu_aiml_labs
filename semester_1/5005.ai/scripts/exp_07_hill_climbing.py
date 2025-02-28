import random


def heuristic(state):
    return sum(abs(b % 3 - g % 3) + abs(b // 3 - g // 3) for b, g in enumerate(state) if g)


def get_neighbors(state):
    i = state.index(0)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dx, dy in moves:
        x, y = i % 3 + dx, i // 3 + dy
        if 0 <= x < 3 and 0 <= y < 3:
            new_state = list(state)
            j = y * 3 + x
            new_state[i], new_state[j] = new_state[j], new_state[i]
            neighbors.append(tuple(new_state))
    return neighbors


def hill_climb(start):
    current = start
    while True:
        neighbors = get_neighbors(current)
        next_state = min(neighbors, key=heuristic, default=current)
        if heuristic(next_state) >= heuristic(current):
            return current
        current = next_state


start = tuple(random.sample(range(9), 9))
goal = tuple(range(9))
solution = hill_climb(start)
print("Initial:", start, "\nSolved:", solution)