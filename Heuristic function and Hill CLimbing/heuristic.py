
import heapq

INITIAL = (2, 8, 3,
           1, 6, 4,
           7, 0, 5)

GOAL = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)

GOAL_POS = {t: divmod(i, 3) for i, t in enumerate(GOAL)}

def misplaced_tiles(state):
    return sum(1 for i, t in enumerate(state)
               if t != 0 and t != GOAL[i])

def manhattan(state):
    total = 0
    for i, t in enumerate(state):
        if t != 0:
            r, c = divmod(i, 3)
            gr, gc = GOAL_POS[t]
            total += abs(r - gr) + abs(c - gc)
    return total

def neighbors(state):
    b = state.index(0)
    r, c = divmod(b, 3)

    moves = {"Up": (-1, 0), "Down": (1, 0),
             "Left": (0, -1), "Right": (0, 1)}

    for name, (dr, dc) in moves.items():
        nr, nc = r + dr, c + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            n = nr * 3 + nc
            s = list(state)
            s[b], s[n] = s[n], s[b]
            yield name, tuple(s)

def a_star(start, heuristic):
    open_list = [(heuristic(start), 0, start)]
    parent = {start: (None, None)}
    best_g = {start: 0}
    closed = set()

    while open_list:
        f, g, state = heapq.heappop(open_list)

        if state in closed:
            continue

        closed.add(state)

        if state == GOAL:
            path = []
            while state is not None:
                prev, move = parent[state]
                path.append((move, state))
                state = prev
            return path[::-1]

        for move, nxt in neighbors(state):
            ng = g + 1

            if nxt not in best_g or ng < best_g[nxt]:
                best_g[nxt] = ng
                parent[nxt] = (state, move)
                heapq.heappush(open_list,
                               (ng + heuristic(nxt), ng, nxt))

    return None

def print_board(state):
    for i in range(0, 9, 3):
        print(" ".join(str(t) if t else "_" for t in state[i:i+3]))

def run(heuristic):
    path = a_star(INITIAL, heuristic)

    if path is None:
        print("Solution Not Found")
        return

    print("Solution Found")
    print("Number of moves:", len(path) - 1)

    for step, (move, state) in enumerate(path):
        print("\nStep", step)
        print_board(state)

run(misplaced_tiles)
run(manhattan)
