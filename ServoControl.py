    
#Created by: Dexter Dixon
#Raspberry Pi Servo control using PWM

from __future__ import division
import time
import pygame
from adafruit_servokit import ServoKit

print('Libraries imported successfully')
pygame.init()

pwm = ServoKit(channels=16)
print('PWM Initialized')

servo_1 = 0

#Makes a new variable gamebad and assigns it the first joystick that was plugged into the RPI. if you want to add a second joystic
#You would put something like "gamepad2 = pygame.joystick.Joystick(1)"
gamepad = pygame.joystick.Joystick(0)
gamepad.init()

#Print statements are super important, especially when debuging code, so try to add them where it makes sense.
print('Joystick Initialized')

while True:

        pygame.event.get()
        
        #We make 2 new variable hat_x and hat_y. These are the 4 D-Pad buttons (You can test how the values change with MapJoystick.py)
        #We will also make another variable and assign it to button(0) which is ussually the "start", select, or "A" button.
        (hat_x,hat_y) = gamepad.get_hat(0)   
        button1 = gampead.get_button(0)
      
''' 
        This is an if statement is going to allow us to use our D-Pad to control the servos. 
        When you press D-Pad up hat_x equals -1, D-Pad down hat_x equals 1.
        servo_1 +=1 and servo_1 -=1 increments/decrements the value of servo1 by 1 each time the program runs through the loop.
        When you hold either up or down the servo will slowly increase or decrease until it reaches it's max 0 or 180.
'''
        #D-Up
        if hat_x == -1:
                if servo_1 == 180:
                    print("Max")
                else:
                    servo_1 +=1
                    print("Opening")
        #D-Down
        if hat_x == 1:
                if servo_1 == 0:
                    print("Max")
                else:
                    servo_1 -=1
                    print("Closing")
'''
        The pwm.servo[].angle function is what sends the PWM signal
        In the "[]" you specify the channel the servo is connected to. Anywhere from 0-15.
        The value you asign, in our case servo1, can be anything from 0-180 (degres).
        This is why above we set a limit with if statments to keep the value in range.
'''
        pwm.servo[0].angle = servo_1
        print("servo_1: ", servo_1)
       
        #If you press button1, then the While True loop stops and the program stops.
        if button1 == 1
                break
                print("Ending Program")

'''
End of Program Tips:
~Keep in mind that in python indentation is very important
~Different controllers have different button and axis values, always double check by running "MapJoystick.py".
~Button and hat values are intergers which don't have percision and can only be a 0 or 1
~Axis values are floats and have precision meaning they have can have decimal places and can be anywhere between -1 and 1
