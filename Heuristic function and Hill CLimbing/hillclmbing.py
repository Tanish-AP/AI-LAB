
import random

N = 4

def cost(state):
    c = 0
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                c += 1
    return c

def neighbors(state):
    result = []
    for row in range(N):
        for col in range(N):
            if col != state[row]:
                nb = state.copy()
                nb[row] = col
                result.append(nb)
    return result

def hill_climbing(state):
    while True:
        current_cost = cost(state)

        if current_cost == 0:
            return state, True

        best, best_cost = None, current_cost

        for nb in neighbors(state):
            c = cost(nb)
            if c < best_cost:
                best, best_cost = nb, c

        if best is None:
            return state, False

        state = best

while True:
    start = [random.randint(0, N - 1) for _ in range(N)]
    final, solved = hill_climbing(start)

    if solved:
        break

print("N =", N)
print("Number of queens:", N)
print("Number of attacking pairs:", cost(final))
print("Solution Found" if solved else "Solution Not Found")

for r in range(N):
    print(" ".join("Q" if final[r] == c else "." for c in range(N)))
