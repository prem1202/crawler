# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = 'konga_bots2'
    allowed_domains = ['konga.com']
    start_urls = [
        'https://www.konga.com/category/laptops-5230'
    ]
    def parse(self, response):
        for product_url in response.css("div._4941f_1HCZm > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(product_url), callback=self.products)
        #next_page = response.css("li.item > a[title='Next'] ::attr(href)").extract_first()
        #if next_page:
            #yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def products(self, response):
        item = {}
        product = response.css("div._680e2_KPkEz")
        item["product_name"] = response.css("h3 ::text").extract_first()
        yield item
