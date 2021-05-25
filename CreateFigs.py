import os 
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns

junk_data = pd.read_csv("./junkData.csv")
sns.lineplot(x = "M/N", y = "SNR, dB", data = junk_data, hue = "Algorithm")
plt.show()