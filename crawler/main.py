from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import SearchPage
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# fix for consistent results in langdetect
DetectorFactory.seed = 0

class Spider(CrawlSpider):
    name = "myCrawler"
    allowed_domains = [
           "wikipedia.org",
           "gutenberg.org",
           "realpython.com",
           "allrecipes.com",
           "ocw.mit.edu",
           "arxiv.org",
           "wikihow.com",
           "w3schools.com",
           "geeksforgeeks.org",
           "reuters.com",
           "propublica.org",
           "openstax.org",
           "archive.org",
           "ted.com",
           "wiki.openstreetmap.org",
           "publicdomainreview.org"]

    start_urls = [
         "https://en.wikipedia.org/wiki/Wikipedia:Contents",
         "https://en.wikipedia.org/wiki/Main_Page",
         "https://en.wikipedia.org/wiki/Category:Technology",
         "https://en.wikipedia.org/wiki/Category:Science",
         "https://en.wikipedia.org/wiki/Category:Main_topic_classifications",
         "https://www.gutenberg.org/",
         "https://realpython.com/",
         "https://allrecipes.com/",
         "https://ocw.mit.edu/",
         "https://arxiv.org/",
         "https://www.medrxiv.org/",
         "https://www.biorxiv.org/",
         "https://doaj.org/search/journals?source=%7B%22query%22%3A%7B%22match_all%22%3A%7B%7D%7D%2C%22size%22%3A50%2C%22sort%22%3A%5B%7B%22created_date%22%3A%7B%22order%22%3A%22desc%22%7D%7D%5D%2C%22track_total_hits%22%3Atrue%7D",
         "https://doaj.org/search/articles?source=%7B%22query%22%3A%7B%22match_all%22%3A%7B%7D%7D%2C%22size%22%3A50%2C%22sort%22%3A%5B%7B%22created_date%22%3A%7B%22order%22%3A%22desc%22%7D%7D%5D%2C%22track_total_hits%22%3Atrue%7D",
         "https://www.ncbi.nlm.nih.gov/guide/all/",
         "https://www.wikihow.com/Main-Page",
         "https://www.wikihow.com/Category:Computers-and-Electronics",
         "https://www.wikihow.com/Category:Finance-and-Business",
         "https://www.w3schools.com/",
         "https://www.geeksforgeeks.org/java/java/",
         "https://www.reuters.com/",
         "https://www.reuters.com/technology/",
         "https://www.reuters.com/business/",
         "https://www.propublica.org/",
         "https://openstax.org/",
         "https://archive.org/details/texts",
         "https://www.ted.com/talks",
         "https://www.ted.com/talks?sort=relevance&topics%5B0%5D=business",
         "https://wiki.openstreetmap.org/",
         "https://publicdomainreview.org/"
    ]

    rules = (
        Rule(LinkExtractor(), callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        item = SearchPage()
        item["url"] = response.url
        item["title"] = response.xpath('//title/text()').get(default='').strip()

        paragraphs = response.xpath('//p//text()').getall()
        paragraph_text = ' '.join([p.strip() for p in paragraphs if p.strip()])

        try:
            lang = detect(paragraph_text)
        except LangDetectException:
            lang = 'unknown'

        if lang == 'en' and paragraph_text:
            item["content"] = paragraph_text
            yield item
        else:
            pass
