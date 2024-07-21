# Name:                         led.py
# Author:                       Michael Sineiro
# Date of latest revision:      7/21/2024
# Purpose:                      Controls a PI 4's onboard LED to display SOS in morse code.

import time

# Define the path to the ACT LED
ledPath = "/sys/class/leds/ACT"

def controlLed(state):
    with open(f"{ledPath}/trigger", "w") as triggerFile:
        triggerFile.write("none")
    with open(f"{ledPath}/brightness", "w") as brightnessFile:
        brightnessFile.write("1" if state else "0")

def dot():
    controlLed(True)
    time.sleep(0.5)
    controlLed(False)
    time.sleep(0.5)

def dash():
    controlLed(True)
    time.sleep(1.5)
    controlLed(False)
    time.sleep(0.5)

try:
    while True:
        # SOS: ... --- ...
        for _ in range(3):  # S: ...
            dot()
        time.sleep(1)  # Pause between letters
        for _ in range(3):  # O: ---
            dash()
        time.sleep(1)  # Pause between letters
        for _ in range(3):  # S: ...
            dot()
        time.sleep(3)  # Pause between SOS repetitions
except KeyboardInterrupt:
    pass
