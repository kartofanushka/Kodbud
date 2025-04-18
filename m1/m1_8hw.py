# pip install pyinstaller
# python -m PyInstaller 8.py ( в повершеле в дир где питон лежить запустить , 8.py  это  имя файла для созд exe)

# Лотерея!

# Что нужно сделать:

# Напишите программу с графическим интерфейсом. В окне программы должна располагаться надпись: “ВЫ ВЫЙГРАЛИ В ЛОТЕРЕЕ!” и кнопка “ПОЛУЧИТЬ ВЫЙГРЫШ!”. 
# При нажатии на кнопку текст меняется на “Чтобы забрать выйгрыш необходимо внести 1000руб.” При этом закрыть окно крестиком нельзя.
# === 1 ===


# from tkinter import *
# window=Tk() # open window
# window.geometry('900x300') #window size
# window.resizable(height=False, width=False)
# window.config(bg='black')
# text=Label(text='ВЫ ВЫЙГРАЛИ В ЛОТЕРЕЕ!', fg='pink', bg='black', font=('Comic Sans', 16), justify='center')
# # text=Label(text=t, fg='pink', bg='black', font=('Comic Sans', 16), justify='center')
# text.place(x=100, y=100, width=700, height=100)

# b=Button(text='ПОЛУЧИТЬ ВЫЙГРЫШ!',font=('arial',12), command = lambda:winer())
# # b['bg']='green' #замена цвета по ходу,если захотелось
# b.place (x=500, y=200)
# def winer():
#     global lottery
#     
#     text=Label(text='Чтобы забрать выйгрыш необходимо внести 1000руб.', fg='pink', bg='black', font=('Comic Sans', 16), justify='center')
#     text.place(x=100, y=100, width=700, height=100)

# def on_close():
#     print('end')
        
# window.protocol('WM_DELETE_WINDOW', on_close)

# window.mainloop()

# === /1 ===



# Собачьи бега

# В собачьих бегах участвует N собак, у каждой из них есть определённое количество очков за сезон. 
# На огромном табло выводятся очки каждой собаки. 
# Однако при выводе был обнаружен баг: собаки с наибольшим и наименьшим количеством очков поменялись местами! 
# Нужно это исправить.
# Дан список очков из N собак. 
# Напишите программу, которая меняет местами наибольший и наименьший элементы в списке.

# ===2 ===
dogs={
    "Бетховен":5, 
    "Вилли":6, 
    "Ричард":7, 
    "Цербер":4, 
    "Тюльпан":25,
    "Ягодка":15, 
    "Малыш":1
}
# dogs_v=dogs.values()
print(dogs.values())
print(dogs.items())
dogs_s=sorted(dogs.items(),key=lambda x:x[1],reverse=True)
print(dogs_s)
dogs_s[-1], dogs_s[0]    =   dogs_s[0], dogs_s[-1]

print(dogs_s)
for i in dogs_s:
    print(i[0], i[1])
    
# правильное решение и описание 
max_dog_points = max(dogs.values())
min_dog_points = min(dogs.values())
print(max_dog_points, min_dog_points)
values = list(dogs.values())
print(values)
max_index = values.index(max_dog_points)
min_index = values.index(min_dog_points)
print(max_index, min_index)
d = list(dogs.items())
d[max_index], d[min_index]    =   d[min_index], d[max_index]
print(d)
dogss = dict(d)
print(dogss)
"""
Не совсем верно.

Сортировать список не надо. Надо найти в списке собак с максимальным/минимальным числом очков. Затем найти их индексы, и по индексам поменять их местами.
Задача значительно усложняется, т.к. ты используешь словарь, а не просто список с очками.
Максимальное значение: max_dog_points = max(dogs.values())
Так же находим минимальное значение (max меняем на min).
Далее, т.к. это словарь, мы не можем просто получить индекс элемента. Надо создать новый список на основе числовых значений в словаре:
values = list(dogs.values())
Находим в новом списке индекс максимального значения:
max_index = values.index(max_dog_points)
Для минимального аналогично.
Далее, опять же, т.к. это словарь, мы не можем в нем поменять местами его элементы. Создаем еще один список с именами собак:
d = list(dogs.items())
Теперь в этом списке d меняем элементы местами, как ты уже делала в своем решении. Только в [] ставишь не 0 и -1, а max_index и min_index.
Далее существующий словарь dogs заменяем на новый:

dogs = dict(d)
и выводим результат.
Можно добавить еще принты после каждого этапа программы, что бы понимать процесс работы.

Должно получиться что-то типа этого:8hw.jpg
"""


# === /2 ===

"""
# Импровизация

# Что нужно сделать:
# Придумайте и напишите свое оконное приложение. 
# Это может быть вирус, подобный тому, что мы сделали на уроке. 
# Или кликер с несколькими кнопками. 
# Можно сделать фотоальбом, в котором при нажатии на разные кнопки открываются разные картинки.

from tkinter import *
from tkinter import ttk

win= Tk()
win.geometry("750x750")
xx=200
yy=100
pic = PhotoImage(file="image1.png")
pic_label = Label(win, image=pic, bg='red', justify='center')
pic_label.place(x=50, y=150, width=xx, height=yy )
def print_text(x):
   global xx, pic_label, text0,text1
   if x==1:
      xx=200
      pic_label.place(x=50, y=150, width=xx, height=yy )
   elif x==2:
      xx= xx+20
      if xx>=600:
         xx=600
         # text1= ttk.Label(win, text='Нажми Сузить',font=('Helvetica 13 bold')).pack()
         # text1.pack(pady=100)
      pic_label.place(x=50, y=150, width=xx, height=yy )
   elif x==3:
      xx=xx-20
      if xx<=0:
         xx=0
         # text0= ttk.Label(win, text='Нажми Расширить',font=('Helvetica 13 bold')).pack()
         # text0.pack(pady=100)
      pic_label.place(x=50, y=150, width=xx, height=yy )
   
 
   # Label(win, text=text,font=('Helvetica 13 bold')).pack()


btn1= ttk.Button(win, text="Исходный размер" ,command= lambda:print_text(1))
btn1.pack(pady=10)
btn2= ttk.Button(win, text="Расширить" ,command= lambda:print_text(2))
btn2.pack(pady=10)
btn3= ttk.Button(win, text="Сузить" ,command= lambda:print_text(3))
btn3.pack(pady=10)





win.mainloop()
"""
def test():
   ww=1
   pp=2
   return ww,pp
print(test())