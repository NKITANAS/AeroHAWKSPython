import gpiod
from mpu6050 import mpu6050

gpiochip = gpiod.Chip('gpiochip0')

# Pin/Line definitions #

# Linear Actuators - numbers are subject to change
LINEAR_ACTUATOR_L_PIN_1 = gpiochip.get_line(1)
LINEAR_ACTUATOR_L_PIN_2 = gpiochip.get_line(2)
LINEAR_ACTUATOR_R_PIN_1 = gpiochip.get_line(3)
LINEAR_ACTUATOR_R_PIN_2 = gpiochip.get_line(4)

# Stepper Motor - numbers are subject to change
STEPPER_MOTOR_DIR_PIN  = gpiochip.get_line(5)
STEPPER_MOTOR_STEP_PIN = gpiochip.get_line(6)

# IMU - numbers are subject to change
IMU = mpu6050(0x68)

# Stepper Motor Windows positions #
DEGREE_TO_STEP = 200 / 360 # 200 steps per revolution, 360 degrees per revolution

WINDOW1_STEPS = 0   * DEGREE_TO_STEP  
WINDOW2_STEPS = 90  * DEGREE_TO_STEP  
WINDOW3_STEPS = 0   * DEGREE_TO_STEP  
WINDOW4_STEPS = 90  * DEGREE_TO_STEP  