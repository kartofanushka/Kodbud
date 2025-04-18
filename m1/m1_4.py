#Условный оператор
# =====================

# повторение
# temp=[]
# import random
# for i in range(7):
#     a = random.randrange(25,40)
#     temp.append(a)
# print (sum(temp)/len(temp))
# ++++++++++++++++++++

# else основной вариант
# elif любые дрегие варианты

# == равно
# != не равно
# > < >= <= равно всегда справа
# and or логическое и (оба условия, пересечение) илогическое или (хотябы одно из условий)

# weather='cold'
# perc='rain'
# if weather=='hot' and perc=='rain':
#     print("coat")
# elif weather=='cold' or  perc=='sunny':
#     print('naked')
# else:
#     print('....')


# a1=input('solve problem x=1+2')
# if int(a1)==3:
#     print('correct')
# else:
#     print('try again')    

# if "a"<"b":
#     print('asas')


# import random
# a=random.randint(1,10)
# b=int(input('input number 1-10: '))
# if a==b:
#     print('OK!')
# elif a+1==b or a-1==b:
#     print('you were very close, but NO', a)    
# else:
#     print('fail', a)

#задаем число, сумма первого и последнего знака равны второму, ок
# import random
# a=random.randint(100,999)
# # a=253
# a=str(a)
# # print(al)
# al=list(map(int,a))
# summa=al[0]+al[2]
# if summa==al[1]:
#     print('OK!')   
# else:
#     print('try more', a)
    
# казино
import random
points=0
if random.randint(1,10) ==5:
    print ('10%')
elif random.randint(1,100) ==5:
    print ('1%')
elif random.randint(1,20) ==5:
    print ('5%')
elif random.randint(1,4) ==4:
    print ('25%')
elif random.randint(1,2) ==2:
    print ('50%')
    
for i in range(1000):
    if random.randint(1,100)==5:
        print("1%")
        points +=1
print(points)