
"""
pas=''
pas=input('Password?  ')
while pas!='12345':
    pas=input('input password: ')
print('Ok')
"""

# while True:
#     if input()=='123':
#         print('Ok')
#         break

# in if and while we can add 'pass' to avoid 'error'
# break -прерывание цикла


# i=1
# while i<=10:
#     print(i**2)
#     i += 1

# print(i)

# i=1
# while i<17000:
#     i+=1
#     print(i)
# else:
#     print('ok')

#=================     
# salary= 300
# goal = 5000

# account=0
# month=0
# while account< goal:
#     account += salary
#     month +=1
# print( account, 'for', month,' month')
#==================
"""
import requests
from bs4 import BeautifulSoup
import random


def get_random_fest():
    responce = requests.get("https://kudago.com/spb/festival/")
    responce = responce.content

    html = BeautifulSoup(responce, "html.parser")  # lxml
    a = html.find_all("article", class_="post")
    rand_a = random.choice(a)
    print(rand_a.text.replace("\n", ""))
    print(rand_a.a.attrs["href"])

def get_random_kino():
    responce = requests.get("https://kudago.com/spb/kino/")
    responce = responce.content

    html = BeautifulSoup(responce, "html.parser")  # lxml
    a = html.find_all("article", class_="post")
    rand_a = random.choice(a)
    print(rand_a.text.replace("\n", ""))
    print(rand_a.a.attrs["href"])
    
user_wish=''
while user_wish!='stop':
    user_wish=input('what r u going to do?  ')
    if user_wish=='fest':
        get_random_fest()
    elif user_wish=='kino':
        get_random_kino()
    else:
        print('Stay home?')

# ======================================
Ориентация страниц:

P or Portrait
L or Landscape
Размеры страниц:

pt : точки
mm : миллиметры
cm : сантиметры
in : дюймы
Форматы страниц:

A3
A4
A5
Letter
Legal
Библиотека fpdf:

https://pyfpdf.readthedocs.io/en/latest/reference/FPDF/index.html

Размеры:

w : ширина
h : высота
Если задать ширину равной 0, то ширина будет рассчитываться автоматически от размера листа (с отступами).

Текст, который хотим написать:

txt : текст, который хотим написать
Рамка - border

0 : нет рамки
1 : есть рамка
Выравнивание - align

L : левое
C : центральное
R : правое
Заливка - fill

True : есть заливка
False : нет заливки
Координаты:

X
y
"""
from fpdf import FPDF
# pdf = FPDF (
#     orientation='P',  # P - portrait, L- landcape
#     unit='mm', # pt, mm, cm, in
#     format='A5', # A3, A4, Legal , (10x10)
    
#     # w,h ширина, высота
#     # x, y координаты
#     # txt - text input
# )
# или так тоже можно
pdf = FPDF('P', 'mm','A5')
pdf.add_page() # page 1
pdf.set_font('Arial','B',16) # C:\Windows\Fonts\impact.ttf', 
pdf.set_author('Ang')
pdf.set_title('itle title')
pdf.set_text_color(100,15,150)
pdf.cell(40,10,'Hello World !',1)
pdf.ln(15)
pdf.cell(60,10,'Powered by FPDF.',0,1,'C')
pdf.add_page() # page 2
pdf.cell(50,10, txt='Hello', align='r', border=1, fill=True, link='http://ya.ru')
pdf.ln(15)
pdf.multi_cell(100,20, txt='kjdfflksdjfksdfk', border=1, align='l')
pdf.output('10.pdf')

