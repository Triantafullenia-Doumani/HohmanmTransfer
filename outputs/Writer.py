# outputs/writer.py
import matplotlib.pyplot as plt

class Writer:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, 'w') as file:
            file.write("Time(s)\tVelocity_X(km/s)\tPosition_X(km)\n")

    def write(self, time, velocity_x, position_x):
        with open(self.filename, 'a') as file:
            file.write(f"{time}\t{velocity_x}\t{position_x}\n")



    def plot_results(self):
        times = []
        velocities_x = []
        positions_x = []


        with open(self.filename, 'r') as file:
            next(file)  # Skip the header
            for line in file:
                time, velocity_x, position_x = map(float, line.split())
                times.append(time)
                velocities_x.append(velocity_x)
                positions_x.append(position_x)

        plt.figure(figsize=(10, 6))
        plt.plot(positions_x, velocities_x, marker='o', linestyle='-')
        plt.title('Position vs Velocity')
        plt.xlabel('Position X (km)')
        plt.ylabel('Velocity X (km/s)')
        plt.grid(True)
        plt.savefig('outputs/position_vs_velocity.png')
        plt.show()
