from t10_2_mikh import *
import time
import random

tank1 = DonateTank("КВ2", 30, 100, 200, 500)
tank1.print_info()

tank2 = Tank("Тигр", 40, 80, 150, 600)
tank2.print_info()

t = [1,2,3,4,5,6]

tanks = [i for i in t if i%2 == 0]
print(tanks)

tanks = [Tank("Tank" + str(i), 30, 100, 200, 500) for i in range(10)]
print(tanks)

for i in range(len(tanks)):
    tanks[i].shoot(tanks[random.randint(0, len(tanks)-1)])
