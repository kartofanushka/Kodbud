import requests
import telebot
from bs4 import BeautifulSoup
import datetime

def cource():
    def getCourse(id):
        cur=xml.find("Valute", {"ID":id}).CharCode.text
        cur=cur+' '+xml.find("Valute", {"ID":id}).Nominal.text
        cur=cur+' '+xml.find("Valute", {"ID":id}).Name.text
        cur=cur+' '+xml.find("Valute", {"ID":id}).Value.text
        # print(cur)
        return cur
            
    today = datetime.datetime.today() 
    today = today.strftime("%d/%m/%Y")
    
    url = "https://www.cbr.ru/scripts/XML_daily.asp?date_req=" + today
    # print(url)
    responce = requests.get(url)
    xml=BeautifulSoup(responce.content,"xml")
    names = xml.find_all('Name')
    codes = xml.find_all('CharCode')
    values = xml.find_all('Value')
    nominals = xml.find_all('Nominal')
     
    print(getCourse(id))
    dl=72
    print('-'.center(dl, '-'))
    print('|' + 'Name'.center(40) + '|' + ' Nominal'.center(9) + '|' + 'Value'.center(9) + '|' + 'CharCode |')
    for i in range(0, len(names)):
        print('-'.center(dl, '-'))
        print(
            f'|{names[i].text.center(40)}|{nominals[i].text.center(9)}|{values[i].text.center(9)}|{codes[i].text.center(9)}|')
    print('-'.center(dl, '-'))

cource()

def exchange (valute_from, valute_to, amount):
    today = datetime.datetime.today() 
    today = today.strftime("%d/%m/%Y")
    
    url = "https://www.cbr.ru/scripts/XML_daily.asp?date_req=" + today
    # print(url)
    responce = requests.get(url)
    xml=BeautifulSoup(responce.content,"xml")
    codes = xml.find_all('CharCode')
    c_l=[]
    for c in codes:
        c_l.append(c.text)
    try:
        amount=float(amount)
    except ValueError:
        print("Вы не ввели сумму")  
        
    if (valute_to or valute_from) in c_l:
        if valute_to == "RUR":
            print(valute_to, valute_from)
            cur_fr=float(xml.find("CharCode", text=valute_from).parent.Value.text.replace(',','.'))
            cur_fr_n=float(xml.find("CharCode", text=valute_from).parent.Nominal.text.replace(',','.'))
            amount2=round(float(amount*(cur_fr/cur_fr_n)),2)
            
            cur=xml.find("CharCode", text=valute_from).parent.Value.text
            print(amount2,valute_to,', комиссия за обмен составила 5%: ',round(amount2/20,2) ,valute_to)
        elif valute_from == "RUR":
            print(valute_to, valute_from)
            cur_to=float(xml.find("CharCode", text=valute_to).parent.Value.text.replace(',','.'))
            cur_to_n=float(xml.find("CharCode", text=valute_to).parent.Nominal.text.replace(',','.'))
            amount2=round(float(amount/(cur_to/cur_to_n)),2)
            
            print(amount2,valute_to,', комиссия за обмен составила 5%: ',round(amount2/20,2) ,valute_to)
        else:
            print(valute_to, valute_from)
            
            cur_to=float(xml.find("CharCode", text=valute_to).parent.Value.text.replace(',','.'))
            cur_to_n=float(xml.find("CharCode", text=valute_to).parent.Nominal.text.replace(',','.'))
            
            cur_fr=float(xml.find("CharCode", text=valute_from).parent.Value.text.replace(',','.'))
            cur_fr_n=float(xml.find("CharCode", text=valute_from).parent.Nominal.text.replace(',','.'))
            
            amount2=round(float((amount/(cur_to/cur_to_n))*(cur_fr/cur_fr_n)),2)
            print(amount2,valute_to,', комиссия за обмен составила 5%: ',round(amount2/20,2) ,valute_to)
    else:
        print("Такую валюту не меняем")  
        print("Выбирайте что-то из этого:")
        print(c_l)

               
# valute_from=input("Что меняем? ").upper()
# amount=input("Сколько? ")
# valute_to=input("Что хотим получить? ").upper()
# exchange(valute_from, valute_to, amount)