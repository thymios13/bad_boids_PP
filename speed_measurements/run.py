from boids_numpy import main as main_numpy
from boids_obj import main as main_obj
import numpy as np

# Define boids_number Array
boids_array = [50, 60, 70]

# Define iterations Array
iterations_array = [10, 50, 100]

# Initialise arrays
time_numpy = np.zeros((len(boids_array), len(iterations_array)))
time_obj = np.zeros((len(boids_array), len(iterations_array)))

for i in range(len(boids_array)):
    for j in range(len(iterations_array)):

        time_numpy[i][j] = main_numpy(boids_array[i], iterations_array[j])

        time_obj[i][j] = main_obj(boids_array[i], iterations_array[j])
