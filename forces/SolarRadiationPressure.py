import numpy as np

class SolarRadiationPressure:
    def __init__(self, solar_pressure, satellite_reflectivity, satellite_area, satellite_mass, r_vector):
        self.solar_pressure = solar_pressure
        self.satellite_reflectivity = satellite_reflectivity
        self.satellite_area = satellite_area
        self.satellite_mass = satellite_mass
        self.r_vector = r_vector

    def calculate_pressure(self):
        # Calculate the magnitude of the distance vector
        distance_magnitude = np.linalg.norm(self.r_vector)
        
        
        # Calculate the direction vector (unit vector)
        direction_vector = self.r_vector / distance_magnitude
        
        # Calculate the force due to solar radiation pressure
        force_magnitude = (self.solar_pressure * self.satellite_reflectivity * self.satellite_area) / self.satellite_mass
        
        # Apply negative sign if necessary (opposes satellite motion)
        if np.dot(direction_vector, self.r_vector) > 0:
            force_magnitude *= -1
        
        # Calculate the force vector
        force_vector = force_magnitude * direction_vector
        
        return force_vector
