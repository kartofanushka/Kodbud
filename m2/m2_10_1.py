from t10_2 import *
import time

tank1 = DonateTank("КВ2", 30, 100, 200, 500)
tank1.print_info()

tank2 = Tank("Тигр", 40, 80, 150, 600)
tank2.print_info()

tanks=[i for i in range(10)if i%2==0]
print(tanks)

tanks =[Tank("Tank"+str(i), 30,100,200,500)for i in range(10)]
print(tanks)

for i in range (len(tanks)):
    tanks[i].shoot(tanks[random.randint(0,len(tanks)-1)])
    
# while tank1.health !=0 and tank2.health != 0:
#     tank1.shoot(tank2)
#     if tank1.health==0:
#         break
#     tank2.shoot(tank1)
#     if tank2.health==0:
#         break
#     time.sleep(0.5)
# tank2.print_info()
# tank1.print_info()