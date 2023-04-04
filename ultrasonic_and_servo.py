#!/usr/bin/env python3
"""
Created by: Evan Beaudoin
Created on: March 2023
Uses the HC-SR04 distance sensor to print the distance
"""

import time
import board
import adafruit_hcsr04
import pwmio
from adafruit_motor import servo
import threading


pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP13, echo_pin=board.GP14)


def main() -> None:
    while True:
        print((sonar.distance,))
        time.sleep(0.1)
        
        if sonar.distance < 10:
            my_servo.angle = 180
            # time.sleep(0.5)
        else:
            my_servo.angle = 0
            # time.sleep(0.5)
            
        
    
if __name__ == "__main__":
    main()
    
