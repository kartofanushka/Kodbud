

import telebot
# from telebot import types
from bs4 import BeautifulSoup
import requests
import random


token='' #sm m1

# # read token from file
# read=open('key.txt,'r'')
# line=read.readline()
# read.close

bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_start(message):
    print(message)
    welcome='Hello'
    print(message.from_user, message.chat.id)
    bot.send_message(message.chat.id, welcome)

@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_t='Take a book and read by yourself'
    bot.send_message(message.chat.id, poem_t)
   
@bot.message_handler(commands=['pic'])
def send_pic(message):
    pict=open('12_bot_py_1.jpg','rb')
    bot.send_photo(message.chat.id, pict)
    pict.close()
 
# @bot.message_handler(commands=["audio"])
# def send_music(message):
#     aud = open("happy.mp3", "rb")
#     bot.send_audio(message.chat.id, aud)
#     aud.close()
        
@bot.message_handler(commands=['fact'])
def send_fact(message):
    responce = requests.get("https://i-fakt.ru/").content
    # responce = responce.content
    html = BeautifulSoup(responce, "html.parser")
    fact=random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link = fact.a.attrs['href']
    bot.send_message(message.chat.id, fact_link)

@bot.message_handler(commands=['gmgm'])
def send_game(message):
    responce = requests.get("https://poki.com/")
    # print(responce)
    responce = responce.content
    html = BeautifulSoup(responce, "html.parser")
    fact=(html.find_all("ul"))
    fact=random.choice(fact[0].find_all("li"))
    # print(fact)
    fact_link = fact.a.attrs['href']
    bot.send_message(message.chat.id, 'https://poki.com/'+fact_link)
#===================

@bot.message_handler(commands=['gmgm1'])
def send_game1(message):
    responce = requests.get("https://poki.com/")
    # print(responce)
    responce = responce.content
    html = BeautifulSoup(responce, "html.parser")
    fact=(html.find_all("ul"))
    fact=random.choice(fact[0].find_all("li"))
    # print(fact)
    fact_link = fact.a.attrs['href']
    bot.send_message(message.chat.id, 'https://poki.com/'+fact_link)
games={"Sandbox":["Minecraft",    "Grand Theft Auto",    "The Sims"],
    "Real-time strategy (RTS)":["Warcraft",    "Age of Empires",    "Command & Conquer"],
    "Shooters (FPS and TPS)":["Halo (FPS)",    "Gears of War (TPS)",    "DOOM (FPS)"],
    "Multiplayer online battle arena (MOBA)":["Dota 2",    "League of Legends",    "Smite"],
    "Role-playing (RPG, ARPG, and More)":["Skyrim",    "The Witcher 3 (ARPG)",    "Fallout 4"],
    "Simulation and sports":["Forza Motorsport",    "Madden NFL",    "NBA2K"],
    "Puzzlers and party games":["Jackbox Party Pack (party game)",    "The Talos Principle (puzzler)",    "Portal 2 (puzzler)"],
    "Action-adventure":["Star Wars Jedi: Fallen Order",    "Sekiro: Shadows Die Twice",    "Assassin’s Creed"]}
@bot.message_handler(commands=['game'])
def start(message):
    # Select language
    keys=games.keys()
    games_markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    games_markup.add( telebot.types.InlineKeyboardButton("Sandbox", callback_data="Sandbox"), 
        telebot.types.InlineKeyboardButton("Real-time strategy (RTS)", callback_data="Real-time strategy (RTS)"), 
        telebot.types.InlineKeyboardButton("Shooters (FPS and TPS)", callback_data="Shooters (FPS and TPS)"), 
        telebot.types.InlineKeyboardButton("Multiplayer online battle arena (MOBA)", callback_data="Multiplayer online battle arena (MOBA)"),
        telebot.types.InlineKeyboardButton("Role-playing (RPG, ARPG, and More)", callback_data="Role-playing (RPG, ARPG, and More)"), 
        telebot.types.InlineKeyboardButton("Simulation and sports", callback_data="Simulation and sports"), 
        telebot.types.InlineKeyboardButton("Puzzlers and party games", callback_data="Puzzlers and party games"),
        telebot.types.InlineKeyboardButton("Action-adventure", callback_data="Action-adventure"))
    bot.send_message(
        text='Выберите жанр игы',
        reply_markup=games_markup,
        chat_id=message.chat.id,
    )
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    global lang
    if call.message:
        if call.data == "none":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Coming Soon :D")
        elif call.data in games.keys():
            print(games[call.data])
            bot.send_message(call.message.chat.id, "Предлагаю игру: "+random.choice(games[call.data]))
        else:
            bot.send_message(call.message.chat.id, call.data)

    print(call.message.chat.id, call.data)

