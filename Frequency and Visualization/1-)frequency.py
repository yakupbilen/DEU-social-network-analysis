# Find the frequencies of words from web source(html) and save it
import pandas as pd
from bs4 import BeautifulSoup
from nltk import WhitespaceTokenizer
import string
from nltk.probability import FreqDist


tokenizer = WhitespaceTokenizer()
stopwords = []
with open("turkish_stop_words.txt", "r", encoding="utf-8-sig") as file_ob:
    text = file_ob.read()
    for word in tokenizer.tokenize(text):
        stopwords.append(word)

df = pd.read_csv("../DataPreparing/Web-Source.csv")
web = df["web"].tolist()
source = df["source"].tolist()
all_words = []
page_all_words = []

for html in source:
    soup = BeautifulSoup(html.encode('utf-16'), "html.parser")
    text = soup.getText(separator=u' ')
    page_all_words.append(text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = tokenizer.tokenize(text)
    for word in text:
        if word not in stopwords:
            all_words.append(word.strip("“").strip("”").lower())


fdist = FreqDist(all_words)
page_count = []
delete =[]

for word in fdist.keys():
    i = 0
    for page in page_all_words:
        if page.__contains__(word):
            i += 1
    if i == 0 or len(word) == 1:
        delete.append(word)
    else:
        page_count.append(i)

for word in delete:
    fdist.pop(word)

dict = {"Word": fdist.keys(), "Frequency": fdist.values(), "Number of Pages": page_count}
data = pd.DataFrame.from_dict(dict)
data = data.sort_values(by=['Frequency', "Number of Pages"], ascending=False)
data.to_csv("Frequency.csv", index=False, encoding="utf-8-sig")

