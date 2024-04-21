import cv2
import os
from datetime import datetime

# URL of the video stream
url = 'http://192.168.97.91:8080/video'

# Directory to store the recordings
output_dir = 'C:/Users/LEN0VO/PROGRAMS JAVA/camera_samples'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Initialize the video capture
cap = cv2.VideoCapture(url)

# Get the video's width, height, and FPS
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 30  # you can adjust the frames per second as needed

# Initialize VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # codec for mp4 format
output_filename = os.path.join(output_dir, 'recordings.mp4')
out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

# Initialize variables for recording
record_interval = 10  # in seconds
start_time = datetime.now()

while True:
    ret, frame = cap.read()
    if frame is not None:
        cv2.imshow('frame', frame)
        
        # Write the frame to the output video
        out.write(frame)

        # Check if it's time to record
        current_time = datetime.now()
        elapsed_time = (current_time - start_time).total_seconds()
        if elapsed_time >= record_interval:
            # Generate a unique filename with timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = os.path.join(output_dir, f'recordings_{timestamp}.mp4')
            
            # Release the current VideoWriter and create a new one with the new filename
            out.release()
            out = cv2.VideoWriter(filename, fourcc, fps, (width, height))
            
            # Update variables for the next recording
            start_time = current_time

    q = cv2.waitKey(1)
    if q == ord("q"):
        break

# Release VideoWriter and video capture
out.release()
cap.release()
cv2.destroyAllWindows()
