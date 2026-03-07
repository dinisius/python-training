import numpy as np
import pylab as plt

print("Depth First Search")

dimensions = 30
start = (10, 10)
goal = (20, 20)
max_depth = 1500
visited = []

state_space = (np.random.rand(dimensions, dimensions) > 0.9) * 0.0
plt.imshow(state_space)
plt.show()
state_space[5:20, 15] = 1 
plt.imshow(state_space)
plt.show()

for i in range(dimensions):
    for j in range(dimensions):
        if state_space[i, j] == 1:
            visited.append((i, j))

actions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def depth_first_search(state, goal, depth, state_space, visited, actions):
    print(state)
    visited.append(state)

    if state == goal:
        return True

    if depth <= 0:
        return False
    
    row_state, col_state = state
    for row, col in actions:
        new_state = row_state + row, col_state + col
        if new_state not in visited and new_state[0] > 0 and new_state[0] < dimensions and new_state[1] > 0 and new_state[1] < dimensions:
            return depth_first_search(new_state, goal, depth-1, state_space, visited, actions)



depth_first_search(start, goal, max_depth, state_space, visited, actions)

# Show results
for row, col in visited:
    state_space[row, col] = 4

state_space[start[0], start[1]] = 2
state_space[goal[0], goal[1]] = 3

plt.imshow(state_space)
plt.show()