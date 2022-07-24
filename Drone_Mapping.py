import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from pylab import *

toplam_x = 0
toplam_y = 0
ort_x = 0
ort_y = 0
hesap_x = 0
hesap_y = 0
rad_req = 0
swarm_x = [0, 2, 5, 10, 8]  #Kırmızıların konumu
swarm_y = [9, 14, 2, 1, 7]

plt.figure(figsize=(6, 6))
plt.scatter(swarm_x, swarm_y, color="red")
plt.ylabel("Swarm (m)")
plt.xlabel("Swarm (m)")
xlim(-10, 20)
ylim(-10, 20)

for i in swarm_x:
    toplam_x = i + toplam_x
for i in swarm_y:
    toplam_y = i + toplam_y

ort_x = toplam_x / len(swarm_x)
ort_y = toplam_y / len(swarm_y)
plt.plot(ort_x, ort_y, 'g^')
rad_req = 5 / (2 * (math.sin(math.radians(360 / (len(swarm_x) * 2)))))
print(rad_req)

circle = plt.Circle((ort_x, ort_y), rad_req, color='b', fill=False)
# plt.scatter(ort_x,ort_y+rad_req,color="yellow")

hesap_x_onceki = 0
hesap_y_onceki = rad_req

for i in range(len(swarm_x)):
    hesap_x = (hesap_x_onceki * math.cos(math.radians((360 / len(swarm_x))))) - (
                hesap_y_onceki * math.sin(math.radians((360 / len(swarm_x)))))

    hesap_y = (hesap_x_onceki * math.sin(math.radians((360 / len(swarm_x))))) + (
                hesap_y_onceki * math.cos(math.radians((360 / len(swarm_x)))))

    hesap_x_onceki = hesap_x
    hesap_y_onceki = hesap_y
    plt.scatter(hesap_x_onceki + ort_x, hesap_y_onceki + ort_y, color="yellow")

plt.gca().add_patch(circle)

plt.show()