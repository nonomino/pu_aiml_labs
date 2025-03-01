from collections import deque

def missionaries_cannibals(m, c):
    queue, visited = deque([((m, c, 1), [])]), set()
    while queue:
        (m, c, b), path = queue.popleft()
        if (m, c, b) == (0, 0, 0):
            return path + [(0, 0, 0)]
        if (m, c, b) in visited:
            continue
        visited.add((m, c, b))
        for dm, dc in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
            nm, nc, nb = m - dm * b + dm * (1 - b), c - dc * b + dc * (1 - b), 1 - b
            if 0 <= nm <= 3 and 0 <= nc <= 3 and (nm == 0 or nm >= nc) and (3 - nm == 0 or 3 - nm >= 3 - nc):
                queue.append(((nm, nc, nb), path + [(m, c, b)]))

m = int(input("Enter number of missionaries (≤3): "))
c = int(input("Enter number of cannibals (≤3): "))

if not (0 <= m <= 3 and 0 <= c <= 3):
    print("Invalid input! Must be between 0 and 3.")
else:
    result = missionaries_cannibals(m, c)
    if result:
        print("\nSolution Found!\n")
        for i, (m, c, b) in enumerate(result):
            side = "Left" if b else "Right"
            print(f"Step {i}: Missionaries: {m}, Cannibals: {c}, Boat: {side}")
    else:
        print("\nNo solution possible!")