import RPi.GPIO as GPIO  # Library to control Raspberry Pi's GPIO pins
import time
import subprocess  # Used to run external programs
import signal  # Used for sending signals like SIGTERM to processes

# Define the GPIO pin connected to the IR sensor
IR_PIN = 23

# Set up GPIO mode (BCM numbering) and configure the IR sensor pin as input
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN)

try:
    while True:
        # Read the IR sensor state: LOW means object detected (based on most IR sensor logic)
        ir_state = GPIO.input(IR_PIN)
        
        if ir_state == GPIO.LOW:
            print("Object detected!")
            
            # Launch app.py as a separate process
            process = subprocess.Popen(["python", "app.py"])
            
            # Keep the process running for 30 seconds
            time.sleep(30)
            
            # Terminate the app.py process after 30 seconds
            process.terminate()  # Sends SIGTERM; for SIGKILL use process.kill()
            print("App terminated.")
        else:
            print("No object detected")
        
        # Delay between sensor checks to prevent CPU overuse
        time.sleep(0.1)

except KeyboardInterrupt:
    # Graceful exit on Ctrl+C
    print("Exiting...")

finally:
    # Clean up GPIO settings to reset pins and avoid conflicts
    GPIO.cleanup()
