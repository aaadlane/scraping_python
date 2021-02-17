
import requests;
from bs4 import BeautifulSoup



# url= 'https://wikileaks.org/popeorders/'
# page =requests.get(url)
# soup = BeautifulSoup(page.content, 'html.parser')

# # print(soup.find(id='summary').h1)


# # print(soup.text)

# def getTitle(url, tag):
#     page =requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     for link in soup.find_all(tag):
#         print(link.get(tag))
#     print(soup.find_all(tag))

# url= 'https://wikileaks.org/'
# getTitle(url, 'h1')


# def getContentArticle(url, tag):
#     page =requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     print(soup.find_all(tag))

# getContentArticle('https://wikileaks.org/dealmaker/Al-Yousef/', 'p')

# def getTitle(url, tag):
#     page =requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     for link in soup.find_all(tag):
#         print(link.get(class))
#     print(soup.find(tag))


# url= 'https://wikileaks.org/popeorders/'
# getTitle(url, id='summary')


# def webscrappy(htmltag, classname, sitename, url):
#     page = requests.get(url)

#     soup = BeautifulSoup(page.content, 'html.parser')
#     results = soup.find("span", class_='pdpprice-row2-main-text')
#     rowcount = db.savetoDB(url, results.text,sitename)
#     print(rowcount)


# url_pricing = "https://www.kohls.com/product/prd-4554171/nespresso-vertuo-next-coffee-espresso-maker-by-delonghi.jsp?skuId=nespresso&search=4554171&submit-search=web-regular"
# webscrappy("span", "pdpprice-row2-main-text", "kohls", url_pricing)

def getTitle(url, tag, class_):
    page =requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for x in soup.find(tag, class_).li:
        print(x)
    print(soup.select()

url='https://wikileaks.org'
# getTitle(url, "ul",class_='grid')

# def getImages(url,tag,class_):
#   page = requests.get(url)
#   soup = BeautifulSoup(page.content, 'html.parser')
#   for y in soup.find_all(tag, class_):
#       print(y)
# getImages(url,'img','spip_logos')


#! /usr/bin/env python

from bs4 import BeautifulSoup
import requests
import mysql.connector


url='https://wikileaks.org'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

def insertInBdd(values):
    mybdd= mysql.connector.connect(
        host='ms',
        user='root',
        password='pw',
        database='my_db'
    )
    mycursor = mybdd.cursor()
    val = values
    sql = "INSERT INTO articles (title,image,content,date) values (%s,%s,%s,%s)"

    mycursor.execute(sql,val)
    mybdd.commit()
    return str(mycursor) + "nouvelle entree"
# def recupTitre():
#     listeTitle = []
#     listeDate = []
#     listeContent = []
#     listeImage = []

#     li_cards = soup.find_all('li', class_="tile")

#     for li in li_cards:
#         # li_title= li.h2.text
#         # li_img = li.img
#         listeTitle.append(li_title)
#         # lidate = li.find('div',class_='timestamp').text
#         listeDate.append(lidate)
#         print(lidate)
#         listeImage.append(li_img)
#         print(li_img)

#     for liste in listeTitle:
#         print(liste)
#         saveValues= insertInBdd([liste])
#         print(saveValues)

#     for liste2 in listeDate:
#         print(liste2)
#         saveValues2 = insertInBdd([liste2])
#         print(saveValues2)
    
#     for liste3 in listeImage:
#         print(liste3)
#         saveValues3 = insertInBdd([liste3])
#         print(liste3)
# recupTitre()

#print('search the latest articles')

def getArticle():
    url='https://wikileaks.org'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    article_main = soup.find_all('li', class_="tile")

    # article_titles = []
    # article_dates = []
    # article_contents = []
    # article_images = []
    

    for article in article_main:
        article_title = article.h2.text
        # article_img = article.img.attrs['src']
        article_img ="http://wikileaks.com" + article.img.attrs['src']
        article_date = article.find('div',class_='timestamp').text
        article_content = article.p.text

        insertInBdd([article_title,article_img,article_content, article_date])


        # article_titles.append(article_title)
        # # for liste in article_titles:
        # #     insertInBdd([liste])
        # article_dates.append(article_date)
        # # insertInBdd([article_dates])
        # article_contents.append(article_content)
        # # insertInBdd([article_contents])
        # article_images.append(article_img)
        # # insertInBdd([article_images])
        # insertInBdd([article_titles],[article_dates],[article_contents],[article_images])

        # print(article_titles)
        # print(article_images)
        # print(article_contents)
        # print(article_dates)

getArticle()


# CREATE TABLE articles (
#   id TINYINT(6) UNSIGNED NOT NULL AUTO_INCREMENT,
#   title VARCHAR(250) NOT NULL,
#   image VARCHAR(250) NOT NULL,
#   content VARCHAR(250) NOT NULL,
#   date VARCHAR(255) NOT NULL,
#   PRIMARY KEY (id)
# );
# import requests;
# from bs4 import BeautifulSoup





# def getTitle(url, tag, class_):
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     for x in soup.find(tag, class_):
#         print(x)
# url = 'https://wikileaks.org'
# getTitle(url, "ul", class_='grid')


# videos = """your html above, fixed""" #the html you have there is malformed
# soup = bs(videos,'lxml')
# targets = soup.select('div[class*="class4"]')
# for target in targets:
#   i= target.attrs['video_id']
#   link = target.select_one('img').attrs['src']
#   filename = f'images/img{i}.jpg'
#   print(filename,link)

# def getTitle(url, tag):
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     listImg = []
#     for li in soup.find_all(tag):
#         img= li.find('img')
#         if img == img:
#             print('')
#         else:
#             print("nope")
#         listImg.append(img)
#     print(listImg)        


# url='https://wikileaks.org'
# getTitle(url, "li")


# url='https://wikileaks.org'
# page = requests.get(url)
# soup = BeautifulSoup(page.content, 'html.parser')


# # for ultag in soup.find_all('ul', {'class': 'tag-navigation'}):
#     # for litag in ultag.find_all('li'):
#         # print(litag.text) 


# li_cards = soup.find_all('li', class_="tile")
# # print(li_cards)

# for li in li_cards:
#     li_title= li.h2.text
#     li_img = li.img
#     li_date = li.find('div',class_='timestamp')
#     # print(li_img.attrs['src'])
#     print(li_date.text)




