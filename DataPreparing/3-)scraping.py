# Scrap all websites contents (Web-Source.csv)

from urllib.request import Request, urlopen
import pandas as pd

df = pd.DataFrame(columns=["web","source"])
list_of_links = []

with open("clean_links.txt", "r") as file_object:
    for line in file_object.readlines():
        list_of_links.append(line.strip("\n"))


for i in range(len(list_of_links)):
    r = Request(list_of_links[i], headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(r).read().decode('utf8', errors="ignore").lower()
    row = {"web": list_of_links[i], "source": page}
    df = df.append(row, ignore_index=True)


df.to_csv("Web-Source.csv", index=False)