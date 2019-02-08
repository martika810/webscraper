from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webscraper.config.beerwulf_config import BeerwulfConfig


def test_get_current_number_page():
    url = 'https://www.beerwulf.com/en-gb/c/beers/?page=4'

    beerwulf_config = BeerwulfConfig()


def setup_browser():
    options = Options()
    #options.add_argument('--headless')  # Comment out if you like to see the browser while the script runs
    #options.add_argument('--disable-gpu')
    prefs = {"profile.default_content_setting_values.geolocation" :2}
    options.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome('chromedriver', options=options)
    browser.implicitly_wait(15)
    return browser