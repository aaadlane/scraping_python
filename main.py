#! /usr/bin/env python

from bs4 import BeautifulSoup
import requests
import mysql.connector


url='https://wikileaks.org'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

def insertInBdd(values):
    mybdd= mysql.connector.connect(
        host="localhost", 
        user="adSql",
        password="kikoolol",
        database="articles"
    )
    mycursor = mybdd.cursor()
    val = values
    sql = "INSERT INTO articles (title,image,content,date) values (%s,%s,%s,%s)"

    mycursor.execute(sql,val)
    mybdd.commit()
    return str(mycursor) + "nouvelle entree"


def getArticle():
    url='https://wikileaks.org'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    article_main = soup.find_all('li', class_="tile")



    for article in article_main:
        article_title = article.h2.text
        article_img ="http://wikileaks.com" + article.img.attrs['src']
        article_date = article.find('div',class_='timestamp').text
        article_content = article.p.text

        insertInBdd([article_title,article_img,article_content, article_date])




getArticle()


