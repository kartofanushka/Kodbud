import telebot
import requests
from bs4 import BeautifulSoup
import datetime



read = open("token.txt", "r")
token = read.readline()
print(token)
read.close()


bot = telebot.TeleBot(token)

def course():
    def getCourse(id):
        print(xml.find("valute", {"id" : id}).value.text)
        return xml.find("valute", {"id" : id}).value.text

    today = datetime.datetime.today() 
    today = today.strftime("%d/%m/%Y")
    
    #https://www.cbr.ru/scripts/XML_daily.asp?date_req=03/02/2007
    url = "https://www.cbr.ru/scripts/XML_daily.asp?date_req=" + today

    responce = requests.get(url)


    xml = BeautifulSoup(responce.content, "html.parser") #


    dollar = (getCourse("R01235") + " Доллар США ")
    euro = (getCourse("R01239") + " Евро ")
    uan = (getCourse("R01375") + " Юань")

    return(dollar + euro + uan)

def weather():
    #https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "Saint Petersburg"
    API_KEY = "380d96f5ffe41c765d9332d950a327f1"
    url = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(url, params={'units': 'metric'})
    data = response.json()
    #data["main"] = {'temp': -0.92, 'feels_like': -0.92, 'temp_min': -1.02, 'temp_max': -0.92, 'pressure': 1005, 'humidity': 80}
    return (str(data["main"]["temp"]) + "--" + str(data["main"]["temp_min"]))

@bot.message_handler(commands=["course"]) #/course
def course_message(message):
    bot.send_message(message.chat.id, course())

@bot.message_handler(commands=["weather"]) #/weather
def course_message(message):
    bot.send_message(message.chat.id, weather())

bot.infinity_polling()