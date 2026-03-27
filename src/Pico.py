import Constants
import serial

class Pico:
    def __init__(self):
        try:
            self.ser = serial.Serial(Constants.PICO_SERIAL_PORT, Constants.PICO_BAUD_RATE, timeout=0.1) # Lower timeout for responsiveness
            self.connected = True
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            self.ser = None
            self.connected = False 
        
    def read_data(self):
        # Only read if there is data waiting in the buffer
        if self.connected and self.ser and self.ser.in_waiting > 0:
            try:
                line = self.ser.readline().decode('utf-8').rstrip()
                return line
            except (serial.SerialException, UnicodeDecodeError) as e:
                print(f"Error reading from serial port: {e}")
                return None
        return None

    def write_data(self, data: str):
        """Sends a string to the Pico via Serial"""
        if self.connected and self.ser:
            try:
                # Add a newline so the Pico's readline() can detect the end of the message
                self.ser.write((data + '\n').encode('utf-8'))
                return True
            except serial.SerialException as e:
                print(f"Error writing to serial port: {e}")
        return False
    
    def close(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("Pico serial connection closed")