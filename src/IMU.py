import gpiod
import Constants
from mpu6050 import mpu6050

class IMU:
    def __init__(self):
        self.IMU = Constants.IMU

    def get_accelerometer_data(self):
        return self.IMU.get_accel_data()
    
    def get_gyroscope_data(self):
        return self.IMU.get_gyro_data()
    
    def get_temperature_data(self):
        return self.IMU.get_temp()