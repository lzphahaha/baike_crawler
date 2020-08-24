# -*- coding:utf-8 -*-

import requests
from lxml import etree


class HtmlDownloader():

    def download(self,url):
        if url is None:
            return None
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel …) Gecko/20100101 Firefox/57.0'.encode('utf-8')}
        r = requests.get(url,headers=headers)
        if r.status_code ==200:
            r.encoding = 'utf-8'
            return r.text
        return None

response = HtmlDownloader().download("https://baike.baidu.com/item/NBA")
print(response)
html = etree.HTML(response)
result = html.xpath("//meta[@name='description']/@content")
print(">>>>>>>>>>>>>>", result)

result = html.xpath("//div[@class='para']/text()")
print(">>>>>>>>>>>>>>", result)
