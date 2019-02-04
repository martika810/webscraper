from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from crawler.scraper import PageScraper
from crawler.config.drizzly_config import DrizzlyConfig

def test_count_product_in_page():
    url_to_test = "https://drizly.com/belgian-beer/co2428-c2"
    browser = setup_browser()
    config = DrizzlyConfig(browser)
    scraper = PageScraper(browser,config)
    browser.get(url_to_test)
    number_products = scraper.count_product_in_page(browser.page_source,url_to_test)

    assert number_products == 24

    browser.quit()

def test_extract_normal_product():
    url_to_test = "https://drizly.com/stella-artois-premium-belgian-lager/p4868"
    browser = setup_browser()
    config = DrizzlyConfig(browser)
    scraper = PageScraper(browser, config)
    browser.get(url_to_test)
    product_data_extracted = scraper.extract_product(browser.page_source)
    assert product_data_extracted['Title'] == 'Stella Artois'
    assert product_data_extracted['Picture'] == 'https://products1.imgix.drizly.com/ci-stella-artois-f4762eb0a31c5839.jpeg?auto=format%2Ccompress&fm=jpeg&q=20'
    assert product_data_extracted['Description'].split('.')[0] == 'Enjoy the European way with the #1 best-selling Belgian beer in the world'
    assert product_data_extracted['Style'] == 'Pilsner'
    assert product_data_extracted['Volume'] == 'Unavailable'
    assert product_data_extracted['ABV'] == '5%'
    assert product_data_extracted['Origin'].replace('\n','') == 'Belgium'

    browser.quit()

def test_extract_from_festival_product():
    url_to_test = "https://www.beerwulf.com/en-gb/c/beers/uk-bundles/Festival-Beer-Bundle/"
    # browser = setup_browser()
    # config = BeerwulfConfig(browser)
    # scraper = PageScraper(browser, config)
    # browser.get(url_to_test)
    # product_data_extracted = scraper.extract_product(browser.page_source)
    # assert product_data_extracted['Title'] == 'Not mentioned'
    # assert product_data_extracted['Picture'] == 'https://www.beerwulf.com/'
    # #assert product_data_extracted['Description'].split('.')[0] == '<p>A selection of easy-to-drink beers, perfect for taking to your festival of choice'
    # assert product_data_extracted['Style'] == 'Not mentioned'
    # assert product_data_extracted['Volume'] == 'Not mentioned'
    # assert product_data_extracted['ABV'] == 'Not mentioned'
    # assert product_data_extracted['Origin'].replace('\n','') == 'Not mentioned'

    #browser.quit()




def setup_browser():
    options = Options()
    #options.add_argument('--headless')  # Comment out if you like to see the browser while the script runs
    #options.add_argument('--disable-gpu')
    prefs = {"profile.default_content_setting_values.geolocation" :2}
    options.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome('chromedriver', options=options)
    browser.implicitly_wait(15)
    return browser