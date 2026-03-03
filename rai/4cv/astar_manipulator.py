import numpy as np
import pylab as plt

from itertools import product

# Init some required variables
arms = 2             # Number of arms
armsLength = 0.5     # Length of each arm in meters
deltaPhi = 1         # Minimal angle difference in movement [degrees]

start = (80, 45)#, 80)
goal = (110, 85)#, 170)
max_depth = 100
visited = {}

# Generate obstacles (lines) into the work space
work_space = [(0, 0.6, 0.1, 0.6)]

# List of available actions
actions = [a for a in product([-deltaPhi, 0, deltaPhi], repeat=arms)]

# https://stackoverflow.com/questions/3252194/numpy-and-line-intersections
def line_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denom == 0:
        return None  # Parallel.
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom
    if 0.0 <= ua <= 1.0 and 0.0 <= ub <= 1.0:
        return (x1 + ua * (x2 - x1)), (y1 + ua * (y2 - y1))
    return None

def armCoordinates(state):
    x2 = np.cos(np.radians(state[0])) * armsLength
    y2 = np.sin(np.radians(state[0])) * armsLength

    x3 = x2 + np.cos(np.radians(state[1])) * armsLength
    y3 = y2 + np.sin(np.radians(state[1])) * armsLength
    return x2, y2, x3, y3


def isFree(state):
    x2, y2, x3, y3 = armCoordinates(state)
    for x4, y4, x5, y5 in work_space:
        if line_intersect(x2, y2, x3, y3, x4, y4, x5, y5) is not None:
            return False
    return True


def manhattanDistance(stateA, stateB):
    """ Manhattan distance """

    # Manhattan distance
    return np.abs(stateA[0] - stateB[0]) + np.abs(stateA[1] - stateB[1])

def select_node(open_nodes):    
    """ Select node """

    # Sort the nodes based on value/cost in the dictionary
    node = min(open_nodes, key=open_nodes.get)
    return node

def a_star(start, goal, depth, state_space, visited, actions):
    """ A* search """

    # Init variables
    prev_state = None, None, None
    g, f = {}, {}
    g[start] = 0
    f[start] = 0

    # Init the list of open nodes
    open_data = {}
    open_data[start] = 0

    # Loop until the goal is finded or some space to explore left 
    while len(open_data) > 0:

        # Get node with the lowest cost
        actual_state = select_node(open_data)
        del open_data[actual_state]

        # If goal reached than done!
        if actual_state == goal:
            print('Goal Reached!')
            return True

        # Get row, col from actual state
        phi2_state, phi3_state = actual_state

        # Move into all possible states from actual state
        for phi2, phi3 in actions:

            # Calculate row, col for new state
            new_state = phi2_state + phi2, phi3_state + phi3

            # Check whether the new state is valid
            #if new_state[0] < 0 or new_state[0] >= 180 or new_state[1] < 0 or new_state[1] >= dimensions or state_space[new_state[0], new_state[1]] > 0.9:
            if new_state[0] < 0 or new_state[0] >= 180 or not isFree(new_state):
                continue

            # If its possible to enter the new state with lower price, than expand it!
            if new_state not in g or g[new_state] > g[actual_state] + 1: 
                """ plus 1 simply means the distance from actual state to new state """

                # Update the cost of the new state with the lover value
                g[new_state] = g[actual_state] + 1                 

                # Get cost of the total path f() = g() + h()
                f[new_state] = g[new_state] + manhattanDistance(new_state, goal)

                # Update list of visited nodes which is later used for path reconstruction
                visited[new_state] = f[new_state], actual_state

                # Add the new state to the list of open nodes if necessary
                if new_state not in open_data:
                    open_data[new_state] = f[new_state]

    return False


if __name__ == "__main__":
    a_star(start, goal, 0, work_space, visited, actions)

    # Show results
    fig = plt.figure()
    ax = fig.subplots(2)
    plt.ion()                               # enable interactive plotting
    fig.show()
    fig.canvas.draw()


    dim = armsLength * arms
    ax[0].plot([-dim, dim, -dim], [-0.1, -0.1, dim], 'bo')

    for x1, y1, x2, y2 in work_space:
        ax[0].plot([x1, x2], [y1, y2], 'bo-')

    # Init path reconstruction backwards from goal node
    node = goal

    # Path reconstruction from the list of visited nodes
    while node != start:

        # Get predecesor of the actual node
        d, prev_state = visited[node]

        x2, y2, x3, y3 = armCoordinates(node)

        ax[0].plot([0, x2, x3], [0, y2, y3], 'r*-')
        node = prev_state


    node = goal

   # Animated path reconstruction from the list of visited nodes
    while node != start:

        # Get predecesor of the actual node
        d, prev_state = visited[node]

        x2, y2, x3, y3 = armCoordinates(node)

        ax[1].clear()
        ax[1].axis('equal')
        dim = armsLength * arms
        ax[1].plot([-dim, dim, -dim], [-0.1, -0.1, dim], 'bo')
        ax[1].plot([0, x2, x3], [0, y2, y3], 'r*-')
    
        for x1, y1, x2, y2 in work_space:
            ax[1].plot([x1, x2], [y1, y2], 'b-')

        fig.canvas.draw()
        
        plt.pause(0.1)    

        node = prev_state

