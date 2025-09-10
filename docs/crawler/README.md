<h1 style="font-size: 48px">verdant crawler</h1>


## Technologies
![Scrapy](https://img.shields.io/badge/Scrapy-60A839?style=for-the-badge&logo=python&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)


## Steps

<h4>1.) The <a href="../../crawler/main.py">crawler</a> starts at a list of hardcoded, allowed, websites: </h4>

```json
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
```

<h4>2.) The url, title (if any), and description is then scraped for each website and stored in a json file.</h4>

<h4>3.) It then searches for english links to other sites within each existing sites page content, and adds it to the queue to scrape. </h4>

<h4>4.) Finally, the page content is broken up into a frequency dictionary, and stored in a MongoDB database totalling ~25k entries.</h4>

