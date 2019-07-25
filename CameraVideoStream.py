#Created by: Dexter Dixon
#Video stream on Raspberry Pi using a single camera
import cv2
import numpy as np

# The cv2.namedWindow() function creates a blank window which is where we will display video later
# In this case, we name the window "Vision" 

cv2.namedWindow("Vision")

#This function takes any number starting at 0 to specify the camera being used 
#For example, to add another camera we would put "camera2 = cv2.VideoCapture(1)"

camera1 = cv2.VideoCapture(0)

while(True):
    # Captures each frame of the camera and puts it into the variable "frame"
    ret, frame = camera1.read()


    # Displays each resulting frame in the window we created earlier called "Vision"
    cv2.imshow('Vision',frame)
    
    # If we press the ESC key, then stop the code and destroy the window "Vision"
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("Vision")
vc.release()
