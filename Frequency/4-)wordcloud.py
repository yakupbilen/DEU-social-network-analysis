# Visualizing frequencies of words with wordcloud

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv("Frequency.csv")
data = dict(zip(df['Word'].tolist(), df['Frequency'].tolist()))

data = df.set_index('Word').to_dict()['Frequency']
word_cloud = WordCloud(background_color="black", width=2000, height=2000, max_words=2000).generate_from_frequencies(data)
plt.figure(figsize=(20, 20))
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis('off')
plt.savefig("4-)WordCloud.png")