import RPi.GPIO as GPIO
import time
import subprocess
import signal

# Define the GPIO pins connected to the IR sensor
IR_PIN = 23

# Setup GPIO mode and pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN)

try:
    while True:
        # Read the state of the IR sensor
        ir_state = GPIO.input(IR_PIN)
        
        # Check if an object is detected by the IR sensor
        if ir_state == GPIO.LOW:
            print("Object detected!")
            # Open the file app.py using subprocess
            process = subprocess.Popen(["python", "app.py"])
            # Wait for 30 seconds
            time.sleep(30)
            # Terminate the subprocess after 30 seconds
            process.terminate()
            print("App terminated.")
        else:
            print("No object detected")
        
        time.sleep(0.1)  # Adjust sleep time as needed

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()  # Clean up GPIO settings before exiting