#===================

@bot.message_handler(commands=['reply'])
def send_repl(message):
    bot.reply_to(message, 'HI')
    
@bot.message_handler(commands=['button'])
def button_message(message):
    markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    b_1=telebot.types.KeyboardButton('Button1')
    b_2=telebot.types.KeyboardButton('Приве')
    b_3=telebot.types.KeyboardButton('fact')
    b_4=telebot.types.KeyboardButton('pic')
    # b_5=telebot.types.KeyboardButton('Button1')
    markup.add(b_1, b_2, b_3,b_4)
    send_fact(message)
    bot.send_message(message.chat.id, 'select what you want', reply_markup=markup)
"""
@bot.message_handler(commands=['but'])
def button_message_inln(message):
    
    markup=telebot.types.InlineKeyboardMarkup(row_width=2)
    b_1=telebot.types.InlineKeyboardButton('url',callback_data='/pic')
    b_2=telebot.types.InlineKeyboardButton('url1',switch_inline_query='/reply')
    b_3=telebot.types.InlineKeyboardButton('url2',callback_data='hi')
    print(message.chat.id)
    # b_5=telebot.types.KeyboardButton('Button1')
    markup.add(b_1, b_2, b_3)
    # send_fact(message)
    bot.send_message(message.chat.id, 'select what you want1', reply_markup=markup)

@bot.message_handler(commands=['game'])
def start(message):
    # Select language
    langs_markup = telebot.types.InlineKeyboardMarkup([[
        telebot.types.InlineKeyboardButton('English {}'.format(b'\xF0\x9F\x87\xAC\xF0\x9F\x87\xA7'.decode()), callback_data='en'),
        telebot.types.InlineKeyboardButton('Русский {}'.format(b'\xF0\x9F\x87\xB7\xF0\x9F\x87\xBA'.decode()), callback_data='ru'),
        telebot.types.InlineKeyboardButton('Português {}'.format(b'\xF0\x9F\x87\xA7\xF0\x9F\x87\xB7'.decode()), callback_data='pt')
    ]])
    
    bot.send_message(
        text='Choose your language / Выберите язык / Escolha seu idioma',
        reply_markup=langs_markup,
        chat_id=message.chat.id,
    )
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    global lang
    if call.message:
        if call.data == "none":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Coming Soon :D")
        elif call.data=='en' or call.data=='pt' or call.data=='ru':
            send_frequency_question(bot, call.message.chat.id, call.data)
        elif call.data == "weekly":
            print('weekly')
            bot.send_message(call.message.chat.id, call.data)
        else:
            bot.send_message(call.message.chat.id, call.data)
    # lang=call.data
    print(call.message.chat.id, call.data)
    

def send_frequency_question(bot, chat_id, lang):
    frequency_markup = telebot.types.InlineKeyboardMarkup([[
        telebot.types.InlineKeyboardButton(FREQUENCY_NONE[lang], callback_data='none'),
        telebot.types.InlineKeyboardButton(FREQUENCY_DAILY[lang], callback_data='daily'),
        telebot.types.InlineKeyboardButton(FREQUENCY_WEEKLY[lang], callback_data='weekly')]])
    bot.send_message(text=FREQUENCY_QUESTION[lang], reply_markup=frequency_markup, chat_id=chat_id)
    # '''

FREQUENCY_QUESTION = {
    'ru': 'Частота уведомлений:',
    'en': 'Reminder frequency:',
    'pt': 'Frequência do Lembrete:'
}

FREQUENCY_NONE = {
    'ru': 'Отключить',
    'en': 'Disable',
    'pt': 'Desabilitar'
}

FREQUENCY_DAILY = {
    'ru': 'Ежедневно',
    'en': 'Daily',
    'pt': 'Diariamente'
}

FREQUENCY_WEEKLY = {
    'ru': 'Еженедельно',
    'en': 'Weekly',
    'pt': 'Semanalmente'
}

"""

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
    
