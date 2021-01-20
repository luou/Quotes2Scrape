import scrapy


class QuotesSpider(scrapy.Spider):
    name = "toscrape-xpath"  # must be unique within a project
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]
    # # return an iterable of Requests (you can return a list of requests or write a generator function)
    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'text': quote.xpath('span/text()').get(),
                'author': quote.xpath('span/small[@class="author"]/text()').get(),
                'tags': quote.xpath('div[@class="tags"]/a[@class="tag"]/text()').getall(),
            }
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(next_page, callback=self.parse)
