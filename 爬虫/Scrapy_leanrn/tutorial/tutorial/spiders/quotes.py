# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from tutorial.items import QuoteItem

class QuotesSpider(scrapy.Spider):  # 用户自定义的爬虫必须继承自basic类
    name = 'quotes'  # 爬虫名
    allowed_domains = ['quotes.toscrape.com']  # 目标网站的域名
    start_urls = ['http://quotes.toscrape.com/']  # 目标网站的url

    def parse(self, response):  # 此方法主要用于解析服务器返回的网页获取我们所需要的内容
        soup=BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('quote')
        for quote in quotes:
            item = QuoteItem()
            item['text'] = quote.find('text').string()
            item['author']=quote.find('author').string()
            items['tags'] = quote.find('tags').find_all('tag').string()

            r'''
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            '''
            yield item

        # 构造下一页的url
        next = response.css('.pager .next a::attr("href")').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)
