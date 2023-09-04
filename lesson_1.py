# однострочный комментарий
"""
многострочный комментарий
int (integer) целые числа -45 23 0
float (float) вещественные(дробные) 3.0 3.14 -5521.92
str (string) строки 'hello' "142"
bool (boolean) True(правда) False(ложь)
None (NoneType) (ничего,пустота)
dict(словарь) list(список) tuple(кортеж) set(множества)
Арифметические операции: +(сложение) -(вычитание) *(умножение) /(деление)
//(целочисленное деление) %(деление с остатком) **(возведение в степень)
Переменные:
нельзя использовать русские символы,
не можем использовать символы вспомогательные *?%$
не можем начинать имя переменной с цифры 1_place
не можем использовать зарезервированые функции int float print input
*************************************************************
world_map (snake case)
worldMap (camel case)
Age
speed
data_network
"""


# динамическая типизация

# some_str_1 = "hello"
# some_str_2 = "world"
# some_int = True

# some_str = 3.14
# some_value_a = 31  # операция присваивания
# some_value_b = 22
# result = some_value_a + some_value_b
# value_int, b = 1, 5 + 52
# some_str = ""
# some_value_1, some_value_2 = int(input("enter some value:")), int(input("enter some value:"))
# some_value_3, some_value_4 = map(int, input("enter values: ").split())
# some_value_3, some_value_4 = 4, 5
# print(some_value_3,"+", some_value_4,"=",some_value_3 + some_value_4)  # функция вывода информации
# print("hello world")

# price = 389
#
# print(price//100)
# print(price % 100 // 50)
# print(price % 50 // 10)
# print(price % 10)

# дано натуральное число вывести следующее за ним чётное натуральное число
# 3 -> 4   3 % 2 ==>  3 - 1 + 2
# 4 -> 6   4 % 2 ==>  4 - 0 + 2
# number =int(input("enter number:"))
# print(number - number % 2 + 2)

# дано четырёхзначное число проверить все ли цифры равны
# 4554  8972 5555
# number = 4444
# print(not number % 1111)

# height = int(input("height:"))
# up = int(input("up:"))
# down = int(input("down:"))
# days = (height - up - 1) // (up - down) + 2
# print(days)
# логические выражения и условный оператор
# True False
# >(больше) <(меньше) >=(больше или равно) <=(меньше или равно) ==(равно) !=(не равно)
# and (и) or(или) not(не)
# True 1 -2 -4 5 "hello" False 0 ""

# print(number_3 > number_1  and number_1 > number_2)
# number_1 = 6
# number_2 = 1
# number_3 = 7
# if number_3 < number_2:  # check(проверка)
#     print("this is true")
#     print("good idea")
# else:
#     print("this is false")
#     print("not good idea")
#
# print("end")
# вывести положительное ли число
# number = float(input("enter number:"))
#
# if number > 0:
#     print("positive")
#     if not(number > 9 and number < 100 and number % 2 == 0):
#         print("two sing")
# elif number == 0:
#     print("zero")
# else:
#     print("negative")
# triangle task

# a = int(input())
# b = int(input())
# c = int(input())
# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("равносторонний")
#     elif a == b or a == c or b == c:
#         print("равнобедренный")
#     else:
#         print("разносторонний")
# else:
#     print("не существует такого треугольника")
# str unmutable
#               -5  -4 -3 -2 -1

# slice[begin:end:step]
#                012345678910

# print(id(some_string_1))

# print(some_string_1.count("o",3,5))
# print(some_string_1.find("o"))
# print(some_string_1.replace("o","all",1))
# print(some_string_1.lower().islower())
# print(some_string_1.swapcase())
# print(some_string_1.isalpha())
# print(some_string_1.isalnum())
# print(some_string_1.isdigit())
# print(some_string_1.capitalize())
# print(some_string_1.split(","))
#
# for elem in some_string_1:
#     print(elem)
# range(start,end,step)
# range(start,end) => step = 1
# range(end) => start = 0 , step = 1
# for ind in range(len(some_string_1)):
#     print(ind,some_string_1[ind])
# in - принадлежит
# not in - не принадлежит

# some_string_1 = "hello,world cat"
# # print("ol" in some_string_1)
# count = 0
# for elem in some_string_1:
#     if elem in "aeyuioAEYUIO":
#         print(elem,ord(elem))
#         count = count + 1 # -= *= /= //= %= **=
# print(count)

# str_1 = ""
# print(ord(str_1))
# name = "AleX"
# age = 27
# print("name:",name, "age:", age)
# print(f"name: {name} age: {age}")
# print("name: {} age: {}".format(name,age))
# print("name: %s age: %d" % (name,age))
# numb_1 = int(input())
# numb_2 = int(input())
# print(numb_1 > numb_2)
# some_str = "hello python"
#
# last_ind = len(some_str)
# print(last_ind)
# for ind in range(last_ind):
#     if some_str[ind] == 'l':
#         print(some_str[ind])
#     else:
#         print(some_str[ind],"- this is no l")
# поэлементный перебор
# for elem in some_str:
#     print(elem)

