from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime

window=Tk() # open window
window.geometry('400x300') #window size
window.resizable(0, 0)
window.title("Courses")

url = "http://www.cbr.ru/scripts/XML_daily.asp" #?
# запросит определенную дату
# ======
# today = datetime.today()
# today = today.strftime("%d/%m/%Y")

# payload = {"date_req": today}
# responce = requests.get(url, params=payload)
# ========
responce = requests.get(url)# это просто текущую

xml = BeautifulSoup(responce.content, "xml") #

def getCourse(id):
    return xml.find("Valute", {"ID" : id}).Value.text
header=xml.find("ValCurs").attrs["name"]
date=xml.find("ValCurs").attrs["Date"]
print(header)
# ValCurs Date="03.03.2023" name="Foreign Currency Market">
img_logo = PhotoImage(file="8-2/logo.png")
logo = Label(window, image=img_logo)
logo.place(x=200, y=120)

course_info = Label(window, text=header, font="Arial 24")
course_info.place(y=20, x=20)

course_info = Label(window, text=date, font="Arial 20")
course_info.place(y=100, x=20)
course_info = Label(window, text="$:" + getCourse("R01235"), font="Arial 20",foreground='green' )
course_info.place(y=150, x=20)
course_info = Label(window, text="€:" + getCourse("R01239"), font="Arial 20",foreground='blue')
course_info.place(y=190, x=20)
course_info = Label(window, text="¥:" + getCourse("R01375"), font="Arial 20",foreground='red')
course_info.place(y=230, x=20)


window.mainloop()
# """


"""
#кнопка кликалка
import os
from pygame import mixer
from gtts import gTTS
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
    tts.save("m2_7/abc.mp3")
    mixer.init()
    mixer.music.load("abc.mp3")
    mixer.music.set_volume(0.03) #от 0 до 1
    mixer.music.play()
    while mixer.music.get_busy():  # ждем когда закончится
        continue
    mixer.quit()  # закрываем миксер
    os.remove("m2_7/abc.mp3")


btn = Button(root, text="Кнопка", background="#555", foreground="#ccc", font="16", activebackground="red", command=sound)
btn.place(x = 400, y = 400)

root.mainloop()
# """
# HW
# Оконные приложения
# 1.Добавьте в приложение курс юаня.


# 2.Доработайте внешний вид приложение. Добавьте красок.
# Запретите пользователю менять размер окна.
# 

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