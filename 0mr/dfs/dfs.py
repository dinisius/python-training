import numpy as np
import pylab as plt

## init
print('Depth first search')

start = (3, 3) # tuple
goal = (3, 5)

## variables
state_space = np.random.rand(20, 20) * 0.0
state_space[start[0], start[1]] = 1
state_space[goal[0], goal[1]] = 2

visited = [start] # list

def check_boundaries(new_state, state_space):
    
    row, col = np.shape(state_space)
    return new_state[0] >= 0 and new_state[0] < row and new_state[1] >= 0 and new_state[1] < col

def depth_first_search(state, goal, depth, state_space, visited):

    visited.append(state)

    # Pokud jsme v cili, vyhra
    if state == goal:
        return True

    ## Kontrola, jestli hloubka neni rovna 0
    if depth <= 0:
        return False
        ## pass  # proc pass

    ## Po kazdem cyklu odectu 1 od hloubky
    # print(depth)
    
    actions = [(0, 1), (-1, 0), (0, -1), (1, 0)] # list

    for row, col in actions:
        new_state = state[0] + row, state[1] + col
        print(new_state, depth)
        if new_state not in visited and check_boundaries(new_state, state_space):
            if depth_first_search(new_state, goal, depth-1, state_space, visited):
                print('path', new_state)
                return True
            else:
                return False

    depth_first_search(state, goal, depth-1, state_space, visited)

print(depth_first_search(start, goal, 100, state_space, visited))

plt.imshow(state_space)
plt.show()
