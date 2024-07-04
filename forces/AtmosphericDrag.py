import numpy as np

class AtmosphericDrag:
    def __init__(self, density, drag_coefficient, reference_area, mass):
        self.density = density  # Atmospheric density (kg/m^3)
        self.drag_coefficient = drag_coefficient  # Drag coefficient (dimensionless)
        self.reference_area = reference_area  # Reference area (m^2)
        self.mass = mass  # Mass of the spacecraft (kg)

    def calculate_drag_force(self, velocity):
        """
        Calculate the drag force using the GMAT's drag force equation.

        Parameters:
            velocity (float): Velocity of the object relative to the fluid (m/s).

        Returns:
            float: Drag force (N).
        """
        # Calculate the magnitude of the relative velocity
        Urel_magnitute = np.linalg.norm(velocity)

        # Calculate the unit vector of the relative velocity
        Vrel_unit_vector = velocity / Urel_magnitute

        # Calculate the drag force
        drag_force = -0.5 * self.density * Urel_magnitute**2 * (self.drag_coefficient * self.reference_area) / self.mass * Vrel_unit_vector

        return drag_force
