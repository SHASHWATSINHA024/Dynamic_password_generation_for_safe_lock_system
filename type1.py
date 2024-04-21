import RPi.GPIO as GPIO
import time

L1 = 5
L2 = 6
L3 = 13
L4 = 19

C1 = 12
C2 = 16
C3 = 20
C4 = 21
servo_pin = 2

# GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Create PWM instance with frequency of 50 Hz
pwm = GPIO.PWM(servo_pin, 50)
OTP_FILE = "otp.txt"

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def rotate_servo():
    
        # Start PWM with duty cycle corresponding to 90 degrees
        pwm.start(7.5)  # 7.5% duty cycle corresponds to 90 degrees

        # Rotate to 90 degrees for 30 seconds
        print("Rotating servo to 90 degrees")
        time.sleep(30)

        # Return to original state (0 degrees)
        print("Returning servo to original state")
        pwm.ChangeDutyCycle(2.5)  # 2.5% duty cycle corresponds to 0 degrees
        time.sleep(1)  # Give time for the servo to reach the position



def readLine(mode, line, characters, prev_input):
    GPIO.setmode(mode)
    GPIO.setup(line, GPIO.OUT)
    GPIO.output(line, GPIO.HIGH)
    time.sleep(0.05)  # Adjust this sleep time as needed
    inputs = [GPIO.input(C1), GPIO.input(C2), GPIO.input(C3), GPIO.input(C4)]
    for i in range(4):
        if inputs[i] == 1 and prev_input[i] == 0:
            return characters[i]
    GPIO.output(line, GPIO.LOW)
    GPIO.setup(line, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set the line back to input
    return None
    
def read_otp_from_file(filename):
    try:
        with open(filename, 'r') as file:
            otp = file.read().strip()
            return otp
    except FileNotFoundError:
        print("OTP file not found.")
        return None

try:
    while True:
        prev_input = [0, 0, 0, 0]
        entered_otp = ""
        print("Enter OTP:")
        while len(entered_otp) < 7:
            input_char = readLine(GPIO.BCM, L1, ["1","2","3","A"], prev_input)
            if input_char is not None:
                entered_otp += input_char
                print("Input:", entered_otp)
                prev_input = [0, 0, 0, 0]
                time.sleep(0.2)  # Additional delay between inputs
                continue
            
            input_char = readLine(GPIO.BCM, L2, ["4","5","6","B"], prev_input)
            if input_char is not None:
                entered_otp += input_char
                print("Input:", entered_otp)
                prev_input = [0, 0, 0, 0]
                time.sleep(0.2)  # Additional delay between inputs
                continue
            
            input_char = readLine(GPIO.BCM, L3, ["7","8","9","C"], prev_input)
            if input_char is not None:
                entered_otp += input_char
                print("Input:", entered_otp)
                prev_input = [0, 0, 0, 0]
                time.sleep(0.2)  # Additional delay between inputs
                continue
            
            input_char = readLine(GPIO.BCM, L4, ["*","0","#","D"], prev_input)
            if input_char is not None:
                entered_otp += input_char
                print("Input:", entered_otp)
                prev_input = [0, 0, 0, 0]
                time.sleep(0.2)  # Additional delay between inputs
        
        print("Entered OTP:", entered_otp)
        
        otp_from_file = read_otp_from_file(OTP_FILE)
        if otp_from_file is not None:
            if entered_otp == otp_from_file:
                print("OTP is correct.")
                rotate_servo()
            else:
                print("Entered OTP does not match.")
        else:
            print("OTP file not found or invalid.")
        
except KeyboardInterrupt:
    print("\nApplication stopped!")
