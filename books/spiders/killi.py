# -*- coding: utf-8 -*-
import scrapy


class KilliSpider(scrapy.Spider):
    name = 'killi_bots'
    allowed_domains = ['kilimall.com']
    start_urls = [
        'https://kilimall.com/ng/category/37'
    ]

    def parse(self, response):
        for product_url in response.css(".-gallery > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(product_url), callback=self.products)
        #next_page = response.css("li.item > a[title='Next'] ::attr(href)").extract_first()
        #if next_page:
            #yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def products(self, response):
        item = {}
        product = response.css("div.col10")
        item["product_name"] = product.css("h1 ::text").extract_first()
        item['price'] = product.css("div.-mtxs > span ::text").extract_first()
        item['brand'] = response.css(".-fs14.-pvxs > a ::text").extract_first()
        item['brand2'] = product.css("#add-to-cart ::attr(data-brand)").extract_first()
        #item['link'] = response.css(".link::attr(href)").extract_first()
        item['images'] = response.css("img::attr(data-src)").extract()
        item['sku'] = product.css("#add-to-cart ::attr(data-id)").extract_first()
        item['categories'] = product.css("#add-to-cart ::attr(data-category)").extract_first()
        item['product_details'] = response.css(".markup.-mhm.-pvl.-oxa::text").extract_first()
        item['key_features'] = response.css(".markup.-pam::text").extract()
        item['specification'] = response.css(".-pvs.-mvxs.-phm.-lsn").extract()
        item['box_have'] = response.css(".markup.-pam::text").extract_first()
        item['rating'] = response.css(".stars._s._al::text").extract()
        item['total_rating'] = response.css(".-plxs.-fs14._more::text").extract()
        item['add_to_cart'] = response.css(".add-to-cart").extract()
        yield item
