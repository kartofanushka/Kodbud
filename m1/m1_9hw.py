# Колумбия

# Что нужно сделать:

# Дан несложный пример HTML-страницы: http://www.columbia.edu/~fdc/sample.html

# Изучите код этой страницы и реализуйте программу, которая получает список всех подзаголовков сайта (они заключены в теги h3).

# Ожидаемый результат:

# ['CONTENTS', '1. Creating a Web Page', '2. HTML Syntax', '3. Special Characters', '4. Converting Plain Text to HTML', '5. Effects', '6. Lists', '7. Links', '8. Tables', '9. Viewing Your Web Page', '10. Installing Your Web Page on the Internet', '11. Where to go from here', '12. Postscript: Cell Phones']

# Сделайте так, чтобы программа работала для любого сайта, где есть такие теги.

"""
import bs4 as bs
# # from bs4 import *
import requests
# import urllib.request

# url= 'http://ya.ru' 
url ='http://www.columbia.edu/~fdc/sample.html'
source=requests.get(url)
source =source.content
soup=bs.BeautifulSoup(source,'html.parser')
# file=open('9test.txt', "a",encoding="utf-8")
lt=str(soup)
h3=soup.find_all('h3')
lst=[]
# print(h3)
if len(h3)>0: 
    for i in h3:
        # print(i)
# file.write(lt)

      #  print(soup.h3)
        # print(i.text)
        # print(soup.h3.string)
        lst.append(i.text)
print(lst)      
        

# print(soup.title.parent.name)
# print(soup.p)
# print(soup.find_all('a'))
# print(soup.title)
"""

# Электроника

# Что нужно сделать:

# Дана следующая ссылка: https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets, спарсите основную информацию об устройствах с этого сайта.

# Пример вывода:

# [{"id":495,"title":"Lenovo IdeaTab","description":"7\" screen, Android","price":"69.99"}, …, {"id":515,"title":"Apple iPad Air","description":"Wi-Fi, 64GB, Silver","price":"603.99"}]

"""
import bs4 as bs
import requests
url ='https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets'
source=requests.get(url)
source =source.content
soup=bs.BeautifulSoup(source,'html.parser')
lt=str(soup)
h3=soup.find_all('div')
divs = soup.find_all("div", class_="ecomerce-items-ajax")
lst=[]
if len(divs)>0: 
    for i in divs:
        print("==================")
        print(i.attrs["data-items"] )
        print("==================")
 """
# file.write(lt)

      #  print(soup.h3)
        # print(i.text)
        # print(soup.h3.string)
        # lst.append(i.text)
# print(divs)      


# Steam

# Что нужно сделать:

# Напишите программу, которая будет советовать в какую игру поиграть, в зависимости от выбранного жанра. 
# За основу можно взять сайт steam https://store.steampowered.com/?l=russian
# """
import bs4 as bs
import random
# # from bs4 import *
import requests
# import urllib.request
# divs = soup.find_all("div", class_="row")
# div class="ecomerce-items-ajax"
url ='https://store.steampowered.com/'
source=requests.get(url)
source =source.content
soup=bs.BeautifulSoup(source,'html.parser')
# file=open('9test.txt', "a",encoding="utf-8")
lt=str(soup)
url_dict={}

divs = soup.find_all("div", class_="popup_genre_expand_header")
for i in divs:
    if i.text!='':
        gnr = i.find_all("a", class_="popup_menu_item")
        for ii in gnr:
            gnr_n=ii.text.strip()
            gnr_n=gnr_n.replace('-',' ')
            gnr_url=ii.attrs['href']
            url_dict[gnr_n] = gnr_url
            # print(gnr_n)
            # print(gnr_url)
print(url_dict)
"""
divs = soup.find_all("div", class_="gutter_header")
for i in divs:
    if i.text=='Browse by genre':
        gnr=i.parent
        gnr = gnr.find_all("a", class_="gutter_item")
        for ii in gnr:
            gnr_n=ii.text.strip()
            gnr_url=ii.attrs['href']
            url_dict[gnr_n] = gnr_url
            # print(gnr_n)
            # print(gnr_url)
# print(url_dict)"""
print(url_dict.keys())
urll='https://store.steampowered.com/tags/en/Racing/?snr=1_4_4__125'
url=url_dict.get(input("Введите название жанра из указаных__"),urll)
# url='https://store.steampowered.com/tags/en/Racing/?snr=1_4_4__125'
source=requests.get(url)
source =source.content
soup=bs.BeautifulSoup(source,'html.parser')
div=[]
div=soup.find('div', id="application_config").attrs['data-ch_main_list_data']
import ast
dvlst = ast.literal_eval(div)

# print(type(dvlst))
dd='top_sellers'
for tag in dvlst:
    
    if tag.get('id')==dd:
        # print(tag.get('apps'))
        games=tag.get('apps')

g=str(random.choice(games).get('id'))
game_url='https://store.steampowered.com/app/'+g
source=requests.get(game_url)
source =source.content
soup=bs.BeautifulSoup(source,'html.parser')

print('Предлагаю поиграть в:')
print(soup.title.string, game_url)
print('==============================================================')
    # print(tag.contents)
# <div id="application_config" style="display: none;"  data-config
# lst=[]
# div=div.attrs['data-search_preferences']
# print(div)
# if len(divs)>0: 
#     for i in divs:
        # i.replace('\n','')
        # i.replace('\t','')
        # print("==================")
        # # print(i.attrs["data-items"] )
        # print("==================")
        
# <div class="gutter_header pad">Browse by genre</div>

# <a class="gutter_item" href="https://store.steampowered.com/genre/Free%20to%20Play/?snr=1_4_4__125">
# 							Free to Play					</a>
# 																																																																																																																																																																																																								<a class="gutter_item" href="https://store.steampowered.com/genre/Early%20Access/?snr=1_4_4__125">
# 							Early Access						</a>
# 																																																																																																																						<a class="gutter_item" href="https://store.steampowered.com/tags/en/Action/?snr=1_4_4__125">
# 							Action						</a>
# """

"""
from bs4 import BeautifulSoup

contents = '<q tag1 tag2>Quote1</q>dome other text<q tag1 tag3>quote2</q>'

soup = BeautifulSoup(contents)

for tag in soup.findAll('q'):
    print(tag.attrs)
    print(tag.contents)
print('Finished')

"""