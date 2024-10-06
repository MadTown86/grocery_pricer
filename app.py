import requests
from bs4 import BeautifulSoup
import scrapy


class Spider(scrapy.Spider):
    def __init__(self, name, start_urls):
        self.name = name
        self.start_urls = start_urls
    def _make_requests(self):
        return requests.get(self.start_urls)
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())


if __name__ == '__main__':
    names = ['target', 'walmart', 'amazon', 'samsclub', 'costco', 'heinens']
    start_urls = ['https://www.target.com/s?searchTerm=snacks', 'https://www.walmart.com/', 'https://www.amazon.com/', 'https://www.samsclub.com/', 'https://www.costco.com/', 'https://www.heinens.com/']
    S = Spider(name=names[0], start_urls=start_urls[0])
    S.parse(S._make_requests())
