import numpy as np
import matplotlib.pyplot as plt

SS_SIZE = 20 # size of state_space
state_space = np.zeros((SS_SIZE, SS_SIZE), dtype=float)
start = (0, 6) # start 
goal = (10, 17) # finish

color_begin = 0 # indicate starting point
color_end = color_begin + 1 # indicate ending point
state_space[start] = color_begin

moves = ((0, -1), (-1, 0), (1, 0), (0, 1)) # define move actions

current_state = start # define start point as current state

visited = [] # init list of visited points
 
plt.imshow(state_space)
plt.show()

pre_checking = 0

find_solution = False

while (find_solution == False): 

    for row, col in moves:
        if (find_solution == True):
            break 

        branch_end = False # when we hit the branches dead-end -> change move action

        while(branch_end == False):

            # if condition that protects from starting pointm which is located out of map
            if pre_checking == 0:
                if current_state[0] >= 0 and current_state[0] < SS_SIZE and current_state[1] >= 0 and current_state[1] < SS_SIZE:
                    pre_checking += 1
                    visited.append(current_state) # and add current state to it
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
            else:
                branch_end = True
                continue
            
            # if every condition is valid -> change current_state to the new
            current_state = new_state
            print(current_state)
 

radky, sloupce = zip(*visited) 
color = 0.75

# cycle for step-by-step drawing the path
for i in visited:
    color += 1/len(visited)
    state_space[i] = color + 1/len(visited)

state_space[start] = 1
state_space[goal] = 2

# print total steps
print("Total steps is", len(visited))
plt.imshow(state_space, vmin = 0, vmax = 2)
plt.colorbar()
plt.show()
