import requests
from bs4 import BeautifulSoup
import logging

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = 'https://wikileaks.org'


class WikiLeaksArticles():

    logging.basicConfig(filename="scrapper_log.log",
    level=logging.DEBUG, format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')


    def __init__(self): 
        try:
            self.response = requests.get(BASE_URL, verify=False, timeout=5)
            if self.response.status_code == 200:
                self.data = BeautifulSoup(self.response.text, 'html.parser')
        except (requests.exceptions.ConnectionError, requests.ConnectionError) :
            logging.warning("failed to access url, check connection or url")
        
        self.article_title = []
        self.article_img = []
        self.article_dates = []
        self.article_content = []

        self.article_main_content = self.data.find_all('li', class_="tile")

        logging.info('accessing class articles')
    
    def get_article_title(self):
        logging.info('getting article title ----> beginning')

        titles=[]
        try:
            for i in self.article_main_content:
                title=i.h2.text
                print(title)
                titles.append(title)
                self.article_title.append(titles)
                print(titles)
                return self.article_title
        except(IndexError, TypeError):
            logging.warning('no article titles in here, look for the h2 text')
        logging.info('getting article title ---> end ')
    
    def get_article_img(self):
        logging.info('getting article images ----> beginning')
        images=[]
        try:
            for i in self.article_main_content:
                image = "http://wikileaks.com" + i.img.attrs['src']
                images.append(image)
                self.article_img.append(images)
                print(images)
                return self.article_img
        except(IndexError, TypeError):
            logging.warning('no article images in here, look for the img attributes src')
        logging.info('getting article images ---> end ')

        


            # article_date = article.find('div',class_='timestamp').text
            # article_content = article.p.text

    def get_article_content(self):
        logging.info('getting article content ----> beginning')
        contents=[]
        try:
            for i in self.article_main_content:
                content = i.p.text
                # print(content)
                contents.append(content)
                self.article_content.append(contents)
                print(self.article_content)
                return self.article_content
                
        except(IndexError, TypeError):
            logging.warning('no article content in here, look for <p>.text')
        logging.info('getting article content ---> end ')

    def get_article_date(self):
        logging.info('getting article dates ----> beginning')
        dates=[]
        try:
            for i in self.article_main_content:
                date = i.find('div',class_='timestamp').text
                dates.append(date)
                self.article_dates.append(dates)
                print(dates)
                return self.article_dates
        except(IndexError, TypeError):
            logging.warning('no article dates in here, look for the timestamp class')
        logging.info('getting article dates ---> end ')

    def bdd_action(self):
        logging.info("ziping all list to transfer db-- Start")

        try:
            result = list(zip(self.article_title, self.article_img, self.article_content, self.article_dates))
        except (IndexError, TypeError):
            logging.warning("check for error zipping the results of scrapping")
        return result

            

wiki = WikiLeaksArticles()


wiki.get_article_title()
# wiki.get_article_img()
# wiki.get_article_date()
# wiki.get_article_content()
print("zip",wiki.bdd_action())
