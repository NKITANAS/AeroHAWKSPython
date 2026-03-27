import Constants
import serial

class Pico:
    def __init__(self):
        try:
            # Short timeout to ensure read_data doesn't hang the main loop
            self.ser = serial.Serial(Constants.PICO_SERIAL_PORT, Constants.PICO_BAUD_RATE, timeout=0.1)
            self.connected = True
            print(f"Pico connected on {Constants.PICO_SERIAL_PORT}")
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            self.ser = None
            self.connected = False 
        
    def read_data(self):
        """Reads a line from the Pico if data is waiting in the buffer."""
        if self.connected and self.ser and self.ser.in_waiting > 0:
            try:
                line = self.ser.readline().decode('utf-8').rstrip()
                return line
            except (serial.SerialException, UnicodeDecodeError) as e:
                print(f"Error reading from serial port: {e}")
                return None
        return None

    def write_data(self, data: str):
        """Sends a string to the Pico."""
        if self.connected and self.ser:
            try:
                # Adding newline because Pico's readline() expects it
                self.ser.write((data + '\n').encode('utf-8'))
                return True
            except serial.SerialException as e:
                print(f"Error writing to Pico: {e}")
        return False
    
    def close(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("Pico serial connection closed")