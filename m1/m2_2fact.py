# facts =['Хамелеон', 'змея', 'коала', 'медведь']
# #print(facts)
# action = int(input("input number 1-4"))
# print (facts[action-1])

# задача сос редним . преобразование типа данных списка
# st=list("5465612897")
# # st= [int(i) for i in st]
# # or
# st=list(map(int,st))
# print(st)
# print(min(st))
# print(max(st))
# print(sum(st))
# print(st.count('5'))
# print('aver')
# print(int(sum(st))/int(len(st)))

# =========ДОМАШКА
# lst=[2,5,3]
# # lst.reverse() #это в принте не работет, только в 2 строки
# print(lst[::-1])

# Дан список из 5 элементов: [1, 2, 3, 4, 5]. Найдите сумму этого списка. Решите задачу двумя способами.
# lst= [1, 2, 3, 4, 5]
# print (sum(lst))
# print(1+2+3+4+5)

# Составьте список покупок минимум из 5 пунктов. И проделайте следующие операции:
# 1.Добавьте еще один пункт
# 2.Замените 2 пункт на новый
# 3.Выведите на экран длину списка
# 4.Отсортируйте список по алфавиту
# 5.Удалите последний пункт списка

facts =['Хамелеон', 'змея', 'коала', 'медведь','картоха']
facts.append ('лук')
print('1:',facts)
facts[1]='новвая змея'
print('2:',facts)
print('3:',len(facts))
print('4:',sorted(facts))
del facts [len(facts)-1]
print('5:',facts)