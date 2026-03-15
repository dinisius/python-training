import numpy as np
import matplotlib.pyplot as plt
import copy

# startin point
start = [[1, 2, 3, 4, 5], [], []]

goal = start[0].copy() # finish

# action is represented by typles 1x2
# first element is pilar where we are now
# second element is pilar where we want to move
actions = ((0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1))

current_state = start # define start point as current state

visited = [] # init list of visited points

visited_dict = {}

visited.append(start) # add start as first visited point

# support variable to run while loop untill solution is not find
# i did it because of for loop will be performed only 6x (in our case)
# and right afte action tuple ends, for end as well
find_solution = False 

pomoc = 0
                    
while (find_solution == False): 

    # for loop for changing actions
    for here, there in actions:
        if (find_solution == True):
            break 

        # main 
        while(True):

            new_state = copy.deepcopy(current_state)
            
            if len(new_state[here]) > 0:    
                new_disk = new_state[here].pop(0)
                new_state[there].insert(0, new_disk)
            else:
                break

            # check if currently we are not in the goal
            # WARNING! Compare the same python types
            # Before it goal was a tupple
            # so i never hit this condition because list will never the same as tupple
            # even if they are identical
            if current_state[1] == goal:
                print("YUPI!")
                find_solution = True
                break
            
            # This is our main rule
            # Check, if the disk, that is on the top, is not bigger than disk under it
            if len(new_state[there]) > 1:
                if new_state[there][0] > new_state[there][1]:
                    print("Out of rules!")
                    break
                else:
                    print("Move is acceptable")
                    print(new_state)
                    pass

            # # Check if we were not be here before
            # if new_state not in visited:
            #     visited.append(new_state) 
            # else:
            #     break

            if pomoc == 0:
                pomoc += 1
                visited_dict[str(new_state)] = [(here, there)]
            else:

                if str(new_state) in visited_dict:
                    if (here, there) not in visited_dict[str(new_state)]:
                         visited_dict[str(new_state)].append((here, there))
                    else:
                        print("Already there")
                        break
                else:
                    visited_dict[str(new_state)] = [(here, there)]

            
            # if every condition is valid -> change current_state to the new
            current_state = copy.deepcopy(new_state)
            print(current_state)