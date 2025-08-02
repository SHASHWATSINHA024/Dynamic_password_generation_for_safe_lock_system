from flask import Flask, request, abort
import random
import threading
import time

# Create a Flask web application instance
app = Flask(__name__)

# List of IP addresses allowed to access the OTP endpoint
whitelisted_ips = ['192.168.25.48', '192.168.25.61', '192.168.234.243']

# Global variable to store the current OTP sequence
current_sequence = ""

# Background function to generate a new OTP sequence every 30 seconds
def generate_sequence():
    global current_sequence
    while True:
        # Generate a 7-character OTP from allowed characters
        sequence = ''.join(random.choices("1234567890ABCD", k=7))
        
        # Save the generated OTP to a file named "otp.txt"
        with open("otp.txt", "w") as f:
            f.write(sequence)
            f.close()

        # Update the global OTP variable
        current_sequence = sequence
        
        # Wait 30 seconds before generating a new OTP
        time.sleep(30)

# Route to serve the current OTP sequence
@app.route('/')
def get_sequence():
    s = 'access denied'
    
    # Get the IP address of the client making the request
    client_ip = request.remote_addr
    print(client_ip)

    # Check if the client IP is in the whitelist
    if client_ip not in whitelisted_ips:
        return s  # Deny access to unauthorized clients

    # Return the current OTP to authorized clients
    return current_sequence

if __name__ == '__main__':
    # Start the OTP generation thread in the background
    threading.Thread(target=generate_sequence, daemon=True).start()

    # Run the Flask server on all available IPs at port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