#content_types=['audio', 'photo', 'voice', 'video', 'document','text', 'location', 'contact', 'sticker'])
@bot.message_handler(content_types=['pinned_message'])
def send_stik_tnx(message):
 bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEHbORj0Qkh8PpXk4_PqhpKA8iZdNtp9gACbAADc_0OMHHI5gXnnXgwLQQ")

@bot.message_handler(content_types=['left_chat_member'])
def left_ppl(message):
 bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEHbOZj0QmN2Ebemu6BuIp_5zsjjW2btgACggADc_0OMAYZ8ZdJ3uEtLQQ")

@bot.message_handler(content_types=['new_chat_members'])
def left_ppl(message):
 bot.reply_to(message.chat.id,"hi hi")
 
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text=='HIHI' or message.text=='Hi' or  message.text=='hi':
        # bot.send_message
        bot.send_message(message.from_user.id, 'hi how r u?')
        bot.reply_to(message, "HIHI")
        stik="CAACAgIAAxkBAAEHbL9j0QKugJ6DSI6SsvPeUr2A-EzVOAACigADc_0OMGc-JbFWHhMgLQQ"
        bot.send_sticker(message.chat.id,stik)
    elif message.text =='Button1':
        bot.send_message(message.chat.id,"CLICK")
        markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        b_5=telebot.types.KeyboardButton('Button2')
        markup.add(b_5)
        # send_fact(message)
        bot.send_message(message.chat.id, 'select what you want', reply_markup=markup)
    elif message.text=="Button2":
        bot.send_message(message.chat.id,"Thanx")
    elif message.text.lower() =='pic':
        send_pic(message)
    elif 'приве' in message.text.lower():
        send_repl(message)
    elif 'игр' or 'game1' in message.text.lower():
        send_game(message)
    elif 'fact' in message.text.lower():
        send_fact(message)

@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    send_repl(message)
    stik="CAACAgIAAxkBAAEHbH5j0Osa29T6Pvj49QnQFERSAAGkk7IAAlUAA3P9DjBbVmJV8HILqC0E"
    bot.send_sticker(message.chat.id,stik)
    
# Дополните функционал бота. Добавьте совет во что поиграть на компьютере.
games={"Sandbox":["Minecraft",
    "Grand Theft Auto",
    "The Sims"],
    "Real-time strategy (RTS)":["Warcraft",
    "Age of Empires",
    "Command & Conquer"],
    "Shooters (FPS and TPS)":["Halo (FPS)",
    "Gears of War (TPS)",
    "DOOM (FPS)"],
    "Multiplayer online battle arena (MOBA)":["Dota 2",
    "League of Legends",
    "Smite"],
    "Role-playing (RPG, ARPG, and More)":["Skyrim",
    "The Witcher 3 (ARPG)",
    "Fallout 4"],
    "Simulation and sports":["Forza Motorsport",
    "Madden NFL",
    "NBA2K"],
    "Puzzlers and party games":["Jackbox Party Pack (party game)",
    "The Talos Principle (puzzler)",
    "Portal 2 (puzzler)"],
    "Action-adventure":["Star Wars Jedi: Fallen Order",
    "Sekiro: Shadows Die Twice",
    "Assassin’s Creed"]}
# Добавьте вопрос от чат-бота, который уточнит жанр игры, в которую хочет поиграть пользователь. На основании ответа предложит игру.


bot.infinity_polling()
# decorator ?
# def function_upgrade(fnktn):
#     print('text1')
#     fnktn()
#     print('text2')
# def funktn1():
#     print('No Text')
    
# new_text=function_upgrade(funktn1)
# ======