# range(end) range(3) 0 1 2
# range (start,end) range(4,8) 4 5 6 7
# range (start,end,step) range(4,11,2) 4 6 8 10
# for numb in range(8,4,-1):
#     print(numb)
# цикл for c параметром(вы знаете конечное число повторение)
# цикл while с условием(вы не знаете конечное число повторение)

# while (условие):
# ....тело цикла

# end = 1
# start = 100
# while start >= end: # True/False
#     if start % 2 == 0:
#         print(start)
#     else:
#         numb = start ** 2
#         print(numb)
#     start -= 1

# money = int(input("enter money:"))
# count_goods = 0
#
# while True:
#     print("money you have:",money)
#     price = int(input("enter price:"))
#     if price > 200:
#         print("big price:",price)
#         continue
#     if price > money:
#         break
#     money -= price
#     count_goods += 1
#
# print("ostatok:", money)
# print("count goods:",count_goods)

# summa = 0
# flag = True
#
# while flag:
#     number = int(input("enter number:"))
#     if number == 0:
#         break
#     if number == 404:
#         flag = False
#     summa += number
# else:
#     print("цикл не был завершён досрочно")
#
# print("summa:",summa)

# проверить является ли число простым
# 2 3 5 7 11 13
# 5 % 1 == 0 True
# 5 % 2 == 1 False
# 5 % 3 == 2 False
# 5 % 4 == 1 False
# 5 % 5 == 0 True


# number = int(input("enter number:"))
# delitel = 2
# # 0 - False
#
# while delitel < number // 2 + 1:
#     if not number % delitel:
#         print(number," - is not simple")
#         break
#     delitel += 1
# else:
#     print(number,"- is simple")
# тернарный оператор - просто if в одну строку
# то что выполняется if (условие верно) else что-то выполняется
# number = int(input())
# print("чётное" if number % 2 == 0 else "нечётное")

# 0 - False
# 2
# 6
# for number in range(2, 101):
#     delitel = 2
#     while delitel < number // 2 + 1:
#         if not number % delitel:
#             break
#         delitel += 1
#     else:
#         print(number)
# задачи на строки. Дана строка - вывести все слова разделёные пробелом на новой строке
# вывести самое длинное слово
# "dsakd dasd    a  dsad   as  asd"
# "dsads" True "" False


# some_str = input("enter sting:") + " "
#
# max_length_word = ""
# len_max_word = 0
# word = ""
# for ind in range(len(some_str)):
#     if some_str[ind] != " ":
#         word += some_str[ind]
#     elif word:
#         if len(word) > len_max_word:
#             max_length_word = word
#             len_max_word = len(word)
#         word = ""
#
# print(f"max lenght word is {max_length_word}. it's length is {len_max_word}")
# 0 2        9 11        18  22
# sda        dsa          dasd          asdads

# 13.	Удалить в строке все буквы 'b', непосредственно за которыми идет цифра.
# das bsda addab2  dsad asdasdbb2dsa

# text = input("enter word:")
# new_word = ""
# ind = 0
# while ind < len(text):
#     if text[ind] == "b" and text[ind + 1].isdigit():
#         ind += 1
#     new_word += text[ind]
#     ind += 1
# print(new_word)
#
# text.replace()

# text = "dsad dasd a dasda"
# for ind,elem in enumerate(text):
#     print(ind,elem)
# str int bool float None
# tuple(кортежи) list(списки) set(множества) dict(словари)

# tup1 = 3
# print(tup1)
#      0  1  2     3       4     5        6      7
# tup = (3, 3, 1, True, "hello", None, (3, 2, 6), 8,)
# some_tup = 23,
# print(id(some_tup))
# tup_str = tuple(some_tup)
# print(id(tup_str))
# tup_1 = (1,2,3)
# tup_2 = (1,2)
# print(id(tup_1))
# tup_3 = tup_2+(3,)
# tup_4 = (1,2,3) * 1
# print(tup_3)
# print(tup_1 is tup_3)
# print(tup_4))
# print(tup.index(True,4))
# if (3,2,6) in tup:
#     print("(3,2,6) in our tuple")
# summa = 0
# for ind,elem in enumerate(tup):
#     # if isinstance(elem,int):
#     #     summa += elem
#     if type(elem) is int:
#         summa += elem
#
#     print(ind,type(elem))
# print(summa)
# some_str = "hello"
# some_numb = 3
# some_tup = (some_str,some_numb)
# print(some_tup)

