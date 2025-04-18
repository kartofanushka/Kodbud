import random
import time

class Tank:
    def __init__(self, model, armor, min_damage, max_damage, health):
        self.model = model
        self.armor = armor
        self.damage = random.randint(min_damage, max_damage)
        self.health = health

    def print_info(self):
        print(f"{self.model} имеет лобовую броню {self.armor}мм при {self.health}ед. здоровья и урон в {self.damage} единиц")
        print("-------------------------")

    def health_down(self, enemy_damage):  # урон, который танк получил
        self.health -= enemy_damage - enemy_damage / self.armor
        print(f"{self.model}: Командир, по экипажу {self.model} попали, у нас осталось {round(self.health)} ед. здоровья")
        print("-------------------------")

    def shoot(self, enemy):  # враг в которого танк стреляет
        try:
            if enemy.health >= 0:
                enemy.health_down(self.damage)
            if enemy.health <= 0:
                enemy.health = 0
                print(f"{self.model}: Танк {enemy.model} уничтожен.")
                print("-------------------------")
        except:
            print("something went wrong")

class DonateTank(Tank):
    def __init__(self, model, armor, min_damage, max_damage, health):
        super().__init__(model, armor, min_damage, max_damage, health)
        self.forceArmor=True
    def health_down(self, enemy_damage):  # урон, который танк получил
        if self.forceArmor==True:
            self.health-= enemy_damage/2
        else:
            self.health -= enemy_damage - enemy_damage / self.armor
        print(f"{self.model}: Командир, по экипажу {self.model} попали, у нас осталось {round(self.health)} ед. здоровья")
        print("-------------------------")

    
tank1 = DonateTank("КВ2", 30, 100, 200, 500)
tank1.print_info()

tank2 = Tank("Тигр", 40, 80, 150, 600)
tank2.print_info()

while tank1.health !=0 and tank2.health != 0:
    tank1.shoot(tank2)
    tank2.shoot(tank1)
    time.sleep(0.5)
tank2.print_info()
tank1.print_info()
# """

class A:
    def one(self):
        print(1)
    def two(self):
        print(2)
class B(A):
    pass
    # или переназначить 
    # def one(self):
    #     print("one")
    # def two(self):
    #     print("two")
b=B()
    
b.one()
b.two()
a=A()

    

    


#  как у миджорни Mijourney
    
"""
class Human:
    def __init__(self, name,color_of_hair, height,weight):
        self.name = name
        self.color_of_hair=color_of_hair
        self.height=height
        self.weight=weight
    def breath(self):
        print(f"{self.name} breathing")
ivan=Human("Ivan","red",190,60)
dima=Human("Dmitri","blue",170,90)

class Boxer(Human):
    # инит можно не писать, но если хотим добавить
    # доп параметры то пишем через супер, иначе будет конфликт. 
    def __init__(self, name, color_of_hair, height, weight, damage, gloves):
        super().__init__(name, color_of_hair, height, weight)
        self.damage=damage
        self.gloves=gloves
    
    pass
boxer=Boxer(height=190, color_of_hair="red",name="Bob", weight=100)
print(boxer.height)
boxer.breath()



# """
        