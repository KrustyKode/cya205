from machine import Pin
from time import sleep

led1 = Pin(15, Pin.OUT)
led2 = Pin(14, Pin.OUT)
led3 = Pin(13, Pin.OUT)
led4 = Pin(12, Pin.OUT)

def setLeds(value):
    led1.value((value >> 3) & 1)
    led2.value((value >> 2) & 1)
    led3.value((value >> 1) & 1)
    led4.value(value & 1)

while True:
    for i in range(16):
        setLeds(i)
        sleep(1)