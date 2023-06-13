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

# class Bus:
#     def __init__(self, name):
#         self.name = name
    
#     def driving(self):
#         print(f"The {self.name} is driving")

# class Car(Bus):
#     def hunk(self):
#         print("Beep, beep!")

# car = Car("BMW")
# car.driving()
# car.hunk()

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display_info(self):
#         print(f"Name - {self.name}")
#         print(f"Salary - {self.salary}")

# class Manager(Employee):
#     def __init__(self, name, salary, depertament):
#         super().__init__(name, salary)
#         self.depertament = depertament

#     def display_info(self):
#         super().display_info()
#         print(f"Depertament - {self.depertament}")

# emp = Employee("jon", 4000)
# manager = Manager("Aygerim", 6000, "Sale")
# emp.display_info()
# print("-----------")
# manager.display_info()

# class Animal:
#     def sound():
#         pass

# class Cat(Animal):
#     def sound(self):
#         print("Мяу-мяу")
    
# class Dog(Animal):
#     def sound(self):
#         print("Гав-гав")

# def make_sound(animal):
#     animal.sound()

# dog = Dog()
# cat = Cat()

# make_sound(dog)
# make_sound(cat)

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass

# class Cat(Animal):
#     def speak(self):
#         return "Мяу, Мяу"

# class Dog(Animal):
#     def speak(self):
#         return "Гав, Гав"

# dog = Dog("Beka - ")
# cat = Cat("Aman - ")

# print(dog.name, dog.speak())
# print(cat.name, cat.speak())

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age) 
#         self.student_id = student_id  

#     def display_info(self):
#          print(f"Имия: {self.name}, Возраст: {self.age}, Номер студента: {self.student_id}") 

# person = Person("Bayel", 19)
# student = Student("Bayel", 19, 703361024)
# student.display_info()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)   
#         self.student_id = student_id
        
# student = Student("Jack", 20, '12')
# print(f"Имя: {student.name}")             
# print(f"Возраст: {student.age}")
# print(f"Номер студента: {student.student_id}")

# class Horse():
#     isHorse = True

# class Donkey():
#     isDonkey = True

# class Mule(Horse, Donkey):
#     pass

# mule = Mule()
# print(mule.isHorse)
# print(mule.isDonkey)

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"I am cat, My name is {self.name}, I am {self.age} years old")

#     def make_sound(self):
#         print("Meow")

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"I am dog, My name is {self.name}, I am {self.age} years old")

#     def make_sound(self):
#         print("Bark")
# cat1 = Cat("Kitty", 2.5)
# dog1 = Dog("Fluffy", 4)

# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()

from math import pi

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."
    
class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2
    
    def fact(self):
        return "Square have each angle equal to 90 degrees."
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius

#     def area(self):
#         return pi*self.radius**2
    
a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())