import numpy as np
import pylab as plt


## init
print('Depth first search')
start = [[3, 2, 1], [], []]
goal = [[], [], [3, 2, 1]]

## variables
state_space = []
# state_space = np.random.rand(12, 12) * 0.0
# state_space[start[0], start[1]] = 1
# state_space[goal[0], goal[1]] = 2

visited = []

def apply_action(state, action):
    rods = [list(s) for s in state]
    source, dest = action

    if len(rods[source]) == 0:
        return None
    
    disk = rods[source][-1]

    if len(rods[dest]) > 0 and rods[dest][-1] < disk:
        return None

    rods[source].pop()
    rods[dest].append(disk)

    return rods

def check_bounderies(new_state, state_space):
    return True
    # row, col = np.shape(state_space)
    # return new_state[0] >= 0 and new_state[0] < row and new_state[1] >= 0 and new_state[1] < col 

def depth_first_search(state, goal, depth, state_space, visited):

    visited.append(state)

    if state == goal:
        return True

    if depth <= 0:
        return False


    actions = [(0, 1), (0, 2), 
               (1, 0), (1, 2),
               (2, 0), (2, 1)]
    
    for action in actions:
        new_state = apply_action(state, action)
        if new_state is not None and new_state not in visited:
            if depth_first_search(new_state, goal, depth-1, state_space, visited):
                print('path', new_state)
                return True
            # else:
            #     return False


print(depth_first_search(start, goal, 1000, state_space, visited))
print(start)