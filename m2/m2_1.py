# MODULE 2
"""
    Переменные, условные операторы. Циклы
Язык программирования — формальный язык, предназначенный для записи компьютерных программ. Язык программирования определяет набор лексических, синтаксических и семантических правил, определяющих внешний вид программы и действия, которые выполнит исполнитель под её управлением.

Интерпретатор — это исполняемый файл, который построчно читает программу, а затем обрабатывает, сразу выполняя ее инструкции.

Переменная — это область в оперативной памяти, которая имеет размер и может хранить какую-то информацию, ну или не хранить.

Строка — это последовательность любых символов, строки можно складывать, это то, что мы с вами сделали, эта операция называется конкатенация.

Условный оператор — это конструкция языка программирования, определяющая более одной последовательности выполнения в программе.

Кострукция try except — это конструкция языка программирования, позволяющая отлавливать исключения в коде программы.

Цикл — это часть кода, которая повторяется.

Функция — это специальный объект, который включает в себя набор команд, которые объединены одним названием.
    """
"""for i in range(10): #print 0-9
    print(i)
    
for i in range(1,10): #print 1-9
    print(i)

for i in range(1,10,3): #print every 3rd
    print(i)"""
'''films = {'1':'gh','1a':'gh','1s':'gh','1d':'gh','1dd':'gfh'}
a=films.get('1a')
print(a)
import time
# 1674211507
try:
    normalt=time.strftime("%D %H:%M",time.localtime('1674211507'))
    print(normalt)

except: # or except TypeError: if you neen to skip exact error type
    print('hgfg')
else:
    normalt=time.strftime("%D %H:%M",time.localtime(1674211507))
    print(normalt)
finally:
    print('Ok')'''
#
# HW
# 
# calculator
"""def calc(a,b,c):
    with open('calc.txt', 'a+', encoding="utf-8") as calcs: 
        if c=='+':
            h=str(a+b)
            calcs.write(h +" \n")
            return (h)
        elif c=='-':
            h=str(a-b)
            calcs.write(h +" \n")
            return(h)
        elif c=='*':
            h=str(a*b)
            calcs.write(h +" \n")
            return(h)
        elif c=='/':
            h=str(a/b)
            calcs.write(h +" \n")
            return(h)
a=int(input('число 1? __ '))
c=input('Знак деействия:  * / + -  ')
b=int(input('число 1? __ '))
print(calc(a,b,c))
  
# print(calc(1,2,'+'))
# print(calc(1,2,'-'))
# print(calc(1,2,'*'))
# print(calc(1,2,'/'))"""
def input_num():
    global num1,num2
    num1=float(input('число 1? __ '))
    num2=float(input('число 2? __ '))

def plus():
    while True:
        input_num()
        try:
            res=float(num1)+float(num2)
            print(res)
            break
        except ValueError:
            print('it\'s not number')
            continue

def minus():
    while True:
        input_num()
        try:
            res=float(num1)-float(num2)
            print(res)
            break
        except ValueError:
            print('it\'s not number')
            continue

def mult():
    while True:
        input_num()
        try:
            res=float(num1)*float(num2)
            print(res)
            break
        except ValueError:
            print('it\'s not number')
            continue
        
def dev():
    while True:
        input_num()
        try:
            res=float(num1)/float(num2)
            print(res)
            break
        except (ValueError, ZeroDivisionError):
            print('it\'s not number or 0')
            continue

def calculator():
    while True:
        # print('+,-,/,* ')
        operation=input('Знак действия:  * / + -  "e" for exit  ')
        if operation=='+':
            plus()
        elif operation=='-':
            minus()
        elif operation=='*':
            mult()
        elif operation=='/':
            dev()
        elif operation=='e':
            print(operation)
            break
        
        
# calculator()

# Допишите функцию, которая принимает значение a, b, c квадратного уравнения и, исходя из этих значений, считает дискриминант.

# b**2-4*a*c


# """
def discr():
    num_a=float(input('Число a '))
    num_b=float(input('Число b '))
    num_c=float(input('Число c ')) 
    # print('Введите число со знаком + или - "5" или "-5"')
    
    d=(num_b**2)-(4*num_a*num_c)
    print('Дискриминант рвен: ' ,d)
    if d>0:
        x1=(-num_b+d**0.5)/(2*num_a)
        x2=(-num_b-d**0.5)/(2*num_a)
        print("x1=",x1,"x2=",x2)
    elif d<0:
        print("Нет действ. корней")
    elif d==0:
        x=-num_b/(2*num_a)
        print("x=",x)

  
# discr()
#  """
games={"Sandbox":["Minecraft",
    "Grand Theft Auto",
    "The Sims"],
    "Real-time strategy (RTS)":["Warcraft",
    "Age of Empires",
    "Command & Conquer"],
    "Shooters (FPS and TPS)":["Halo (FPS)",
    "Gears of War (TPS)",
    "DOOM (FPS)"],
    "Multiplayer online battle arena (MOBA)":["Dota 2",
    "League of Legends",
    "Smite"],
    "Role-playing (RPG, ARPG, and More)":["Skyrim",
    "The Witcher 3 (ARPG)",
    "Fallout 4"],
    "Simulation and sports":["Forza Motorsport",
    "Madden NFL",
    "NBA2K"],
    "Puzzlers and party games":["Jackbox Party Pack (party game)",
    "The Talos Principle (puzzler)",
    "Portal 2 (puzzler)"],
    "Action-adventure":["Star Wars Jedi: Fallen Order",
    "Sekiro: Shadows Die Twice",
    "Assassin’s Creed"]}
buttons=[]
for key in games.keys():
    # print(key)
    buttons.append('telebot.types.InlineKeyboardButton("'+key+'", callback_data="'+key+'")')
print(buttons)