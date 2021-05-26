import os 
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns

fig1_data = pd.read_csv("./junkData.csv")
#Upper left in Carrillo Paper
sns.lineplot(x = "M/N", y = "SNR, dB", data = fig1_data, hue = "Algorithm")
plt.show()
fig2_data = pd.read_csv("./fig2.csv")
#Upper right in Carrillo Paper
sns.lineplot(x = "M/N", y = "Time, sec", data = fig2_data, hue = "Algorithm", markers = True)
plt.show()