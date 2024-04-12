import magQ
import math
import random

mag_sensors = magQ.gy801()
mag_compass = mag_sensors.compass

ans = random.randint(0, 360)
print(ans)

try:
    while True:
        input("press enter to measure")
        mag_compass.getX()
        mag_compass.getY()
        mag_compass.getZ()
        angle = mag_compass.getHeading()
        print("angle = ",angle)

        if angle <= ans + 10 and angle >= ans - 10:
            print("correct")
            break

        elif angle >= ans + 10:
            print("too high")
        
        elif angle <= ans - 10:
            print("too low")
            


        
except KeyboardInterrupt:
    print("Cleanup")
