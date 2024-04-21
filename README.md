This is our 4th sem project titled "Dynamic_password_generation_for_safe_lock_system".
We have built a system to host a server (to show otp) for 30 seconds after the ir sensor detects any motion.The prime reason for ir sensor was for power efficiency motive, as this stops unnecessary running of server when not required.
After the server begins , I can access the website using my phone and also as only few ip addr are in the list only those can access the otp else it shows access denied. After entering the otp in keypad 4x4 the servo motor rotates to open 
the gate(but only for 30 sec and it comes back to original position).So this was our safe lock system part.

We also implemented a cctv operation using a smart phone, where the phone is recording and hosting the recording in a server.Our cameraphone.py file connects to the server at start and saves every 20 sec recording and stores it in a directory 
specified in the code itself.

Here we have used three sensors,
1)Camera (smart phone).
2)keypad 4x4
3)ir sensor
NOTE: all the devices are in same network .

We learned about the capability the raspberry pi holds and seek to do more such projects using raspberry pi.




