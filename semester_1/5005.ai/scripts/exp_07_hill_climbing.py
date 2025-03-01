import heapq

def heuristic(state, goal):
    return sum(s != g and s != 0 for s, g in zip(state, goal))

def neighbors(state):
    i = state.index(0)
    swaps = [(1, 3), (-1, -3), (3, 1), (-3, -1)]
    for dx, dy in swaps:
        j = i + dx if abs((i % 3) - ((i + dx) % 3)) <= 1 else i + dy
        if 0 <= j < 9:
            new_state = list(state)
            new_state[i], new_state[j] = new_state[j], new_state[i]
            yield tuple(new_state)

def hill_climb(start, goal):
    queue = [(heuristic(start, goal), start)]
    visited = set()
    while queue:
        _, state = heapq.heappop(queue)
        if state == goal:
            return state
        if state in visited:
            continue
        visited.add(state)
        print(f"Current state: {state[:3]}\n               {state[3:6]}\n               {state[6:]}\n")
        for n in neighbors(state):
            if n not in visited:
                heapq.heappush(queue, (heuristic(n, goal), n))
    print("No solution found.")

def get_input(msg):
    return tuple(map(int, input(msg).split()))

start = get_input("Enter initial state (space-separated 9 numbers, 0 for empty): ")
goal = get_input("Enter goal state: ")

hill_climb(start, goal)