import libmpu9250
import time
import sys

mpu9250 = libmpu9250.MPU9250()

try:
    v0 = 0
    while True:
        accel = mpu9250.readAccel()
        # print(" ax = " , ( accel['x'] ))
        # print(" ay = " , ( accel['y'] ))
        # print(" az = " , ( accel['z'] ))

        a = pow(accel['x'], 2) + pow(accel['y'], 2) + pow(accel['z'], 2)
        a = pow(a, 0.5)
        print(" a = " , ( a ))

        v = v0 + a * 0.5
        print(" v0 = " , ( v0 ))
        print(" v = " , ( v ))

        s = v0 * 0.5 + (a * 0.25) / 2
        print(" s = " , ( s ))

        v0 = v
        time.sleep(0.5)

except KeyboardInterrupt:
    sys.exit()
