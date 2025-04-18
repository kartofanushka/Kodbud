import telebot
import requests
from bs4 import BeautifulSoup
import random

# read = open("token.txt", "r")

# line = read.readline()
# read.close()

# token = line
token='' #m1_12_mih_token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def send_message(message):
    print(message.from_user)
    welcome = "Привет я бот, я у мею шутить"
    bot.send_message(message.chat.id, welcome)

@bot.message_handler(commands=["poem"])
def send_message(message):
    text_poem = "Скажи-ка дядя ведь не даром..."
    bot.send_message(message.chat.id, text_poem)


@bot.message_handler(commands=["fact"])
def send_message(message):
    responce = requests.get("https://i-fakt.ru/")
    responce =responce.content
    html = BeautifulSoup(responce, "html.parser")
    facts = html.find_all(class_ = "p-2 clearfix")
    fact = random.choice(facts)
    fact_link = fact.a["href"]
    bot.send_message(message.chat.id, fact_link)

@bot.message_handler(commands=["cat"])
def send_message(message):
    # cat_num = random.randint(1, 10)
    # cat_img = open("imgz/" + str(cat_num)+ ".jpg", "rb")
    cat_img = open("12_bot_py_1.jpg", "rb")
    bot.send_photo(message.chat.id, cat_img)

@bot.message_handler(commands=["audio"])
def send_message(message):
    aud = open("happy.mp3", "rb")
    bot.send_audio(message.chat.id, aud)



@bot.message_handler(commands=["button"])
def button_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = telebot.types.KeyboardButton("Кнопка")
    markup.add(but1)
    bot.send_message(message.chat.id, "Блаблабла", reply_markup=markup)

# CONTENT_TYPES = ["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
#                  "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
#                  "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
#                  "migrate_from_chat_id", "pinned_message"]

@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, "Привет как дела")
        bot.reply_to(message, "Привет привет")


bot.polling()


# def tachka_na_prokachku(tachka):
    
#     def prokachanaya_tachka():
#         print("добавили ТВ")
#         tachka()
#         print("Добавили еще два ТВ")
    
#     return prokachanaya_tachka

# def func():
#     print("Я обычная некрасивая тачка")

# cool_func = tachka_na_prokachku(func)

# # cool_func()


# @tachka_na_prokachku
# def my_func():
#     print("Я хочу прокачаться")


# my_func()