#Created by: Dexter Dixon
#Raspberry Pi Motor control usint PWM

from __future__ import division
import time
import pygame
from adafruit_servokit import ServoKit

print('Libraries imported successfully')
pygame.init()

pwm = ServoKit(channels=16)
print('PWM Initialized')

motor_1 = 0

#Makes a new variable gamebad and assigns it the first joystick that was plugged into the RPI. if you want to add a second joystic
#You would put something like "gamepad2 = pygame.joystick.Joystick(1)"
gamepad = pygame.joystick.Joystick(0)
gamepad.init()

#Print statements are super important, especially when debuging code, so try to add them where it makes sense.
print('Joystick Initialized')

while True:

        pygame.event.get()
        
        #We make a new variable "leftstick" and asign it the value of our gamepad's axis one
        #(Ussually the Y-axis on the left or right joystick) You can check by running the mapjostick program.
        leftstick = gamepad.get_axis(1)
      
''' 
        This is an if statement that allows us to find a stopping value. Normally giving motor_1 a value of 0 will completely
        stop the motors, but in the case that is does not come to a complete stop you can increment or decrement the stopValue
        by 0.01 (depending on the direction in spins while idle) until your motors are completely stopped when you not moving the joystick.
        The "if abs(leftstick) < 0.2:" is like a safety, so it will ignore any value under 0.2. This is not necessary, but it is useful.
'''
        stopValue = 0
        if abs(leftstick) < 0.2:
                motor_1 = stopValue
        else:
                motor_1 = leftstick
        
        pwm.continuous_servo[0].throttle = motor_1
        
        print("Motor_1: ", motor_1)
'''
        The pwm.continuous_servo[0].throttle function is what sends the PWM signal
        In the "[]" you specify the channel the speed controller is connected to, so anywhere from 0-15
        In our case we pass the value motor_1 (value after the "=" sign), which we mapped our left joystick to. We can send a value anywhere from
        -1 which is full reverse, 0 which is stopping, and +1 which is full forward.
'''
