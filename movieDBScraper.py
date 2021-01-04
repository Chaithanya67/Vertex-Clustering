import scrapy

class MovieDBSpider(scrapy.Spider):
    name = 'movieDB'
    allowed_domains = ['themoviedb.org']

    def start_requests(self):
        yield scrapy.Request('https://www.themoviedb.org', self.parse)

    def parse(self, response):
        filename = response.url + '.html'
        filename = filename.replace('https://www.themoviedb.org/', '')
        filename = filename.replace('/', '?')
        filename = './movieDB/' + filename
        with open(filename, "wb") as f:
            f.write(response.body)
        for href in response.xpath('//a/@href').getall():
            yield scrapy.Request(response.urljoin(href), self.parse)

