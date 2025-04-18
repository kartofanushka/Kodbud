#Работа API ЦБ РФ
# 
import requests
import telebot
from bs4 import BeautifulSoup
import datetime
token='' # sm m1
bot = telebot.TeleBot(token)

# url="https://www.cbr.ru/scripts/XML_daily.asp?date_req=03/02/1994"
url="https://www.cbr.ru/scripts/XML_daily.asp"
responce=requests.get(url)
xml=BeautifulSoup(responce.content,"xml")# 
# print(xml)

cur=xml.find("CharCode", text="AUD").parent.Value.text
cur1=xml.find("CharCode", text="AUD").parent.attrs['ID']
# ("div", text="inner")
# import lxml.etree
# doc = lxml.etree(responce.content)
# print(doc)
# print (doc.xpath('//element[text()="A"]')[0].text)
# print (doc.xpath('//element[text()="A"]')[0].tagimport lxml.etree)

print(cur,cur1)
    
def cource():
    def getCourse(id):
        # cur=xml.find("Valute",{"ID" : id })
        cur=xml.find("Valute", {"ID":id}).CharCode.text
        cur=cur+xml.find("Valute", {"ID":id}).Nominal.text
        cur=cur+xml.find("Valute", {"ID":id}).Name.text
        cur=cur+xml.find("Valute", {"ID":id}).Value.text
        print(cur)
        return cur
        # return xml.findAll

    # url="https://www.cbr.ru/scripts/XML_daily.asp?date_req=03/02/1994"
    # https://openweathermap.org/guide
    # 380d96f5ffe41c765d9332d950a327f1
    
    today = datetime.datetime.today() 
    today = today.strftime("%d/%m/%Y")
    
    #https://www.cbr.ru/scripts/XML_daily.asp?date_req=03/02/2007
    url = "https://www.cbr.ru/scripts/XML_daily.asp?date_req=" + today
    print(url)
    responce = requests.get(url)
    xml=BeautifulSoup(responce.content,"xml")
    names = xml.find_all('Name')
    codes = xml.find_all('CharCode')
    values = xml.find_all('Value')
    nominals = xml.find_all('Nominal')
    
    id=xml.find("Valute").attrs['ID']
   
    print(id)
    # for name in names:
        # print(name.text, codes[names.index(name)].text )
    # print(xml)
    usd=getCourse("R01090B")
    dollar = (getCourse("R01235") + " Доллар США")
    euro = (getCourse("R01239") + " Евро")
    rmb = (getCourse("R01375") + " Юань")
    dl=72
    #'''
    print('-'.center(dl, '-'))
    print('|' + 'Name'.center(40) + '|' + ' Nominal'.center(9) + '|' + 'Value'.center(9) + '|' + 'CharCode |')
    for i in range(0, len(names)):
        print('-'.center(dl, '-'))
        print(
            f'|{names[i].text.center(40)}|{nominals[i].text.center(9)}|{values[i].text.center(9)}|{codes[i].text.center(9)}|')
    print('-'.center(dl, '-'))
    # '''
    my_file=open("m2_6.txt","a",encoding="UTF-8")
    my_file.write(str(usd)+"\n")
    my_file.close()
    return(dollar + euro + rmb)
cource()

def weather():
    #https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "Moscow"#"Saint Petersburg"
    API_KEY = "380d96f5ffe41c765d9332d950a327f1"
    url = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(url, params={'units': 'metric'})
    data = response.json()
    #data["main"] = {'temp': -0.92, 'feels_like': -0.92, 'temp_min': -1.02, 'temp_max': -0.92, 'pressure': 1005, 'humidity': 80}
    return (str(data["main"]["temp"]) + "--" + str(data["main"]["temp_min"])+CITY)
# ========== bot
@bot.message_handler(commands=["cource"]) #/cource
def course_message(message):
    bot.send_message(message.chat.id, cource())

