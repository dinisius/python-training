import copy

print("Towers of Hanoi - Recursion DFS")

start = [[1, 2], [], []]
goal = [[], [], [1, 2]]

visited = []

actions = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

visited.append(start)

def apply_action(state, here, there):

    new_state = copy.deepcopy(state)

    if len(new_state[here]) > 0:
        new_disk = new_state[here].pop(0)
        new_state[there].insert(0, new_disk)

    if len(new_state[there]) > 1 and new_state[there][0] < new_state[there][1] or len(new_state[there]) == 1:
        return new_state
    else:
        return False


def state_space_search(state, goal, depth):

    if state == goal:
        print("Yupi!")
        return True
    
    if depth > 0:
        depth -= 1
        pass
    else:
        print("Depth end")
        return False
    
    for here, there in actions:
        new_state = apply_action(state, here, there)

        if (new_state and new_state not in visited):
            visited.append(new_state)
            if(state_space_search(new_state, goal, depth)):
                print("path", new_state)
                return True
        
print("path", state_space_search(start, goal, 100))

