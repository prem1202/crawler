# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = 'jumia_bots'
    allowed_domains = ['jumia.com.ng']
    start_urls = ['https://www.jumia.com.ng/laptops/']

    def parse(self, response):
        for product_url in response.css(".-gallery > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(product_url), callback=self.products)
        #next_page = response.css("li.next > a ::attr(href)").extract_first()
        #if next_page:
            #yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def products(self, response):
        item = {}
        product = response.css("div.col10")
        item["product_name"] = product.css("h1 ::text").extract_first()
        item['price'] = product.css("div.-mtxs > span ::text").extract_first()
        item['link'] = response.css(".link::attr(href)").extract_first()
        item['link2'] = response.css(".link::attr(href)").extract()
        item['images'] = response.css("img::attr(data-src)").extract()
        item['brand'] = product.css(".-fs14.-pvxs > a::text").extract()
        item['product_details'] = response.css(".markup.-mhm.-pvl.-oxa::text").extract_first()
        yield item
