import yaml
# Import initial configurations from a config file
configs = yaml.load(open("config_file.yml"))

boids_number = configs["boids_number"]
flock_attraction = configs["flock_attraction"]
avoidance_radius = configs["avoidance_radius"]
formation_flying_radius = configs["formation_flying_radius"]
speed_matching_strength = configs["speed_matching_strength"]



def update_boids(boids):
    [x_positions, y_positions, x_velocities, y_velocities] = boids

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
