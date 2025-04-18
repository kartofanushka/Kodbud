# Tkinter
# Графический интерфейс – это графическая среда организации взаимодействия пользователя с устройства (компьютера). Графический интерфейс позволяет управлять устройством через визуальные элементы управления: окна, списки, кнопки, гиперссылки и другое

# Цвет
# Что нужно сделать:

# Доработайте кликер. Сделайте так, чтобы при достижении 20 очков цвет кнопки менялся.

from tkinter import *
import random

window = Tk()
window.geometry('700x500')
window.title('Кликер')


points = 17

def check():
    global points
    if points <19:
        b.place(x=random.randint(1,550),y=random.randint(1,350))
    else:
        b.place(x=random.randint(1,550),y=random.randint(1,350))
        b['bg']='red'
    points +=1
    label['text'] = points



b = Button(text='нажми меня', font=('Arial', 20), fg='black', command=check)
b.place(x=200,y=130)
label = Label(text = points, font=('Arial',15), fg='black')
label.place(x=10,y=10)






window.mainloop()
# Время

# Что нужно сделать:

# Доработайте кликер, сделайте так, чтобы при достижении 20 очков программа “зависала на 2 секунды”.

# Подсказка:

# Используйте встроенный модуль time, ознакомьтесь с документацией по ссылке.

"""В задании не уточняется, но, вроде, зависание должно быть один раз. Только при достижении 20 очков. 
У тебя зависание идет при каждом клике после 20.
Так то все верно. Зачет, конечно!
    """

from tkinter import *
import random
import time

window = Tk()
window.geometry('700x500')
window.title('Кликер')


points = 18

def check():
    global points
    if points <19:
        b.place(x=random.randint(1,550),y=random.randint(1,350))
    else:
        b.place(x=random.randint(1,550),y=random.randint(1,350))
        time.sleep(2)
    points +=1
    label['text'] = points



b = Button(text='нажми меня', font=('Arial', 20), fg='black', command=check)
b.place(x=200,y=130)
label = Label(text = points, font=('Arial',15), fg='black')
label.place(x=10,y=10)






window.mainloop()
# Ещё одна кнопка

# Что нужно сделать:

# Добавьте в кликер ещё одну кнопку, которая тоже будет прыгать каждый раз, когда на неё нажимаешь. 
# Сделайте так, чтобы при нажатии на одну из кнопок более 10-ти раз и при отсутствии нажатия на другую 
# кнопку, та кнопка, на которую не нажимали меняла текст на “Ну пожалуйста image_description”.

# Отлично!
# Интересное решение со сбросом очков у второй кнопки)


from tkinter import *
import random
import time

window = Tk()
window.geometry('700x500')
window.title('Кликер')


points = 0
p1=0
p2=0
def check(h):
    global points, p1, p2
    if h==1:
        b1.place(x=random.randint(1,550),y=random.randint(1,350))
        b1['text'] = 'нажми меня1'
        p1+=1
        p2=0
    else:
        b2.place(x=random.randint(1,550),y=random.randint(1,350))
        b2['text'] = 'нажми меня2'
        p1=0
        p2+=1
 
    if (p1>9 and p2==0):
        b2['text'] = 'Ну пожалуйста :('
    elif (p2>9 and p1==0):
        b1['text'] = 'Ну пожалуйста :('

    
    points +=1
    label['text'] = points
    abel1['text'] = p1
    abel2['text'] = p2



b1 = Button(text='нажми меня1', font=('Arial', 20), fg='black', command = lambda:check(1))
b1.place(x=200,y=130)
b2 = Button(text='нажми меня2', font=('Arial', 20), fg='black', command = lambda:check(0))
b2.place(x=400,y=130)
label = Label(text = points, font=('Arial',15), fg='black')
label.place(x=10,y=10)
abel1 = Label(text = p1, font=('Arial',15), fg='black')
abel1.place(x=50,y=10)
abel2 = Label(text = p2, font=('Arial',15), fg='black')
abel2.place(x=100,y=10)






window.mainloop()
