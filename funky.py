from machine import Pin
from time import sleep

# Initialize the LEDs
led1 = Pin(15, Pin.OUT)
led2 = Pin(14, Pin.OUT)
led3 = Pin(13, Pin.OUT)
led4 = Pin(12, Pin.OUT)

# Each entry is a tuple: (leds, duration)
# leds is a list of LED objects to turn on
# duration is the time in seconds to keep the LEDs on

# "Won't you take me to Funky Town"
beats = [
    ([led1, led2, led3, led4], 0.3), ([], 0.15),  # "Won't"
    ([led1, led3], 0.15), ([], 0.15),  # "you"
    ([led2, led4], 0.15), ([], 0.15),  # "take"
    ([led1, led2, led3], 0.3), ([], 0.3),  # "me"
    ([led1, led3], 0.15), ([], 0.15),  # "to"
    ([led2, led4], 0.15), ([], 0.15),  # "Funky"
    ([led1, led2, led3, led4], 0.45), ([], 0.45),  # "Town"
]

def flashLeds(leds, duration):
    for led in leds:
        led.value(1)
    sleep(duration)
    for led in leds:
        led.value(0)

while True:
    for leds, duration in beats:
        flashLeds(leds, duration)
