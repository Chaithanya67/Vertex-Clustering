import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MovieDBSpider(CrawlSpider):
    name = 'movieDB'
    
    custom_settings = {
        'DOWNLOAD_DELAY' : '0.1',
        'CONCURRENT_REQUESTS_PER_IP' : '10' 
        }
    
    
    allowed_domains = ['themoviedb.org']
    start_urls = ['https://www.themoviedb.org/discuss']
    base_url = 'https://www.themoviedb.org'
    
    rules = [Rule(LinkExtractor(allow=['/discuss/'], 
                                deny=[ '/movie/.*changes', '/tv/.*changes', '/tv/.*season',
                                      '/person/.*changes','/person/.*images','/u/.*activity','/u/.*list']), callback='parse', follow=False),
             Rule(LinkExtractor(allow=(''),deny=['/network/','/u/','/apps/','/signup/','/talk/','/search/',
                                                 '/keyword/','/collection/','/person/','/company/', '/tv/','/review/']))]



    def parse(self, response):
        filename = response.url + '.html'
        filename = filename.replace('https://www.themoviedb.org/', '')
        filename = filename.replace('/', '?')
        filename = 'discuss?' + filename
        filename = './movieDB_cluster/' + filename
        with open(filename, "wb") as f:
            f.write(response.body)

