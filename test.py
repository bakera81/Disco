import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
green1 = 24
green2 = 20
red1 = 16 #DUD
red2 = 23
orange1 = 25
orange2 = 21
blue1 = 12
blue2 = 18

rest = 0.2

def initialize():

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

        n = n-1

def green(rest, n):

    while n >= 0
        gpio.output(green1, 1)
        gpio.output(green2, 1)
        time.sleep(rest)
        gpio.output(green1,0)
        gpio.output(green2, 0)

        n = n-1

def accelerate(rest, n, increment):

    while n >= 0:
        cycle(rest, 0)
        rest = rest - increment
        n = n-1

def run():
    initialize()
    red(0.2, 5)
    green(2, 0)
    alternate_colors(.2, 0)
    accelerate(1.01, 10, .1)
