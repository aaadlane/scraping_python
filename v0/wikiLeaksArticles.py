import requests

from bs4 import BeautifulSoup

BASE_URL ='https://wikileaks.org'


class WikiLeaksArticles:

    def load_page(self,url):
        content = requests.get(url)
        if content.status_code == 200:
            page = BeautifulSoup(content.text, 'html.parser')
            return page

    def getArticleWelcome(self, article):
        page = requests.get(BASE_URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        article_main = soup.find_all('li', class_="tile")

        for article in article_main:
            article_title = article.h2.text
            article_img ="http://wikileaks.com" + article.img.attrs['src']
            article_date = article.find('div',class_='timestamp').text
            article_content = article.p.text

            

