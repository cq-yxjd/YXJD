# -*- coding: utf-8 -*-
import scrapy
import redis
import json
import re

class SinaListSpiderSpider(scrapy.Spider):
    name = 'sina_list_spider'
    allowed_domains = ['sina.com']
    start_urls = []
    r = redis.Redis(host='localhost', port=6379, db=0)
    for i in range(1, 51):
        page_url = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=%s&r=0.7700911531246319&callback=jQuery11120037454374210910135_1566702904687&_=1566702904688' % i
        start_urls.append(page_url)


    def parse(self,response):
        # if 'proxy' not in request.meta:
        #     return request
        resp =response.text
        json_str = re.findall('try{jQuery[\d_]+\((.*?)\);}c', resp)[0]
        datas = json.loads(json_str)
        newsList = datas['result']['data']
        # print('Data:',datas['result']['data'])
        dataLen = len(datas['result']['data'])
        for idx in range(dataLen):
            if self.r.sadd('sina_dupefilter', newsList[idx]["url"]):
                self.r.lpush('xinlang_content_url',newsList[idx]["url"])