import mysql.connector
import logging
import os
from dotenv import load_dotenv
from main import *

logging.basicConfig(filename="db_scrapping.log",
                    level=logging.INFO, format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')

load_dotenv()


class Table_articles():

    def __init__(self):
        logging.info('Connection with sql docker')
        try:
            self.mydb = mysql.connector.connect(
                host=os.getenv('MYSQL_HOST'),
                user=os.getenv('MYSQL_USER'),
                database=os.getenv('MYSQL_DATABASE'),
                password=os.getenv('MYSQL_PASSWORD'),
            )
        except(mysql.connector.errors.InterfaceError, mysql.connector.errors.ProgrammingError):
            logging.warning(
                'Failed to connect to docker container, check password, or docker connection')

        try:
            self.c = self.mydb.cursor()
        except AttributeError:
            logging.warning(
                'Failed to establish query, check syntax, will affect creation of table')

        logging.info('Connection with sql connector : end')

    def create_table_articles(self):

        self.c.execute("DROP TABLE articles")
        self.c.execute("CREATE TABLE IF NOT EXISTS articles (id TINYINT(6) UNSIGNED NOT NULL AUTO_INCREMENT, title VARCHAR(250) NOT NULL, image VARCHAR(250) NOT NULL, content VARCHAR(250) NOT NULL,  date VARCHAR(255) NOT NULL,  PRIMARY KEY (id))")

    def insert_articles(self):

        insert = "INSERT INTO articles (title,image,content,date) values (%s,%s,%s,%s);"
        value = wiki_articles.bdd_action()
        self.c.executemany(insert, value)
        self.mydb.commit()
