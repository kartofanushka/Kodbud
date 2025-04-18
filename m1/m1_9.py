# # Hypertext Markup Language HTML — это язык разметки для создания веб-страниц или веб-приложений.

# # Теги — команды в HTML. Это своеобразные кирпичики, из которых строится страница

# # BeautifulSoup – это библиотека, позволяющая сделать разбор (парсинг) HTML кода текст, заголовки, ссылки.
# pip install beautifulsoup4
# pip install requests
import bs4 as bs
# from bs4 import *
import requests
import urllib.request

url ='http://www.columbia.edu/~fdc/sample.html'
# url= 'https://www.alleng.me/edu/comp.htm'
source=urllib.request.urlopen(url).read()
soup=bs.BeautifulSoup(source,'html.parser')
# file=open('9test.txt', "a",encoding="utf-8")
# lt=str(soup)
# file.write(lt)
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.h3)
print(soup.find_all('h3'))
print(soup.title)
# === Занятие 9 ====
# статья https://us06st1.zoom.us/web_client/bai5dum/html/externalLinkPage.html?ref=https://infosecwriteups.com/make-a-self-replicating-virus-in-python-bb29404e3f6b 
# про вирус
# import pip._vendor.requests 
# import requests
# from bs4 import BeautifulSoup
# import random
# ==============
# responce=requests.get('https://i-fakt.ru/')
# responce=responce.content

# html=BeautifulSoup(responce, 'html.parser') #lxml -xml, html.parser lxml
# print(html.prettify()) 
# print(html.title)
# art=html.find_all('article')
# # print(art[0].text) # .text только для одного эл-та
# divs = html.find_all(class_="row")
# print(divs)
# divs = html.find_all("div", class_="row")
# print(divs)

# first_art=html.find("article")
# print(first_art.text)
# link=first_art.find("a").attrs["href"] # находин первый тег и из него атриб href
# print(first_art.text)
# ===============

# def get_random_fest():
#     responce=requests.get('https://kudago.com/spb/kino/')
#     # responce=requests.get('https://kudago.com/spb/festival/')
    
#     responce=responce.content
    
#     html= BeautifulSoup(responce, "html.parser")
#     a=html.find_all('article', class_="post")
#     rand_a=random.choice(a)
#     print(rand_a.text.replace('\n',''))
#     print(rand_a.a.attrs['href'])
# get_random_fest()

# for index, tr in ennumerate(trs[0])

# import csv # operate with csv files

# 1 use .find_all
