import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'guide2research.com'
    allowed_domains = ['guide2research.com']
    start_urls = ['https://www.guide2research.com']
    base_url = 'https://www.guide2research.com'
    
    rules = [Rule(LinkExtractor(allow = ["/u/","/journal/","/conference/","/special-issue/","/research/"]), callback='parse', follow=False), 
             Rule(LinkExtractor(allow =('')))]
    

    def parse(self, response):
        filename = response.url + '.html'
        #filename = response.url[31:] + '.html'
        filename = filename.replace('https://www.guide2research.com/', '')
        filename = filename.replace('https://guide2research.com/', '')
        filename = filename.replace('/','?')
        filename = './prova/' + filename
        with open(filename, 'wb') as f:
            f.write(response.body)
        #for href in response.xpath('//a/@href').getall():
        #    yield scrapy.Request(response.urljoin(href), self.parse)



    











 
            
            
