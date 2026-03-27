from LoRaRF import SX126x

class LORA:
    def __init__(self):
        try:
            self.Lora = SX126x()
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
            print("LoRa module initialized successfully")
        except Exception as e:
            print(f"Error initializing LoRa module: {e}")
            self.Lora = None
            self.initialized = False
    
    def receive(self) -> str:
        if not self.initialized or not self.Lora:
            return ""
            
        try:
            # Put into receive mode
            self.Lora.request()
            # Check if a packet is available without a long wait
            # If your library version blocks here, you may need a small timeout
            self.Lora.wait() 

            if self.Lora.available() > 0:
                message = ""
                while self.Lora.available() > 1:
                    message += chr(self.Lora.read())
                _ = self.Lora.read() # Consume the counter byte
                return message
            return ""
        except Exception as e:
            return ""
    
    def transmit(self, message: str) -> bool:
        if not self.initialized or not self.Lora:
            return False
            
        try:
            print(f"DEBUG: Transmitting: {message}")
            messageList = [ord(c) for c in message]

            self.Lora.beginPacket()
            self.Lora.write(messageList)
            self.Lora.write(self.counter)
            self.Lora.endPacket()
            self.Lora.wait() # Wait for Tx to finish
            self.counter += 1
            return True
        except Exception as e:
            print(f"Error transmitting LoRa message: {e}")
            return False