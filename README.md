
# <div align="center">DEU(Dokuz Eylul University) Social Network Analysis</div>

---
| ❗ | **The outputs of the files are linked, run them in the order in the table of contents.**        |
|---|:------------------------------------------------------------------------------------------------|
---

### <div align="center">Wordcloud</div>

<p align="center">
  <img width="600" height="400" src="wordcloud.png">
</p>
<hr>

### <div align="center">Frequency Plot</div>

<p align="center">
  <img width="700" height="430" src="freq.gif">
</p>
<hr>

### <div align="center">Network Graph</div>

<p align="center">
  <img width="700" height="430" src="degree.gif">
</p>
<hr>



### <div align="center">Table of Contents</div>
1. DataPreparing
   - 1-spider.py
     - MySpider(CrawlSpider)
     - The domain is restricted due to the running time of the program. For other domains, you can see or customize other crawl options in the CrawlOptions.txt file.
   - 2-)clean_link.py
   - 3-)scraping.py
     - Scraping web pages contents.
   - 4-)graph_edges_to_csv.py
     - Find and save all links(edges) between web pages.
2. Frequency
   - 1-)frequency.py
     - Find and save the frequencies of words from web source.
   - 2-)visualize_freq.py
   - 3-)interactive_visualize_freq.py
   - 4-)wordcloud.py
3. Centrality
   - centrality.py
     - Calculates and visualizes web pages centrality values.
4. Sample Result
   - Here, you can see ready results.

