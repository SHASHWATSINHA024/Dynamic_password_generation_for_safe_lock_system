import RPi.GPIO as GPIO
import time

# GPIO pin mapping for rows (R1 to R4) and columns (C1 to C4) of a 4x4 matrix keypad
R1 = 5
R2 = 6
R3 = 13
R4 = 19
C1 = 12
C2 = 16
C3 = 20
C4 = 21

# Setup GPIO mode
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Define GPIO pin for servo control
servoPIN = 18
GPIO.setup(servoPIN, GPIO.OUT)

# Setup PWM for servo motor with 50Hz frequency
pwm = GPIO.PWM(servoPIN, 50)

# Configure row pins as input with pull-down resistors
GPIO.setup(R1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(R2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(R3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(R4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Configure column pins as input with pull-down resistors
GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Helper function to scan a single row for input
def readLine(line, characters, prev_input):
    GPIO.setup(line, GPIO.OUT)
    GPIO.output(line, GPIO.HIGH)  # Enable the current row
    
    # Check each column for button press
    if GPIO.input(C1) == 1 and prev_input[0] == 0:
        prev_input[0] = 1
        return characters[0]
    elif GPIO.input(C2) == 1 and prev_input[1] == 0:
        prev_input[1] = 1
        return characters[1]
    elif GPIO.input(C3) == 1 and prev_input[2] == 0:
        prev_input[2] = 1
        return characters[2]
    elif GPIO.input(C4) == 1 and prev_input[3] == 0:
        prev_input[3] = 1
        return characters[3]
    
    # Reset row to input mode
    GPIO.output(line, GPIO.LOW)
    GPIO.setup(line, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    return None

# Function to rotate servo motor to 90 degrees and back after 30 seconds
def rotate_servo():
    pwm.start(2.5)  # Start PWM with initial duty cycle
    pwm.ChangeDutyCycle(7.5)  # Move servo to 90 degrees
    print("Rotating servo to 90 degrees")
    time.sleep(30)
    pwm.ChangeDutyCycle(2.5)  # Move servo back to 0 degrees
    print("Returning to 0 degrees")
    time.sleep(1)

# Read stored OTP from text file
with open("otp.txt", "r") as file:
    otp = file.read().strip()

# Loop to capture 7-digit OTP input from keypad
entered_otp = ""
prev_input = [0, 0, 0, 0]  # Track previous input state for each column
print("Enter 7-digit OTP:")

while len(entered_otp) < 7:
    for line, chars in zip([R1, R2, R3, R4], [['1', '2', '3', 'A'],
                                              ['4', '5', '6', 'B'],
                                              ['7', '8', '9', 'C'],
                                              ['*', '0', '#', 'D']]):
        char = readLine(line, chars, prev_input)
        if char:
            entered_otp += char
            print("Input:", entered_otp)
    
    # Reset column states if no input
    if all(GPIO.input(pin) == 0 for pin in [C1, C2, C3, C4]):
        prev_input = [0, 0, 0, 0]

# Compare entered OTP with stored OTP
if entered_otp == otp:
    print("OTP matched! Rotating servo.")
    rotate_servo()
else:
    print("Incorrect OTP!")

# Clean up GPIO after execution
pwm.stop()
GPIO.cleanup()