# exp = 22
# tup = (48, 92, 16, 11, 81, 33, 85, 23)
# max_el = max(tup)
# max_ind = tup.index(max_el)
# print(sum(tup))

# max_el = tup[0]
# max_ind = 0
# for ind in range(len(tup)):
#     if max_el < tup[ind]:
#         max_el = tup[ind]
#         max_ind = ind
# print(max_ind,max_el)
# tup = tuple()
# print(tup.__sizeof__())
# lst = list()
# print(lst.__sizeof__())
#      0   1     2       3       4    5     6
# lst = [-51, 62, 2, -10, 19]
# tup = (2, 6, [2, 6, 2], 7)
# tup[2].clear()
# print(tup)
# lst.append(5)# добавляет в конец
# lst.insert(1,89)# добавляет на определённую позицию
# lst[2] = 7.8
# elem = 4
# if elem in lst:
#     lst.remove(elem)
# ind = 8
# if len(lst) > ind:
#     del_elem = lst.pop(8)
# del lst[1:5]
# print(lst)
# lst_test = (8,)
# # lst.extend(lst_test)
# lst += lst_test
# lst2 = lst.copy()
# lst2 = lst[:]
# lst.pop()
# print(lst)
# print(lst2)
# lst.sort(key=lambda elem: abs(elem) % 10)
# print(lst)
# lst = []
# for i in range(5):
#     elem = int(input(f"enter elem {i+1}:"))
#     lst.append(elem)
# print(lst)
# list comprehension
# [что хотим добавить for из чего in итерабельный объект]
# [что хотим добавить for из чего in итерабельный объект если условие верно]
# [что хотим добавить if условие верно else что хотим добавить for из чего in итерабельный объект]
# lst = [int(input(f"enter elem {i+1}:")) for i in  range(5)]
# lst.sort()
# print(lst)
# print([i**2 for i in (10,3,7,2)])
# lst = []
# for elem in (10,3,7,2):
#     if elem % 2 == 0:
#         lst.append(elem**2)
#     else:
#         lst.append(elem/3)
# print(lst)
# print([i**2 for i in (10,3,7,2) if i % 2 == 0])
# print([i ** 2 if i % 2 == 0 else i / 3 for i in (10, 3, 7, 2)])
# print([int(i) for i in input().split()])
#         0       1       2
#       0 1 2   0 1 2   0 1 2
# lst = [[5,2,6],[2,2,6],[6,2,7]]
# lst = []
# for i in range(3):
#     lst.append([])
#     for j in range(3):
#         elem = int(input(f"enter elem for row {i}:"))
#         lst[i].append(elem)
# for row in range(len(lst)):
#     print(lst[row])
# print([[int(input(f"enter elem for row {i}:")) for j in range(3)]
#        for i in range(3)])

# множества(set) хэш-таблица
# mutable(изменяемые) list,set,dict
# unmutable(не изменяемые) int float str NoneType tuple bool,frozenset,frozendict

# set_2 = set() пустое множество

# for elem in set_1:
#     print(elem)

# set_1.update([3,2,-8])
# set_1.add(22)
# set_1.remove(21)
# elem = set_1.pop()
# set_2 = set_1.copy()
# set_1.discard(21)
# set_1 = set()
# tup_1 = ()
# lst_1 = []
# set_2 = {"hello", 24, 7, 0, 9}
# set_3 = {"hello", 24, 1, 6, 10}
#
#
# print("union:",set_1.union(set_2))
# print(set_2 | set_3)
# print("difference set_1:",set_1.difference(set_2))
# print(set_1 - set_2)
# print("difference set_2:",set_2.difference(set_1))
# print(set_2 - set_1)
# print("symmetric_difference:",set_1.symmetric_difference(set_2))
# print(set_2 ^ set_1)
# print("intersection:",set_1.intersection(set_2))
# print(set_3 & set_2)
# print(set_1.issubset(set_2))
# print(set_2.issuperset(set_1))
# print(set_1.isdisjoint(set_2))
# print(set_1.__sizeof__())
# print(tup_1.__sizeof__())
# print(lst_1.__sizeof__())
# print()

# lst = [2, 2, 8, 2, 2, 2, 5, 2, 2]
# ind = 0
# while ind < len(lst):
#     if lst.count(lst[ind]) != 1:
#         del lst[ind]
#         continue
#     ind += 1
# print(lst)
# dict (словари) ассоциативный массив (ключ,значение)
# key - unmutable
# value - любое
#          key           value
# phone = {"Pavel": "+375(29)3452312", "Anna": "+375(29)3452309"}

