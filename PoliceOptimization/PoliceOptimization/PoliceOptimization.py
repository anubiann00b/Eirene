import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.tools as stools

from scipy import stats

from mpl_toolkits.mplot3d import Axes3D

def to_num(data):
    return sum([data[b] << b for b in range(len(data))])

raw = pd.read_csv("C:\\Temp\\Random\\Crime_Map.csv")

count = 10000

longi = raw["Longitude"][:count]
lat = raw["Latitude"][:count]
encoded = np.array([to_num(x) for x in stools.categorical(np.array(raw["Offense Type"]),drop=True).astype(int)])[:count]

kde = stats.gaussian_kde(np.row_stack((longi,lat)))

plt.scatter(longi,lat,c=kde(np.row_stack((longi,lat))))
plt.show()
