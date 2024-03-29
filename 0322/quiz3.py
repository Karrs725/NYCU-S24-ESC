import libmpu9250
import time
import sys
import math

mpu9250 = libmpu9250.MPU9250()

try:
    while True:
        gyro = mpu9250.readGyro()
        print(" gx = " , ( gyro['x'] ))
        print(" gy = " , ( gyro['y'] ))
        print(" gz = " , ( gyro['z'] ))

        roll = math.atan(gyro['y'] / gyro['z'])
        print(" roll = " , ( roll ))

        pitch = math.atan(-gyro['x'] / pow(pow(gyro['y'], 2) + pow(gyro['z'], 2), 0.5))
        print(" pitch = " , ( pitch ))

        time.sleep(0.5)

except KeyboardInterrupt:
    sys.exit()
