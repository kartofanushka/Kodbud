#===библиотеки и циклы===
# math – различные математические операции 
# time – работа со временем 
# tkinter – графический интерфейс 
# pygame – 2д игры 
# os – работа с операционной системой 
# 
import random
# random.seed(1) #даст предсказемый одинаковый результат
print (random.random()) #0--1
print (random.randint(1,10))
#+++++++++++
lst=[1,2,4,5,8,6]
print(random.choice(lst))#выбрать элемент списка

# time 36:05
import time
time1=time.time()
print(time1)
# time.sleep(2)
time2=time.time()
dif=time2-time1
time1=time.ctime(time1)
time2=time.ctime(time2)
print(time1, time2)
print(dif)
# # datetime
# print('datetime')
# import datetime
# st_time=datetime.timezone()
# # end_time=datetime.now()
# print(st_time)
# =============OS
print('===OS===')
import os
print(os.name)
print(os.getcwd)
print(os.listdir())
# .mkdir  #('name')
# .rename #('name', 'newname')
# .rmdir #remove directory
# .remove #remove file 9('1.txt')
# ====math===
import math
print(round(math.sin(30*math.pi/180),2))
# ===tkinter===