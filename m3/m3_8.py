'''Лямбда функции
lambda-функции (безымянные функции) – функции, которые не имеют названия и используются в коде единожды, то есть не требуют постоянного вызова в разных точках кода. С помощью лямбда функций можно сократить кол-во строчек кода.

Допустим:
'''
goods=[{'n':'apple','price':25,'brand':'kolhoz'},
       {'n':'cucumder','price':15, 'brand':'ogorod' },
       {'n':'carrot','price':12, 'brand':'ogorod' },
       {'n':'pear','price':20, 'brand':'kolhoz' },
    ]
# def i_price(item):
#     return item['price']
# print(sorted(goods, key=i_price))   
'''OR''' 
print(sorted(goods, key=lambda item:item['price']))
'''Сортировка списка, который состоит из словарей по ключу price

Функция filter

Представим ситуацию, что нам необходимо отобрать из нашего списка только товары бренда Apple. Для этого, конечно, мы можем воспользоваться циклом, но это трата времени, есть гораздо более лаконичное и верное решение – использование встроенной функции filter.

Допустим:
'''
# kolhoz_list=filter(lambda item: item['brand']=='kolhoz', goods)
# print(list(kolhoz_list)) # list можно тоже вынести выше

# '''OR long version'''

# def kolhoz(goods):
#     kolhoz_list=[]
#     for g in goods:
#         if g['brand']=='kolhoz':
#             kolhoz_list.append(g)
#     return kolhoz_list
# print(kolhoz(goods))

'''Фильтрация списка, который состоит из словарей, по бренду kolhoz.

Функция filter принимает два параметра – условие фильтрации и итерируемую коллекцию по которой будет происходить фильтрация элементов в ней.

Функция map

Представим, что мы стали жертвой не очень продуманного API и нам пришёл список, 
состоящий из чисел, но все эти числа представлены как строки. Нам необходимо 
превратить все эти строки в числа. Конечно, мы можем написать цикл и решить эту задачу, 
но это уже не наш уровень. Для решения данной проблемы воспользуемся функцией map:

Допустим:

'''
# numbers_list=list('123456789') #['1', '2', '3', '4', '5', '6', '7', '8', '9']
# print(numbers_list)
# numbers_list=list(map(int, numbers_list)) #map()
# print(numbers_list)

names_list=['ivan', 'petr','arkadii']
# surnames_list=['sfgsdf','ivanos','pak']
# full_list=list(map(lambda name, surname: f"{name} {surname}", names_list,surnames_list))
# print(full_list)
# words=['hello','dog','apple','pear']
# print(list(map(len,words)), 'words len')
# num=[1,2,5,8,7]
# pow=[2,4,6,1,0]
# import math
# print(list(map(lambda n,p: math.pow(n,p),num,pow)))

'''

Функция map позволяет применять какую-либо функцию к каждому элементу итерируемой коллекции, при этом кол-во итерируемых объектов не ограничено.

Функция enumerate

Функция enumerate используется в циклах, когда помимо элемента списка, нам необходимо также получить его индекс. Функция возвращает кортеж вида (индекс, элемент).

Допустим:

'''
# indexed_goods=[] 
# for i in enumerate(goods):
#     indexed_goods.append(i[:item])
# vals=['a','b','c']
# index=0
# for val in vals:
#     print(index,val)
#     index+=1
# print('===same===')
# for i in range(len(vals)):
#     print(i, vals[i])
# print('===same===')
# for index,val in enumerate(vals):
#     print(index,val)
# print('===same===')
# from typing import Iterator
# print("")

# def my_enumerate(iterable, start:int=0) -> Iterator:
#     index = start
#     for elem in iterable:
#         yield index, elem
#         index += 1

# for index, val in my_enumerate(vals):
#     print(index, val)
# from typing import Iterator
# print(isinstance(enumerate(goods), Iterator))

'''
Функция zip

Функция zip используется в циклах, когда нам необходимо одновременно перебирать элементы сразу несколько итерируемых объектов за раз. Функция принимает неограниченное кол-во элементов.

Допустим:
'''
# names_list=['ivan', 'petr','arkadii']
# surnames_list=['sidorov','ivanos','pak']
# otche_list=['petrovich','pavlovich','ivanovich']

# for name, surname, otche in zip(names_list, surnames_list,otche_list):
#     print(name, otche, surname)
'''==============END==============='''
# l= lambda x:x**2
# print(l(3))

# # OR SAME

# def f(x):
#     return x**2
# print(f(3))

# help(sorted) # help i pythion
# t=(1,2,5,78,6,5,5)
# print(sorted(t)) #always return list
# string ='dgd514sdfGHJKLK`'
# print(sorted(string)) #always return list
# f=[False,True,1,0,2==1,5==5]
# print(sorted(f))

'''OTHER|||'''
print(__name__,type(__name__)) #__main__ <class 'str'>

''' Это выполняется только при запуске основного файла '''
if __name__=='__main__':
    print('Trhis is main file')
else:
    print('Print only in descendant file')
    
'''=======HW================'''
# 1. У вас есть класс Item и список, с этими объектами. Вам необходимо отфильтровать данный
# список таким образом, чтобы после фильтрации остались товары лишь одного бренда. 
# Решение необходимо реализовать в одну строчку, за исключением print(result).
class Item:
    def __init__(self,price,brand):
        self.price=price
        self.brand=brand
    def __repr__(self):
        return self.brand
items_list=[
    Item(1020, "Apple"),
    Item(1500, "Apple"),
    Item(1070, "Samsung"),
    Item(2100, "Oppo"),
    Item(1500, "Asus"),
    Item(1800, "Mi"),
]
""" ANSWER"""
fl_list=filter(lambda item: item.brand =="Mi", items_list)   
print(list(fl_list))
print(items_list)
"""==="""

# 2.У вас есть список с именами, однако, так получилось, что копирайтер написал их с маленькой буквы. Вам необходимо реализовать код в одну строчку, за исключением print(result), который изменит все первые буквы имён на заглавные буквы.
""" ANSWER"""
names_list = ['данил', 'артём', 'никита', 'влад']
new_names=list(map(lambda item: item.capitalize(), names_list))
print(new_names)   
"""==="""
