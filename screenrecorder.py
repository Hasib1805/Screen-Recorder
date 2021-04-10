import pyautogui    # pip install pyautogui
import cv2          # pip install opencv-python
import numpy as np  # pip install numpy


#Specify resolution
resolution = pyautogui.size() 

#Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")  

#Specify name of output file
filename = "Recording.avi"

#Specify frames rate.
fps = 60.0

#Creating a video writer object
out = cv2.VideoWriter(filename, codec, fps, resolution)


# Create an emptywindow
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize window
cv2.resizeWindow("Live", 480, 270)

while True:
    # Take screenshot using pyautogui
    img = pyautogui.screenshot() 

    # Convert screenshot to a numpy array
    frame = np.array(img)   
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write it to the output file
    out.write(frame) 

    # Display the recording screen(Optional)
    cv2.imshow('Live', frame)   
    
    # Stop recording when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()