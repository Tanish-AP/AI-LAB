GOAL = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]  # 0 is empty tile

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right


def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def generate_moves(state):
    x, y = find_zero(state)
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            yield new_state


def dfs(state, visited):
    if state == GOAL:
        return [state]
    visited.add(tuple(tuple(r) for r in state))
    for next_state in generate_moves(state):
        key = tuple(tuple(r) for r in next_state)
        if key not in visited:
            path = dfs(next_state, visited)
            if path:
                return [state] + path
    return None


def print_state(state):
    for row in state:
        print(" ".join(str(n) if n != 0 else "_" for n in row))
    print()


if __name__ == "__main__":
    start = [[1, 2, 3],
             [4, 0, 6],
             [7, 5, 8]]

    solution = dfs(start, set())
    if solution:
        for step in solution:
            print_state(step)
    else:
        print("No solution found.")
