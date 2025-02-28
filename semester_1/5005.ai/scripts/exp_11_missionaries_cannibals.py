from collections import deque


def missionaries_cannibals():
    queue, visited = deque([((3, 3, 1), [])]), set()
    while queue:
        (m, c, b), path = queue.popleft()
        if (m, c, b) == (0, 0, 0):
            return path + [(0, 0, 0)]
        if (m, c, b) in visited:
            continue
        visited.add((m, c, b))
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for dm, dc in moves:
            nm, nc, nb = m - dm * b + dm * (1 - b), c - dc * b + dc * (1 - b), 1 - b
            if 0 <= nm <= 3 and 0 <= nc <= 3 and (nm == 0 or nm >= nc) and (3 - nm == 0 or 3 - nm >= 3 - nc):
                queue.append(((nm, nc, nb), path + [(m, c, b)]))


print(missionaries_cannibals())