# -*- coding: utf-8 -*-
import scrapy
from ..items import SinaItemsItem
from scrapy_redis.spiders import RedisSpider

class SinaItemsSpiderSpider(RedisSpider):
    name = 'sina_items_spider'
    allowed_domains = ['sina.com']
    # start_urls = ['http://sina.com/']
    redis_key = 'xinlang_content_url'

    def parse(self, response):
        title = response.xpath('//h1/text()').get()
        url = response.url
        publish_time = response.xpath("//span[@class='date']/text()").get()
        source = response.xpath("//div[@class='date-source']/a/text()").get()
        category = response.xpath("//div[@class='channel-path']/a/text()").get()
        content = "".join(response.xpath("//div[@class='article']//p/text()").getall()).strip()
        author = response.xpath("//div[@class='article']/p[last()]/text()").get()
        keywords = ",".join(response.xpath("//div[@class='keywords']//a/text()").getall())
        item = SinaItemsItem(title=title, url=url, publish_time=publish_time, source=source, category=category,content=content, author=author, keywords=keywords)
        yield item

