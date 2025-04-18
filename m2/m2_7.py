from tkinter import *
from pygame import mixer
from gtts import gTTS
import os
import gtts.tokenizer
def play_file():
    my_file=open("m2_7/tts.txt","r")
    my_str=my_file.read()
    my_file.close()
    my_str=gtts.tokenizer.pre_processors.tone_marks(my_str)
    # print(my_str)
    my_str=gtts.tokenizer.pre_processors.end_of_line(my_str)
    my_str=gtts.tokenizer.pre_processors.abbreviations(my_str)
    my_str=gtts.tokenizer.pre_processors.word_sub(my_str)
    gtts.tokenizer.tokenizer_cases.tone_marks()
    gtts.tokenizer.tokenizer_cases.period_comma()
    gtts.tokenizer.tokenizer_cases.colon()
    gtts.tokenizer.tokenizer_cases.other_punctuation()
    # my_str="Предыстория. Обнаружил что вулли недоплачивает дохрена монет относительно калькулятора. Перешел на другой пул - там все ок. Проверил выплаты других майнеров из топа вули. У всех одно и тоже. 35-40% недоплат. Создал ветку на реддите, надеялся что они просто признают ошибку, извинятся, выплатят недоплаченное , но видимо ошибался. Итак. Ветка реддита кому интересно."
    # ppr=[pre_processors.tone_marks, pre_processors.end_of_line, pre_processors.abbreviations, pre_processors.word_sub]
    tts=gTTS(text=my_str, lang="uk")
    tts.save("m2_7/abc.mp3")
    mixer.init()
    mixer.music.load("m2_7/abc.mp3")
    mixer.music.set_volume(0.25) #от 0 до 1
    mixer.music.play()
    res=False
    
    while True:
        # if mixer.music.get_busy():
            print("p -pause, r -resume , e - exit")
            uin= input(": ")
            if uin=="p":
                mixer.music.pause()
            elif uin=="r":
                mixer.music.unpause()
                res=True
            elif uin=="e":
                mixer.music.stop()
                break
            if (res):
                mixer.music.play()
                res=False
            
        # continue
# play_file()

"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""

"""
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text="Hello, World!")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
"""
# ----- find input device-----
# import pyaudio
# pa = pyaudio.PyAudio()
# print(pa.get_default_input_device_info())
#----------------
# device_index=None
# for i in range(pa.get_device_count()):
#     device_info=pa.get_default_input_device_info()
#     print(i, "======", device_info)
#     if device_info.get("defaulstSampleRate")==44100.0:
#         device_index=i
#         break
# ------------------------------
# pa.get_device_count() #get available devices

# """
import speech_recognition as sr
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
# answer("ghas") 
# """
r=sr.Recognizer()
while True:
    with sr.Microphone(device_index=0) as source: # у нас нет микрофона
        print("Speak")
        stream=r.listen(source=source,phrase_time_limit=10)
    try:
        print("Recognizing...")
        speech=r.recognize_google(stream, language="en-US").lower()
        print("answer "+ speech)
        # if "обнаружил" in speech:
        #     answer("Привет, Кожанный")
    except:
        break
        # pass
# """
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
#кнопка кликалка
import os

root=Tk()

root.title("Bla Bla0")
root.geometry("500x500")

lab=Label(root, text="Some TextSome TextSome Text", bg= "#FF6666", fg="gold", font="16")
lab.place(x=100, y=100)

count=0
def cLabel():
    global count
    count +=1
    lab["text"]=str(count)
    

btn=Button(root, text="BtnBtn", background="#555", foreground="#ccc", font="16", activebackground="red", command=cLabel)
btn.place(x=200, y=200)

input_field=Entry(root)
input_field.place(x=20, y=20)

def sound():
    text = input_field.get()
    tts = gTTS(text=text , lang="ru", slow=True)
    tts.save("abc.mp3")
    mixer.init()
    mixer.music.load("abc.mp3")
    mixer.music.set_volume(0.03) #от 0 до 1
    mixer.music.play()
    while mixer.music.get_busy():  # ждем когда закончится
        continue
    mixer.quit()  # закрываем миксер
    os.remove("abc.mp3")


btn = Button(root, text="Кнопка", background="#555", foreground="#ccc", font="16", activebackground="red", command=sound)
btn.place(x = 400, y = 400)

root.mainloop()
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