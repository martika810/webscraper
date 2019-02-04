from bs4 import BeautifulSoup
import pandas as pd
from crawler.progress import save_number_items_scraped_so_far

class PageScraper:
    def __init__(self,browser,config):
        self.browser = browser
        self.config = config

    def total_number_items_to_scrape(self,page_html, url):
        if not self.config.isProductUrl(url):
            return self.config.extract_total_number_items(page_html)
        else:
            return 0


    def count_product_in_page(self, page_html, url):
        # load the product url from configuration
        if not self.config.isProductUrl(url):
            html_parser = BeautifulSoup(page_html, 'html.parser')
            all_products_in_this_page = html_parser.select(self.config.product_css_selector)
            return len(all_products_in_this_page)
        else:
            return 0

    def extract_all_products_in_this_page(self, filename_to_store_results,number_products,dataframe):

        for product_index in range(1,number_products+1):
            all_products_in_this_page = self.browser.find_elements_by_css_selector(self.config.product_css_selector)
            all_products_in_this_page[product_index-1].click()

            product_serie = self.extract_product(self.browser.page_source)
            dataframe = dataframe.append(product_serie, ignore_index=True)
            save_number_items_scraped_so_far(dataframe.shape[0])

        dataframe.to_csv(filename_to_store_results)
        json_filename = filename_to_store_results.replace(".csv",".json")
        dataframe.to_json(json_filename)
        return dataframe

    def extract_product(self,product_html_page):
        product_data = self.config.extract_product_data(product_html_page)
        self.browser.back()
        return pd.Series(product_data,index= product_data.keys())

