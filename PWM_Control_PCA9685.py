#Created by: Dexter Dixon
#PWM example using Adafruit PCA9685 library

from __future__ import division
import time
import pygame
import Adafruit_PCA9685
pygame.init()

pwm = Adafruit_PCA9685.PCA9685()
motor_1 = 0
motor_2 = 0
motor_3 = 494

servo_min = 300
servo_max = 494


pwm.set_pwm_freq(60)

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
    
        pwm.set_pwm(0, 0, int(motor_1))
        pwm.set_pwm(1,0, int(motor_2))
        pwm.set_pwm(2, 0, int(motor_3))
        print("Motor_3: ", motor_3)



