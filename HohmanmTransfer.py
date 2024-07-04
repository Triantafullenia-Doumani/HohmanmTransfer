import numpy as np
from forces.SolarRadiationPressure import SolarRadiationPressure
from forces.AtmosphericDrag import AtmosphericDrag
from forces.Gravity import Gravity
from NewtonSecondLaw import NewtonSecondLaw
from propagator.Integrator import Integrator
from solvers.BoundaryValueSolver import BoundaryValueSolver
from outputs.Writer import Writer
import matplotlib.pyplot as plt
from constants import *

# Adjust initial position to be more realistic (in meters)
initial_position = np.array([7100e3, 0, 0])
initial_velocity = np.array([0, 7.35e3, 0])

# Corrected SRP constant to a more realistic value (N/m^2)
solar_pressure = 4.5e-6  

# Corrected mass of the Earth for gravity calculations (kg)
m2 = 5.9722e24

# ----------- Gravity --------------------
gravity_calculator = Gravity(G)
gravity_force = gravity_calculator.calculate_force(spacecraft_mass, m2, initial_position)
print("Gravitational force:", gravity_force, "N")

# ----------- Solar Radiation Pressure (SRP)--------------------
SRP_calculator = SolarRadiationPressure(solar_pressure, reflectivity_coefficient, SRP_area, spacecraft_mass, initial_position)
pressure_force = SRP_calculator.calculate_pressure()
print("Solar Radiation Pressure Force Vector:", pressure_force, "N")

# ----------- Drag Force --------------------
drag_calculator = AtmosphericDrag(density, drag_coefficient, drag_area, spacecraft_mass)
drag_force = drag_calculator.calculate_drag_force(velocity)
print("Drag force:", drag_force, "N")

# ----------- Total External Force --------------------
total_force = gravity_force + pressure_force + drag_force
print("Total External Force:", total_force, "N")

# ----------- Newton's 2nd Law --------------------
newton_2nd_law = NewtonSecondLaw(spacecraft_mass)
newton_2nd_law.update_total_external_forces(total_force)

acceleration = newton_2nd_law.calculate_acceleration()
print("Acceleration:", acceleration, "m/s^2")

# ----------- Equations of Motion --------------------
def equations_of_motion(t, y):
    position = y[:3]
    velocity = y[3:]

    gravity_force = gravity_calculator.calculate_force(spacecraft_mass, m2, position)
    pressure_force = SRP_calculator.calculate_pressure()
    drag_force = drag_calculator.calculate_drag_force(velocity)

    total_force = gravity_force + pressure_force + drag_force
    acceleration = total_force / spacecraft_mass

    return np.hstack((velocity, acceleration))

# ----------- Hohmann Transfer Specifics --------------------
initial_orbit_radius = np.linalg.norm(initial_position)
final_orbit_radius = 42164e3  # Geostationary orbit radius in meters

# Calculate delta-v for Hohmann transfer
mu = G * m2  # Gravitational parameter for Earth

# Delta-v for the first burn (circular to elliptical orbit)
v1 = np.sqrt(mu / initial_orbit_radius)
v_transfer = np.sqrt(mu * (2 / initial_orbit_radius - 1 / ((initial_orbit_radius + final_orbit_radius) / 2)))
delta_v1 = v_transfer - v1

print("Delta-v for first burn:", delta_v1, "m/s")

# Apply the first burn
velocity_after_burn1 = initial_velocity + np.array([delta_v1, 0, 0])

# Propagate the orbit until apogee (half the orbital period of the transfer orbit)
a_transfer = (initial_orbit_radius + final_orbit_radius) / 2
orbital_period_transfer = 2 * np.pi * np.sqrt(a_transfer**3 / mu)
time_to_apogee = orbital_period_transfer / 2

# Integrate the trajectory from initial position to apogee
integrator = Integrator(method='DOP853', initial_step_size=initial_step_size, accuracy=accuracy,min_step_size = min_step_size, max_step_size=max_step_size, max_step_attempts=max_step_attempts, stop_if_accuracy_violated=stop_if_accuracy_violated)
y0 = np.hstack((initial_position, velocity_after_burn1))

positions = []
velocities = []

def log_equations_of_motion(t, y):
    position = y[:3]
    velocity = y[3:]

    positions.append(position)
    velocities.append(velocity)

    return equations_of_motion(t, y)

final_state = integrator.integrate(log_equations_of_motion, y0, 0, time_to_apogee, initial_step_size)
print("State at apogee:", final_state)

