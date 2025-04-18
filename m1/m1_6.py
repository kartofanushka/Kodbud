#Работа с файлами и функции

# r only read r+ coursor in the beginning 
# w rewrite data
# a append data
# + read and write
# file=open('re.txt', "r",encoding="utf-8")
# file=open('re.txt', "w",encoding="utf-8")
# file=open('re.txt', "a",encoding="utf-8")
# for line in file:
    # print(line)
#     # print(line.rstrip ("\n")) # убирает переносы строк line.rstrip ("\n")
    
# file.close()  #close file 


# # открывает выполняется и закрывает
# with open('Desktop\PY\re.txt', "r",encoding="utf-8") as file:
#     for line in file:
#         print(line)
# # ситает и выводит в список
#         print(file.readlines(), 'readlines')


# print(file.read()) read all file#
# print(file.read(10)) #1st 10 simbols
# file.write('jsfhkjhksjfhsdhf')

# file.writelines(10) # хз не работает

#=== Функции ===
        
# def sum(a,b):
#     return (a+b)

# #     return (a+b) строка завершает функц, дальше ничего не выполняется

# print(sum(5,5))

l=[1,5,9,7,5,3,4,5]
def list_sum(some_list):
    s=0
    for num in some_list:
        s += num
    # print(s)
    return(s)

# print(list_sum(l))

# проверяет на наличие четных чисел

def list_odd(list_some):
    for x in list_some:
        if x%2 !=0:
            return False
    return True
l1=[0,2,4]
l2=[0,3,4]
# print(list_odd(l1))
# print(list_odd(l2))


# pas='123'
def pas_check(pasw):
    return pasw =='123'

pas= input('input passord')
print(pas_check(pas))

def check(login):
    with open('logins.txt', "r+", encoding="utf-8") as logins: # r+ работает только потому что мы сначала читаем файл и курсор уходит вниз
        login_list = logins.readlines()
        print (login_list)
        for j in login_list:
            if login ==j.rstrip("\n"):
                print('taken')
                return
            else:
                logins.write("\n") #
                logins.write(login)
            return

check(input())

# ===1

# for in range

# ==2


# =====HW====

# ===1===
"""
def summa_n(a):
    la=[]
    if isinstance(a,int):
        for i in range (1,a):
            la.append(int(i))
        return('Я знаю, что сумма чисел от 1 до '+str(a) +' равна ' +str(sum(la))+'!')
    else:
        return('Это не число')        

print(summa_n((input())))  #как проверить что ввели именно число
"""
# почему-то не все скопировалось при сдаче
# ===/1===

# ===2===
# """
def calc(a,b,c):
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
# print(calc(1,2,'/'))
# """
# # reading file to check data added
# with open('calc.txt', "r") as logins:
#         login_list = logins.readlines()
#         print (login_list)

# ===/2===
# ===3===
"""# === correct ===
def greeting():

    print('Привет!')

    print('Добро пожаловать!')

for i in range(5):

    a = input('Зайдёте? Да/Нет: ')

    if a == 'Да':

        greeting()

    print('Следующий.\n')
# ===/ correct==="""
# print(greeting())

"""
def greeting():
    for i in range(1,5):
        a = input('Зайдёте? Да/Нет: ')
        if a == 'Да':
            print('Привет!')
            print('Добро пожаловать!')
            print('Следующий.\n')
    return

# print(greeting())
"""
# ===/3===