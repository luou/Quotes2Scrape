import scrapy
from ..items import ScrapyMiniProjectItem


class QuotesSpider(scrapy.Spider):
    name = "toscrape-css"  # must be unique within a project
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

        items = ScrapyMiniProjectItem()

        for quote in response.css('div.quote'):

            items['text'] = quote.css('span.text::text').get()
            items['author'] = quote.css('small.author::text').get()
            items['tags'] = quote.css('div.tags a.tag::text').getall()

            yield items

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(next_page, callback=self.parse)
