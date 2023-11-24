import math as m
import matplotlib.pyplot as plt
import numpy as np


a, b, c, d = 5, 16, 8, 18
theta2 = 0
theta = [0, theta2, 0.2, 1.2]
dtheta = [0, 0]
jacobian = np.zeros((2, 2))

x1, y1 = 0, 0
x2, y2 = a * m.cos(theta[1]), a * m.sin(theta[1])
x3, y3 = d + c * m.cos(theta[2]), c * m.sin(theta[2])
x4, y4 = d, 0

plt.figure(figsize=(8, 6))
plt.plot([x1, x2, x3, x4, x1], [y1, y2, y3, y4, y1], 'bo-')
plt.title('4-Bar Linkage')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

