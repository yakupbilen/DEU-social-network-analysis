# You should run this py file from command line from right location (scrapy runspider 1-)spider.py)
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MySpider(CrawlSpider):
    name = 'deü'
    allowed_domains = ['www.deu.edu.tr']
    start_urls = ['https://www.deu.edu.tr']
    rules = [
        Rule(LinkExtractor(deny=["https://debis.deu.edu.tr/+",
                                 "https://www.deu.edu.tr/engelsiz/+"],
                           deny_domains="https://debis.deu.edu.tr"),
             callback='parse_item', follow=True)]

    def parse_item(self, response):
        new_response = response.url+"\n"
        with open("all_links.txt", "a") as file_object:
            file_object.write(new_response)
