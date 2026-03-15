from copy import deepcopy

def is_valid_move(state, from_peg, to_peg):
    if not state[from_peg]:
        return False
    if not state[to_peg]:
        return True
    return state[from_peg][-1] < state[to_peg][-1]

def move(state, from_peg, to_peg):
    new_state = deepcopy(state)
    disk = new_state[from_peg].pop()
    new_state[to_peg].append(disk)
    return new_state

def state_to_tuple(state):
    return tuple(tuple(peg) for peg in state)

def dfs(state, goal, visited, path):
    if state == goal:
        return path

    visited.add(state_to_tuple(state))

    for i in range(3):
        for j in range(3):
            if i != j and is_valid_move(state, i, j):
                new_state = move(state, i, j)
                t = state_to_tuple(new_state)

                if t not in visited:
                    result = dfs(new_state, goal, visited, path + [(i, j)])
                    if result:
                        return result
    return None


def solve_hanoi(n):
    start = [list(range(n, 0, -1)), [], []]
    goal = [[], [], list(range(n, 0, -1))]

    solution = dfs(start, goal, set(), [])

    if solution:
        for step, (f, t) in enumerate(solution, 1):
            print(f"Krok {step}: {f} -> {t}")
    else:
        print("Řešení nenalezeno")


if __name__ == "__main__":
    solve_hanoi(5)