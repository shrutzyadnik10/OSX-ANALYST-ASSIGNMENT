# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 17:39:24 2023

@author: Shruti
"""
import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
df = pd.read_csv("C:/Users\Shruti\OneDrive\Documents\Company Task\police_department_data.csv")

# Plot the graph
df.plot(kind = 'line')
plt.title('Graph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
