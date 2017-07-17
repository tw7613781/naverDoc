# -*- coding: utf-8 -*-
import scrapy



class EliSpider(scrapy.Spider):
    name = 'eli'
    allowed_domains = ['naver.com']
    start_urls = ['http://blog.naver.com/zacking01/221015968811']

    def parse(self, response):
        jump_url = response.xpath('//frame[@id="mainFrame"]/@src').extract()
        real_url = response.urljoin(jump_url[0])
        if real_url is not None:
            yield response.follow(real_url, callback=self.parse_real)
     
     
    def parse_real(self, response):
        for text in response.xpath('//span[@class="se_fs_T4"]/text()').extract():
            yield {'text':text}