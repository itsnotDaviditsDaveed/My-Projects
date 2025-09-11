import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([1, 2, 3, 4])
y_points = np.array([165.4, 200.31, 954, 560])


plt.grid()
plt.plot(x_points, y_points, "g")

plt.xlabel('Week')
plt.ylabel('Pay')

plt.show()
