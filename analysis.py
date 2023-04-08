# script analyse data and calculate charging speed

import matplotlib.pyplot as plt
import numpy as np

filename = "data_25W.txt"

out = open(filename, 'r')
raw_data = out.read()
out.close()

raw_data = raw_data.split("\n")

charge_time = []
charge_level = []

for data in raw_data:
    if len(data.split(",")) != 2:
        break
    charge_time.append(int(data.split(",")[0]) / 60)
    charge_level.append(int(data.split(",")[1]))

coefs = np.polyfit(charge_time, charge_level, 1)
y_calc = []

for i in charge_time:
    y_calc.append(coefs[0] * i + coefs[1])

charge_speed = coefs[0]

plt.plot(charge_time, charge_level, charge_time, y_calc)
plt.title("Charge speed: " + str(round(charge_speed, 2)) + " %/min")
plt.xlabel("charging time [min]")
plt.ylabel("charging level [%]")
plt.show()
