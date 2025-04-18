from pygame import mixer
from gtts import gTTS
import os
import speech_recognition as sr
import random

""" файл со списком приложен"""
my_file=open("m2_7/hello.txt","r")
# my_file=open("m2_7/films.txt","r")
my_str=my_file.readlines()
my_file.close()
# print(random.choice(my_str))
def answer(my_str):
    tts=gTTS(text=my_str, lang="ru")
    tts.save("m2_7/answ.mp3")
    mixer.init() 
    mixer.music.load("m2_7/answ.mp3")
    mixer.music.set_volume(0.25) #от 0 до 1
    mixer.music.play()
    while mixer.music.get_busy():
        continue
    mixer.quit()
    
    os.remove("m2_7/answ.mp3")

def commandtalk():
    r=sr.Recognizer()
    while True:
        with sr.Microphone(device_index=0) as source: # у нас нет микрофона
            print("Говорите")
            stream=r.listen(source=source,phrase_time_limit=10)
        try:
            print("Думаю ...")
            speech=r.recognize_google(stream, language="ru-RU").lower()
            # print("answer "+ speech)
            if "обнаружил" in speech:
                # answer("Предлагаю посмотреть "+ random.choice(my_str))
                answer(random.choice(my_str))
        except:
            break
            # pass
            
commandtalk()
"""
def takecommand():

    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="ru-RU").lower()
        print(f"User Said: {query}\n")

    except Exception as e:
        # print(e)

        # speak("Please Say that Again")
        print("Say that Again...")
        return "None"
    return query
# takecommand()
"""
# =====HW======
# Создайте список с приветствиями помощника. Он должен случайным образом выбирать
# приветствие и отправлять его вам на фразу «Привет».

# Создайте список фильмов и добавьте функцию помощника 
# советовать случайный фильм пользователю на фразу «Фильм».
#=====/HW=====






# """



"""
import time
window=Tk() # open window
window.geometry('900x300') #window size
window.resizable(height=False, width=False)
window.config(bg='black')
text=Label(text='Ваш комп заражен ...', fg='green', bg='black', font=('Courier', 16), justify='center')
text.place(x=100, y=100, width=700, height=100)

count= Label(text='5', fg='green', bg='black', font=('Courier', 36))

# count.place(x=100, y=200,width=100,height=100)
def count_start():
    if int(count['text'])>0:
        count['text']= int(count['text']) -1
        count.place(x=70, y=180,width=700,height=70)
        window.after(1000, count_start) # (милисек, что делать)
    else:
        count['text']=0
        width=window.winfo_screenwidth()
        height=window.winfo_screenheight()
        window.geometry(str(width) +'x'+str(height))
        photo=PhotoImage(file='skelet.gif')
        label=Label(image = photo, bg='black')
        label.image = photo
        label.place(width=width, height=height,x=0,y=0) # типа должно на полный экран,  но не  коректно открывает
        print('END')
        

def on_close():
    count_start()
    # time.sleep(5) # задержка перед закрытием
    # window.destroy()

        
window.protocol('WM_DELETE_WINDOW', on_close)
# window.tool window True
window.mainloop()

# Make .exe file
# 1.  run in python terminal
# # pip install pyinstaller
# 2. python -m PyInstaller 8.py ( в повершеле в дир где нужный скрипт лежить запустить , 8.py  это  имя файла для созд exe)
"""