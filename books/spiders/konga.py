
import scrapy
class BooksSpider(scrapy.Spider):
    name = 'new_test'
    allowed_domains = ['www.kilimall.ng']
    start_urls = [
        'https://www.kilimall.ng/new/commoditysearch?c=1746&aside=Tablets&gc_id=1746'
    ]
    def parse(self, response):
        for product_url in response.css("div.grid-content.bg-purple > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(product_url), callback=self.products)
        #next_page = response.css("li.item > a[title='Next'] ::attr(href)").extract_first()
        #if next_page:
            #yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def products(self, response):
        item = {}
        product = response.css("div.wrap.goods-info.el-col.el-col-13")
        item["product_name"] = response.css(".title ::text").extract_first()
        yield item
