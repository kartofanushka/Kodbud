# def sum(integers):
#     result = 0
#     for i in integers:
#         result += i
#     print(result)

# list_ints = [1,2,3,4,5,6]
# sum(list_ints)

# def sum(a,b,*integers):
#     result = a+b
#     for i in integers: #цикл со счетчиком, который проходится по списку и принимает значения из него по очереди
#         result += i
#     print(result)

# sum(1,2,1)

# #kwargs - здесь аргументы должны быть с названиями
# #создается словарь - из названий - ключей и аргументов - значений
# def string_sum(*arg, **kwargs):
#     result = ""
#     print(kwargs)
#     for val in kwargs.values(): #.values - берет из словаря список только с его значениями, без ключей
#         result += val
#     print(result)
#     print(arg)

# string_sum(1,2,3,4, a="Hello. ", b="Kak dela ? ", c="Kak pogoda ? ", d="Azaza...")


# def price(*prices, **kwargs):
#     high = kwargs.get("highest_price", max(prices))
#     l = []
#     for price in prices:
#         if price < high:
#             l.append(price)
#     print(l)

# price(100, 500, 50, 100, highest_price = 300)


# def ab(a, b=5):
#     print(a+b)

# ab(1,3)

#ctrl + / - чтобы закомментировать выделенное
# at = [x for x in range(10)]
# print(at)

# at1 = []
# for i in range(10):
#     if i >3:
#         at1.append(i**3)
# print(at1)

# print([i**3 for i in range(10)])

# print([i**3 for i in range(10) if i>3 and i%5==0])

# print([i**3 if i > 3 else i for i in range(10)])

# print({x:len(x) for x in ["orange", "apple", "grapes", "watermellon"]})


# t = (1,2,3,4)
# print(t)
# #d = {[1,2,3]:"Hello"} - ошибка
# d = {(1,2,3):"Hello"}

# lonely = (1, )

# l = list(t)
# l.append(5)
# t = tuple(l)
# print(t)

# for i in t:
#     print(i)

# #самостоятельное задание
# #list compreneshion - генератор списка - который генирует список чисел кратных 30 или 31 в промежутке от - 0 до 500
# print([i for i in range(500) if i%30 == 0 or i%31==0])
# #*
# #Дан список целых чисел - нужно сделать из него кортеж уникальных чисел в обратном порядке
# #[1,2,3,4,5]
# # listt = [1, 2, 3, 4, 4, 5, 5]
# # tuplee = tuple(sorted(set(listt), reverse=True))
# # print(tuplee)
# l=[1,2,3,3,4,5]
# # l.sort(reverse=1)
# # t=tuple(l)
# # print (t)

# print(tuple([x for x in sorted(set(l), reverse=True)]))



# #**
# #Написать функцию split_numbers, которая принимает строку целых чисел, разделённых пробелами, и возвращает кортеж из этих чисел.
# s="1 2 3 4 5"
# l = s.split(" ")
# print(l)
# t = tuple(l)
# print(t)

# print(tuple(i for i in s.split(" ")))

is_nice = True

state = "nice" if is_nice else "not_nice"
print(state)

is_nice = False

state = "nice" if is_nice else "not_nice"
print(state)

age = 19

is_allowed_to_drive_in_Russia = True if age >= 18 else False
print(is_allowed_to_drive_in_Russia)
is_allowed_to_drive_in_Russia = age >= 18
print(is_allowed_to_drive_in_Russia)

val = None
if val:
    print(1)
if val == None:
    print(1)

def my_func(real_name, opt_display_name=None):
    display_name = opt_display_name or real_name
    print(display_name)

my_func("Mikhail")

my_func("Daniil","poprigunchik228")

# Задание 1 Дома вам нужно написать программу, которая принимает на вход 10 чисел и генерирует 
# два списка. Один с четными числами, второй с нечетными.

# Задание 2

# Создайте кортеж a = (5, 3, 2, 1, 4) и отсортируйте его по возрастанию. С помощью метода sorted. 
# После сортировки, а должен остаться кортежем, а не списком

