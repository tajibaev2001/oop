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