# class Hello:
#     def  __init__(self, name, age, hair):
#         self.name = name
#         self.age = age
#         self.hair = hair
#     def info(self):
#         print(f"My name is {self.name}, I am {self.age} yesars old, My hair is {self.hair}")
# hello = Hello("Ilyas", 21, "shirt") 
# hello.info()
# person2 = Hello("Asan", 22, "long")
# person2.info()

# import math

# class Math:
#     def  __init__(self, a):
#         self.a = a 
    
#     def perimetr(self):
#         return self.a * 4
    
#     def squear(self):
#         return self.a ** 2
    
#     def diogonal(self):
#         res = (self.a ** 2 + self.a ** 2)
#         res2 = math.sqrt(res)
#         return res2
    
# mathh = Math(5)
# print(mathh.diogonal())
# print(mathh.perimetr())
# print(mathh.squear())

# class Rectangle():
#     def __init__(self, width, heigth):
#         self.width = width
#         self.heigth = heigth

#     def get__area(self):
#         area = self.width * self.heigth
#         return f"Площадь прямоугольника {area}"
# persona = Rectangle(3, 4)
# print(persona.get__area())

# class Car:
#     def __init__(self, brend, model):
#         self.brend = brend
#         self.model = model

#     def get_info(self):
#         print(f"{self.brend}, {self.model}")
# persona = Car("Tayota","supra")
# persona.get_info()

# class Circle():
#     def  __init__(self, radius):
#         self.radius = radius

#     def get_circumference(self):
#         return 2 * 3.14 * self.radius

#     def get_area(self):
#         return 3.14 * self.radius ** 2
    
# c = Circle(5)
# print(c.get_circumference())
# print(c.get_area())    


# class Bank():
#     def __init__(self, name, money=0):
#         self.name = name
#         self.money = money

#     def plus(self, amount):
#         self.money += amount

#     def minus(self, amount):
#         if self.money >= amount:
#             self.money -= amount
#         else:
#             print(f"Недостаточно средств ")

#     def get_money(self):
#         print(f"Name - {self.name}, money - {self.money}")

# bank = Bank("Bayel")
# bank.plus(500)
# bank.plus(600)
# bank.minus(300)
# bank.get_money

# class Student:
#     def __init__(self, name):
#         self.name  = name
#         self.baa  = []

#     def student_baa(self, num):
#         self.baa.append(num)

#     def student_info(self):
#         if len(self.baa) > 0:
#             return sum(self.baa) / len(self.baa)
#         else:
#             return 0
# s = Student("Bayel")
# s.student_baa(5)
# s.student_baa(5)
# s.student_baa(5)
# s.student_baa(5)
# print(s.student_info())
