# -*- coding: utf-8 -*-
import scrapy
from scrapy_maoyan.items import NewsItem
from scrapy import Request
import re


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com/board/4']
    base_urls = 'http://maoyan.com/board/4?offset='

    def start_requests(self):
        for i in range(0,11):
            offset = i*10
            url = self.base_urls + str(offset)
            yield Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        dds = response.css('dd')
        for dd in dds:
            item = NewsItem()
            item['rank'] = dd.css('.board-index::text').extract_first()
            item['movie_name'] = dd.css('.name a::text').extract_first()
            item['actor'] = dd.css('.star::text').extract()
            item['time'] = dd.css('.releasetime::text').extract()
            item['score'] = dd.css('.integer::text').extract()+dd.css('.fraction::text').extract()
            yield item






