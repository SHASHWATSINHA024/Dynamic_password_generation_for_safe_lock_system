This is our 4th sem project titled "Dynamic_password_generation_for_safe_lock_system".
We have built a system to host a server (to show otp) for 30 seconds after the ir sensor detects any motion.The prime reason for ir sensor was for power efficiency motive, as this stops unnecessary running of server when not required.
After the server begins , I can access the website using my phone and also as only few ip addr are in the list only those can access the otp else it shows access denied. After entering the otp in keypad 4x4 the servo motor rotates to open 
the gate(but only for 30 sec and it comes back to original position).So this was our safe lock system part.<br />

We also implemented a cctv operation using a smart phone, where the phone is recording and hosting the recording in a server.Our cameraphone.py file connects to the server at start and saves every 20 sec recording and stores it in a directory 
specified in the code itself.<br />

Here we have used three sensors,<br />
1)Camera (smart phone).<br />
2)keypad 4x4<br />
3)ir sensor<br />
NOTE: all the devices are in same network .<br />

We learned about the capability the raspberry pi holds and seek to do more such projects using raspberry pi.<br />





Firstly connect the ir sensor by going through ir.py.
keypad 4x4 and servo motor connections in type1.py.
ir sensor and servo motor 5v and gnd ports should be connected to 5v and gnd gpio's ,A quick google search can show the gpio table of raspberry pi




