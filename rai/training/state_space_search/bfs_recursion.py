import matplotlib.pyplot as plt
import numpy as np

SS_SIZE = 20

state_space = np.random.rand(SS_SIZE, SS_SIZE) * 0.0

start = (3, 3)
goal = (7, 14)

actions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

visited = []

visited.append(start)

path_memory = {}

i = 0


def apply_action(state, action):
    new_state = state[0] + action[0], state[1] + action[1]
    return new_state

def check_boundaries(state):

    if state[0] >= 0 and state[0] < SS_SIZE and state[1] >= 0 and state[1] < SS_SIZE:
        return True
    else:
        print("Hit the boundary!")
        return False

def check_visited(state):

    if state not in visited:
        return True
    else:
        print("Already in visited!")
        return False
    
def state_space_search(state, depth, goal, actions, i):

    i += 1

    if state == goal:
        print("Yupi!")
        return True

    if depth > 0:
        depth -= 1
        pass
    else:
        print("Depth end")
        return False

    for action in actions:
        new_state = apply_action(state, action)
        if check_boundaries(new_state) and check_visited(new_state):
            visited.append(new_state)
            path_memory[new_state] = state

    if(state_space_search(visited[i], depth, goal, actions, i)):
        print("path", visited[i])
        return True
    

def return_path(path_memory):

    var = True
    zpet = goal
    vektor = [zpet]
    while(var):
        zpet = path_memory[zpet]
        vektor.append(zpet)
        if zpet == start:
            vektor.reverse()
            var = False

    return vektor

print(state_space_search(start, 500, goal, actions, i))


vektor = return_path(path_memory)

const = len(vektor)
const_dva = 1/const
for path in vektor:
    state_space[path] += const_dva
    const_dva += 1/const

# state_space[goal] = 1
plt.imshow(state_space)
plt.show()