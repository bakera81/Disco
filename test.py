import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
green1 = 24
green2 = 20
red1 = 16 #DUD
red2 = 23
orange1 = 25
orange2 = 21
blue1 = 12
blue2 = 18

rest = 0.2

GPIO.setup(green1, GPIO.OUT)
GPIO.setup(green2, GPIO.OUT)
GPIO.setup(red1, GPIO.OUT)
GPIO.setup(red2, GPIO.OUT)
GPIO.setup(orange1, GPIO.OUT)
GPIO.setup(orange2, GPIO.OUT)
GPIO.setup(blue1, GPIO.OUT)
GPIO.setup(blue2, GPIO.OUT)

GPIO.output(green1,0)
GPIO.output(green2,0)
GPIO.output(red1,0)
GPIO.output(red2,0)
GPIO.output(orange1,0)
GPIO.output(orange2,0)
GPIO.output(blue1,0)
GPIO.output(blue2,0)

def alternate_colors():
    n = 5
    while n >= 0:
        GPIO.output(green1, 1)
        time.sleep(rest)
        GPIO.output(green1,0)
        GPIO.output(green2, 1)
        time.sleep(rest)
        GPIO.output(green2, 0)
        GPIO.output(orange1, 1)
        time.sleep(rest)
        GPIO.output(orange1, 0)
        GPIO.output(orange2, 1)
        time.sleep(rest)
        GPIO.output(orange2, 0)
        GPIO.output(blue1, 1)
        time.sleep(rest)
        GPIO.output(blue1, 0)
        GPIO.output(blue2, 1)
        time.sleep(rest)
        GPIO.output(blue2, 0)
        GPIO.output(red1, 1)
        time.sleep(rest)
        GPIO.output(red1, 0)
        GPIO.output(red2, 1)
        time.sleep(rest)
        GPIO.output(red2, 0)
  
        n = n-1

def cycle():
    n = 10
    while n >= 0:
        GPIO.output(green1, 1)
        time.sleep(rest)
        GPIO.output(green1,0)
        GPIO.output(orange1, 1)
        time.sleep(rest)
        GPIO.output(orange1, 0)
        GPIO.output(blue1, 1)
        time.sleep(rest)
        GPIO.output(blue1, 0)
        GPIO.output(red1, 1)
        time.sleep(rest)
        GPIO.output(red1, 0)
        
        GPIO.output(green2, 1)
        time.sleep(rest)
        GPIO.output(green2, 0)
        GPIO.output(orange2, 1)
        time.sleep(rest)
        GPIO.output(orange2, 0)
        GPIO.output(blue2, 1)
        time.sleep(rest)
        GPIO.output(blue2, 0)
        GPIO.output(red2, 1)
        time.sleep(rest)
        GPIO.output(red2, 0)

        n = n-1

cycle()
