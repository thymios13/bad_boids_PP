"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

def main_oo(boids_number, iterations):

    from matplotlib import pyplot as plt
    from matplotlib import animation
    from numpy import array
    from my_update_boids import update_boids
    import time
    import yaml

    # Import initial configurations from a config file
    configs = yaml.load(open("config_file.yml"))

    #boids_number = configs["boids_number"]
    x_pos_range = configs["x_pos_range"]
    y_pos_range = configs["y_pos_range"]
    x_vel_range = configs["x_vel_range"]
    y_vel_range = configs["y_vel_range"]

    # Define Animation (True/False)
    animation_flag = False

    # Define Iterations of update_boids to measure execution time
    #iterations = 1000

    # Starting the timer
    start_time = time.time()

    class Boid(object):
        def __init__(self, x_position, y_position, x_velocity, y_velocity):
            self.x_position = x_position
            self.y_position = y_position
            self.x_velocity = x_velocity
            self.y_velocity = y_velocity

        def get_position(self):
            return array([self.x_position, self.y_position])

        def get_velocity(self):
            return array([self.x_velocity, self.y_velocity])


    def generate_random_boid():
        import random

        x_position = random.uniform(x_pos_range[0], x_pos_range[1])
        y_position = random.uniform(y_pos_range[0], y_pos_range[1])
        x_velocity = random.uniform(x_vel_range[0], x_vel_range[1])
        y_velocity = random.uniform(y_vel_range[0], y_vel_range[1])

        return Boid(x_position, y_position, x_velocity, y_velocity)


    def initialize_boids(total):
        new_boids = []

        for i in range(total):
            new_boids.append(generate_random_boid())

        return new_boids


    def get_boids(total_boids):
        x_pos = []
        y_pos = []
        x_vel = []
        y_vel = []

        for boid in total_boids:
            x_pos.append(boid.get_position()[0])
            y_pos.append(boid.get_position()[1])
            x_vel.append(boid.get_velocity()[0])
            y_vel.append(boid.get_velocity()[1])

        return x_pos, y_pos, x_vel, y_vel


    # Positions/velocities of boids initialization
    all_boids = initialize_boids(boids_number)
    boids = get_boids(all_boids)

    for i in range(iterations):
        update_boids(boids)
    print("--- Elapsed in %s seconds, for %d Boids and %d iterations ---" % (time.time() - start_time, boids_number, iterations))


    # Boids Animation
    if animation_flag == True:
        figure = plt.figure()
        axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
        scatter = axes.scatter(boids[0], boids[1])


        def animate(frame):
            update_boids(boids)
            zipped = []
            for i in range(boids_number):
                zipped.append((boids[0][i], boids[1][i]))

            scatter.set_offsets(zipped)

        anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

        if __name__ == "__main__":
            plt.show()

    return time.time() - start_time, boids_number, iterations