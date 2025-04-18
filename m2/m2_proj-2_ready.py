import telebot
from telebot import types
from telebot.util import quick_markup
from bs4 import BeautifulSoup
import requests
# import random


# token='свой токен'


bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_start(message):
    # print(message)
    welcome='привет, я могу читать субтитры с ютуба. команда /sub'
    stik="CAACAgIAAxkBAAEIIQtkEBjRGd9Z0PuQ5pc74S8XdS3zVgACbAEAAjDUnRE3KemtWRSs6y8E"#
    bot.send_sticker(message.chat.id,stik)
    # print(message.from_user, message.chat.id)
    bot.send_message(message.chat.id, welcome)
    video_id='bAOnDhDDSrg'
    

@bot.message_handler(commands=['sub'])
def y_url(message):
    bot.send_message(message.chat.id, 'давай ссылку на видео.')
    bot.register_next_step_handler(message, get_text_message)
    
@bot.message_handler(commands=['tt'])
def buttonss(message):
    # yesno_markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    # yesno_markup.add( telebot.types.InlineKeyboardButton("Да", callback_data="yes"), 
    #         telebot.types.InlineKeyboardButton("Нет", callback_data="no"), 
    #         )
    tt=['en','ru','de']
    a={}
    b={}
    for i in tt:
        a={}
        a['callback_data']=i
        print (a)
        b[i]=a
        print(b)
        
    print(b)
    markup=quick_markup(b,row_width=2)
    markup1 = quick_markup({
            'Press me':{'callback_data': 'press'},
            'Press me too':{'callback_data': 'press_too'},
            'Back': {'callback_data': 'whatever'}},
        row_width=2)
    bot.send_message(
            text='text',
            reply_markup=markup,
            chat_id=message.chat.id )
    
        
def get_id(mesag_url):
    if "?" in mesag_url:
        yt_v_id=str(mesag_url).split('v=')[-1]
        # print(yt_v_id,1)
        if "&" in yt_v_id:
            yt_v_id=str(yt_v_id).split('&')[0]
            # print(yt_v_id,2)
    else:
        yt_v_id=str(mesag_url).split('/')[-1]
        if "&" in yt_v_id:
            yt_v_id=str(yt_v_id).split('&')[0]
            # print(yt_v_id,3)
    return yt_v_id

def get_sub_list(yt_v_id): # получаем список сабов
    global subturl, lang_list
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details" 
    querystring = {"videoId":yt_v_id} 
    headers = { 	"X-RapidAPI-Key": "m2_proj!!!!!!!!!!!!!!!!!",
           "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com" } 
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    # print(response["status"], 'line97')
    # print(response)
    if response["status"]==True:
        if "subtitles" in response:
            subturl=response["subtitles"]["items"]#[0]["url"]
            print (subturl, len(subturl))
            lang_list=[]
            if len(subturl)>1:
                lang_list=[i["code"] for i in subturl if len(i)>0]
                print(lang_list, type(lang_list))
                
                return lang_list# получить язык
            elif len(subturl)==1:
                lang_list=[subturl[0]["code"]]
                print(type(lang_list))
                return lang_list
            else:
                return "empty"
    else:
        lang_list=""
        return response["reason"]
            
def lang_markup(lang_list):       
    b={}
    for i in lang_list:
        a={}
        a['callback_data']=i
        print (a)
        b[i]=a
    lang_markup=quick_markup(b,row_width=3)
    print(lang_markup)
    return lang_markup


def get_lang_code(message):# return sub url
    for i in subturl:
        print(message)
        if type(message)!=str:
            message=message.text
        if i["code"]==message:
            surl=i["url"]
            langname=i["text"]
            print(surl)
            return surl,langname
            

def get_sub_text(message,chat_id):#get all sub text in list
    surl=get_lang_code(message)[0]
    langname=get_lang_code(message)[1]
    print(surl)
    global sub_text
    response=requests.request("GET", surl).text
    xml = BeautifulSoup(response, "xml")
    sub_text=xml.find_all("text")
    # print(sub_text)

    bot.send_message(text="найдено " + str(len(sub_text))+" строк. Язык - '"+ langname +"'. Будешь читать?",reply_markup=yesno_markup,chat_id=chat_id )

    # return (sub_text,"найдено " + str(len(sub_text))+" строк. Язык - '"+ langname +"'. Будешь читать?", chat_id)
