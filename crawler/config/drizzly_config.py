from bs4 import BeautifulSoup
import time

# https://drizly.com/belgian-beer/co2428-c2
class DrizzlyConfig:
    product_url_pattern='/p'
    product_css_selector = 'div.product-container > section > ul > li > div > a'
    next_button_css_selector = 'div.products-pagination #RightChevronIcon'
    total_number_items_selector = ''

    element_indicates_if_last_page = 'div.products-pagination #RightChevronIcon'
    next_button_disabled_class = 'disabled'

    #If the page has popup
    is_there_popup_question_beginning = False
    question_yes_button = ''
    is_there_cookies_question_beginning = True
    agree_use_cookies = '#ExitIntent div.ExitIntentModal__dismiss'
    host= 'https://drizly.com'

    #product properties
    title_css_selector = 'div.ProductMeta__attribution-container h1'
    picture_css_selector = 'div.ProductMeta__product-image img'
    price_css_selector = 'div.ProductMeta__attribution-container div.product-meta-info span'
    description_css_selector = 'div.ProductDescription div.TextWidget__TextWidget--clamp-5___1RiuE div'
    style_css_selector = 'div.PDPAttributesAndReviews__row__value___1EoK- > span > span'
    volume_css_selector = ''
    abv_css_selector = 'div.PDPAttributesAndReviews__row__value___1EoK- > span > span'
    origin_css_selector = 'div.PDPAttributesAndReviews__row__value___1EoK- > span > span'

    def __init__(self,browser):
        self.browser = browser

    def answer_prompt_questions(self):
        if(self.is_there_cookies_question_beginning):
            try:
                time.sleep(10)
                yes_button = self.browser.find_element_by_css_selector(self.agree_use_cookies)
                yes_button.click()
                self.is_there_cookies_question_beginning = False
            except Exception as e:
                self.is_there_cookies_question_beginning = False



    def is_last_page(self):
        try:
            next_button = self.browser.find_element_by_css_selector(self.element_indicates_if_last_page)
            return next_button == None
        except Exception as e:
            return True

    def go_to_next_page(self,page_number=0):
        next_page_element = self.browser.find_element_by_css_selector(self.next_button_css_selector)
        next_page_element.click()

    def get_current_number_page(self,current_url=''):
        print('Do nothing')
        return 1

    def isProductUrl(self,url):
        return (url.find(self.product_url_pattern) > -1) and (not url.find('/page'))


    def extract_product_data(self,product_html):
        product_dict = {}
        print("Extracting product...")
        html_parser = BeautifulSoup(product_html, 'html.parser')

        # title, picture, price, description, style, volume, abv(percentage of alcohool) and origin
        title_element = html_parser.select(self.title_css_selector)
        title = title_element[0].text
        product_dict['Title'] = title

        picture_element = html_parser.select(self.picture_css_selector)
        picture = picture_element[0].get('src')
        product_dict['Picture'] = picture

        price_element = html_parser.select(self.price_css_selector)
        if(len(price_element)>0):
            price = price_element[0].text
        else:
            price = 'Unavailable'
        product_dict['Price'] = price

        description_element = html_parser.select(self.description_css_selector)
        if(len(description_element)>0):
            description = description_element[0].text.replace('/n','').strip()
        else:
            description = 'Unavailable'
        product_dict['Description'] = description

        style_element = html_parser.select(self.style_css_selector)
        if(len(style_element)>0):
            style = style_element[0].text
        else:
            style = 'Unavailable'
        product_dict['Style'] = style

        volume_element = html_parser.select(self.volume_css_selector)
        if(len(volume_element)):
            volume = volume_element[1].text
        else:
            volume = 'Unavailable'
        product_dict['Volume']  = volume

        abv_element = html_parser.select(self.abv_css_selector)
        if(len(abv_element)>0):
            abv = abv_element[2].text
        else:
            abv = 'Unavailable'
        product_dict['ABV'] = abv

        origin_element = html_parser.select(self.origin_css_selector)
        if(len(origin_element)):
            origin = origin_element[1].text
        else:
            origin = 'Unavailable'
        product_dict['Origin'] = origin
        print("Finish extracting product...")

        return product_dict

