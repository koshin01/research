import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import common_theme

common_theme.setSettings(xtick_labelbottom=True, ytick_labelleft=True)

benford_probs = [np.log10(1 + 1 / d) * 100 for d in range(1, 10)]

digits = range(1, 10)
data = {"digits": digits, "Probability": benford_probs}

sns.barplot(x="digits", y="Probability", data=data, color="limegreen")

plt.xlabel("一桁目")
plt.ylabel("確率(%)")

plt.savefig("./output/benfordlaws.png")
