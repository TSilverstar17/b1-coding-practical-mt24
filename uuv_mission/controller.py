# Code to produce a PD controller for the UUV mission

class Controller:
    def __init__(self, Kp: float = 0.15, Kd: float = 0.6):
        self.prev_error = 0.0

        self.Kp = Kp
        self.Kd = Kd

    def compute_control(self, r: float, y: float) -> float:
        # Calculate the current error and the previous error
        error = r - y

        # Use control law to calculate the control action
        u = self.Kp * error + self.Kd * (error - self.prev_error)

        # Update previous values for the next iteration
        self.prev_error = error

        return u
