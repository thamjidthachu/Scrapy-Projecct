import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class QuotesSpider(scrapy.Spider):
    name = "properties"
    start_urls = [
        'https://www.bayut.com/property/details-5690203.html'
    ]


    def parse(self, response):
        for quote in response.css('div#body-wrapper'):
            yield {
                'Property_Id' :quote.xpath('main/div[3]/div[1]/div[4]/div/div[2]/ul/li[3]/span[2]/text()').get(),
                'Type' :quote.xpath('main/div[3]/div[1]/div[4]/div/div[2]/ul/li[1]/span[2]/text()').get(),
                'Pupose' :quote.xpath('main/div[3]/div[1]/div[4]/div/div[2]/ul/li[2]/span[2]/text()').get(),
                'Furnishing' :quote.xpath('main/div[3]/div[1]/div[4]/div/div[2]/ul/li[4]/span[2]/text()').get(),
                'Added On' :quote.xpath('main/div[3]/div[1]/div[4]/div/div[2]/ul/li[6]/span[2]/text()').get(),
                'Agent' :quote.xpath('main/div[3]/div[2]/div[1]/div[1]/div/div[2]/div/span/text()').get(),
                'Permit_Number': quote.xpath('main/div[3]/div[2]/div[1]/div[1]/div/div[2]/div/div/span[2]/text()').extract(),
                'Price': quote.css('span._105b8a67::text').extract(),
                'Image_URL': quote.xpath('main/div[3]/div[1]/div[1]/div[1]/picture/img/@src').get(),
                'Location': quote.xpath('main/div[3]/div[1]/div[2]/div[2]/text()').get(),
                'Bed_bath_size': quote.xpath('main/div[3]/div[1]/div[2]/div[3]/div/span[2]/span/text()').getall(),
                'Bread-Crumbs': quote.xpath('main/div[1]/div/div[2]/a/span/text()').get(),
                'Aminities': quote.xpath('main/div[3]/div[1]/div[9]/div/div/div/div[2]/span/text()').getall(),
                'Discription': quote.xpath('main/div[3]/div[1]/div[4]/div/div[1]/div[1]/div/div/div/span[1]/text()').get()
            }
