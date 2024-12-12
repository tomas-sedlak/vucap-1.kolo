import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("polohy_turbin.csv")

plt.scatter(data["Longitude"], data["Latitude"])

for i, txt in enumerate(data["Turbine"]):
    plt.annotate(txt, (data["Longitude"][i], data["Latitude"][i]))

plt.show()