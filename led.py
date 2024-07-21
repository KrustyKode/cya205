import time

# Define the path to the ACT LED
ledPath = "/sys/class/leds/ACT"

def controlLed(state):
    with open(f"{ledPath}/trigger", "w") as triggerFile:
        triggerFile.write("none")
    with open(f"{ledPath}/brightness", "w") as brightnessFile:
        brightnessFile.write("1" if state else "0")

try:
    while True:
        controlLed(True)  # Turn on the LED
        time.sleep(1)     # Wait for 1 second
        controlLed(False) # Turn off the LED
        time.sleep(1)     # Wait for 1 second
except KeyboardInterrupt:
    pass
