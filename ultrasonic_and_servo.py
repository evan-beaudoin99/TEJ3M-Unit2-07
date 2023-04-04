#!/usr/bin/env python3
"""
Created by: Evan Beaudoin
Created on: March 2023
Uses the HC-SR04 distance sensor to move a servo
"""

import time
import board
import adafruit_hcsr04
import pwmio
from adafruit_motor import servo


pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP13, echo_pin=board.GP14)


def main() -> None:
    # setup
    train_coming = False
    arm_up = True
    
    my_servo.angle = 180
    print("starting")
    time.sleep(1.0)
    
    
    # loop
    while True:
        print((sonar.distance,))
        time.sleep(0.1)
        
        if sonar.distance < 10:
            train_coming = True
        else:
            train_coming = False
            
        if arm_up == True and train_coming == True:
            # move arm down
            my_servo.angle = 0
            time.sleep(1.5)
            arm_up = False
        elif arm_up == False and train_coming == False:
            # move arm up
            my_servo.angle = 180
            time.sleep(1.5)
            arm_up = True            
        
    
if __name__ == "__main__":
    main()
    
