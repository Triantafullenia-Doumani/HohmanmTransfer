import numpy as np
from scipy.optimize import newton
from constants import max_iterations, differential_corrector_algorithm

class BoundaryValueSolver:
    def __init__(self, func, x0):
        self.func = func
        self.x0 = x0

    def derivative(self, x):
        h = 1e-5  # Small step for numerical derivative
        return (self.func(x + h) - self.func(x - h)) / (2 * h)

    def find_root(self):
        if differential_corrector_algorithm == 'NewtonRaphson':
            root = newton(self.func, self.x0, fprime=self.derivative, maxiter=max_iterations)
            return root
        else:
            raise ValueError(f"Algorithm {differential_corrector_algorithm} not implemented")
