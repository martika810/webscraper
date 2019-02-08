
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webscraper.crawler import BeerCrawler
from webscraper.config.beerwulf_config import BeerwulfConfig

#1. https://www.beerwulf.com/en-gb
#2. https://drizly.com/beer/c2

def main(browser,url, config):

    beer_crawler = BeerCrawler(browser, BeerwulfConfig(browser))
    beer_crawler.scrape(url, 'beerwulf_results.csv')

def setup_browser():
    # Set up the selenium browser
    options = Options()
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')
    browser = webdriver.Chrome('./webscraper/chromedriver', chrome_options=options)
    browser.implicitly_wait(15)
    return browser

def run_beerwulf_scraping():
    beerwulf_url = 'https://www.beerwulf.com/en-gb/c/beers/?page={0}'.format(1)
    browser = setup_browser()
    config = BeerwulfConfig(browser)

    main(browser, beerwulf_url, config)
    browser.quit()

if __name__ == '__main__':

    beerwulf_url = 'https://www.beerwulf.com/en-gb/c/beers/?page={0}'.format(1)
    browser = setup_browser()
    config = BeerwulfConfig(browser)

    main(browser, beerwulf_url, config)
    browser.quit()