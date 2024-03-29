import libmpu9250
import time
import sys

mpu9250 = libmpu9250.MPU9250()

try:
    while True:
        accel = mpu9250.readAccel()
        print(" ax = " , ( accel['x'] ))
        print(" ay = " , ( accel['y'] ))
        print(" az = " , ( accel['z'] ))

        a = pow(accel['x'], 2) + pow(accel['y'], 2) + pow(accel['z'] - 0.6, 2)
        a = pow(a, 0.5)
        print(" a = " , ( a ))

        if a > 0.7:
            print(" falling ")

        time.sleep(0.5)

except KeyboardInterrupt:
    sys.exit()
