from scrapper import *
from bd_scrap import *
import logging


###### thx to MarwaCoding for encapsuling the functions into classes : https://github.com/Marwacoding/web_scrapping ######

logging.basicConfig(level=logging.DEBUG,
                    filename="scrapper_main.log",
                    filemode="a", 
                    format='%(asctime)s : %(levelname)s : %(message)s')

def main(): 
    wiki_articles = WikiLeaksArticles()

    try:
        title = wiki_articles.get_article_title()
        logging.info('article title : OK')
    except:
        logging.warning('article title : MISSING')

    try:
        img = wiki_articles.get_article_img()
        logging.info('article image : OK')
    except:
        logging.warning('article image : MISSING')

    
    try:
        content = wiki_articles.get_article_content()
        logging.info('article content : OK')
    except:
        logging.warning('article content : MISSING')

    try:
        date = wiki_articles.get_article_date()
        logging.info('article date : OK')
    except:
        logging.warning('article date : MISSING')

    try:
        results = wiki_articles.bdd_action()
        logging.info('getting the list')
    except:
        logging.warning('list is missing')


    my_table = Table_articles()

    try:
        create_db = my_table.create_table_articles()
        logging.info("Create table articles: OK")
    except:
         logging.warning("failed to create table")

    try:
        insert = my_table.insert_articles()
        logging.info("successfully inserted to table article")
    except:
        logging.warning("failed to insert into table article")

if __name__ == '__main__':
    main()