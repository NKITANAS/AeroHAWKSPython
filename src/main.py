import gpiod
import mpu6050
from time import sleep
import datetime

import Constants
import LinearActuators
import LORA
import StepperMotor
import Pico
import tests

from enum import Enum

# Instantiate the classes
pico            = Pico.Pico()
linearactuators = LinearActuators.LinearActuators()
lora            = LORA.LORA()
steppermotor    = StepperMotor.StepperMotor()

class Status(Enum):
    IDLE = 1
    ASCENT = 2
    DESCENT = 3
    LANDED = 4


def main():
    turn_on_signal_received: bool = False
    # Wait for the "Turn On" signal from the ground station before starting the main loop
    while not turn_on_signal_received:
        message = lora.recieve()
        if message == "100:1":
            turn_on_signal_received = True
            print("STATUS: Turn On Recieved")
    # Init
    start_time          = datetime.datetime.now()
    start_height: float = 0.00 # MAJOR TODO: Altimiter

    # Data
    status: Status = Status.IDLE

    old_time                 = datetime.datetime.now()

    orientation: dict = pico.read_gyroscope() # For deciding optimal window, might have to use y instead depending on sensor orient

    optimal_window: StepperMotor.Windows = StepperMotor.Windows.WINDOW1 # Default to WINDOW1, will be updated in main loop based on orientation data

    # Main loop
    while True:
        # Time of measurement
        time = datetime.datetime.now()

        # Altimiter data
        height: float = 0.00   # MAJOR TODO: Altimiter

        # IMU data
        accelerometer_data: dict = pico.read_accelerometer()
        gyroscope_data:     dict = pico.read_gyroscope()

        orientation += (gyroscope_data['x']) * (time - old_time) # For deciding optimal window, might have to use y instead depending on sensor orient

        old_time = time

        # Keep orientation within 0-360 degrees
        if orientation > 360.00:
            orientation -= 360.00
        elif orientation < 0.00:
            orientation += 360.00
        
        # set current status based on accelerometer and height data
        if accelerometer_data['z'] > 1.5: # MAJOR TODO: Tune this threshold
            status = Status.ASCENT

        elif accelerometer_data['z'] < -1.0: # MAJOR TODO: Tune this threshold
            status = Status.DESCENT

        elif accelerometer_data['z'] == 0.0 and height <= start_height + 20 and status != Status.IDLE: # MAJOR TODO: Tune this threshold
            status = Status.LANDED # MAJOR TODO: Make sure through testing that this condition is sufficient to determine landing
            sleep(5) # Sleep for 5 seconds to ensure that the payload fully lands
        
        if status == Status.LANDED:
            if orientation < 90.00:
                optimal_window = StepperMotor.Windows.WINDOW1

            # Begin data collection sequence
            steppermotor.step_to_windows(optimal_window)

            # Read Linear Actuators and read soil moisture data(Finally!)
            if optimal_window == StepperMotor.Windows.WINDOW1 or optimal_window == StepperMotor.Windows.WINDOW3:
                reading = pico.read_moisture(1)
            else:
                reading = pico.read_moisture(2)
            lora.transmit(f"MOISTURE_READING:{reading}")


if not Constants.TEST_MODE:
    main()
else:
    tests.test_stepper_motor()
    tests.test_linear_actuators()
    tests.test_imu()               
    tests.test_lora_transmission()
    #tests.test_lora_reception()
