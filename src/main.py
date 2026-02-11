import gpiod
from time import sleep

import Constants
import IMU
import LinearActuators
import LORA
import StepperMotor
from enum import Enum

# Instantiate the classes
imu             = IMU.IMU()
linearactuators = LinearActuators.LinearActuators()
lora            = LORA.LORA()
steppermotor    = StepperMotor.StepperMotor()

# Create enum for flight stages
class FlightStage(Enum):
    TAKEOFF = 0
    DRIFT   = 1
    DROGUE  = 2
    MAIN    = 3
    LAND    = 4
    MEASURE = 5

def main():
    state = FlightStage.TAKEOFF
    while True:
        newstage = False

        temperature   = imu.get_temperature_data()
        gyroscope     = imu.get_gyroscope_data()
        accelerometer = imu.get_accelerometer_data()

        # Transmit to know that LoRa system is working
        lora.transmit("000:1")


        if state == FlightStage.TAKEOFF:

            if newstage:
                # Inform the Ground Station about stage change
                lora.transmit(f"001:{state}")

            # Transmit Temp Data
            lora.transmit(f"002:{temperature}")

        if state == FlightStage.DRIFT:

            if newstage:
                # Inform the Ground Station about stage change
                lora.transmit(f"001:{state}")

        if state == FlightStage.DROGUE:

            if newstage:
                # Inform the Ground Station about stage change
                lora.transmit(f"001:{state}")

        if state == FlightStage.MAIN:

            if newstage:
                # Inform the Ground Station about stage change
                lora.transmit(f"001:{state}")

        if state == FlightStage.LAND:

            if newstage:
                # Inform the Ground Station about stage change
                lora.transmit(f"001:{state}")
            

main()