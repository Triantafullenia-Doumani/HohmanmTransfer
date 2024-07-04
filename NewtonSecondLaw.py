class NewtonSecondLaw:
    def __init__(self, mass):
        """

        Args:
        mass (float): Mass of the spacecraft (in kg).
        """
        self.total_external_forces = 0.0
        self.mass = mass

    def calculate_acceleration(self):
        """
        Calculate acceleration based on the second law of Newton.

        Returns:
        float: Acceleration (in meters per second squared).
        """
        acceleration = self.total_external_forces / self.mass
        return acceleration
    
    def update_total_external_forces(self, new_total_external_forces):
        """
        Update the total_external_forces attribute with a new value.

        Args:
        new_total_external_forces (float): New total of external forces value to be updated.
        """
        self.total_external_forces =  self.total_external_forces + new_total_external_forces
