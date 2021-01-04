import scrapy


class MySpider(scrapy.Spider):
    name = 'guide2research.com'
    allowed_domains = ['guide2research.com']

    def start_requests(self):
        yield scrapy.Request('https://www.guide2research.com', self.parse)

    def parse(self, response):
        filename = response.url + '.html'
        #filename = response.url[31:] + '.html'
        filename = filename.replace('https://www.guide2research.com/', '')
        filename = filename.replace('https://guide2research.com/', '')
        filename = filename.replace('/','?')
        filename = './guide2research/' + filename
        with open(filename, 'wb') as f:
            f.write(response.body)
        for href in response.xpath('//a/@href').getall():
            yield scrapy.Request(response.urljoin(href), self.parse)



    











 
            
            
