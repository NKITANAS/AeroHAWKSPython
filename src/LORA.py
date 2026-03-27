from LoRaRF import SX126x

class LORA:
    def __init__(self):
        try:
            self.Lora = SX126x()

            # Hardware Configuration
            self.Lora.setSpi(0, 0, 7800000)
            self.Lora.begin()
            self.Lora.setTxPower(22, self.Lora.TX_POWER_SX1262)
            self.Lora.setRxGain(self.Lora.RX_GAIN_POWER_SAVING)
            self.Lora.setFrequency(915000000)
            self.Lora.setLoRaModulation(8, 125000, 5, False)
            self.Lora.setLoRaPacket(self.Lora.HEADER_EXPLICIT, 12, 15, True, False)
            self.Lora.setSyncWord(0x3444)
            
            self.counter = 0
            self.initialized = True
            
            # Start the initial listen request
            self.start_receiving()
            print("LoRa module initialized and listening at 915MHz")
        except Exception as e:
            print(f"Error initializing LoRa module: {e}")
            self.Lora = None
            self.initialized = False

    def start_receiving(self):
        """Non-blocking: tells the radio to start listening for a packet."""
        if self.initialized and self.Lora:
            self.Lora.request()

    def check_for_message(self) -> str:
        """
        Checks if a packet has arrived. 
        Returns the message string if found, else an empty string.
        """
        if not self.initialized or not self.Lora:
            return ""
            
        try:
            # Only process if a packet is actually in the buffer
            if self.Lora.available() > 0:
                message = ""
                # Read all bytes except the last (counter) byte
                while self.Lora.available() > 1:
                    message += chr(self.Lora.read())
                
                # Consume the counter/trailing byte
                _ = self.Lora.read() 
                
                # Immediately return to listening mode
                self.start_receiving()
                return message
            return ""
        except Exception as e:
            print(f"Error in check_for_message: {e}")
            return ""
    
    def transmit(self, message: str) -> bool:
        """Sends a message and then returns the radio to listening mode."""
        if not self.initialized or not self.Lora:
            return False
            
        try:
            message_list = [ord(char) for char in message]

            self.Lora.beginPacket()
            self.Lora.write(message_list)
            self.Lora.write(self.counter)
            self.Lora.endPacket()
            
            # TX wait is usually very short (~100ms)
            self.Lora.wait()
            self.counter += 1
            
            # Crucial: Go back to listening mode after transmitting
            self.start_receiving()
            return True
        except Exception as e:
            print(f"Error transmitting LoRa message: {e}")
            self.start_receiving()
            return False