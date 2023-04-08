import psutil
import time

dt = 20
t = 0

filename = "data_20W"
while psutil.sensors_battery()[0] < 40:
    time.sleep(dt)

data = psutil.sensors_battery()[0]
last = 0

while data < 70:
    data = psutil.sensors_battery()[0]
    if data != last:
        out = open(filename, 'a')
        out.write(str(t) + ", " + str(data) + '\n')
        out.close()
        print("time: " + str(t) + " percentage: " + str(data))
        last = data
    t += dt
    time.sleep(dt)
