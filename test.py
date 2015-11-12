from __future__ import division
import RPi.GPIO as gpio
import time
import sys
import os

gpio.setmode(gpio.BCM)
green1 = 25
green2 = 21
red1 = 23 
red2 = 20
orange1 = 12
orange2 = 18
blue1 = 24
blue2 = 16

switch = 5

rest = 0.2

def initialize():
    
    gpio.setup(switch, gpio.IN, gpio.PUD_UP)

    gpio.setup(green1, gpio.OUT)
    gpio.setup(green2, gpio.OUT)
    gpio.setup(red1, gpio.OUT)
    gpio.setup(red2, gpio.OUT)
    gpio.setup(orange1, gpio.OUT)
    gpio.setup(orange2, gpio.OUT)
    gpio.setup(blue1, gpio.OUT)
    gpio.setup(blue2, gpio.OUT)

    gpio.output(green1,0)
    gpio.output(green2,0)
    gpio.output(red1,0)
    gpio.output(red2,0)
    gpio.output(orange1,0)
    gpio.output(orange2,0)
    gpio.output(blue1,0)
    gpio.output(blue2,0)



def alternate_colors(rest, n):

    while n >= 0:
        gpio.output(green1, 1)
        time.sleep(rest)
        gpio.output(green1,0)
        gpio.output(green2, 1)
        time.sleep(rest)
        gpio.output(green2, 0)
        gpio.output(orange1, 1)
        time.sleep(rest)
        gpio.output(orange1, 0)
        gpio.output(orange2, 1)
        time.sleep(rest)
        gpio.output(orange2, 0)
        gpio.output(blue1, 1)
        time.sleep(rest)
        gpio.output(blue1, 0)
        gpio.output(blue2, 1)
        time.sleep(rest)
        gpio.output(blue2, 0)
        gpio.output(red1, 1)
        time.sleep(rest)
        gpio.output(red1, 0)
        gpio.output(red2, 1)
        time.sleep(rest)
        gpio.output(red2, 0)

        n = n-1

def cycle(rest, n):

    while n >= 0:
        gpio.output(green1, 1)
        time.sleep(rest)
        gpio.output(green1,0)
        gpio.output(orange1, 1)
        time.sleep(rest)
        gpio.output(orange1, 0)
        gpio.output(blue1, 1)
        time.sleep(rest)
        gpio.output(blue1, 0)
        gpio.output(red1, 1)
        time.sleep(rest)
        gpio.output(red1, 0)

        gpio.output(green2, 1)
        time.sleep(rest)
        gpio.output(green2, 0)
        gpio.output(orange2, 1)
        time.sleep(rest)
        gpio.output(orange2, 0)
        gpio.output(blue2, 1)
        time.sleep(rest)
        gpio.output(blue2, 0)
        gpio.output(red2, 1)
        time.sleep(rest)
        gpio.output(red2, 0)

        n = n-1

def red(rest, n):

    while n >= 0:
        gpio.output(red1, 1)
        gpio.output(red2, 1)
        time.sleep(rest)
        gpio.output(red1, 0)
        gpio.output(red2, 0)
        time.sleep(rest)
        n = n-1

def green(rest, n):

    while n >= 0:
        gpio.output(green1, 1)
        gpio.output(green2, 1)
        time.sleep(rest)
        gpio.output(green1,0)
        gpio.output(green2, 0)
        time.sleep(rest)
        n = n-1

def blue(rest, n):

    while n >= 0:
        gpio.output(blue1, 1)
        gpio.output(blue2, 1)
        time.sleep(rest)
        gpio.output(blue1,0)
        gpio.output(blue2, 0)
        time.sleep(rest)
        n = n-1

def orange(rest, n):

    while n >= 0:
        gpio.output(orange1, 1)
        gpio.output(orange2, 1)
        time.sleep(rest)
        gpio.output(orange1,0)
        gpio.output(orange2, 0)
        time.sleep(rest)
        n = n-1

def accelerate(rest, n, increment, linear_flag):

    while n >= 0:
        cycle(rest, 0)

        if linear_flag:
            rest = rest - increment
        else:
            rest = rest/increment
        #print "REST = " + str(rest)
        n = n-1

def cleanup():
    initialize()
    gpio.cleanup()

def run():
    initialize()
    while True:
	try:
            red(0.5, 5)
            green(2, 0)
            alternate_colors(.5, 1)
            accelerate(1, 6, 1.5, False)
            cycle((1/1.5)**(6+1), 20)
	    if not gpio.input(switch):
		print "Switch engaged, shutting down..."
		cleanup()
		os.system("sudo shutdown -h now") 
		sys.exit()   
	except KeyboardInterrupt:
	    print "Cleaning up..."
	    cleanup()
	    sys.exit()

#run()
