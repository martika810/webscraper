from crawler.scraper import PageScraper
from pathlib import Path
import pandas as pd
import pickle

class BeerCrawler:
    def __init__(self,browser,config):
        self.browser = browser
        self.config = config

    def crawl_all_pages_to_end(self,initial_url,file_to_save_results):

        page_scraper = PageScraper(self.browser,self.config)

        try:
            self.browser.get(initial_url)
            self.config.answer_prompt_questions()

            if(self.config.isProductUrl(self.browser.current_url)):
                self.browser.refresh()
                self.browser.back()

            is_last_page = self.config.is_last_page()

            dataframe_file = Path(file_to_save_results)
            if(not dataframe_file.exists()):
                dataframe = pd.DataFrame()
            else:
                dataframe = pd.read_csv(file_to_save_results)

            if(is_last_page):
                number_products_in_this_page = page_scraper.count_product_in_page(self.browser.page_source, self.browser.current_url)
                page_scraper.extract_all_products_in_this_page(file_to_save_results, number_products_in_this_page, dataframe)
                return True
            page_number = self.config.get_current_number_page(self.browser.current_url)
            while not is_last_page:
                number_products_in_this_page = page_scraper.count_product_in_page(self.browser.page_source, self.browser.current_url)
                print('Products found in this page: {0}'.format(number_products_in_this_page))
                dataframe = page_scraper.extract_all_products_in_this_page(file_to_save_results, number_products_in_this_page, dataframe)
                page_number = page_number + 1
                self.config.go_to_next_page(page_number)

                is_last_page = self.config.is_last_page()

            number_products_in_this_page = page_scraper.count_product_in_page(self.browser.page_source, self.browser.current_url)
            page_scraper.extract_all_products_in_this_page(file_to_save_results, number_products_in_this_page, dataframe)

            return True
        except Exception as e:
            print(str(e))
            return False

    def scrape(self, initial_url, file_to_save_results):
        got_to_end = False
        print("Start crawling...")


        got_to_end = self.crawl_all_pages_to_end(initial_url,file_to_save_results)
        if(got_to_end):
            print('Scraping finished successfully')
        else:
            print("Error during scraping")

        print("Finish crawling...")