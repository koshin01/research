import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import common_theme
import numpy as np

common_theme.setSettings(xtick_labelbottom=True, ytick_labelleft=True)

x = np.linspace(0, 25, 100)
y = x**2


plt.figure(figsize=(10, 6), dpi=300)

sns.lineplot(x=x, y=y, color="limegreen", label="y = x²")

plt.xlim(0, 10)
plt.ylim(0, 100)

plt.xticks(range(0, 11))

for i in range(1, 11):
    plt.plot([0, i], [i**2, i**2], linestyle="--", color="#d1d5db")
    plt.plot([i, i], [i**2, 0], linestyle="--", color="#d1d5db")


plt.savefig("./output/exp.png")
