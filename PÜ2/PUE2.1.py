import numpy as np
import matplotlib.pyplot as plt

file_name = 'input_data/power_data_1.txt'
power_data_watts = open(file_name).read().split("\n")
x = np.array(power_data_watts)

#plt.title("Line graph")
plt.plot(x, color="red")
plt.show()
