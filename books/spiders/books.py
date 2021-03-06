# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = 'jumia_bots'
    allowed_domains = ['jumia.com.ng']
    start_urls = [
        'https://www.jumia.com.ng/home-office/'
    ]

    def parse(self, response):
        for product_url in response.css(".-gallery > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(product_url), callback=self.products)
        #next_page = response.css("li.item > a ::attr(href)").extract_first()
        #if next_page:
            #yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def products(self, response):
        item = {}
        product = response.css("div.col10")
        item["product_name"] = product.css("h1 ::text").extract_first()
        item['price'] = product.css("div.-mtxs > span ::text").extract_first()
        item['brand'] = response.css(".-fs14.-pvxs > a").extract()
        item['link'] = response.css(".link::attr(href)").extract_first()
        item['images'] = response.css("img::attr(data-src)").extract()
        item['sku'] = product.css("#add-to-cart ::attr(data-id)").extract_first()
        item['sku2'] = response.css(".sku.-gallery ::attr(data-sku)").extract()
        item['product_details'] = response.css(".markup.-mhm.-pvl.-oxa::text").extract_first()
        item['key_features'] = response.css(".markup.-pam::text").extract()
        item['specification'] = response.css(".-pvs.-mvxs.-phm.-lsn").extract()
        item['box_have'] = response.css(".markup.-pam::text").extract_first()
        item['rating'] = response.css(".stars._s._al::text").extract()
        yield item
