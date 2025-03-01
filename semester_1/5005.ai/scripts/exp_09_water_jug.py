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

        for state in [(j1, b), (a, j2), (0, b), (a, 0),
                      (a - min(a, j2 - b), b + min(a, j2 - b)),
                      (a + min(b, j1 - a), b - min(b, j1 - a))]:
            if state not in visited:
                print(f"Exploring: {state}")
                queue.append(state)

    print("No solution found")
    return None

j1 = int(input("Enter capacity of jug 1: "))
j2 = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target amount: "))

print(water_jug(j1, j2, target))