# """
yesno_markup = quick_markup({'Да':{'callback_data': 'yes'},'Нет':{'callback_data': 'no'},'Первые 10 строк':{'callback_data': 'no10'}},row_width=3)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    global lang
    if call.message:
        if call.data == "yes":
            # print(call.data)
            bot.send_message(call.message.chat.id, "ok")
            # bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Coming Soon :D")
            print(call.message.chat.id)
            read_all(call.message.chat.id,"full")
        elif call.data == "no10":
            # print(call.data)
            bot.send_message(call.message.chat.id, "ok")
            # bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Coming Soon :D")
            print(call.message.chat.id)
            read_all(call.message.chat.id,9)
        elif call.data == "no":
            # print(call.data)
            bot.send_message(call.message.chat.id, "ok")
           
        elif call.data in lang_list:
            print(call.data,123)
            get_sub_text(call.data,call.message.chat.id)
        #     bot.send_message(call.message.chat.id, "ok")
        else:
            bot.send_message(call.message.chat.id, call.data)

    print(call.message.chat.id, call.data)

def read_all(message,stroki):
    # print(message)
    i = 0
    while i < len(sub_text):
        sub_text_line=sub_text[i].text
        print(sub_text_line)
        bot.send_message(message, sub_text_line)
        # print(i,stroki)
        if (i == stroki):
            break
        i += 1 
        # return sub_text_line



# vidid="a_GcMGkwNpI"
def youtube(message):
# bot.send_message
    # print('text')
    bot.send_message(message.from_user.id, 'Сейчас посмотрим, ожидай.')
    video_id=get_id(message.text)
    # bot.send_message(message.from_user.id, video_id)
    answer=get_sub_list(get_id(message.text))
    userid=message.from_user.id
    # print(answer,'answer', type(answer))
    
    if len(answer)>1 and type(answer)==list:
        bot.send_message(message.from_user.id, str(answer)+" - вот что нашлось")
        bot.send_message(text="На каком языке загрузить?",reply_markup=lang_markup(answer),chat_id=message.chat.id )
        # bot.register_next_step_handler(message,get_sub_text(message.text,message.from_user.id))
        # bot.register_next_step_handler(message,read_all)
        
    elif len(answer)==1 and type(answer)==list:
        # bot.register_next_step_handler(answer,get_lang_code)
        answer_t=get_sub_text(answer[0],userid)
    elif answer=="empty":
        stik='CAACAgIAAxkBAAEIIUtkEDutF3uEMjhuJvzNgEdZEKNr5wACbwEAAjDUnRGACuH3001FOC8E'
        bot.send_sticker(message.chat.id,stik)
        text = '[К этому видео нет субтитров, придется смотреть](https://www.youtube.com/watch?v='+video_id+')'
        bot.send_message(message.chat.id, text, parse_mode='Markdown')
    else:    
        stik='CAACAgIAAxkBAAEIIUtkEDutF3uEMjhuJvzNgEdZEKNr5wACbwEAAjDUnRGACuH3001FOC8E'
        bot.send_sticker(message.chat.id,stik)
        bot.send_message(message.from_user.id, answer)
        bot.send_message(message.from_user.id, "Что-то сломалось")

 
       
# """
@bot.message_handler(content_types=['text'])
def get_text_message(message): 
    if 'youtube.com' in message.text.lower():
        print (message.text.lower(),1)
        youtube(message)
        # bot.register_next_step_handler(message,youtube)
    elif 'youtu.be' in message.text.lower():       
        print (message.text.lower(),2)
        # bot.register_next_step_handler(message,youtube)
        youtube(message)
    # elif:
    elif message.text=="but":
       yesno_markup = telebot.types.InlineKeyboardMarkup(row_width=2)
       yesno_markup.add( telebot.types.InlineKeyboardButton("Yes", callback_data="yes"), 
            telebot.types.InlineKeyboardButton("No", callback_data="no"), 
            )
       bot.send_message(
            text='Выберите жанр игы',
            reply_markup=yesno_markup,
            chat_id=message.chat.id        )
    else:
        bot.send_message(message.from_user.id, "Ничего не понятно. Надо бы повторить")
        stik="CAACAgIAAxkBAAEIIQlkEBh0nN50xKZAXuNzIwABPY3O4wsAAlsBAAIw1J0RUbJV48N__j8vBA"
        bot.send_sticker(message.chat.id,stik)


bot.infinity_polling()
# """ 
