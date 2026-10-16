# Code to produce a PD controller for the UUV mission

class Controller:
    def __init__(self, Kp: float = 0.15, Kd: float = 0.6):
        self.r_prev = None
        self.y_prev = None

        self.Kp = Kp
        self.Kd = Kd

    def compute_control(self, r: float, y: float) -> float:

        # Initialize previous values as 0 if they are None
        if self.r_prev is None:
            self.r_prev = 0
            self.y_prev = 0

        # Calculate the current error and the previous error
        error = r - y
        prev_error = self.r_prev - self.y_prev

        # Use control law to calculate the control action
        u = self.Kp * error + self.Kd * (error - prev_error)

        # Update previous values for the next iteration
        self.r_prev = r
        self.y_prev = y
