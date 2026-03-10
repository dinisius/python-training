import numpy as np
import matplotlib.pyplot as plt
import copy

start = [[1, 2, 3], [], []]

state_space = start

goal = [1, 2, 3] # finish

actions = ((0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1))

# actions = (0, 1, 2)

# actions = [state_space.insert(0, state_space[0][0])]

current_state = start # define start point as current state

visited = [] # init list of visited points

visited.append(start)
 
pre_checking = 0

find_solution = False

while (find_solution == False): 

    for here, there in actions:
        if (find_solution == True):
            break 

        branch_end = False # when we hit the branches dead-end -> change move action

        while(branch_end == False):

            new_state = copy.deepcopy(current_state)
            
            if len(new_state[here]) > 0:    
                new_disk = new_state[here].pop(0)
                new_state[there].insert(0, new_disk)
            else:
                break

            # check if currently we are not in th goal
            if current_state[2] == goal:
                print("YUPI!")
                find_solution = True
                break

            if len(new_state[there]) > 1:
                if new_state[there][0] > new_state[there][1]:
                    print("Out of rules!")
                    break
            else:
                print("Move is acceptable")
                pass

            # check if we were not be here before
            if new_state not in visited:
                visited.append(new_state) 
            else:
                branch_end = True
                continue         
            
            # if every condition is valid -> change current_state to the new
            current_state = new_state
            print(current_state)