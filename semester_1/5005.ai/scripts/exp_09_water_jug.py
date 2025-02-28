from collections import deque

def water_jug(j1, j2, target):
    visited, queue = set(), deque([(0, 0)])
    while queue:
        a, b = queue.popleft()
        if (a, b) in visited:
            continue
        visited.add((a, b))
        
        print(f"Current state: ({a}, {b})")
        
        if a == target or b == target:
            print(f"Solution found: ({a}, {b})")
            return (a, b)

        next_states = [
            (j1, b), (a, j2), (0, b), (a, 0),
            (a - min(a, j2 - b), b + min(a, j2 - b)),
            (a + min(b, j1 - a), b - min(b, j1 - a))
        ]

        for state in next_states:
            if state not in visited:
                print(f"Exploring: {state}")
                queue.append(state)
    
    print("No solution found")
    return None

print(water_jug(4, 3, 2))  # Example usage