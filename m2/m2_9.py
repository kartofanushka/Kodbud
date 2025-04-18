"""
 *args — обозначение неограниченного кол-ва позиционных аргументов функции.

**kwargs — обозначение неограниченного кол-ва именованных аргументов функции.

Генераторы списков и словарей (реализация) — встроенная в ЯП возможность использовать циклы внутри структур данных.

my_list = [i for i in ITERABLE]

Кортежи — это те же списки за одним исключением: кортежи неизменяемые структуры данных. Так же как списки они могут состоять из элементов разных типов, перечисленных через запятую.   
    """
# """
# *args
def sum1(integers):
    print(integers)
    result=0
    for u in integers:
        result +=u
    print(result, "sum1")
list_ints = [1,2,3,4,5,6,8,9,4]

def sum(*args):
    # здесь одним аргументом стал весь список в списке
    print(args)
    result=0
    for i in args[0]: # взяли первый эл-т это весь list_ints
        result+=i
    print(result, "sum")

sum1(list_ints)
sum(list_ints)

# **kwarg
# kwargs аргументы должны быть с названиями d="fsdgdfg"

def string_sum(*arg,**kw):
    result = ""
    # print('kw:',kw)
    for val in kw.values():
        result+=val+" "
    print('result:',result)
    # print('arg:',arg)

string_sum(1,2,3,4,a="sdf",d="fsdgdfg",e="sdfkjdf",f="dsfssdf")

def price(*prices,**kw):
    high=kw.get('h_price',max(prices))
    l=[]
    for p in prices:
        if p<high:
            l.append(p)
    print (l)

price(100,500,50,100,60,65, h_price=300)
"""
def ab(a,b=5):
    print(a+b)
ab(1,3)
ab(1)

my_lst=[i for i in range(100)]
my_lst1=[i for i in list_ints]
print(my_lst)
print(my_lst1)

print([i**3 for i in range (10)])
print([i**3 for i in range (10) if i>3])
print([i**3 for i in range (10) if i>3 if i%5==0 ])
print([i**3 if i>3 else i for i in range (10) ])
print({x:len(x)for x in ["a","bbbbb","ccc","ff"]})
"""

#===========

#list compreneshion - генератор списка - который генирует список чисел кратных 30 и 31 в промежутке от - 0 до 500
# print([i for i in range (5000) if i%30==0 and i%31==0])

#самостоятельное задание
#list compreneshion - генератор списка - который генирует список чисел кратных 30 или 31 в промежутке от - 0 до 500

# print([i for i in range(500) if i%30 == 0 or i%31==0])
#*
#Дан список целых чисел - нужно сделать из него кортеж уникальных чисел в обратном порядке

# l=[1,2,3,3,4,5]
# t = tuple(sorted(set(l), reverse=True))
# print(t)

# print(tuple ([x for x in sorted(set(l),reverse=1)]))

# #**
# #Написать функцию split_numbers, которая принимает строку целых чисел, разделённых пробелами, и возвращает кортеж из этих чисел.
# s="1 2 3 4 5"
# l = s.split(" ")
# print(l)
# t = tuple(l)
# print(t)

# print(tuple(i for i in s.split(" ")))
# print(tuple(int(i) for i in s.split(" ")))
#===========


# """
# Кортежи — это те же списки за одним исключением: кортежи неизменяемые структуры данных. Так же как списки они могут состоять из элементов разных типов, перечисленных через запятую.   
# """
"""t=(1,2,3,4,4,5)
# print(sorted.t())
d={t:"Hello"}
t1=(1,)
l=list(t)
l.append(6)
l=tuple(l)
# print(l)
# print(d)

# тернарный оператор
is_nice=True
state="nice" if is_nice else "not nice"
print(state)
is_nice=False
state="nice" if is_nice else "not nice"
print(state)

age=15
al_dr_rus=True if age>=18 else False
print(al_dr_rus)
al_dr_rus=age>=18
print(al_dr_rus)

# /тернарный оператор

val = None
if val:
    print(1)
if val == None:
    print(11)

def my_func(real_name, opt_display_name=None):
    display_name = opt_display_name or real_name
    print(display_name)

my_func("Mikhail")

my_func("Daniil","poprigunchik228")"""

# HW 
# 
# Создайте кортеж a = (5, 3, 2, 1, 4) и отсортируйте его по возрастанию с помощью метода sorted.
# После сортировки, а должен остаться кортежем, а не списком.

# a = (5, 3, 2, 1, 4)
# print(tuple(sorted(a)))

# Дома вам нужно написать программу, 
# которая принимает на вход 10 чисел и генерирует два списка. 
# Один с четными числами, второй с нечетными.

# Комментарий преподавателя:
# Заполнение списка через инпут оставь. Потом разбиение на четные и нечетные числа надо сделать через тернарный оператор, как в лекции.
l=[]
print("Введите 10 чисел")
# for i in range(10):
#     aa=input("Введите число: _ ")
#     l.append(int(aa))
aa="52 45 69 78 26 45 8 52 6 4 7 9 12 18 17 557 3 31"
l = [int(i) for i in aa.strip().split(" ")]
list_num=[l.copy]
# print(type(list_num))

# print(l)
l1=[]
l2=[]
for ii in l:
    l2.append(ii) if ii%2==0 else l1.append(ii) # после комента преаода. тернарный оператор
"""
над было так
Так тоже сойдет.
Вообще вот:"""
# эта херь не работает !!!
a = [[x for x in list_num]].copy
b = [x for x in list_num]
print("Четные: ", a)
print("Нечетные: ", b)
text = "word1anotherword23nextone456lastone333"
numbers = [x for x in text if x.isdigit()]
print(numbers,"numbers")
"""

В лекции, вроде, не сильно этому внимание уделили.
"""
    # if ii%2==0:
    #     l2.append(ii)
    # else:
    #     l1.append(ii)
print("нечетными",l1,"четными", l2)