# print(phone.keys())
# print(phone.values())
# phone["Sarah"] = "+375(29)3452311" # add key:value
# phone["Pavel"] = "+375(29)3452333" # change value
# phone.update({"Irina":"+375(29)3452322","Oleg":"+375(29)3452132"})
# phone.update([("Egor","+375(29)3952322"),("Mixail","+375(29)4952322")])
# value = phone.pop("Tom")
# value = phone.get("Tom","not user in phone")
# value = phone["Tom"]
# value = phone.popitem()
# print(phone.items())
# del phone["Sarah"]
# print(phone)
# for name in phone:
#     print(name,phone[name])

# for name,value in phone.items():
#     print(name,value)
# friends_numbers = {input("enter name:"): input("enter phone our friend:") for i in range(3)}
# for i in range(5):
#     name = input("enter name:")
#     if name not in friends_numbers:
#         value = input("enter phone our friend:")
#         friends_numbers[name] = value
# print(friends_numbers)
# lst = [(3, 2, 5), 2, "7", 8, 3.19, 3.22]
# print(bool(float))
# print({elem: elem ** 2 for elem in lst if type(elem) == int or type(elem) == float})
# print({elem: elem ** 2 for elem in lst if isinstance(elem,(int,float))})
# lst_keys = [3, 2, 5]
# lst_value = [8, 3, 2]
# some_dict = dict(zip(lst_keys,lst_value))
# print(some_dict)
# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)
#
# products = {
#     "orange": {
#         "wash": 8.99,
#         "pol": 9.11,
#     },
#     "apple": {
#         "ant": 1.67,
#         "kr": 2.22,
#     }
# }
# print(products["orange"]['wash'])
# set_1 = {1,6,2}
# set_1 = frozenset(set_1)
# print(set_1)
# lst = list(set_1)
# print(lst)
# lst = [5, 2, 6, 1, 5, 2]
# # O(N)
# for el in lst:
#     print(el)
#
# # O(N)
# for el in lst:
#     print(el)
#
# # O(N) + O(N) = O (N+N) = O(2N) = O(N)
#
# for ind in range(len(lst)):
#     if lst[ind] in lst:
#         print(lst[ind], "yes")
#
# # (O(N)+O(1)) * O(N) = O (NxN) = O(N*N)
#
# lst_2 = [[2, 4, 1], [2, 3, 1], [2, 4, 5]]
# for

# some_dnk = input("input some data:").lower() + " "
# dnk = ""
# count = 1
# for ind in range(1,len(some_dnk)):
#     if some_dnk[ind-1] == some_dnk[ind]:
#         count += 1
#     else:
#         dnk += some_dnk[ind-1] + str(count)
#         count = 1
# print(dnk)
# 17.	Дано число n. Определить первую цифру этого числа

# number = int(input("enter number:"))
# while number >= 10:
#     number //= 10
# print(number)
# cows
# cows = int(input("enter cows:"))

# for cow in range(1,cows+1):
#     if cow % 10 == 1 and cow % 100 != 11:
#         print(f"на лугу {cow} корова")
#     elif (cow % 10 == 2 and cow % 100 != 12) or \
#          (cow % 10 == 3 and cow % 100 != 13) or \
#          (cow % 10 == 4 and cow % 100 != 14):
#         print(f"на лугу {cow} коровы")
#     else:
#         print(f"на лугу {cow} коров")

# Дан кортеж.
# Найти максимальную по длине монотонную последовательность
# ( убывающую или возрастающую) чисел.
#
# tup = (5, 2, 6, 5, 7, 8)
# count = 1
# max_count = 1
# for ind in range(1, len(tup)):
#     if tup[ind - 1] < tup[ind]:
#         count += 1
#         if max_count < count:
#             max_count = count
#             ind_l = ind
#     else:
#         count = 1
#
# print(tup[ind_l + 1 - max_count:ind_l + 1])
# Дан кортеж. Без функций и дополнительных списков вывести все
# повторяющиеся элементы. (count не использовать)

# tup = (5, 2, 6, 5, 7, 8, 2, 5, 2)
#
# for ind in range(len(tup)):
#     if tup[ind] in tup[ind + 1:] and tup[ind] not in tup[:ind]:
#         print(tup[ind])

# dct = {}
# while True:
#     text = input()
#     if text == ".":
#         break
#     text_list = text.split("-",maxsplit=1)
#     key,value = text_list[0],text_list[1]
#     dct[key] = value
# print(dct)
# print([i for i in range(1,11)])
# names = ["Kolya","Vasya","Vasya","Kate"]
# ages = [14,15,18,19]
# print(set(names))
# print(dict(zip(names,ages)))

# функции(процедуры)
# функциональный
# ООП
# DRY don't repeat yourself
# # - много кода
# # - сложно редактировать
# # - увеличивается количество возможных ошибок
# # - ухудшается читабельность

