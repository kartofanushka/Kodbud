"""Метод __add__.
Давайте вспомним код, который нам известен ещё начиная с нашего первого занятия, 
когда мы склеивали строки. Мы пользовались этим как данное, строки складывались 
и получалась одна общая строка, настало время разобраться с тем, как этот механизм 
устроен изнутри. Чтобы это выяснить, необходимо познакомиться с новым магическим 
методом __add__.

Метод __add__ - магический метод класса, который определяет поведение класса, 
когда мы его с чем-либо складываем. Другими словами, определяет поведение 
при арифметической операции сложения.

Метод __add__ принимает два параметра. Первый, как обычно, self – ссылка на экземпляр
нашего класса, а второй – other, тот объект с которым складывается экземпляр нашего класса. 
В методе __add__ мы явно определили, что необходимо вернуть в качестве результата, 
когда экземпляр нашего класса будет складываться с чем-либо.

Допустим:
"""
# class Item:
#     def __init__(self,name, price,weight):
#         self.name=name
#         self.price=price
#         self.weight=weight
        
#     def __add__(self,other):
#         return self.price + other.price
# item_1=Item("potato", 15_000,0.8)
# item_2=Item("kotlets", 12_000,0.3)

# total_price=item_1+item_2
# print(total_price)
"""
Функция isinstance()

Данная функция позволяет проверять, принадлежит ли объект к тому или иному типу (классу). Давайте ею воспользуемся:

Допустим:
 """
def __add__(self,other):
    if isinstance(other,Item):
        return self.price+other.price
"""
Принадлежит ли объект other к классу Item

Tkinter

Функция find_overlapping возвращает все id объектов, которые попадают в определенный заданный периметр. Она принимает четыре атрибута: x1, y1, x2, y2. На этих точках строится прямоугольник. Если какой-либо объект попадает в его пределы – функция вернёт нам его id.
"""       

class Item:
    def __init__(self,name, price,weight):
        self.name=name
        self.price=price
        self.weight=weight
        
    def __add__(self,other):
        if isinstance(other,Item): # проверка для строки с ошибкой
            return self.price*self.weight+other.price*self.weight # изменен после самост задания, добавлен вес
        elif(other,(int,float)):
            return self.price+other
    #обратный add, меняются местами reversed add        
    def __radd__(self,other):
        # if isinstance(other,Item): # проверка для строки с ошибкой
        #     return self.price*self.weight+other.price*self.weight
        # elif(other,(int,float)):
        #     return self.price+other
        # or
        return self.__add__(other)
        
item_1=Item("potato", 15_000,0.8) # выполняется  __init__
item_2=Item("kotlets", 12_000,0.3)
item_3=Item("Makaroni",20_000,0.8)
# total_price=item_1+item_2 # на глубинном уровне + и add в питоне одно и тоже

# print(total_price)
# print(item_1.__add__(item_2))
# #Error
# # print(item_1+500) # AttributeError: 'int' object has no attribute 'price' 
# print(500+item_1) # __radd__(self,other): обрабатывает

# # мы выполняем только с __radd__
# goode=[item_1,item_2,item_3]
# print(sum(goode))

# #  если нужно ситать другие пераметры, так \/ это многобукв, добавляем в класс
# print(f"Итого: {((item_1.price*item_1.weight *1.1+item_2.price*item_2.weight*1.2)*1.15)}")

# # написать метод add для цены за кг
# # вместо
# item_1.price 
# # написали 
# item_1.price*item_1.weight 


'''===========HW============'''
'''
1.Самостоятельно узнайте про другие магические методы, 
которые позволяют работать с арифметическими операциями 
внутри класса. Добавьте в класс Item вычитание, умножение 
и деление объекта. Что с чем будете умножать/делить/вычитать
– выбор исключительно за вами, можно также эксперементировать 
с ценой (атрибут price), а можно взять вес (атрибут weight).
__mul__ __divmod__ __sub__'''
# print(dir(float))
num=10
print(num.__sub__(7))
# print(num.__truediv__(5))
# print(num.__mul__(5))

class Item1:
    def __init__(self,name, price,weight):
        self.name=name
        self.price=price
        self.weight=weight
    
    def __sub__(self,other):
        if isinstance(other,Item1): # проверка для строки с ошибкой
            return self.price*self.weight-other.price*other.weight
        elif(other,(int,float)):
            return self.price*self.weight-other
    def __truediv__(self,other):
        if isinstance(other,Item1): # проверка для строки с ошибкой
            return int(self.price*self.weight)/int(other.price*other.weight)
        elif(other,(int,float)):
            return (self.price*self.weight)/other
    def __mul__(self, other):
        # return self.price*self.weight
        if isinstance(other,Item1): # проверка для строки с ошибкой
            return self.price*self.weight*other.price*other.weight
        elif(other,(int,float)):
            return self.price*self.weight*other       
    def __add__(self,other):
        if isinstance(other,Item1): # проверка для строки с ошибкой
            return self.price*self.weight+other.price*other.weight
        elif(other,(int,float)):
            return self.price*self.weight+other

    
item_1=Item1("kartofan", 15_000,0.8) 
item_2=Item1("kotletki", 12_000,0.3)
item_3=Item1("makaroshki",20_000,0.8)

print(item_1+item_3,item_1-item_3,item_1*item_2,item_2/item_3)


'''
2.Модернизируйте нашу игру алхимию. Добавьте как минимум 
ещё две химические реакции на ваше усмотрение.



'''