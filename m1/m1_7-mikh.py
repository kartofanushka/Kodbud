from tkinter import *


window = Tk()
window.geometry("700x500")
window.title("Максимум Тест")

#window["bg"] = "Black"



facts = [
{'text': 'Человеческое имя Халка - Брюс Беннер', 'right': 1},
{'text': 'Уолт Дисней является создателем вселенной Marvel', 'right': 0},
{'text': 'До появления костюма супергероя, человек муравей занимался воровством ', 'right': 1},
{'text': 'Выдуманный город Дженоша является родиной Черной пантеры', 'right': 0}
]

question_number = 0
points = 0
title_label = Label(text="Привет", font=("Arial", 25), bg="Green")

title_label.place(x=0, y=0, width=700, height=50)

fact = Message(text= facts[question_number]["text"], justify=CENTER, font=("Arial", 14), width=680)
fact.place(x=10, y =70)

var = IntVar()

true = Radiobutton(text="Правда", variable=var, value=1)
false = Radiobutton(text="Ложь", variable=var, value=0)

true.place(x=10, y=120)
false.place(x=10, y=170)

def check():
    global question_number, points
    answer = var.get()
    if bool(answer) == facts[question_number]["right"]:
        points += 1
        print(points)
    if question_number < len(facts)-1:
        question_number += 1
        fact["text"] = facts[question_number]["text"]
    else:
        points_label =Label(text="Вы набрали " + str(points) +" Очков", font=("Arial", 25), bg="Green")
        points_label.place(x=0,y=0,width=700, height=250)
        happy_label.place(x=0, y=250)

b = Button(text="Ответить", font=("Arial", 24), command=check)
b.place(x=220, y=130)

b["bg"] = "Green"
happy = PhotoImage(file="happy.png")

happy_label = Label(image=happy)

window.iconphoto(True, happy)
window.mainloop()