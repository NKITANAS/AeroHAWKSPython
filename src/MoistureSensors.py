import gpiod

import Constants


# Since the raspbarry pi does not have analog pins, we need to use the sensor's digital output, which is HIGH when the soil is dry and LOW when the soil is wet.
# This does not accomplish the Payload Expiriment, but it is better than nothing and will at least give us some data on whether the soil is dry or wet.
# Possibly use a pico and send the date to the pi via wifi or bluetooth, but that is a major TODO and should be done after the main functionality of the payload is complete.
class MoistureSensors:
    def __init__(self):
        self.moisture_sensor_1_pin = Constants.MOISTURE_SENSOR_1_PIN
        self.moisture_sensor_2_pin = Constants.MOISTURE_SENSOR_2_PIN

    def read_moisture(self) -> float:
        # Read the digital output of the moisture sensors
        moisture_1 = Constants.request.get_value(self.moisture_sensor_1_pin)
        moisture_2 = Constants.request.get_value(self.moisture_sensor_2_pin)

        # Return the average of the two sensors as the final moisture reading
        return moisture_1, moisture_2
