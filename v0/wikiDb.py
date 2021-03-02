import logging
import mysql.connector
import sys


def createDB():
    dbCon = mysql.connector.connect(
        host="localhost",
        user="adSql",
        password="kikoolol",
        database="articles"
    )
    cursor = dbCon.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS articles;')
    dbCon.commit()
    dbCon.close()


def createTableAndInsert(articles):
    dbCon = mysql.connector.connect(
        host="localhost",
        user="adSql",
        password="kikoolol",
        database="articles"
    )
    cursor = dbCon.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS articles (
  id TINYINT(6) UNSIGNED NOT NULL AUTO_INCREMENT,
  title VARCHAR(250) NOT NULL,
  image VARCHAR(250) NOT NULL,
  content VARCHAR(250) NOT NULL,
  date VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
); INSERT INTO articles (title,image,content,date) values (%s,%s,%s,%s);''' articles)
    dbCon.commit()
    dbCon.close()


def handleDB(articles):
    try:
        createDB()
        createTableAndInsert(articles)
    except mysql.connector.Error as err:
        logging.error(f'{err}')
        sys.exit(1)
