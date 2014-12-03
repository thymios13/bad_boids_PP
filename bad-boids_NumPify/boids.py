"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np
import time
import yaml

# Import initial configurations from a config file
configs = yaml.load(open("config_file.yml"))

boids_number = configs["boids_number"]
x_pos_range = configs["x_pos_range"]
y_pos_range = configs["y_pos_range"]
x_vel_range = configs["x_vel_range"]
y_vel_range = configs["y_vel_range"]
flock_attraction = configs["flock_attraction"]
avoidance_radius = configs["avoidance_radius"]
formation_flying_radius = configs["formation_flying_radius"]
speed_matching_strength = configs["speed_matching_strength"]


# Define Animation (True/False)
animation_flag = False

# Define Iterations of update_boids to measure execution time
iterations = 1000

start_time = time.time()

boids_x_pos = []
boids_y_pos = []
boids_x_vel = []
boids_y_vel = []

#for i in range(boids_number):
#    x_pos = np.random.uniform(-450, 50.0)
#    y_pos = np.random.uniform(300.0, 600.0)
#    x_vel = np.random.uniform(0, 10.0)
#    y_vel = np.random.uniform(-20.0, 20.0)

#    boids_x_pos = np.append(boids_x_pos, x_pos)
#    boids_y_pos = np.append(boids_y_pos, y_pos)
#    boids_x_vel = np.append(boids_x_vel, x_vel)
#    boids_y_vel = np.append(boids_y_vel, y_vel)


boids_x_pos = np.random.uniform(x_pos_range[0], x_pos_range[1], boids_number)
boids_y_pos = np.random.uniform(y_pos_range[0], y_pos_range[1], boids_number)
boids_x_vel = np.random.uniform(x_vel_range[0], x_vel_range[1], boids_number)
boids_y_vel = np.random.uniform(y_vel_range[0], y_vel_range[1], boids_number)

boids = (boids_x_pos, boids_y_pos, boids_x_vel, boids_y_vel)

def update_boids(boids):
    x_positions, y_positions, x_velocities, y_velocities = boids
    for i in range(boids_number):
        for j in range(boids_number):
            # Fly towards the middle
            x_velocities[i] += (x_positions[j] - x_positions[i]) * flock_attraction / boids_number
            y_velocities[i] += (y_positions[j] - y_positions[i]) * flock_attraction / boids_number

            check_velocity = (x_positions[j] - x_positions[i]) ** 2 + (y_positions[j] - y_positions[i]) ** 2

            # Fly away from nearby boids
            if check_velocity < avoidance_radius:
                x_velocities[i] += (x_positions[i] - x_positions[j])
                y_velocities[i] += (y_positions[i] - y_positions[j])

            # Try to match speed with nearby boids
            elif check_velocity < formation_flying_radius:
                x_velocities[i] += (x_velocities[j] - x_velocities[i]) * speed_matching_strength / boids_number
                y_velocities[i] += (y_velocities[j] - y_velocities[i]) * speed_matching_strength / boids_number

        # Move according to velocities
        x_positions[i] += x_velocities[i]
        y_positions[i] += y_velocities[i]

iterations = 1000
for i in range(iterations):
#    print i
    update_boids(boids)
print("--- Elapsed in %s seconds, for %d Boids and %d iterations ---" % (time.time() - start_time, boids_number, iterations))


# Boids Animation
if animation_flag == True:
    figure = plt.figure()
    axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
    scatter = axes.scatter(boids[0], boids[1])

    def animate(frame):
        update_boids(boids)
        scatter.set_offsets(zip(boids[0], boids[1]))

    anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

    if __name__ == "__main__":
        plt.show()
