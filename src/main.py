from time import sleep
import datetime
import Constants
import LORA
import Pico

pico = Pico.Pico()
lora = LORA.LORA()

try:
    logfile = open(Constants.LOG_FILE_PATH, 'a')
except IOError as e:
    print(f"Error opening log file: {e}")
    logfile = None

def main():
    print("STATUS: System starting in Full-Duplex Polling mode...")

    while True:
        try:
            # --- PHASE 1: RECEIVE FROM LORA ---
            incoming_lora = lora.receive()
            if incoming_lora:
                print(f"LORA_IN: {incoming_lora}")
                
                # Logic: Check for PING, otherwise forward to Pico
                if incoming_lora.strip().upper() == "PING":
                    print("STATUS: Received PING, sending PONG")
                    lora.transmit("PONG")
                else:
                    print(f"STATUS: Forwarding LoRa message to Pico")
                    pico.write_data(incoming_lora)

            # --- PHASE 2: RECEIVE FROM PICO & TRANSMIT ---
            pico_data = pico.read_data()
            if pico_data:
                print(f"PICO_IN: {pico_data}")
                
                # Transmit sensor data via LoRa
                if lora.transmit(pico_data):
                    print("STATUS: LoRa Transmission Successful")
                
                # Log the data
                if logfile:
                    logfile.write(f"{datetime.datetime.now()}: {pico_data}\n")
                    logfile.flush()
            
            # Small delay to prevent 100% CPU usage
            sleep(0.05)
            
        except KeyboardInterrupt:
            print("\nSTATUS: Shutting down...")
            break
        except Exception as e:
            print(f"ERROR: Main loop failure: {e}")
            sleep(1)

    # Cleanup
    if logfile: logfile.close()
    pico.close()

if not Constants.TEST_MODE:
    main()