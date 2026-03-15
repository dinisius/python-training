import matplotlib.pyplot as plt
import numpy as np

SS_SIZE = 20

state_space = np.random.rand(SS_SIZE, SS_SIZE) * 0.0

start = (3, 3)
goal = (4, 4)

actions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

visited = []


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
    
def state_space_search(state, depth, goal, actions):

    visited.append(state)

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

            if(state_space_search(new_state, depth, goal, actions)):
                state_space[new_state] = 0.5
                print("path", new_state)
                return True

print(state_space_search(start, 100, goal, actions))

const = len(visited)

const_dva = 1/const

for path in visited:
    
    state_space[path] += const_dva
    const_dva += 1/const

# state_space[goal] = 1
plt.imshow(state_space)
plt.show()