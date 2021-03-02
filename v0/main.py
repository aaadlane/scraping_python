#! /usr/bin/env python
import logging
import requests
import pathlib
import os
import mysql.connector

from bs4 import BeautifulSoup


BASE_URL ='https://wikileaks.org'


LOGFILE = pathlib.Path(f'{os.getcwd()}/logs.log')

logging.basicConfig(filename=LOGFILE,
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    datefmt='[%Y-%m-%d %H:%M:%S]')


page = requests.get(BASE_URL)
soup = BeautifulSoup(page.content, 'html.parser')

# def insertInBdd(values):
#     mybdd= mysql.connector.connect(
#         host="localhost", 
#         user="adSql",
#         password="kikoolol",
#         database="articles"
#     )
#     mycursor = mybdd.cursor()
#     val = values
#     sql = "INSERT INTO articles (title,image,content,date) values (%s,%s,%s,%s)"

#     mycursor.execute(sql,val)
#     mybdd.commit()
#     return str(mycursor) + "nouvelle entree"


# def getArticleWelcome():
#     page = requests.get(BASE_URL)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     article_main = soup.find_all('li', class_="tile")

#     for article in article_main:
#         article_title = article.h2.text
#         article_img ="http://wikileaks.com" + article.img.attrs['src']
#         article_date = article.find('div',class_='timestamp').text
#         article_content = article.p.text

#         insertInBdd([article_title,article_img,article_content, article_date])

# getArticleWelcome()
