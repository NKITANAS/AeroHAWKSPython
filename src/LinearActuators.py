import gpiod
import Constants

class LinearActuators:
    def __init__(self):
        # Initialize the linear actuator control pins
        self.left_actuator_pin_1  = Constants.LINEAR_ACTUATOR_L_PIN_1
        self.left_actuator_pin_2  = Constants.LINEAR_ACTUATOR_L_PIN_2
        self.right_actuator_pin_1 = Constants.LINEAR_ACTUATOR_R_PIN_1
        self.right_actuator_pin_2 = Constants.LINEAR_ACTUATOR_R_PIN_2

        self.left_actuator_pin_1 .request(consumer='linear-actuators', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])
        self.left_actuator_pin_2 .request(consumer='linear-actuators', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])
        self.right_actuator_pin_1.request(consumer='linear-actuators', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])
        self.right_actuator_pin_2.request(consumer='linear-actuators', type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])

    # The Linear Actuators are controlled with an H-Bridge Motor Controller(DRV 8833)
    # You can look up the datasheet, but basically:
    # pin1 HIGH + pin2 LOW  = Forward
    # pin1 LOW  + pin2 HIGH = Backward
    # pin1 LOW  + pin2 LOW  = Stop
    # pin1 HIGH + pin2 HIGH = Stop
    def extend_left_actuator(self):
        self.left_actuator_pin_1 .set_value(1)
        self.left_actuator_pin_2 .set_value(0)

    def retract_left_actuator(self):
        self.left_actuator_pin_1 .set_value(0)
        self.left_actuator_pin_2 .set_value(1)

    def extend_right_actuator(self):
        self.right_actuator_pin_1.set_value(1)
        self.right_actuator_pin_2.set_value(0)

    def retract_right_actuator(self):
        self.right_actuator_pin_1.set_value(0)
        self.right_actuator_pin_2.set_value(1)

    def reset_actuators(self):
        self.left_actuator_pin_1 .set_value(0)
        self.left_actuator_pin_2 .set_value(0)
        self.right_actuator_pin_1.set_value(0)
        self.right_actuator_pin_2.set_value(0)