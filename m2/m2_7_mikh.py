import os
from pygame import mixer
from gtts import gTTS
#from playsound import playsound
import winsound

# my_file = open("some.txt", "r") # r, w, a, r+, rb, wb
# my_string = my_file.read()
# my_file.close()

# tts = gTTS(text=my_string, lang="ru", slow=True)
# tts.save("m2_7/abc.mp3")
# mixer.init()
# mixer.music.load("m2_7/abc.mp3")
# mixer.music.set_volume(0.03) #от 0 до 1
# mixer.music.play()

# res = True
# while True:
#     print("Input p to pause")
#     print("Input r to resume")
#     print("Input e to exit")
    
#     uin = input(": ")
#     if uin == "p":
#         mixer.music.pause()
#     elif uin == "r":
#         mixer.music.unpause()
#         res = True
#     elif uin == "e":
#         mixer.music.stop()
#         break
#     if (res):
#         mixer.music.play()
#         res = False

import pyaudio
import speech_recognition as sr

#чтобы найти микрофон (а точнее его индекс)
#-------------------
p = pyaudio.PyAudio()
device_index = None
for i in range(p.get_device_count()):
    device_info = p.get_device_info_by_index(i)
    if device_info.get("defaultSampleRate") == 44100.0:
        device_index = i
        break
#--------------------
def answer(my_string):
    mixer.init()
    tts = gTTS(text=my_string, lang="ru", slow=True)
    tts.save("m2_7/abc.mp3")
    mixer.init()
    mixer.music.load("m2_7/abc.mp3")
    mixer.music.set_volume(0.03) #от 0 до 1
    mixer.music.play()

r = sr.Recognizer()
while True:
    with sr.Microphone(device_index = device_index) as source:
        print("Говори и будет ответ тебе: ")
        audio = r.listen(source = source, phrase_time_limit=5)
    try:
        speech = r.recognize_google(audio, language="ru_RU").lower()
        print("Ты сказал: " + speech)
        if "привет" in speech:
            print("Привет, Андрей")
    except:
        pass

