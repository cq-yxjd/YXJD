import requests
from lxml import etree
import redis
headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome"
}
start_url ='https://news.china.com'
r = redis.Redis(host='localhost',port=6379,db=0)
def get_cate():
    resp =requests.get(url=start_url,headers=headers).text
    html = etree.HTML(resp)
    cate_url = html.xpath("//div[@id='newsNav']//a/@href")
    c_cate_url=list(map(lambda x:'https:'+x,cate_url))
    for ur in c_cate_url:
        get_list(ur)
def get_list(url):
    resp = requests.get(url, headers=headers).text
    html = etree.HTML(resp)
    info_list=html.xpath("//div[@class='bd defList']//h3/a/@href")

    if len(info_list)==0:
        info_list = html.xpath("//div[@class='left']//a/@href")#政务
    if len(info_list)==0:
        info_list = html.xpath("//div[@class='r1_left']//a/@href")#公益
    # if len(info_list)==0:
    #     info_list = html.xpath("//div[@id='js-media-0']/div//h3/a/@href")#财经
    if len(info_list)==0:
        fina_cateurl = html.xpath("//div[@class='bd defList']//h3/a/@href")#财经分类URL
        for u in fina_cateurl:
            cont_resp = requests.get(url='https:'+u, headers=headers).text
            info_list = cont_resp.xpath("//h3/a/@href")
    for info_url in info_list:
        print(info_url)
        if r.sadd('zhonghua_allurl',info_url):
            r.lpush('zh_info',info_url)



if __name__ == '__main__':
    get_cate()