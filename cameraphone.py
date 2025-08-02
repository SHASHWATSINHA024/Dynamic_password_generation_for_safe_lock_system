import cv2
import os
from datetime import datetime

# URL of the video stream (from mobile/IP camera)
url = 'http://192.168.97.91:8080/video'

# Directory where recordings will be saved
output_dir = 'C:/Users/LEN0VO/PROGRAMS JAVA/camera_samples'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Open the video stream using OpenCV
cap = cv2.VideoCapture(url)

# Get video properties like width, height, and frames per second
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 30  # Set FPS manually (can be adjusted as needed)

# Initialize the first VideoWriter for recording to a default file
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
output_filename = os.path.join(output_dir, 'recordings.mp4')
out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

# Set interval to split recordings (in seconds)
record_interval = 10
start_time = datetime.now()  # Record when the first recording started

# Continuously read frames from the stream
while True:
    ret, frame = cap.read()
    
    if frame is not None:
        cv2.imshow('frame', frame)  # Show the current frame

        # Write the current frame to the video file
        out.write(frame)

        # Check how much time has passed since last file switch
        current_time = datetime.now()
        elapsed_time = (current_time - start_time).total_seconds()
        
        if elapsed_time >= record_interval:
            # Create a new file with a timestamped filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = os.path.join(output_dir, f'recordings_{timestamp}.mp4')
            
            # Close the old writer and open a new one for the new file
            out.release()
            out = cv2.VideoWriter(filename, fourcc, fps, (width, height))
            
            # Reset the start time for the next interval
            start_time = current_time

    # Exit recording if 'q' is pressed
    q = cv2.waitKey(1)
    if q == ord("q"):
        break

# Release all resources properly
out.release()
cap.release()
cv2.destroyAllWindows()
