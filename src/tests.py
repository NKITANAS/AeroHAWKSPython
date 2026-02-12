import StepperMotor
import LinearActuators
import IMU
import LORA
import Constants

from time import sleep

stepper_motor: StepperMotor.StepperMotor = StepperMotor.StepperMotor()
linear_actuators: LinearActuators.LinearActuators = LinearActuators.LinearActuators()
imu: IMU.IMU = IMU.IMU()
lora: LORA.LORA = LORA.LORA()

def test_stepper_motor():
    sleep(0.2)
    stepper_motor.step_forward()
    sleep(0.2)
    stepper_motor.step_backward()
    sleep(0.5)
    stepper_motor.step_to_windows(StepperMotor.Windows.WINDOW2)
    sleep(2)

def test_linear_actuators():
    sleep(0.2)
    linear_actuators.extend_left_actuator()
    sleep(1)
    linear_actuators.retract_left_actuator()
    sleep(1)
    linear_actuators.reset_actuators()
    linear_actuators.extend_right_actuator()
    sleep(1)
    linear_actuators.retract_right_actuator()
    sleep(1)
    linear_actuators.reset_actuators()

def test_imu():
    temperature   = imu.get_temperature_data()
    gyroscope     = imu.get_gyroscope_data()
    accelerometer = imu.get_accelerometer_data()

    print(f"Temperature: {temperature} C")
    print(f"Gyroscope: {gyroscope} degrees/s")
    print(f"Accelerometer: {accelerometer} g")

def test_lora_transmission():
    lora.transmit("Hello, World!")

def test_lora_reception():
    while True:
        message = lora.recieve()
        if message:
            print(f"Received: {message}")