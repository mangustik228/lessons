from typing import Iterable
import scrapy
from scrapy.http import Request, TextResponse
from app.items import ParsingerItem
from app.itemloaders import ParsingerLoader


class PasingerSpider(scrapy.Spider):
    name = "parsinger"
    allowed_domains = ["parsinger.ru"]
    start_urls = ["https://parsinger.ru"]

    def start_requests(self):
        self.logger.info("start")
        i = 1
        url = f"https://parsinger.ru/html/index1_page_{i}.html"
        yield Request(url, meta={"page_number": i})

    def parse(self, response: TextResponse):
        items = response.xpath('//div[@class="item"]')
        for item in items:
            loader = ParsingerLoader(item=ParsingerItem(), selector=item)
            loader.add_xpath("title", './/a[@class="name_item"]/text()')
            loader.add_xpath("url", './/a[@class="name_item"]/@href')
            loader.add_xpath("price", './/p[@class="price"]/text()')
            yield loader.load_item()
        i = response.meta['page_number']
        if i < 5:
            i += 1
            url = f"https://parsinger.ru/html/index1_page_{i}.html"
            yield response.follow(url, meta={"page_number": i}, callback=self.parse)