#
# def greeting_for_my_friend(name: str, age: int = 24) -> tuple:
#     print("=================")
#     print(f"Hello {name.title()} your age is {age}")
#     print("=================")
#     return name.title(), age + 1
#
#
# name, age= greeting_for_my_friend("tom")
# # greeting_for_my_friend(age=30, name="Kate")
# print(name, age)
# global scope
# enclosing scope
# some_value = 5
# summa = 2
# some_lst = [4,2,5]
# print(some_lst)
# a = 2
#
#
# def some_fun():
#     # local scope
#     b = a
#     b += 2
#     print(b)
#
#
# some_fun()
# print(a)

# def fun(some_value, name=23, *args, some_value_2, **kwargs):
#     print(some_value)
#     print(f"name {name}")
#     print(args)
#     print(some_value_2)
#     print(kwargs)
#
# friends = {"Tom":32131231,"Kate":48129412}
# some_tup = (5,2,5,1)
#
# fun(34, 24, 5, 2,*some_tup, some_value_2=6, name_1="Oleg", age=23,**friends)

# def sort_args_lst(elem):
#     if elem % 2 == 0:
#         return elem

# lst = [5, 2, 6, 1]
# lst = sorted(lst,key=lambda elem:elem % 2 == 0)
# print(lst)
# fun = lambda *args: tuple([elem**2 for elem in args])
# print(fun(4,2))

# some_str = """
#     '''hello world'''
#     dsad dasd dasdas
#     #dasdasdasda\n
#     #dasdasfasgas\n
#     '''
#     #dasdasdas
#     dasdas
#     '''
# """
# print(some_str)
# def fun(arg_1, arg_2) -> int:
#     if isinstance(arg_2, int):
#         if arg_1 > arg_2:
#             return arg_1
#         return arg_2
#     return arg_1

# def find_max_elem(lst: list) -> int:
#     lst = format_lst(lst)
#
#     max_el = lst[0]
#     for elem in lst:
#         if elem > max_el:
#             max_el = elem
#     return max_el
#
# def format_lst(lst: list) -> list:
#     ind = 0
#     while len(lst) - 1 > ind:
#         if isinstance(lst[ind], int):
#             ind += 1
#         else:
#             del lst[ind]
#     return lst
#
#
# data = [5, 22, "4", 10, (9,), 1]
#
# max_el = find_max_elem(data)
#
# print(max_el)

# max_el = data[0]
#
# for elem in data:
#     max_el = fun(max_el, elem)
#
# print(max_el)

# def fun(**kwargs):
#     print(kwargs)
#
#
# fun(val_1=5, val_2=2, val_3=6)

# function map, filter,reduce

# val_1= [int(i) for i in input().split()]

# def square_lst(elem):
#     return elem ** 2
#
#
# #
# # val_1 = list(map(int, input().split()))
# lst = [5, 2, 6, 1, 77]
# lst = list(map(lambda elem: elem ** 2, lst))
#
# print(lst)
# lst = [5, 6, 8, 16, 18]
# new_lst = list(map(lambda elem: elem ** 2, filter(lambda elem: elem > 15, lst)))
# print(new_lst)

# from functools import reduce
#
# print(reduce(lambda x, y: x if x > y else y, [8, 2, 3, 4, 5]))
# closures(замыкания) decorators(декораторы) recursion

# local enclosing global  build-in
# def fun_1():# объемлющая функция (wrapper)
#     # enclosing scope
#     x = 10
#     print("fun 1")
#     def fun_2():#вложенная функция (inner)
#         # local
#         nonlocal x
#         x += 1
#         print("x in fun 2 is:",x)
#     fun_2()

# fun_1()
# def wrapper(a):
#     def inner():
#         nonlocal a
#         a += 1
#         return a
#     return inner
#
# fun_inner = wrapper(4)
#
# print(fun_inner())
# print(fun_inner())
# print(fun_inner())

# def decorator_1(fun):
#     def inner_1():
#         print("inner_1 begin")
#         fun()
#         print("inner_1 end")
#     return inner_1

# def decorator(fun):
#     def inner(value):
#         print("inner begin")
#         res = fun(8)
#         print("inner end")
#         return res + 1
#
#     return inner
#
#
# @decorator
# def some_fun(value):
#     return value
#
#
# print(some_fun(4))

# from datetime import datetime
#
#
# def not_during_the_night(func):
#     def wrapper():
#         if 8 <= datetime.now().hour < 21:
#             func()
#         else:
#             pass  # Тише, соседи спят!
#
#     return wrapper
#

# def say_whee():
#     print("Ура!")
#
#
# # say_whee = not_during_the_night(say_whee)
# say_whee()

