import numpy as np
import matplotlib.pyplot as plt

# ADD OBSTACLES FOR NEXT REVISIONS

SS_SIZE = 30 # size of state_space

# np.random.rand is useful when we want to add obstacles
# state_space = np.random.rand(SS_SIZE, SS_SIZE)*0.0

# without obstacles just use zeros()
state_space = np.zeros((SS_SIZE, SS_SIZE), dtype=float)
start = (0, 6) # start 
goal = (28, 17) # finish

moves = ((0, 1), (1, 0), (-1, 0), (0, -1)) # define move actions

visited = [] # init list of visited points

visited.append(start) # add start point as visited point

# support variable for checking if start point is out of map
pre_checking = 0

# support variable to increment visited index to work with the next point
visited_index = 0

# support variable for checking if we are in the goal point
find_solution = False

# Dictionary - very powerful instrument. Was used to reconstruct path to goal
# We know, that dictionary doesn't allow duplicate keys. And we know, that in
# we won't have the same child point. So we could have a child node as key, and
# a parent point (from which child point was generated) as value to it. So to
# familiar with first practical usage of dictionary, see line 86
parent_map = {}

while (find_solution == False): 
    
    current_state = visited[visited_index]
    visited_index += 1

    for row, col in moves:

        if (find_solution == True):
            break 

        # if condition that protects from starting pointm which is located out of map
        if pre_checking == 0:
            if current_state[0] >= 0 and current_state[0] < SS_SIZE and current_state[1] >= 0 and current_state[1] < SS_SIZE:
                pre_checking += 1
                # visited.append(current_state) # and add current state to it
                pass
            else:
                find_solution = True
                branch_end = True
                print("START IS OUT OF MAP!")
                break

        new_state = current_state[0] + row, current_state[1] + col # define new_state to check, if it was either in visited or out of map 

        # check if currently we are not in th goal
        if current_state == goal:
            print("YUPI!")
            find_solution = True
            break

        # check if we are out of map
        if new_state[0] >= 0 and new_state[0] < SS_SIZE and new_state[1] >= 0 and new_state[1] < SS_SIZE:
            pass
        else:
            branch_end = True
            continue

        # check if we were not be here before
        if new_state not in visited:
            visited.append(new_state)
            parent_map[new_state] = current_state 
        else:
            branch_end = True
            continue

current = goal
path = []

while (current != start):
    path.append(current)
    current = parent_map[current]

row_path, col_path = zip(*path)
state_space[row_path, col_path] = 0.75

state_space[start] = 1
state_space[goal] = 2

# print total steps
print("Total steps is", len(visited))
plt.imshow(state_space)
plt.colorbar()
plt.show()
