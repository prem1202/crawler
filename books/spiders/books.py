# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = 'jumia_bots'
    allowed_domains = ['jumia.com.ng']
    start_urls = ['https://www.jumia.com.ng/laptops/']

    def parse(self, response):
        laptops = response.xpath('//a[@class="link"]/@href').extract()
        for laptop in laptops:
            yield Request(laptop, callback=self.parse_page)

    def parse_page(self, response):
        title = response.xpath('//h1[@class="title"]/text()').extract_first()
        product_url = response.url
        brand = response.xpath(
            '//div[@class="sub-title"]/a/text()').extract_first()
        price = '#' + response.xpath(
            '//span[contains(@class, "price")]/span[@dir="ltr"]/@data-price'
        ).extract_first()
        rating1 = response.xpath(
            '//div[@class="container"]/i/following-sibling::span/text()'
        ).extract_first()
        rating2 = response.xpath(
            '//div[@class="container"]/following-sibling::footer/text()'
        ).extract_first()
        rating = rating1 + ': ' + rating2
        rating = rating.replace(',', '.')
        image_urls = response.xpath(
            '//div[@id="thumbs-slide"]/a/@href').extract()
        description = response.xpath(
            '//div[@class="product-description"]/text()').extract_first()

        # Validate fields
        title = field_validator(title)
        product_url = field_validator(product_url)
        brand = field_validator(brand)
        price = field_validator(price)
        rating = field_validator(rating)
        image_urls = field_validator(image_urls)
        description = field_validator(description)

        yield {
            'title': title,
            'product_url': product_url,
            'brand': brand,
            'price': price,
            'rating': rating,
            'image_urls': image_urls,
            'description': description
        }
