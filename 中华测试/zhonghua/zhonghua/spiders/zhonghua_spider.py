# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import ZhonghuaItem
import re

class ZhonghuaSpiderSpider(RedisSpider):
    name = 'zhonghua_spider'
    allowed_domains = ['china.com']
    # start_urls = ['https://news.china.com/']
    redis_key = 'zh_info'
    def parse(self, response):
        url = response.url
        title = response.xpath('//h1/text()').get()
        category = response.xpath("//div[@id='chan_breadcrumbs']/a[last()]/text()").get()
        publish_time = response.xpath("//div[@class='chan_newsInfo_source']//span[@class='time']//text()").get()
        source = response.xpath("//div[@class='chan_newsInfo_source']//span[@class='source']//text()").get()
        content = ''.join(response.xpath("//div[@id='chan_newsDetail']//text()").getall()).strip()
        # if response.xpath("//div[@class='pageStyle5']/div/a[last()]/text()").get()=='下一页':
        #     next_url = re.findall('https://\w+.china.com/\w+/\d+/\d+/',url)[0]+response.xpath("//div[@class='pageStyle5']/div/a[last()]/@href").get()
        #     next_cont = str(scrapy.Request(url=next_url,callback=self.continue_page))
        #     content = content+next_cont

        item = ZhonghuaItem(url=url,publish_time=publish_time,title=title,category=category,source=source,content=content)
        yield item
    # def continue_page(self,response):
    #     next_cont = ''.join(response.xpath("//div[@id='chan_newsDetail']//text()").getall()).strip()
    #     url = response.url
    #     if response.xpath("//div[@class='pageStyle5']/div/a[last()]/text()").get()=='下一页':
    #         next_url = re.findall('https://\w+.china.com/\w+/\d+/\d+/', url)[0] + response.xpath("//div[@class='pageStyle5']/div/a[last()]/@href").get()
    #         next_cont = next_cont+str(scrapy.Request(url=next_url, callback=self.continue_page))
    #     return next_cont