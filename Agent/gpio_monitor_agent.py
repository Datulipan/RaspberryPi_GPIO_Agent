#!/usr/bin/env python3

"""
Script Name: gpio_monitor_agent.py
Synopsis:
    A simple GPIO monitoring agent for Raspberry Pi.

    This agent uses the BCM (GPIO numbering) mode for specifying the GPIO pins.
    This means you should refer to the pins by their GPIO numbers (e.g., GPIO2, GPIO3) 
    rather than their physical pin numbers on the Raspberry Pi's P1 header.

    - BCM mode (GPIO numbering): Uses the chip's GPIO numbers, i.e., GPIO2, GPIO3, etc.
    - BOARD mode (Physical numbering): Uses the actual physical pin numbers, i.e., Pin 1, Pin 2, etc.
    
    As the script is currently set up, please use the BCM (GPIO) numbering scheme when configuring.

Requirements:
    - Raspberry Pi with Raspbian GNU/Linux 10 (buster) or later
    - Install RPi.GPIO: pip3 install RPi.GPIO
"""

import RPi.GPIO as GPIO
import time
import os
import logging

# Logging configuration
LOG_DIR = "/home/pi/GPIO/Logs"  # <-- Define the desired logging directory
LOG_FILE = "gpio_monitor_agent.log"
logging.basicConfig(filename=os.path.join(LOG_DIR, LOG_FILE), level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIOs to monitor {pin_number: {"state": desired_state, "script": path_to_script}}
"""
Example configuration for multiple pins:
MONITOR_PINS = {
    18: {"state": GPIO.HIGH, "script": "/path/to/script1.py"},
    23: {"state": GPIO.LOW, "script": "/path/to/script2.py"},
    24: {"state": GPIO.HIGH, "script": "/path/to/script3.py"},
    25: {"state": GPIO.LOW, "script": "/path/to/script4.py"}
}
"""
MONITOR_PINS = {
    12: {"state": GPIO.LOW, "script": "/home/pi/GPIO/RunScripts/ignition_off_detected.py"}
}


def setup_gpio():
    """Setup the GPIO pins for monitoring."""
    for pin, data in MONITOR_PINS.items():
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # assuming a normally LOW pin, change as necessary

def detect_change(pin):
    """Callback function to be triggered when a defined condition is detected."""
    if GPIO.input(pin) == MONITOR_PINS[pin]["state"]:
        logging.info("Detected change on GPIO {}. Running script: {}".format(pin, MONITOR_PINS[pin]['script']))
        os.system(f"python3 {MONITOR_PINS[pin]['script']}")

def main():
    setup_gpio()

    # Attach event detect for each GPIO
    for pin, data in MONITOR_PINS.items():
        GPIO.add_event_detect(pin, GPIO.BOTH, callback=detect_change, bouncetime=300)  # 300ms debouncing

    try:
        logging.info("Started GPIO Monitoring Agent")
        while True:
            time.sleep(1)  # Keep the script running

    except KeyboardInterrupt:
        logging.info("GPIO Monitoring Agent stopped by user")

    finally:
        GPIO.cleanup()
        logging.info("GPIO Monitoring Agent stopped and GPIO cleaned up")

if __name__ == "__main__":
    main()
