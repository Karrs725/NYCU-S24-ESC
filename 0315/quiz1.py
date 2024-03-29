import RPi.GPIO as GPIO
import time

v = 343
LED_PIN = 12
TRIGGER_PIN = 16
ECHO_PIN = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def measure():
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()
    t = pulse_end - pulse_start
    d = t * v
    d = d / 2
    return d * 100

def blink(s):
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(s)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(s)

try:
    while True:
        d = measure()
        if d <= 50:
            blink(0.5)
        elif d < 100:
            blink(1)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)

        print(d)

except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")

finally:
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()