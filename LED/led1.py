import RPi.GPIO as GPIO
import time

led = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

try:
    while True:
        GPIO.output(led, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)
        GPIO.output(led, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)
except KeyboardInterrupt:
   print("\nSucessfully Interupted")

finally:
    print("Sucessfully Exited")
    GPIO.cleanup()
