import numpy as np
import matplotlib.pyplot as plt
import os 

def dateien_lesen ():
    for i in range(1,3):   
        file_name =  "input_data/power_data_" + str(i) +".txt"
        power_data_watts = open(file_name).read().split("\n")
        x = np.array(power_data_watts)

        plt.title("Line graph"+ str(i))
        plt.plot(x, color="red")
        plt.show()