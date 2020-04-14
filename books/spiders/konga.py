
import scrapy
class BooksSpider(scrapy.Spider):
    name = 'new_test'
    allowed_domains = ['www.kara.com.ng']
    start_urls = [
        'https://www.kara.com.ng/computers-accessories'
    ]
    def parse(self, response):
        for product_url in response.css("h2 > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(product_url), callback=self.products)
        #next_page = response.css("li.item > a[title='Next'] ::attr(href)").extract_first()
        #if next_page:
            #yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def products(self, response):
        item = {}
        product = response.css("div.product-info-main")
        item["product_name"] = response.css(".product-item-link ::text").extract_first()
        yield item
