# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from .settings import IP_POOL
class PROXY_IP(object):
    pro_url = ''
    def process_request(self,request,spider):
        if 'proxy' not in request.meta:
            if len(IP_POOL) != 0:
                pro_url = IP_POOL[0]
                request.meta['proxy']=pro_url

        # print(request.meta['proxy'])
    # def get_proxy(self):
    #     print('*'*30,'调用了一次代理IP')
    #     headers = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', }
    #     proxy_url = 'http://http.tiqu.alicdns.com/getip3?num=1&type=2&pro=&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
    #     ip_text = requests.get(proxy_url, headers=headers).text
    #     print(ip_text)
    #     if '再试' not in ip_text:
    #         ip_text = json.loads(ip_text)
    #         ip = ip_text['data'][0]['ip']
    #         port = ip_text['data'][0]['port']
    #         # exipre_time = ip_text['data'][0]['expire_time']
    #         print(str(ip) + ':' + str(port))
    #         self.pro_url= str(ip) + ':' + str(port)
    #         time.sleep(5)