@bot.message_handler(commands=["weather"]) #/weather
def course_message(message):
    bot.send_message(message.chat.id, weather())
bot.infinity_polling()
# ======= end bot
"""Добавьте еще минимум 2 валюты в программу.

Создайте программу, которая будет конвертировать валюту.

У нас есть главная функция, она принимает 3 аргумента
valute_from и её требуется перевести в валюту valute_to через рубль (код: RUR)
amount, сумма денег, которую мы хотим конвертировать
Для начала мы находим значения valute_to, обратите внимание, что номинал может быль больше 1
Затем условие, если валюта, из которой мы конвертируем это RUR, мы просто парсим курс
Если эта валюта != RUR, то мы узнаём её курс исходя из курса рубля и делим amount на курс валюты, в которую переводим
valute_from = "EUR"

valute_to = "USD"

amount = int(input())

⠀"""

def exchange (valute_from, valute_to, amount):
    # valute_from=input()
    # valute_from = "ZAR"
    # valute_from = "RUR"
    # valute_from = "THB"
    # valute_from = "INR"
    # valute_to = "USD"
    # valute_to = "KRW"
    # valute_to = "RUR"
    # amount = 100#int(input())

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
# exchange(1,2,5)
# exchange(valute_from, valute_to, amount)
# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№
"{""method"":""getblockcount"", ""params"": [], ""id"":1, ""jsonrpc"":2.0}"
# $ curl http://nodes.hashvault.pro:18081/update -d '{"command":"check"}' -H 'Content-Type: application/json'
# responce = requests.post('http://nodes.hashvault.pro:18081/update -d',None,'{"command":"check"}',).content
# print(responce)

# nodes.hashvault.pro:18081
"""
import json


def main():
    url = "http://mainbrain.ca:18081"

    # Example echo method
    payload = {
        "method": "echo",
        "params": ["echome!"],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(url, json=payload).json()

    assert response["result"] == "echome!"
    assert response["jsonrpc"]
    assert response["id"] == 0

# if __name__ == "__main__":
#     main()
# print(main())
url = "https://chad.fiatfaucet.com:443/json_rpc"
payload = {
        "method": "echo",
        "params": ["echome!"],
        "jsonrpc": "2.0",
        "id": 0,
    }
#  
url="http://188.83.252.166:16167/json_rpc"
payload={ "jsonrpc": "2.0", "method": "getblockcount", "params": {} }
# payload = { 'jsonrpc':'2.0', 'id':'0', 'method':'get_block', 'params': { 'height': 2815427, 'verbose':4} } 

responsem = requests.post(url, json=payload, headers={"Content-Type": "application/json"})#.json()
my_file=open("XMR.txt","w",encoding="UTF-8")
my_file.write(str(responsem)+"\n ++++++++++++++++")
my_file.close()
print(responsem)
for rr in responsem['result'].items():
    print(rr)
"""# """ # ====
# payload = { 'jsonrpc':'2.0', 'id':'0', 'method':'get_block', 'params': { 'height': 101 } } 
# rpc_url = 'http://testnet.community.xmr.to:28081/json_rpc' 
# req = requests.post(rpc_url, json=payload) 
# # result = req#.json().get('result') 
# print(req)
# =======
# 07e916a5-945d-42af-9f25-11d31b6a358a
# curl --location --request POST 'https://xmr.getblock.io/mainnet/json_rpc' \ 
# --header 'x-api-key: YOUR-API-KEY' \ --header 'Content-Type: application/json' \ 
# --data-raw { "jsonrpc": "2.0", "method": "get_last_block_header", "params": {}, "id": "getblock.io" }
# url="https://xmr.getblock.io/mainnet/json_rpc"
# payload={ "jsonrpc": "2.0", "method": "get_last_block_header", "params": {}, "id": "getblock.io" }
# response = requests.post(url, json=payload, headers={"x-api-key":"07e916a5-945d-42af-9f25-11d31b6a358a","Content-Type": "application/json"})
# print(response)
