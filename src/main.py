from time import sleep
import datetime
import Constants
import LORA
import Pico

# Instantiate the classes
pico = Pico.Pico()
lora = LORA.LORA()

try:
    logfile = open(Constants.LOG_FILE_PATH, 'a')
except IOError as e:
    print(f"Error opening log file: {e}")
    logfile = None

def main():
    print("--- System Active (Press Ctrl+C to stop) ---")

    while True:
        try:
            # 1. Check for incoming LORA commands (from Ground Station)
            incoming_lora = lora.check_for_message()
            
            if incoming_lora:
                clean_msg = incoming_lora.strip().upper()
                print(f"RX LORA: {incoming_lora}")

                if clean_msg == "PING":
                    print("ACTION: Responding to PING with PONG")
                    lora.transmit("PONG")
                else:
                    print("ACTION: Forwarding command to Pico")
                    pico.write_data(incoming_lora)

            # 2. Check for incoming PICO data (Sensors)
            pico_data = pico.read_data()
            
            if pico_data:
                print(f"RX PICO: {pico_data}")
                
                # Transmit sensor data via LoRa
                if lora.transmit(pico_data):
                    print("TX LORA: Data sent successfully")
                
                # Log the data locally
                if logfile:
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    logfile.write(f"{timestamp}: {pico_data}\n")
                    logfile.flush()

            # 3. Prevent CPU spiking (Adjust 0.01 to 0.05 depending on required latency)
            sleep(0.01)
            
        except KeyboardInterrupt:
            print("\nSTATUS: Shutting down gracefully...")
            break
        except Exception as e:
            print(f"CRITICAL ERROR in main loop: {e}")
            sleep(1) # Pause briefly on error before retrying

    # Cleanup
    if logfile:
        logfile.close()
    pico.close()

if __name__ == "__main__":
    if not Constants.TEST_MODE:
        main()
    else:
        print("Test mode enabled. Main loop bypassed.")