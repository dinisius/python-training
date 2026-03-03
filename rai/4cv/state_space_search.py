import numpy as np
import pylab as plt


# PROJIT DICTIONARY A VSECHNY UKOLY

def check_boundaries(new_state, state_space):
    row, col = np.shape(state_space)
    return new_state[0] >= 0 and new_state[0] < row and new_state[1] >= 0 and new_state[1] < col

# init
print("State Space Search")
max_depth = 18
start = (3, 3)
goal = (11, 10)
state_space = (np.random.rand(12, 12)) * 0.0

# list of possible actions
actions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

# support structures
# visited = [start]
visited = {}
visited[start] = start, 0
open_nodes = [start]


#state-space search main
while len(open_nodes) > 0:
    
    node = open_nodes[0]
    open_nodes.remove(node)
    # visited.append(node)

    if node == goal:
        print('Goal reached!')
        break

    for row, col in actions:
        new_state = node[0] + row, node[1] + col
        _, cost = visited[node]
        if new_state not in visited.keys() and check_boundaries(new_state, state_space) and cost <= max_depth:
            visited[new_state] = node, cost+1
            # open_nodes.append(new_state)    # BFS
            open_nodes.insert(0, new_state) # DFS, zajimavy. Doma si to nakresli a porovnej vysledek se svou predstavou

# path reconstruction
node = goal

while node != start:
    prev_state, _ = visited[node]
    print(prev_state)
    state_space[prev_state[0], prev_state[1]] = 1
    node = prev_state

# CHCEME NASTAVIT HLOUBKU

# show results
plt.imshow(state_space)
plt.show()