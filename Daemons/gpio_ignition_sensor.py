#!/usr/bin/env python3

# Import necessary modules:
# - RPi.GPIO: to interact with Raspberry Pi's GPIO pins
# - time: to introduce delays in the loop, for debouncing purposes
# - os: to run shell commands

import RPi.GPIO as GPIO
import time
import os

# Configurable variables
GPIO_NUMBER = 12  # replace with your GPIO number
COMMAND = "sudo shutdown now"
TRIGGER_STATE = GPIO.LOW  # set to GPIO.HIGH for triggering on high state

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Setup the GPIO as an input pin with an internal pull-up resistor.
GPIO.setup(GPIO_NUMBER, GPIO.IN)

# The main function that contains our monitoring loop
def main():
    # Store the previous input state.
    prev_input = GPIO.input(GPIO_NUMBER)

    # Infinite loop to constantly check the GPIO's state
    while True:
        # Read the current state of the GPIO.
        current_input = GPIO.input(GPIO_NUMBER)

        # Detect a state change
        if current_input == TRIGGER_STATE and current_input != prev_input:
            print(f"GPIO {GPIO_NUMBER} is {TRIGGER_STATE}, triggering command!")
            os.system(COMMAND)

        # Update the previous input state for the next iteration.
        prev_input = current_input
        time.sleep(0.05)

if __name__ == "__main__":
    main()
