import threading
from webscraper.main_beerwulf_scraper import run_beerwulf_scraping

class CrawlingThreading:
    def __init__(self,url):
        self.url = url
        thread = threading.Thread(target=self.run,args=())
        thread.daemon = True
        thread.start()

    def run(self):
        print('Thread to crawl beerwulf has started')
        run_beerwulf_scraping()
