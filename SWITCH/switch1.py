import RPi.GPIO as GPIO
import time

led = 18
switch = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)

try:
    while True:
        switch_state = GPIO.input(switch)
        time.sleep(0.1)

        if switch_state == 0:
            print("Switch ON - LED ON")
            GPIO.output(led, GPIO.HIGH)
        elif switch_state == 1:
            print("Switch OFF - LED OFF")
            GPIO.output(led, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()