# def info(arg1, arg2):
#     print('Decorator arg1 = ' + str(arg1))
#     print('Decorator arg2 = ' + str(arg2))
#
#     def the_real_decorator(function):
#         def wrapper(*args, **kwargs):
#             print('Function {} args: {} kwargs: {}'.format(function.__name__, str(args), str(kwargs)))
#             return function(*args, **kwargs)
#
#         return wrapper
#
#     return the_real_decorator
#
# @info(3,"python")
# def doubler(number):
#     return number * 2


# decorator = info(3, 'Python')(doubler)
# print(decorator(5))

# decorator_function = info(3, 'Python')
# actual_decorator = decorator_function(doubler)
# # Вызываем декорированную функцию
# print(actual_decorator(5))
# print(doubler(5))

# local enclosing global build-in

# # определение функции декоратора
# def select(input_func):
#     print()
#     n = 1
#     def output_func():  # определяем функцию, которая будет выполняться вместо оригинальной
#         print("*****************")  # перед выводом оригинальной функции выводим всякую звездочки
#
#         nonlocal  n
#         n += 1
#         print(n)
#         input_func()  # вызов оригинальной функции
#         print("*****************")  # после вывода оригинальной функции выводим всякую звездочки
#
#     return output_func  # возвращаем новую функцию
#
#
# # определение оригинальной функции
# @select  # применение декоратора select
# def hello():
#     print("Hello METANIT.COM")
#
#
# # вызов оригинальной функции
# hello()
# hello()
# hello()

# FILE  text/binary
# documentaition, logs

# open file
# to do some
# close file
# w(write) rewrite data r(read) read data a(append) write back file x
# w+ r+ a+ wb ab rb rb+ ab+ wb+ x+ xb+

# file = open("C:/Users/Denis/PycharmProjects/py91/test_file.txt",mode="a+",encoding="UTF-8")
# file.seek(0,0)
# data = file.read()
# file.close()
# # data = data.replace("\n"," ")
# data = list(map(int,data.split("\n")))
# print(data)
# with open("C:/Users/Denis/PycharmProjects/py91/test_file.txt",mode="r",encoding="UTF-8") as file:
#     students = {}
#     data = list(map(lambda line:line.rstrip(),file.readlines()))
#     print(data)
#     file.seek(0,0)
#     for line in file:
#         student = line.split()
#         students[student[0]] = int(student[1])
#     print(students)

# CSV comma separate value

# import csv

# some_lst = [[5, 2, 6, 1, 6, 2, 7, 2, 1],[4,2,4,5,1,25,2],[4,2,5,6,2,5,2,1]]
#
# with open("test_csv.csv","a",encoding="UTF-8",newline="") as csv_file:
#     csv_obj = csv.writer(csv_file,delimiter=";")
#     # csv_obj.writerow(some_lst)
#     csv_obj.writerows(some_lst)

# with open("test_csv.csv","r",encoding="UTF-8",newline="") as csv_file:
#     csv_obj = csv.reader(csv_file, delimiter=";")
#     lst = []
#     for elem in csv_obj:
#         numbers = list(map(int,elem))
#         lst.extend(numbers)
#
#     print(lst)

# import json
#
# some_dict = {
#     "firstName": "Joe",
#     "lastName": "Jackson",
#     "gender": "male",
#     "age": 28,
#     "address": {
#         "streetAddress": "101",
#         "city": "San Diego",
#         "state": "CA"
#     },
#     "phoneNumbers": [
#         {
#             "type": "home",
#             "number": "7349282382"
#         },
#         {
#             "type": "workphone",
#             "number": "73421412"
#         }
#     ]
# }
#
# serialize_dict = json.dumps(some_dict)
# print(serialize_dict)
# desirialize_data = json.loads(serialize_dict)
# print(type(desirialize_data))
# ===============================================
# desirialize data fom file
# with open("sample2.json", "r") as json_file:
#     person_info = json.load(json_file)
#     print(person_info['address']['streetAddress'])
# serialize data to json
# with open("smith_info.json", "w") as json_file:
#     json.dump(some_dict, json_file, indent=4)
# some_data = {
#     42351: ("John", 25),
#     12461: ("Peter", 28),
#     66666: ("Marty", 21),
# }
# person;42351;John;25
# person;66666;Marty;21
# person;12461;Peter;28

# from datetime import datetime
# import time
#
#
# def elapsed(func):
#     def wrapper(a, b, delay=0):
#         start = datetime.now()
#         func(a, b, delay)
#         end = datetime.now()
#         elapsed = (end - start).total_seconds() * 1000
#         print(f'>> функция {func.__name__} время выполнения (ms): {elapsed}')
#
#     return wrapper
#
#
# @elapsed
# def add_with_delay(a, b, delay=0):
#     a = a ** b
#     time.sleep(delay)
#
#
# print('старт программы')
# add_with_delay(10, 2000)
# add_with_delay(10, 2000000)
# print('конец программы')


