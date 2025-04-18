

import telebot
from bs4 import BeautifulSoup
import requests
import random

token='' # m1_12_token

# # read token from file
# read=open('key-file.txt,'r'')
# line=read.readline()
# read.close

bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_message(message):
    print(message.from_user)
    welcome='Hello'
    bot.send_message(message.chat.id, welcome)

@bot.message_handler(commands=['poem'])
def send_message(message):
    poem_t='Take a book and read by yourself'
    bot.send_message(message.chat.id, poem_t)
   
@bot.message_handler(commands=['pic'])
def send_message(message):
    pict=open('12_bot_py_1.jpg','rb')
    bot.send_photo(message.chat.id, pict)
 
# @bot.message_handler(commands=["audio"])
# def send_message(message):
#     aud = open("happy.mp3", "rb")
#     bot.send_audio(message.chat.id, aud)
        
@bot.message_handler(commands=['fact'])
def send_message(message):
    responce = requests.get("https://i-fakt.ru/")
    responce = responce.content
    html = BeautifulSoup(responce, "html.parser")
    facts=html.find_all(class_='p-2 clearfix')
    fact=random.choice(facts)
    fact_link = fact.a['href']
    bot.send_message(message.chat.id, fact_link)

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    b_1=telebot.types.KeyboardButton('Button1')
    markup.add(b_1)
    bot.send_message(message.chat.id, 'ksdjhkjdnv', reply_markup=markup)


@bot.message_handler(commands=['lp'])      
def logpass(message):            
    read=open('logins.txt','r', encoding="utf-8")
    lines=read.read().splitlines()
    read.close()
    ln=''
    for i in lines:
        # print((i))
        if lines.index(i) %2==0:
            l= 'log: '+ i
        else :
            l='pass: '+ i +'\n'
        ln = ln + l
    bot.send_message(message.chat.id, ln)
"""
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text=='HIHI' or message.text=='Hi' or  message.text=='hi':
        # bot.send_message
        bot.send_message(message.from_user.id, 'hi how r u?')
        bot.reply_to(message, "HIHI")
"""
bot.polling()
# decorator ?
# def function_upgrade(fnktn):
#     print('text1')
#     fnktn()
#     print('text2')
# def funktn1():
#     print('No Text')
    
# new_text=function_upgrade(funktn1)
# ======