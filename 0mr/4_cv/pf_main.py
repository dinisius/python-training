from matplotlib import pylab as plt
import math
import random

MAX_PARTICLES = 100
NUM_STEPS = 5
DEF_STEPS = 1

STD_ANGLE = 0.1
STD_DISTANCE = 0.1

state = (0.0, 0.0, 0.0)  # float over int
particles = [(0.0, 0.0, 0.0) for _ in range(MAX_PARTICLES)]

LANDMARK_POSITIONS = [(2.0, 1.0), (3.0, 2.0), (5.0, 1.0)]

# CTRL + /
# ALT + SIPKAqqqq
# CODE RUNNER EXTENSION


plt.figure()
plt.plot(state[0], state[1], 'ro')


#lx = []
#ly = []
#for landmark in LANDMARK_POSITIONS:
#    lx.append(landmark[0])
#    ly.append(landmark[1])

#lx = [l[0] for l in LANDMARK_POSITIONS]

lx, ly = zip(*LANDMARK_POSITIONS)
plt.plot(lx, ly, 'ko')

px, py, _ = zip(*particles)
plt.plot(px, py, 'go', alpha=0.2, markersize=3)

plt.xlim(-1, 11)
plt.ylim(-2, 6)
plt.pause(0.3)

def motion_model(state, phi, d):
    x, y, theta = state
    theta = phi+theta
    x += x + d * math.cos(theta)
    y += y + d * math.sin(theta)
    return x, y, theta

def move_robot(state_robot):
    angle = random.gauss(0.0, STD_ANGLE)
    distance = DEF_STEPS + random.gauss(0.0, STD_DISTANCE)
    return motion_model(state_robot, angle, distance)

def update_particles(state_particles):
    angle = random.gauss(0.0, STD_ANGLE)
    distance = DEF_STEPS + random.gauss(0.0, STD_DISTANCE)
    return motion_model(state_particles, angle, distance)

def calculate_distance(point_a, point_b):
    xa, ya = point_a
    xb, yb = point_b
    return math.sqrt((xa - xb)**2 + (ya - yb)**2)

def measure_distance(state_robot, target):
    noise = random.gauss(0.0, 0.01)
    return calculate_distance(state_robot[:2], target[:2]) + noise

def update_weights(particles, landmarks, measurements):
    weights = []
    for particle in particles:
        total_error = 0.0
        for landmark, measurement in zip(landmarks, measurements):
            distance = calculate_distance(particle[:2], landmark[:2])
            error = abs(measurement - distance)
            total_error += error
        weight = 1.0 / (total_error + 0.0001)
        weights.append(weight)
        
    total_weights = sum(weights)
    return [w / total_weights for w in weights] 

def resample(particles, weights):
    return random.choices(population=particles, weights=weights, k = len(particles))

def get_estimate(particles):
    px, py, ptheta = zip(*particles)
    num = len(particles)
    avg_x = sum(px) / num
    avg_y = sum(py) / num
    avg_theta = sum(ptheta) / num 
    return avg_x, avg_y, avg_theta

for steps in range(NUM_STEPS):
    state = move_robot(state)
    particles = [update_particles(p) for p in particles]
    measurements = [measure_distance(state, lm) for lm in LANDMARK_POSITIONS]
    weights = update_weights(particles, LANDMARK_POSITIONS, measurements)
    particles = resample(particles, weights)
    estimated_state = get_estimate(particles)

    px, py, _ = zip(*particles)
    plt.plot(px, py, 'go', alpha=0.2, markersize=3)

    plt.plot(state[0], state[1], 'ro')
    plt.plot(estimated_state[0], estimated_state[1], 'bo')


    plt.pause(0.3)


plt.show()