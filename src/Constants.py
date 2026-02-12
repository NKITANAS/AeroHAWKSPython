import gpiod
from mpu6050 import mpu6050

# Test Mode #
TEST_MODE: bool = True

gpiochip: gpiod.Chip = gpiod.Chip('/dev/gpiochip0')

# Pin/Line definitions #

# Linear Actuators - numbers are subject to change
LINEAR_ACTUATOR_L_PIN_1: int = 1
LINEAR_ACTUATOR_L_PIN_2: int = 2
LINEAR_ACTUATOR_R_PIN_1: int = 3
LINEAR_ACTUATOR_R_PIN_2: int = 4

# Stepper Motor - numbers are subject to change
STEPPER_MOTOR_DIR_PIN:   int = 5
STEPPER_MOTOR_STEP_PIN:  int = 6

# Moisture Sensors - numbers are subject to change
MOISTURE_SENSOR_1_PIN: int = 7
MOISTURE_SENSOR_2_PIN: int = 8

# Altimiter(Barometer) - numbers are subject to change
ALTIMITER_SDA_PIN: int = 9
ALTIMITER_SCL_PIN: int = 10

# IMU - numbers are subject to change
IMU: mpu6050 = mpu6050(0x68)

# Stepper Motor Windows positions #
DEGREE_TO_STEP: float = 200 / 360 # 200 steps per revolution, 360 degrees per revolution

WINDOW1_STEPS: float  = 0   * DEGREE_TO_STEP  
WINDOW2_STEPS: float  = 90  * DEGREE_TO_STEP  
WINDOW3_STEPS: float  = 0   * DEGREE_TO_STEP  
WINDOW4_STEPS: float  = 90  * DEGREE_TO_STEP  

default_settings: gpiod.LineSettings = gpiod.line_settings(
    direction=gpiod.line.Direction.OUTPUT
    )
input_settings: gpiod.LineSettings = gpiod.line_settings(
    direction=gpiod.line.Direction.INPUT
    )

request: gpiod.LineRequest = gpiochip.request_lines(
    consumer="payload",
    config={
        LINEAR_ACTUATOR_L_PIN_1: default_settings,
        LINEAR_ACTUATOR_L_PIN_2: default_settings,
        LINEAR_ACTUATOR_R_PIN_1: default_settings,
        LINEAR_ACTUATOR_R_PIN_2: default_settings,
        STEPPER_MOTOR_DIR_PIN:   default_settings,
        STEPPER_MOTOR_STEP_PIN:  default_settings,
        MOISTURE_SENSOR_1_PIN:   input_settings,
        MOISTURE_SENSOR_2_PIN:   input_settings
    },
)