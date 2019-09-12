# -*- coding: utf-8 -*-
import scrapy
import redis
import time
class ZhlistSpiderSpider(scrapy.Spider):
    name = 'zhlist_spider'
    allowed_domains = ['china.com']
    start_urls = ['https://news.china.com/']
    r = redis.Redis(host='localhost', port=6379, db=0)

    def parse(self, response):
        cate_url = response.xpath("//div[@id='newsNav']//a/@href").getall()
        c_cate_url = list(map(lambda x: 'https:' + x, cate_url))
        for ur in c_cate_url:
            yield scrapy.Request(ur,callback=self.get_list)


    def get_list(self,response):
        info_list = response.xpath("//div[@class='bd defList']//h3/a/@href").getall()
        if len(info_list) == 0:
            info_list =response.xpath("//div[@class='left']//a/@href").getall()  # 政务
        if len(info_list) == 0:
            info_list = response.xpath("//div[@class='r1_left']//a/@href") .getall() # 公益
        if response.url =='https://finance.china.com/':
            info_list = response.xpath('//div[@id="js-media-0"]/div[1]//h3//a/@href').getall()
            info_list=list(map(lambda x:'https://finance.china.com'+x,info_list))
        for info_url in info_list:
            if self.r.sadd('zhonghua_allurl', info_url):
                self.r.lpush('zh_info', info_url)