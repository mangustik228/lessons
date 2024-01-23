from typing import Iterable
import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request, TextResponse
from app.utils import get_url


class ExampleSpider(RedisSpider):
    name = "example"
    allowed_domains = ["parsinger.ru"]
    start_urls = ["https://parsinger.ru"]
    redis_key = "queue"
    # redis_batch_size = 1
    # max_idle_time = 7

    def parse(self, response: TextResponse):
        items = response.xpath('//div[@class="item"]')
        task = response.meta["task_number"]
        for item in items:
            yield {
                "task": task,
                "title": item.xpath('.//a[@class="name_item"]/text()').get(),
                "url": item.xpath('.//a[@class="name_item"]/@href').get(),
                "price": item.xpath('.//p[@class="price"]/text()').get(),
            }
