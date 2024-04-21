from flask import Flask, request, abort
import random
import threading
import time

app = Flask(__name__)
whitelisted_ips =['192.168.25.48','192.168.25.61','192.168.234.243']  # Example list of whitelisted IPs
current_sequence = ""

def generate_sequence():
    global current_sequence
    while True:
        sequence = ''.join(random.choices("1234567890ABCD", k=7))
        with open("otp.txt", "w") as f:
            f.write(sequence)
            f.close()
        current_sequence = sequence
        time.sleep(30)

@app.route('/')
def get_sequence():
    s='access denied'
    client_ip = request.remote_addr
    print(client_ip)
    if client_ip not in whitelisted_ips:
        return s # Access Denied
    return current_sequence

if __name__ == '__main__':
    threading.Thread(target=generate_sequence, daemon=True).start()
    app.run(host='0.0.0.0', port=5000, debug=True)  # Run the Flask app
