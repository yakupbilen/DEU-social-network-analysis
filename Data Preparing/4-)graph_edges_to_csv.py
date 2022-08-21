# find and save(GraphEdges.csv) all links(edges) between webpages

import pandas as pd
from bs4 import BeautifulSoup
import re
df = pd.read_csv("Web-Source.csv")
web = df["web"].tolist()
source = df["source"].tolist()
targets = []
sources = []


for i in range(len(web)):
    sources.append("https://www.deu.edu.tr/")
    targets.append(web[i])
    links = source[i].encode('utf-16')
    soup = BeautifulSoup(links, "html.parser")
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        sources.append(web[i])
        targets.append(link.get('href'))


dict = {"Source": sources, "Target": targets}
data = pd.DataFrame.from_dict(dict)
data = data.sort_values(by=["Source"],ascending=False)
data.to_csv("GrahpEdges.csv", index=False, encoding="utf-8-sig")