#Created by: Dexter Dixon
#PWM example using ServoKit library

from __future__ import division
import time
import pygame
from adafruit_servokit import ServoKit
pygame.init()

pwm = ServoKit(channels=16)
motor_1 = 0
motor_2 = 0
motor_3 = 180

servo_min = 0
servo_max = 180

print('Initialized')

gamepad = pygame.joystick.Joystick(0)
gamepad.init()


while True:

        pygame.event.get()

        leftstick = gamepad.get_axis(1)
        rightstick = gamepad.get_axis(3)
        Lservo = gamepad.get_button(5)
        Rservo = gamepad.get_button(4)

            
        if Lservo == 1:
            motor_3 = motor_3 + .3
            
            if motor_3 > servo_max:
                motor_3 = servo_max
            print("Lservo active")
            
        elif Rservo == 1:
            motor_3 = motor_3 - .3
            
            if motor_3 < servo_min:
                motor_3 = servo_min
            print("Rservo active")

        
        motor_1 = (185  * -leftstick + 390)
        motor_2 = (185 * rightstick +390)
    
        pwm.continuous_servo[0].throttle = motor_1
        pwm.continuous_servo[1].throttle = motor_2

        pwm.servo[2].angle = motor_3
        print("Motor_3: ", motor_3)
