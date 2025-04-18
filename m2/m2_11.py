# sm m2_11

# классы
# print(type("abc"), id("abc"))
# print(type(id), id(id))
# print(type(type), id(type))
# print(type(1), id(1))
# print(type("abc"), id("abc"))

class Drink:
    def __init__(self, color, alcohol, flavour):
        self._color = color
        self._alcohol = alcohol
        self._flavour = flavour

    def __change(self): #полный запрет обращения  строка 25 даст ошибку, нельзя вызывать
        print("вы чета поменяли")
    
    def p(self): 
        self.__change() #обход запрета строка 26

d = Drink("red", 0, "orange")

print(d._color)
# d.__change()
# d.p()

class Panda:
    # _max_weight = 200
    def __init__(self, weight):
        self.__max_weight = 200
        self._color = "black and white"
        self._weight = weight if weight <= 200 else 200
    
    def print_info(self):
        print(f"Вес панды: <{self._weight} кг>, цвет панды: <{self._color}>") #()"Вес панды: " , self.weight , "цвет панды : ", self.color)

    #служебный метод - тот, что используется только в классе
    def _can_eat(self, food):
        if self._weight >= self.__max_weight - food:
            print("Худей, панда, а то наешься и не проснешься")
            return False
        return True

    def eat(self):
        if self._can_eat(3):
            self._weight += 3
            print("Наелась и спит")
    def snack(self):
        if self._can_eat(0.5):
            self._weight += 0.5
            print("Перекусила и отдыхает")
    #Сделать метод - перекус для панды, чтобы можно было кормить не 3 кг еды, а 0.5 кг еды
    #не забудьте про проверку веса
# _объект - protected, __объект - private    

class RedPanda(Panda):

    def __init__(self, weight):
        super().__init__(weight)
        self.__max_weight = 15
        self._color = "Brown"
        self._cute = True
        self._tail = True
    def eat(self):
        if self._can_eat(0.5):
            self._weight += 0.5
            print("Наелась и спит")
    
panda = Panda(20)
panda.eat()
panda.print_info()

redPanda = RedPanda(10)
redPanda.eat()
redPanda.print_info()
"""
*args — это сокращение от arguments (аргументы), 
**kwargs — это сокращение от keyword arguments (именованные аргументы).
"""