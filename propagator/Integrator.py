from scipy.integrate import solve_ivp

class Integrator:
    def __init__(self, method, initial_step_size, accuracy, min_step_size, max_step_size, max_step_attempts, stop_if_accuracy_violated):
        self.method = method
        self.initial_step_size = initial_step_size
        self.accuracy = accuracy
        self.min_step_size = min_step_size
        self.max_step_size = max_step_size
        self.max_step_attempts = max_step_attempts
        self.stop_if_accuracy_violated = stop_if_accuracy_violated

    def get_parameters(self):
        return {
            'Method': self.method,
            'InitialStepSize': self.initial_step_size,
            'Accuracy': self.accuracy,
            'MinStepSize': self.min_step_size,
            'MaxStepSize': self.max_step_size,
            'MaxStepAttempts': self.max_step_attempts,
            'StopIfAccuracyViolated': self.stop_if_accuracy_violated
        }

    def integrate(self, f, y0, t0, tf, h):
        """
        Integrate an ODE using solve_ivp.
        f: function to integrate
        y0: initial state vector
        t0: initial time
        tf: final time
        h: initial time step
        Returns the state vector at tf.
        """
        sol = solve_ivp(f, [t0, tf], y0, method=self.method, rtol=self.accuracy, atol=self.accuracy, 
                        first_step=h, min_step=self.min_step_size, max_step=self.max_step_size)

        if sol.success:
            return sol.y[:, -1]
        else:
            raise RuntimeError("Integration failed: " + sol.message)
