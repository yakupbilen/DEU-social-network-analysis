# Visualizing Frequencies of words with matpoltlib
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Frequency.csv")
word = df["Word"]
freq = df["Frequency"]
page = df["Number of Pages"]

plt.style.use('seaborn')
plt.scatter(page, freq, c='green', edgecolors='black', alpha=0.7, linewidth=1)

cbar = plt.colorbar()
cbar.set_label('Frequency Plot')
plt.xlabel('Number of Pages')
plt.ylabel('Frequency of Words')
plt.xscale('log')
plt.yscale('log')

plt.savefig("2-)Freq.png")
