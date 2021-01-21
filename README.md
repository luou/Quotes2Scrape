# Quotes2Scrape
This project is created to scrape the website `quotes.toscrape.com <http://quotes.toscrape.com/>` that lists quotes from famous authors using Scrapy. The scraped data are stored in an SQLite database and/or json files.

# Usage
If Scrapy is not already installed on your system, please simply run `pip install scrapy`. 

To put a spider with name ``toscrape-css`` to work and store the scraped data in json files, go to the project's top level directory ``scrapy_mini_project`` and run: ```scrapy crawl toscrape-css -o css-scraper-results.json```. Spiders (see the python files in the spiders folder) are classes that we define and that Scrapy uses to scrape information from a website (or a group of websites). They define the initial requests to make, optionally how to follow links in the pages, and how to parse the downloaded page content to extract data.

We can also provide command line arguments to a spider by using the ``-a`` option when running them: ``scrapy crawl quotetag -o quotes-humor.json -a tag=humor``. These arguments are passed to the spider's ``__init__`` method and become spider attributes by default.

# Resources
`<https://docs.scrapy.org/en/latest/intro/tutorial.html>`
