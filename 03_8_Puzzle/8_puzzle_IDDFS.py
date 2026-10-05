GOAL = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dls(state, depth, path, visited):

    if state == GOAL:
        return path

    if depth == 0:
        return None

    key = tuple(map(tuple, state))
    visited.add(key)

    x, y = next((i, j) for i in range(3)
                for j in range(3)
                if state[i][j] == 0)

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:

            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = \
                new_state[nx][ny], new_state[x][y]

            key2 = tuple(map(tuple, new_state))

            if key2 not in visited:

                result = dls(new_state,
                             depth - 1,
                             path + [new_state],
                             visited)

                if result:
                    return result

    return None


def iddfs(start):

    depth = 0

    while True:

        visited = set()

        solution = dls(start,
                       depth,
                       [start],
                       visited)

        if solution:
            return solution

        depth += 1


def print_state(state):
    for row in state:
        print(" ".join("_" if x == 0 else str(x) for x in row))
    print()


start = [[1, 2, 3],
         [4, 0, 6],
         [7, 5, 8]]

solution = iddfs(start)

if solution:
    for state in solution:
        print_state(state)
else:
    print("No solution")
