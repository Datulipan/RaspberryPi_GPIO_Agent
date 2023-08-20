import RPi.GPIO as GPIO

def main():
    # Use the BCM numbering scheme
    GPIO.setmode(GPIO.BCM)

    # List of GPIO pins on the Raspberry Pi 3B+
    gpio_pins = [14,23,24,25,5,12,6,16]

    try:
        for pin in gpio_pins:
            # Set each pin as an input
            GPIO.setup(pin, GPIO.IN)

            # Read the state of the pin
            state = GPIO.input(pin)
            
            print(f"GPIO {pin} is {'HIGH' if state else 'LOW'}")

    finally:
        # Clean up the GPIO settings
        GPIO.cleanup()

if __name__ == '__main__':
    main()
