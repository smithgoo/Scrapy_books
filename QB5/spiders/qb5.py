import scrapy
from bs4 import BeautifulSoup
import requests
from QB5.pipelines import dbHandle
from QB5.items import Qb5Item

class Qb5Spider(scrapy.Spider):
    name = 'qb5'
    allowed_domains = ['qb5.tw']
    start_urls = ['https://qb5.tw']

    def parse(self, response):
        soup = BeautifulSoup(response.text)
        ######获取最近更新的数据
        tlists = soup.find_all('div', attrs={'class': 'txt'})
        # print(tlist)
        item = Qb5Item() 
        for tlist in tlists: 
            xx = tlist.find_all('a')[0]
            print(xx['href'])
            item['url'] = xx['href']
            item['name'] = xx.text
            print('********************************')
            yield item
