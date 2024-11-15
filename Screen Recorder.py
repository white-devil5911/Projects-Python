import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

# Get screen dimensions
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dim = (width, height)

# Define codec and initialize VideoWriter
f = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("test.mp4", f, 30.0, dim)

# Set start and end time
now_start_time = time.time()
dur = 7 + 4
end_time = now_start_time + dur

# Recording loop
while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    output.write(frame)
    c_time = time.time()
    if c_time > end_time:
        break

# Release resources
output.release()
print("---END---")
