import RPi.GPIO as GPIO
import time
import magQ
import math

v = 343
TRIGGER_PIN = 16
ECHO_PIN = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

mag_sensors = magQ.gy801()
mag_compass = mag_sensors.compass

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

def cosine_law(a, b, C):
    C = math.radians(C)
    c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(C))
    return c

input("press enter to measure AC")
ac_dist = measure()
mag_compass.getX()
mag_compass.getY()
mag_compass.getZ()
ac_angle = mag_compass.getHeading()

input("press enter to measure BC")
bc_dist = measure()
mag_compass.getX()
mag_compass.getY()
mag_compass.getZ()
bc_angle = mag_compass.getHeading()

theta = bc_angle - ac_angle

ab_dist = cosine_law(ac_dist, bc_dist, theta)

print(ab_dist)

GPIO.cleanup()