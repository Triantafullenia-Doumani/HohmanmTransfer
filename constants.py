import numpy as np

# Elements
initial_position = np.array([7100, 0, 13000])
initial_velocity = np.array([0, 7.35, 1]) # UNUSED

# General Constants
spacecraft_mass = 850  # kg(does not include fuel mass)

# Gravity Constants
G = 6.67430e-11  # m^3 kg^-1 s^-2

# Solar Radiation Pressure Constants
solar_pressure = 4.5  # N/m^2              CAN'T FIND IT ON GMAT
reflectivity_coefficient = 1.8
SRP_area = 1 # m^2

# Drag Force Constants
density = 1.225    # kg/m^3        approximately value found online(it is not defined in the script or GUI and the calculation of it looks complicated)
drag_coefficient = 2.2
drag_area = 15  # m^2


# Gravity Parameters
m2 = 5.9722* (10 ^ 24)  # mass of Earth (kg)

# Drag Force Parameters
velocity = np.array([0, 7.35, 1])  # The flow velocity relative to the object (m/s)

# Integrator Constants
integrator_type = 'RK4'
initial_step_size = 60
accuracy = 1e-6 # to meiwsa gia dokimh, sto gmat einai 9.999999999999999e-12
min_step_size = 0.001
max_step_size = 2700
max_step_attempts = 50
stop_if_accuracy_violated = True

# Differential Corrector Constants
max_iterations = 25
differential_corrector_algorithm = 'NewtonRaphson'
derivative_method = 'ForwardDifference'