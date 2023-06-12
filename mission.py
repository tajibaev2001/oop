# def info(name, salary=5000):
#      return f"{name} - {salary}"

# name = "Asan"
# salary = 10000
# result = info(name, salary)
# print(result)

# def generate_list():
#     num = int(input())
#     my_list  = []
#     for i in range(1, num+1):
#         my_list.append(i)
#     return my_list

# print(generate_list())

# lst = [4, 7, 2, 9, 9, 2, 4, 5, 6]
# list1 = set(lst)
# list1.intersection()
# list2 = list(list1)
# print(list2)

# numbers = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
# for i in range (len(numbers) - 1):
#     a = numbers[i]
#     b = numbers[i+1]
#     sum = a + b
#     print(sum)

# from datetime import datetime

# current_time = datetime.today()
# print(current_time.time())

# import time

# for i in range(10):
#     time.sleep(5)
#     print(i)

# names = ['Jyldyz', 'Aigerim', 'Bekmamat', 'Nurbek', 'Azamat','Shirin']


# print(names[2:5])

# list = ['Ilyaz', 'Asan', 'Alya', 'Aygerim']
# list2 = ""
# a = list2.join(list)
# print(a)

# set = {5, 6, 7, 8, 3, 9}
# set.add(1)
# set.pop()
# print(set)

# for i in range(1,10):

#     # if i == 5:

#         print(i)

#     # else:

    #     print("Unkown Number")




# import os 
# import shutil

# def register():
#     login = input("Введите логин: ")
#     password = input("Введите пароль: ")
#     photo_path = input("Введитие путь до фото: ")
    
#     if os.path.exists(photo_path):
#         _,photo_split = os.path.splitext(photo_path)
#         valid_photo_split = ['.jpeg', '.jpg', '.png']
        
#         if photo_split.lower() in valid_photo_split:
#             photo = f"registred_foto/{login}{photo_split}"   
            
#             shutil.copyfile(photo_path, photo)
            
#             with open("database.txt", 'a') as file:
#                 file.write(f"{login}:{password}:{photo}\n")
#             print("Регистрация успешна завершена")
        
#         else:
#             print("Неподдерживаемое расширение фотографии. Регистрация отменена")
#     else:
#         print("Фото не найдено. Регистрация отменена")        
        
# os.makedirs('registred_foto', exist_ok=True)

# register()

# def aritfmetic():
#     num1 = int(input())
#     num3 = input()
#     num2 = int(input())
#     if num3 == "+":
#         return num1 + num2
#     elif num3 == "-":
#         return num1 - num2
#     elif num3 == "*":
#         return num1 * num2
#     elif num3 == "/":
#         return num1 / num2
#     else:
#         print("Неизвестная операция")
# print(aritfmetic())

# r = int(input("Введите цифру "))
# res1 = r * 4
# res3 = r**2 + r**2
# res4 = r**2
# print(f"Периметр- {res1}")
# print(f"Диоганаль {res3}")
# print(f"Квадрат {res3}")

# import math
# def square(a):
#     p = a * 4
#     s = a ** 2
#     d = (a ** 2) + (a ** 2)
#     d2 = math.sqrt(d)
#     print(f"Переметр - {p}, Плошадь - {s}, Диоганаль - {round(d2, 1)}")

# a = int(input())
# square(a)

# import os
# import shutil

# def image():
#     image1 = input()
#     image2 = input()
#     if os.path.exists(image1) and os.path.exists(image2):
#         shutil.copyfile(image1, image2)
#     else:
#         if not os.path.exists(image1):
#             print(f"Файл {image1} отсуствует")
#         if not os.path.exists(image2):
#             print(f"Файл {image2} отсуствует")

# image()


# def bank_depos():
#     a = int(input("Введите вклад - "))
#     b = int(input("На сколько лет ? "))
#     res = b *(a / 100 * 10)
#     print(round(res))
# bank_depos()

# def is_prime():
#     a = int(input("Ведите число "))
#     b = 1000
#     c = 0
#     if c <= a <= b:
#         print(True)
#     else:
#         print(False)
# is_prime()
    
# is_nice = True
# state = "nice" if is_nice else "not_nice"
# print(state)

# nice = True
# personality = ("вредная", "добрая")[nice]
# print("кошка", personality)

# user = int(input())
# state = "chatnyi" if user % 2 == 0 else "nechatnyi"
# print(state) 
    
# num = int(input())
# res = ("no", "yes")[num % 2 == 0]
# print(res)

# def palindrom(x):
#     if len(x)<=1:
#         return True
#     if x[0] != x[-1]:
#         return False
#     return palindrom(x[1:-1])

# print(palindrom("нан"))

# def rec(w):
#     if len(w) == 1 or len(w) == 2:
#         return w
#     return w[0] + "(" + rec(w[1:-1]) + ")" + w[-1]
# w = input()
# print(rec(w))

# def search_find(str1, str2):
#     if str1.lower() in str2.lower():
#         print("Есть контакт")
#     else:
#         print("Мимо")
# str1 = "Ilyaz"
# str2 = "IlyazTajibaev"
# search_find(str1, str2)

# def  biggest_dict(**kwargs):
#     my_dict = {'first_one': 'we can do it'}
#     my_dict.update(kwargs)
#     return my_dict
# print(biggest_dict(name = 'Ilyaz', lasname = 'Tajibaev', age = 22))
    

# list1 = [5, 10, 15, 20, 25, 50, 20]
# a = list1.index(20)
# list1[a] = 200
# print(list1)

# aList = [1, 2, 3, 4, 5, 6, 7]
# res = []
# for i in aList:
#     res.append(i**2)
# print(res)
   
# list = [5, 20, 15, 20, 25, 50, 20]

# def removeValue(sampleList, val):
#    return [value for value in sampleList if value != val]
# resList = removeValue(list, 20)
# print(resList)

# letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
# list = ""
# for i in letters:
#     if not i.isupper():
#         list += i
# letters = list
# print(letters)

# numbers = [1, 2, 3, 4, 5, 1, 2, 3]
# list1 = set(numbers)
# # list1.intersection()
# # list2 = list(list1)
# print(list1)

# import random

# def arit(c):
#     a = random.randint(20, 30)
#     b = random.randint(1, 20)
#     if c == "+":
#         print(a + b)
#     elif c == "-":
#         print(a - b)
#     elif c == "*":
#         print(a * b)
#     elif c == "/":
#         print(a / b)
#     else:
#         print("Неизвестная операция")
#     print(f"Перовое число - {a}, Второе число - {b}")
# c = input()
# arit(c)
      
          