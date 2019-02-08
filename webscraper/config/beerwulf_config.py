from bs4 import BeautifulSoup
from urllib.parse import urljoin

class BeerwulfConfig:
    product_url_pattern='/en-gb/p/'
    product_css_selector = '#product-items-container a.product'
    next_button_css_selector = 'li.VuePagination__pagination-item-next-page > a'
    total_number_items_selector = 'div.meta-header-container > h3'

    element_indicates_if_last_page = 'li.VuePagination__pagination-item-next-page'
    next_button_disabled_class = 'disabled'
    delay_time_in_seconds = 0

    #If the page has popup
    is_there_popup_question_beginning = True
    question_yes_button = '#eighteenTrigger'
    is_there_cookies_question_beginning = True
    agree_use_cookies = '#agreeAndEighteen'
    initial_page = 'https://www.beerwulf.com/en-gb/c/beers/?page={0}'
    host= 'https://www.beerwulf.com/'

    #product properties
    title_css_selector = 'div.product-detail-info-row h1'
    title_alternative_css_selector = 'div.callout h1'
    picture_css_selector = '#product-image'
    picture_alternative_css_selector = 'div.row-packdetail img'
    price_css_selector = 'div.product-detail-info-price div.price-container span.price'
    price_alternative_css_selector = 'div.callout div.price-container span.price'
    description_css_selector = 'div.product-info > div.mobile-pull'
    description_alternative_css_selector = 'div.callout p'
    style_css_selector = 'div.product-info dl dd.columns > a'
    volume_css_selector = 'div.product-info dl dd.columns'
    abv_css_selector = 'div.product-info dl dd.columns'
    origin_css_selector = 'div.product-info dl dd.columns'

    def __init__(self,browser):
        self.browser = browser

    def isProductUrl(self,url):
        return (url.find(self.product_url_pattern) > -1)


    def answer_prompt_questions(self):
        if(self.is_there_popup_question_beginning):
            self.answer_yes_to_popup_question()

        if(self.is_there_cookies_question_beginning):
            self.answer_yes_to_cookies_question()

    def answer_yes_to_popup_question(self):
        yes_button = self.browser.find_element_by_css_selector(self.question_yes_button)
        yes_button.click()
        self.is_there_popup_question_beginning = False

    def answer_yes_to_cookies_question(self):
        yes_button = self.browser.find_element_by_css_selector(self.agree_use_cookies)
        yes_button.click()
        self.is_there_cookies_question_beginning = False

    def get_current_number_page(self,current_url):
        return int(current_url.split('page=')[1])

    def is_last_page(self):
        next_button = self.browser.find_element_by_css_selector(self.element_indicates_if_last_page)
        return next_button.get_attribute('class').find(self.next_button_disabled_class) > -1

    def go_to_next_page(self, current_page_number):
        next_page_element = self.initial_page.format(current_page_number)
        #javascript =next_page_element.get_attribute('href')
        self.browser.get(next_page_element)

    def extract_product_data(self,product_html):
        product_dict = {}
        html_parser = BeautifulSoup(product_html, 'html.parser')

        # title, picture, price, description, style, volume, abv(percentage of alcohool) and origin
        product_dict['Title'] = self.extract_field(html_parser,self.title_css_selector,self.title_alternative_css_selector)

        picture_element = html_parser.select(self.picture_css_selector)
        if(len(picture_element)>0):
            picture = picture_element[0].get('src')
        elif(self.picture_alternative_css_selector):
            if(len(picture_element)>0):
                picture_element = html_parser.select(self.picture_alternative_css_selector)
                picture = picture_element[0].get('src')
            else:
                picture = ''
        else:
            picture = ''
        picture = urljoin(self.host,picture)
        product_dict['Picture'] = picture

        product_dict['Price'] = self.extract_field(html_parser,self.price_css_selector,self.price_alternative_css_selector)

        description = self.extract_field(html_parser,self.description_css_selector,self.description_alternative_css_selector)
        description = description.replace('/n','').strip()
        product_dict['Description'] = description

        product_dict['Style'] = self.extract_field(html_parser,self.style_css_selector,index=0)

        product_dict['Volume']  = self.extract_field(html_parser,self.volume_css_selector,index=1)

        product_dict['ABV'] = self.extract_field(html_parser, self.abv_css_selector,index=2)

        product_dict['Origin'] = self.extract_field(html_parser, self.origin_css_selector,index=3)

        return product_dict

    def extract_field(self,html_parser, css_selector,alternative_css_selector=None,index=0):
        web_element = html_parser.select(css_selector)
        if(len(web_element)>0):
            result = web_element[index].text
        elif(alternative_css_selector):
            web_element = html_parser.select(alternative_css_selector)
            if(len(web_element)>0):
                result = web_element[index].text
            else:
                result = 'Not mentioned'
        else:
            result = 'Not mentioned'

        return result

    def extract_total_number_items(self,html_page):
        html_parser = BeautifulSoup(html_page, 'html.parser')
        total_number_items_element =html_parser.select(self.total_number_items_selector)
        total_number_items =int(total_number_items_element[1].text.split('/')[1].split(' ')[1])
        return total_number_items