# class Human:
#     # class attrs
#     LEGS = 2
#     COUNT_HUMAN = 0
#     HUMAN_INFO_LIST = []
#
#     def __init__(self, name: str, age: int, legs: int = 2):  # конструктор(инициализатор)
#         self.legs = legs
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def count_human(cls, name, age):
#         human = cls(name, age)
#         cls.COUNT_HUMAN += 1
#         cls.info(human)
#         cls.human_info(human)
#         return human
#
#     @classmethod
#     def human_info(cls, human):
#         cls.HUMAN_INFO_LIST.append(human)
#
#     @staticmethod
#     def weather_today(weather = None):
#         if weather == 'sunny':
#             print("weather is sunny")
#         elif weather == "rainy":
#             print("weather is rainy")
#         else:
#             print("what are you want for me???")
#
#     def info(self):
#         print(f"Human {self.name} age is {self.age}")
#
#     def set_age(self, age):
#         self.age = age
#
#     def get_age(self):
#         return self.age
#
#
# # Vasya = Human(name="Vasya", age=29)  # создали объект(экземпляр) класса instance
# # Petya = Human("Petya", 22)
# # Human.info(Petya)
#
# human_1 = Human.count_human("Vasya", 29)
# human_2 = Human.count_human("Petya", 21)
#
# Human.weather_today()
# human_1.weather_today("sunny")

# Human.HUMAN_INFO_LIST[0].info()
# class Car:
#     def __init__(self, model="BMW", color="black",motor ="DIESEL"):
#         self.model = model # public attr
#         self._color = color # protected attr
#         self.__motor = motor # private attr
#
#     def __info(self):
#         print(f"model {self._color} {self.model} motor: {self.__motor}")
#
#     def method_example(self):
#         self.__info()
#
#
# bmw = Car()
# bmw.model = "Audi"
# bmw._Car__info()

# class Human(object):
#     # def __new__(cls, *args, **kwargs):
#     #     print("new obj create")
#     #     return super().__new__(cls)
#
#     # def __init__(self, name, age):
#     #     self.name = name
#     #     self.age = age
#
#     def info(self):
#         print(f"method info Human")

# def __str__(self):
#     return f"name {self.name} age {self.age}"
#
# def __del__(self):
#     print("del work")
#     del self

# def __repr__(self):
#     return f"{self.__dict__}"


# class Student(Human):
#     def __init__(self, name, age, mark):
#         # Human.__init__(self, name, age)
#         super().__init__(name, age)
#         self.mark = mark
#
#     def info_student(self):
#         super().info()
#         print(f"mark {self.mark}")


# class Car():
#     def info(self):
#         print("info method car")
#         Human.info(self)
#
# class Driver(Car, Human):
#     def info(self):
#         super().info()
#         print("method info driver")

# student = Student("Vasya", 22, 9.2)
# student.info_student()

# human = Human("Vasya",25)
# print(human)
# human.info()
# del human
# human.info()

# class F:
#     pass
#
#
# class D:
#     pass
#
#
# class E:
#     pass
#
#
# class B(D, E):
#     pass
#
#
# class C(D, F):
#     pass
#
#
# class A(B,C , F):
#     pass

#
# driver = Driver()
# driver.info()

# полиморфизм
# class Alive:
#     def live(self):
#         print("some live")
#
#
# class Dog(Alive):
#     def dog_live(self, var_1, var_2=None):
#         if var_2:
#             print(f"{var_1} {var_2}")
#         else:
#             print(f"{var_1}")
#
#
# class Cat(Alive):
#     def cat_live(self):
#         print("cats live")
#
#
# cat = Cat()
# dog = Dog()
# animals = [cat, dog]
#
# dog.dog_live(2)
# for animal in animals:
#     if isinstance(animal, Dog):
#         animal.dog_live()
#     elif isinstance(animal, Cat):
#         animal.cat_live()
#     else:
#         animal.live()

# from abc import ABC, abstractmethod
#
#
# class Weapon(ABC):
#     @abstractmethod
#     def shoot(self):
#         print("something use")
#
#     def some_method(self):
#         pass
#
#
# class Gun(Weapon):
#     def shoot(self):
#         print("bax")
#
#
# class Automat(Gun):
#     def shoot(self):
#         print("bax bax bax")
#
#
# class Knife(Weapon):
#     def shoot(self):
#         print("vjoox")
#
#
# class Player:
#     def shoot(self, weapon: Weapon):
#         print(f"player got {weapon}")
#         weapon.shoot()
#
#
# # weapon = Weapon()
# # weapon.shoot()
# tokarev = Gun()
# tokarev.shoot()
# ak_47 = Automat()
# ak_47.shoot()
#
# knife = Knife()
# knife.shoot()
#
# player = Player()
# player.shoot(ak_47)

