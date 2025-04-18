# Очень простая задача

# Что нужно сделать:

# У вас есть список numbers. Напишите программу, которая заполняет список числами от 0 до 100 и выводит его на экран.
# numbers =[]
# for i in range(101):
#        numbers.append(i)
# print(numbers)
# Животные 2

# Что нужно сделать:

# Напишите программу, которая принимает сначала 3 названий животных, а потом 3 описаний для животных. После чего случайным образом выбирает одно описание и одного животного и выводит 3 разных комбинации.

# Пример ввода: Кот Мохнатый

# Пример вывода:

# Мохнатый кот
"""
# типа надо все через циклы
animals=[]
features=[]
for i in range(3):
       animals.append(input("Ж"+str(i+1)))
       print(animals)
for i in range(3):
       features.append(input("features"+str(i+1)))
       print(features)
import random
for i in range(3):
       print(random.choice(animals),random.choice(features))
   """    
#  это не зачли
# animals =['dog','cat','pig']
# features=['black','red','pink']
# import random
# print(random.choice(animals),random.choice(features))

# Случайности не случайны
# Что нужно сделать:
# Напишите программу, которая заполняет список случайными числами от 0 до 5 (30 итераций). После этого посчитайте количество пятерок в списке.
"""
numbers =[]
import random
for i in range(30):
       numbers.append(random.randint(0,5))
print("Число \"5\" встречается ", (numbers.count(5)), "раза в списке:")
print (numbers)"""