# a = 17391 / 17
# b = 546 / 17
# c = 934 / 17
# if a > b:
#     print(f"{a} больше {b}")
# elif c < b:
#     print(f"{c} меньше {b}")
# else:
#     print(f"{c} больше {b}")


# 1

# list1 = [3, 5, 2, 1, 4]
# list2 = [4, 2, 6, 8, 1]
# merged_list = list(set(list1 + list2))
# merged_list.sort()
# print("Объединенный и отсортированный список:", merged_list)

# 2
# lst = []
# for i in range(16):
#     lst.append(i)

# max_lst = max(lst)
# min_lst = min(lst)
# print(max_lst + min_lst)


# 3
# month = int(input("Введите номер месяца: "))
# if month == 12 or month == 1 or month == 2:
#     print("Сезон года: Зима")
# elif month >= 3 and month <= 5:
#     print("Сезон года: Весна")
# elif month >= 6 and month <= 8:
#     print("Сезон года: Лето")
# elif month >= 9 and month <= 11:
#     print("Сезон года: Осень")
# else:
#     print("Некорректный номер месяца")

# a = ["a", "e", "y", "u", "i"]
# strr = input("Введите слово")
# new = strr.split()

# for i in new:
#     if i[0].lower() in a:
#         print(i)                              


# list1 = [3, 5, 2, 1, 4]
# list2 = [4, 2, 6, 8, 1]
# a = list1 + list2
# b = set(a)
# a = list(b)

# print(a)

# num = []
# for i in range(1, 16):
#     num.append(i)
# print(min(num) + max(num))      

# a = int(input("Ведите число месяца -"))
# if a ==1 or a == 2 or a == 12:
#     print("Winter")
# elif a >= 3 and a <= 5:
#     print("Spring")
# elif a >= 6 and a <= 8:
#     print("Summer")
# elif a >= 9 and a <= 11:
#     print("Autumn")
# else:
#     print("Некорректный число месяца -")

# a = set()
# for i in range(5):
#     b = int(input("Ведите число :"))
#     a.add(b)

# print(min(a))

# try:
#     a = int(input())
#     b = int(input())
#     print(a / b)
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")
 
# try:
#     print(10 + '10')
# except TypeError:
#     print("Нельзя сложить число на строку")

# values = ['a', 'b', (4, 5), 'c']

# convertibility = []
# for item in values:
#     try:
#         set(item)
#         convertibility.append(True)
#     except TypeError:
#         convertibility.append(False)

# can_convert = all(convertibility)
# print("Можно ли конвертировать values в SET?", can_convert)
      

# user_input = input("Ведите Python фунцию:")

# try:
#     result = eval(user_input)
#     print("Результат выполнения фунции:")
# except NameError:
#     print("В Python нет такой финции")

# try:
#     my_list = [1, 2, 3, 4]
#     print(my_list[7])
# except IndexError:
#     print("Нет такого индекса")

# try:
#     if = 5 = 6:
#         print(5==6)
# except SyntaxError:
#     print("Возникла синтаксическая ошибка")

# while True:
#     try:
#         num1 = int(input())
#         a = input()
#         num2 = int(input())
#         if a == '+':
#             print(num1+num2)
#         elif a == '-':
#             print(num1-num2) 
#         elif a == '*':
#             print(num1*num2)
#         elif a == '/':
#             try:
#                 print(num1/num2)
#             except ZeroDivisionError:
#                 print("Нельзя делить на ноль")
#             finally:
#                 print("Yes")
#         elif a == '**':
#             print(num1**num2)
#         else:
#             print("Нет такого оператора")
#     except ValueError:
#         print("Ведите цифру")

# dict = {'name': 'Ilyaz', 'lastname': 'Tajibaev', 12 : 'age'}
# try:
#     for i in dict.keys():
#         a = i + "abc"
#         print(a)
# except TypeError:
#     print("Нельзя сложить  строку на число")

# file = open("new.txt", "w")
# file.write("Heloo, Words")

# file = open("new.txt", "a")
# file.write("Heloo, Words")
# # # s = file.read()
# # # print(s)
# file.close()

# login = input("Ведите логин: ")
# password = int(input("Ведите парол: "))
# with open("user.txt", "a", encoding="utf-8") as file:
#     file.write(f"Ваш логин- {login}, Ваш пароль- {password}\n")

# try:
#     with open("sueh.txt", "r") as file:
#         s = file.read()
#         print(s)
#         file.close()
# except FileNotFoundError:
#     print("Файл не найден")

# file_name = "new.txt"
# try:
#     with open(file_name, "r") as file:
#         text = file.read()

#         if "w" in text.lower():
#             print("Да, в тексте есть w")
#         else:
#               print("Нет, в тексте есть w")
# except FileNotFoundError:
#      print("Файл не найден")

# file_name = "user.txt"
# with open(file_name, "w") as file:
#     text = file.write("tkj jdh ruht jhu49")

# with open(file_name, "r") as file:
#     text = file.read()

# t_words = []
# for word in text.split():
#     if "t" in word.lower():
#         t_words.append(word)
      
# for word in t_words:
#     print(word)

# numbers = [12, 34, 54, 2, 23, 1]
# file_name  = "user.txt"
# with open(file_name, "w") as file:
#     for number in numbers:
#         file.write(str(number) + "\n")

# max_number = float("-inf")
# min_number = float("inf")

# with open(file_name, "r") as file:
#     for i in file:
#         number = int(i.strip())
#         max_number = max(max_number, number)
#         min_number = min(min_number, number)
# output_file = "result.txt"
# with open(output_file, "w") as file:
#    file.write("Максимальное число: " + str(max_number) + "\n")
#    file.write("Минимальное число: " + str(min_number) + "\n")
# print("Максимальное и минимальное число записан файл", output_file)

# import time
# password = 123456
# count = 3
# loged_in = False

# while count > 0:
#     user_input = int(input("Введите пароль"))
    
#     if user_input == password:
#         loged_in = True
#         break
#     else:
#         count -= 1
#         print("Неверный пароль.Повторите попытку")
#         time.sleep(5) 
# if loged_in:
#     print("Вход выполнен") 
# else:
#     print("У вас не осталось попыток")