# метакласс

# def some_method(self,x):
#     print(x)
#
# Bar = type('Bar', (), dict(attr=100,attrs2=0,some_method=some_method))
# bar = Bar()
# bar.some_method(12)


# -=================================2========================================
# def find_possible_sums(numbers, target_sum):
#     def backtrack(index, path, current_sum):
#         if current_sum == target_sum:
#             possible_combinations.append(path[:])
#             return
#         if current_sum > target_sum or index == len(numbers):
#             return
#
#         for count in range(3):
#             if current_sum + count * numbers[index] <= target_sum:
#                 for _ in range(count):
#                     path.append(numbers[index])
#                 backtrack(index + 1, path, current_sum + count * numbers[index])
#                 for _ in range(count):
#                     path.pop()
#
#     possible_combinations = []
#     backtrack(0, [], 0)
#     return possible_combinations
#
#
# required_amount, bill_numbers = map(int,input().split())
# banknote_denominations = list(map(int,input().split()))
# combinations = find_possible_sums(banknote_denominations, required_amount)
# if combinations:
#     print(len(combinations[0]))
#     print(combinations[0])
# else:
#     print(1)


# =============================1================================

#
# def can_get_winning_sequence(n, start_sequence, win_sequence):
#     for i in range(n):
#         for j in range(i,n+1):
#             part_sort_seq =start_sequence[:i] + sorted(start_sequence[i:j]) + start_sequence[j:n]
#             if part_sort_seq == win_sequence:
#                 return "YES"
#     return "NO"
#
# n = int(input())
# start_sequence = list(map(int, input().split()))
# win_sequence = list(map(int, input().split()))
# result = can_get_winning_sequence(n, start_sequence, win_sequence)
# print(result)

#====================================3==========================================

# def count_states(x, roads, n):
#     # Создаем массив для хранения представления штатов в виде дерева
#     state_repr = list(range(n))
#
#     # Функция для поиска представителя штата
#     def find_state_repr(state):
#         if state_repr[state] != state:
#             state_repr[state] = find_state_repr(state_repr[state])
#         return state_repr[state]
#
#     # Сортируем дороги по длине в порядке убывания
#     roads.sort(key=lambda road: -road[2])
#
#     # Итерируемся по всем дорогам и уничтожаем их, если их длина больше x
#     for u, v, w in roads:
#         if w > x:
#             repr_u, repr_v = find_state_repr(u - 1), find_state_repr(v - 1)
#             if repr_u != repr_v:
#                 state_repr[repr_u] = repr_v
#
#     # Считаем количество уникальных представителей штатов
#     unique_states = set()
#     for i in range(n):
#         unique_states.add(find_state_repr(i))
#
#     return len(unique_states)
#
#
# def find_optimal_x(n, m, roads):
#     # Начальные значения для бинарного поиска
#     left, right = 1, max(road[2] for road in roads)
#
#     while left < right:
#         mid = (left + right) // 2
#         states_count = count_states(mid, roads, n)
#
#         # Если количество штатов увеличилось или осталось неизменным, уменьшаем верхнюю границу
#         if states_count <= n:
#             right = mid
#         else:
#             left = mid + 1
#
#     return left
#
#
# # Ввод данных
# n, m = map(int, input().split())
# roads = [list(map(int, input().split())) for _ in range(m)]
#
# # Находим оптимальное значение x
# optimal_x = find_optimal_x(n, m, roads)
#
# # Выводим результат
# print(optimal_x)
#===================================================4=====================================================
#
# class DSU:
#     def __init__(self, n):
#         self.parent = list(range(n))
#         self.size = [1] * n
#
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
#
#     def union(self, x, y):
#         root_x = self.find(x)
#         root_y = self.find(y)
#         if root_x != root_y:
#             if self.size[root_x] < self.size[root_y]:
#                 root_x, root_y = root_y, root_x
#             self.parent[root_y] = root_x
#             self.size[root_x] += self.size[root_y]
#
#     def get_size(self, x):
#         root_x = self.find(x)
#         return self.size[root_x]
#
#
# n, m = map(int, input().split())
# dsu = DSU(n)
# answers = []
#
# for _ in range(m):
#     query = input().split()
#     if query[0] == '1':
#         x, y = map(int, query[1:])
#         dsu.union(x - 1, y - 1)
#     elif query[0] == '2':
#         x, y = map(int, query[1:])
#         answers.append("YES" if dsu.find(x - 1) == dsu.find(y - 1) else "NO")
#     elif query[0] == '3':
#         x = int(query[1])
#         answers.append(str(dsu.get_size(x - 1)))
#
# for ans in answers:
#     print(ans)



























