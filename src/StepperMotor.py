import gpiod
import Constants
from time import sleep
from enum import Enum

class Windows(Enum):
    WINDOW1 = 1
    WINDOW2 = 2
    WINDOW3 = 3
    WINDOW4 = 4

class StepperMotor:
    # Initialize the stepper motor control pins
    def __init__(self):
        self.dir_pin  = Constants.STEPPER_MOTOR_DIR_PIN
        self.step_pin = Constants.STEPPER_MOTOR_STEP_PIN

        self.dir_pin.request(consumer='stepper-motor', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])
        self.step_pin.request(consumer='stepper-motor', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])

    # One Step Forward
    def step_forward(self):
        self.dir_pin.set_value(1)   # Set direction to forward
        sleep(0.01)                 # Delay for direction change
        self.step_pin.set_value(1)  # Step
        sleep(0.01)                 # Delay for step timing
        self.step_pin.set_value(0)  # Reset step pin
        sleep(0.01)                 # Delay for step timing

    # One Step Backward
    def step_backward(self):
        self.dir_pin.set_value(0)   # Set direction to backward
        sleep(0.01)                 # Delay for direction change
        self.step_pin.set_value(1)  # Step
        sleep(0.01)                 # Delay for step timing
        self.step_pin.set_value(0)  # Reset step pin
        sleep(0.01)                 # Delay for step timing

    def step_to_windows(self, window):
        if window == Windows.WINDOW1:
            for step in range(Constants.WINDOW1_STEPS):
                self.step_forward()
        elif window == Windows.WINDOW2:
            for step in range(Constants.WINDOW2_STEPS):  
                self.step_forward()
        elif window == Windows.WINDOW3:
            for step in range(Constants.WINDOW3_STEPS):  
                self.step_forward()
        elif window == Windows.WINDOW4:
            for step in range(Constants.WINDOW4_STEPS):  
                self.step_forward()