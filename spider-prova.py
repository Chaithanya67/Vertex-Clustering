import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'study.eu'
    allowed_domains = ['www.study.eu']
    start_urls = ['https://www.study.eu']
    base_url = 'https://www.study.eu'
    
    rules = [Rule(LinkExtractor(allow = ["/university/..*/..*"]), callback='parse', follow=True), 
             Rule(LinkExtractor(allow =('')),follow=True)]
    

    def parse(self, response):
        filename = response.url + '.html'
        filename = filename.replace('https://www.study.eu/', '')
        filename = filename.replace('https://study.eu/', '')
        if(filename[0] == 'u'):
            filename = 'facoltà_' + filename
        filename = filename.replace('/','?')
        filename = './prova/' + filename
        with open(filename, 'wb') as f:
            f.write(response.body)
        #for href in response.xpath('//a/@href').getall():
        #    yield scrapy.Request(response.urljoin(href), self.parse)



    











 
            
            
