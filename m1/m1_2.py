marks =[1,2,3,4,5,5,5,6,7,8,9,10,11,12,13,14,15]
print (marks)
print (marks[0])
print (marks [1:15:2]) #вывели из всех каждый второй
ls = [1, "stroka", 1.5, True] #можно делать списки с разными типами данных, но не надо
count_5=marks.count(5) # считаем сколько элементов "5"
print(ls,count_5)

#вложенный список
print (["Ivan","Mikhail"],[5,5])
#добавить эл в список
ls.append (3000)
print(ls)
#MIn
print(min(marks))
import random
print (random.choice(marks))
p=[5,3,8,6,1,5]
p.sort()
print (p)
p=list("dfgjoiv") #создать список иг набора букв
print('sort')#сортировка
p.sort()
print (p)
p.sort(reverse=True)
print (p)
print('average')
print(int(sum(marks))/int(len(marks)))
# удалить эл-т списка
del marks [1] #удалили 1й эл-т
print (marks)
marks.remove (10) #удалили цифру 10
print (marks)
a= marks.pop(7) #вырезать и присвоить переменной
print (marks)
print (a)
ser={1,5,4,5,7,8,9,6,5,4,6,4,7} #set выделяяет тошлько уникальные эл-ты
print (ser)
# min()
# max()
# sum()
# len()
# p.sort()
# p.index()
# p.clear()
# p.copy()
# list()
# Python List Methods

# Python has a set of built-in methods that you can use on lists.

# MethodDescription
# append() Adds an element at the end of the list
# clear() Removes all the elements from the list 
# copy() Returns a copy of the list
# count() Returns the number of elements with the specified value
# extend()Add the elements of a list (or any iterable), to the end of the current list
# index() Returns the index of the first element with the specified value
# insert() Adds an element at the specified position
# pop() Removes the element at the specified position
# remove() Removes the item with the specified value
# reverse() Reverses the order of the list
# sort() Sorts the list
# ======!!!======
arr =[1,2,3]
arr2=arr
arr.append(159)
arr.insert(1,135)
print(arr)
print(arr2)
# /============
read=open('logins.txt','r', encoding="utf-8")
lines=read.read().splitlines()
read.close()
for i in lines:
    # print((i))
    if lines.index(i) %2==0:
        print('log: '+ i)
    else :
        print('pass: '+ i)

