import numpy as np

class Gravity:
    def __init__(self, G):
        """
            G: Gravitational constant.
        """
        self.G = G

    def calculate_force(self, m1, m2, r):
        """
        Calculate gravitational force between two objects.

        Args:
            m1: Mass of the first object.
            m2: Mass of the second object.
            r: Vector representing the distance and direction from m1 to m2.

        Returns:
            F_gravity: Gravitational force vector.
        """
        r_magnitude = np.linalg.norm(r)
        F_gravity = - (self.G * m1 * m2 / r_magnitude**3) * r
        return F_gravity
