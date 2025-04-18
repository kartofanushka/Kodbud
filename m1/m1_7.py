# Tkinter
# Графический интерфейс – это графическая среда организации взаимодействия пользователя с устройства (компьютера). Графический интерфейс позволяет управлять устройством через визуальные элементы управления: окна, списки, кнопки, гиперссылки и другое

# Пример графического интерфейса в tkinter:

from tkinter import* #call libr (*) это чтобы не вызывать библиотеку каджый раз типа random.randint
# text
# font
# fg & bg 
window=Tk() # open window
window.geometry('750x500') #window size
window.title('Test test') #title
window['bg']='#f0f8ff'

facts = [
{'text': 'Человеческое имя Халка - Брюс Беннет', 'right': 1},
{'text': 'Уолт Дисней является создателем вселенной Marvel', 'right': 0},
{'text': 'До появления костюма супергероя, человек муравей занимался воровством ', 'right': 1},
{'text': 'Выдуманный город Дженоша является родиной Черной пантеры', 'right': 0}
]
quest_num=0
points=0
title_lable =Label(text='Quiz',
                    font=('Arial', 14), fg='black', bg='#f5f5f5')
                    
title_lable.place(x=15,y=5)
# координаты считают от верхнего левого угла 
# y вниз увеличивается, x вправо


fact=Message(text=facts[quest_num]['text'], justify=CENTER,font=('arial',9), width=300) # Message позволяет много строк вставлять
fact.place(x=80, y=50)

var= IntVar()
true= Radiobutton(text='tr', variable=var, value=1)
false= Radiobutton(text='fl', variable=var, value=0)
true.place (x=90, y=90)
false.place(x=130, y=90)


# def check():
#     global quest_num, points
#     answer = var.get()
#     if bool(answer) == facts[quest_num]["right"]:
#         points += 1
#         print(points)
#     if quest_num < len(facts)-1:
#         quest_num += 1
#         fact["text"] = facts[quest_num]["text"]
#     else:
#         points_label =Label(text="Вы набрали " + str(points) +" Очков", font=("Arial", 25), bg="Green")
#         points_label.place(x=0,y=0,width=700, height=250)
#         happy_label.place(x=0, y=250)

# ====MY===
def check():
    global quest_num, points
    answer=var.get()
    if bool(answer) == facts[quest_num]['right']:
        points+=1
        # print(points)
    if quest_num < len(facts)-1:
        print(quest_num)
        print(len(facts)-1)
        quest_num += 1
        fact['text']=facts[quest_num]['text']
        print('ok',quest_num)
        # print('ok', points)
    else:
        points_label =Label(text="Вы набрали " + str(points) +" Очков", font=("Arial", 25), bg="Green")
        points_label.place(x=0,y=0,width=550, height=400)
        happy_label.place(x=0, y=250)

b=Button(text='Submit',font=('arial',12),command=check)
b['bg']='green' #замена цвета по ходу,если захотелось
b.place (x=50, y=150)

# happy = PhotoImage(file='image1.png')
# happy_label= Label(image=happy)
# window.iconphoto(True, happy)
happy = PhotoImage(file="c:/Users/EuG/Desktop/PY/image1.png")

happy_label = Label(image=happy)

window.iconphoto(True, happy)
window.mainloop() #keep window oppened1
# print()


# Цвет
# Что нужно сделать:

# Доработайте кликер. Сделайте так, чтобы при достижении 20 очков цвет кнопки менялся.


# Время

# Что нужно сделать:

# Доработайте кликер, сделайте так, чтобы при достижении 20 очков программа “зависала на 2 секунды”.

# Подсказка:

# Используйте встроенный модуль time, ознакомьтесь с документацией по ссылке.


# Ещё одна кнопка

# Что нужно сделать:

# Добавьте в кликер ещё одну кнопку, которая тоже будет прыгать каждый раз, когда на неё нажимаешь. Сделайте так, чтобы при нажатии на одну из кнопок более 10-ти раз и при отсутствии нажатия на другую кнопку, та кнопка, на которую не нажимали меняла текст на “Ну пожалуйста image_description”.