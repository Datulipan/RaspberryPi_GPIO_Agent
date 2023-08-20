GPIO Monitoring Agent for Raspberry Pi

This agent monitors specified GPIO pins on a Raspberry Pi for defined state changes. When a change to a defined state is detected on a given pin, the agent executes a specified script.

Table of Contents:

Prerequisites
Setup
Usage
Configuration
Stopping the Agent
Contributing
License
Prerequisites:

Raspberry Pi with Raspbian GNU/Linux 10 (buster) or later
Python 3.x
RPi.GPIO library

Setup:

Clone this repository or download the gpio_monitor_agent.py script.
Navigate to the directory containing the script.
Install the required libraries:
pip3 install RPi.GPIO
Make the script executable:
chmod +x gpio_monitor_agent.py
Usage:
To start the monitoring agent:
./gpio_monitor_agent.py
or
python3 gpio_monitor_agent.py

Configuration:
To specify the pins to monitor, the desired state to detect, and the script to run upon detection, modify the MONITOR_PINS dictionary in the gpio_monitor_agent.py file.

Example:
MONITOR_PINS = {
18: {"state": GPIO.HIGH, "script": "/path/to/script1.py"},
23: {"state": GPIO.LOW, "script": "/path/to/script2.py"}
}

In the above example, the agent will monitor GPIO pin 18 for a state change to HIGH and will execute /path/to/script1.py when detected. Similarly, it will monitor GPIO pin 23 for a change to LOW and execute /path/to/script2.py when detected.

Stopping the Agent:
To stop the agent, simply press Ctrl + C in the terminal where it's running.

Contributing:
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

License:
This project is open-source. Ensure you comply with the license agreements when using or distributing this software in your projects.