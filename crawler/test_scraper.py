from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from crawler.scraper import PageScraper
from crawler.config.beerwulf_config import BeerwulfConfig

def test_count_product_in_page():
    url_to_test = "https://www.beerwulf.com/en-gb/c/beers/?page=1"
    browser = setup_browser()
    config = BeerwulfConfig(browser)
    scraper = PageScraper(browser,config)
    browser.get(url_to_test)
    number_products = scraper.count_product_in_page(browser.page_source,url_to_test)

    assert number_products == 48

    browser.quit()

def test_extract_normal_product():
    url_to_test = "https://www.beerwulf.com/en-gb/p/de-molen-bommen--granaten2/"
    browser = setup_browser()
    config = BeerwulfConfig(browser)
    scraper = PageScraper(browser, config)
    browser.get(url_to_test)
    product_data_extracted = scraper.extract_product(browser.page_source)
    assert product_data_extracted['Title'] == 'De Molen Bommen & Granaten'
    assert product_data_extracted['Picture'] == 'https://www.beerwulf.com/globalassets/catalog/beerwulf/beers/de-molen---bommen-en-granaten_v2.png?h=500&rev=420719671'
    assert product_data_extracted['Description'].split('.')[0] == 'Reddish-brown beer with little foam'
    assert product_data_extracted['Style'] == 'Barley Wine'
    assert product_data_extracted['Volume'] == '33cl'
    assert product_data_extracted['ABV'] == '11.9%'
    assert product_data_extracted['Origin'].replace('\n','') == 'The Netherlands'

    browser.quit()

def test_extract_from_festival_product():
    url_to_test = "https://www.beerwulf.com/en-gb/c/beers/uk-bundles/Festival-Beer-Bundle/"
    browser = setup_browser()
    config = BeerwulfConfig(browser)
    scraper = PageScraper(browser, config)
    browser.get(url_to_test)
    product_data_extracted = scraper.extract_product(browser.page_source)
    assert product_data_extracted['Title'] == 'Not mentioned'
    assert product_data_extracted['Picture'] == 'https://www.beerwulf.com/'
   # assert product_data_extracted['Description'].split('.')[0] == '<p>A selection of easy-to-drink beers, perfect for taking to your festival of choice'
    assert product_data_extracted['Style'] == 'Not mentioned'
    assert product_data_extracted['Volume'] == 'Not mentioned'
    assert product_data_extracted['ABV'] == 'Not mentioned'
    assert product_data_extracted['Origin'].replace('\n','') == 'Not mentioned'

    browser.quit()




def setup_browser():
    options = Options()
    #options.add_argument('--headless')  # Comment out if you like to see the browser while the script runs
    #options.add_argument('--disable-gpu')
    prefs = {"profile.default_content_setting_values.geolocation" :2}
    options.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome('chromedriver', options=options)
    browser.implicitly_wait(15)
    return browser