import matplotlib.pyplot as plt


f = open("imu.log", "r")
ax = []
ay = []
az = []
gx = []
gy = []
gz = []
for line in f:
    line = line.split()
    if len(line) < 2:
        continue
    if line[0] == "ax":
        ax.append(float(line[2]))
    if line[0] == "ay":
        ay.append(float(line[2]))
    if line[0] == "az":
        az.append(float(line[2]))
    if line[0] == "gx":
        gx.append(float(line[2]))
    if line[0] == "gy":
        gy.append(float(line[2]))
    if line[0] == "gz":
        gz.append(float(line[2]))

plt.subplot(2, 1, 1)
plt.plot(ax, label="ax", marker = "o")
plt.plot(ay, label="ay", marker = "o")
plt.plot(az, label="az", marker = "o")
plt.xlabel("time")
plt.title("accelerometer")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(gx, label="gx", marker = "o")
plt.plot(gy, label="gy", marker = "o")
plt.plot(gz, label="gz", marker = "o")
plt.xlabel("time")
plt.title("gyroscope")

plt.legend()
plt.show()

f.close()