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

# from math import pi

# class Shape:
#     def __init__(self, name):
#         self.name = name

#     def area(self):
#         pass

#     def fact(self):
#         return "I am a two-dimensional shape."
    
# class Square(Shape):
#     def __init__(self, length):
#         super().__init__("Square")
#         self.length = length

#     def area(self):
#         return self.length**2
    
#     def fact(self):
#         return "Square have each angle equal to 90 degrees."
    
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius

#     def area(self):
#         return pi*self.radius**2

# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius

#     def area(self):
#         return pi*self.radius**2
    
# a = Square(4)
# b = Circle(7)
# print(b)
# print(b.fact())
# print(a.fact())
# print(b.area())

# class Nikola:
#     def __init__(self, name, age):
#         self.name = self._process_name(name)
#         self.age = age

#     def _process_name(self, name):
#         if "Николай" not in name:
#             return "Я не " + name + " а Николай"
#         return name
# nik = Nikola("Николай", 25)
# print(nik._process_name("Максим"))        


# class Phone:
#     username = "Kate"
#     __how_many_times_turned_on = 0

#     def call(self):
#         print("Rin-ring")

#     def __turn_on(self):
#         self.__how_many_times_turned_on += 1
#         print("Times waas turbed on", self.__how_many_times_turned_on )

# my_phone = Phone()
# my_phone.call()
# my_phone._Phone__turn_on()
# my_phone._Phone__how_many_times_turned_on
# print(my_phone._Phone__how_many_times_turned_on)

# class Person:
#     def __init__(self, name):
#         self.__name = name
#         self.__age = 1

#     def set_age(self, age):
#         if 1 < age < 110:
#             self.__age = age
#         else:
#             print("Не допустимый возраст")
    
#     def get_age(self):
#         return self.__age
    
#     def get_name(self):
#         return self.__name
    
#     def display_info(self):
#         print(f"Имя: {self.__name}\tВозраст: {self.__age}")

# tom = Person("Tom")
# tom.display_info()


# class ShoppingCar:
#     def __init__(self):
#         self.__items = []

#     def add_item(self, item):
#         self.__items.append(item)
           
#     def remove_items(self, item):
#         if item in self.__items:
#             self.__items.remove(item)

#     def get_items(self):
#         return self.__items 
    
#     def claer_items(self):
#         self.__items = []
# c = ShoppingCar()
# c.add_item("Обувь")
# c.add_item("Худи")
# c.remove_items("Обувь")
# print(c.get_items())
                     

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length * self.width

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return 3.14 * self.radius**2

# # shape = Shape()  # Нельзя создать экземпляр абстрактного класса

# rectangle = Rectangle(4, 6)
# circle = Circle(5)

# print(rectangle.area())  # Выводит: 24
# print(circle.area())     # Выводит: 78.5

# from abc import ABC, abstractmethod  
# class Car(ABC):  
#     @abstractmethod
#     def mileage(self):  
#         pass 
 
# class Tesla(Car):  
#     def mileage(self):  
#         print("The mileage is 30kmph")  

# class Suzuki(Car):  
#     def mileage(self):  
#         print("The mileage is 25kmph")  

# class Duster(Car):  
#    def mileage(self):  
#         print("The mileage is 24kmph ")  
 
# class Renault(Car):  
#     def mileage(self):  
#         print("The mileage is 27kmph ")  
 
# # Driver code  
# t= Tesla ()  
# t.mileage()  
 
# r = Renault()  
# r.mileage()  
 
# s = Suzuki()  
# s.mileage() 
 
# d = Duster()  
# d.mileage()

# from abc import ABC, abstractmethod
# class Absclass(ABC):
#     def print(self,x):
#         print("Passed value: ", x)
#     @abstractmethod
#     def task(self):
#         print("We are inside Absclass task")

# class test_class(Absclass):
#     def task(self):
#         print("Мы внутри задачи test_class")

# class example_class(Absclass):
#     def task(self):
#         print("Мы внутри задачи example_class")

# #object of test_class created
# test_obj = test_class()
# test_obj.task()
# test_obj.print(10)

# # #object of example_class created
# example_obj = example_class()
# example_obj.task()
# example_obj.print(200)

# print("test_obj is instance of Absclass? ", isinstance(test_obj, Absclass))
# print("example_obj is instance of Absclass? ", isinstance(example_obj, Absclass))

# class Car:
#     def __init__(self, make, model, mileage):
#         self._make = make
#         self._model = model
#         self.mileage = mileage
    
#     def get_info(self):
#         return self._make
    
#     def get_info(self):
#         print(f{self.__model})
    
#     def get_info(self):
#         print(self.mileage)
    
# car = Car("tayota", "supra", "The mileage is 300km")
# car.get_info()
# car.get_info()
# car.get_info()

# class Banknote:
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return f"Банкнот {self.value} сом"
    
#     def __eq__(self, object):
#         if object is None and not isinstance(object, Banknote):
#             return False
#         return self.value == object.value
    
#     def __lt__(self,object):
#         if object is None and not isinstance(object, Banknote):
#             return False
#         return self.value < object.value
#     def __gt__(self, object):
#         if object is None and not isinstance(object, Banknote):
#             return False
#         return self.value > object.value
    
#     def __le__(self, object):
#         if object is None and not isinstance(object, Banknote):
#             return False
#         return self.value <= object.value
    
#     def __ge__(self, object):
#         if object is None and not isinstance(object, Banknote):
#             return False
#         return self.value >= object.value
    
# class Wallet:   
#     def __init__(self, *banknotes:Banknote):
#         self.conteiner = []
#         self.conteiner.extend(banknotes)
#         self.index = 0
#     def __str__(self):
#         return f"Wallet {self.conteiner}"
    
#     def __contains__(self, item):
#         return item in self.conteiner
    
#     def __bool__(self):
#         return len(self.conteiner) > 0
    
#     def __len__(self):
#         return len(self.conteiner)

#     def __call__(self):
#         return f"{sum(i for i in self.conteiner)} money"
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if 0 <= self.index < len(self.conteiner):
#             value = self.conteiner[self.index]
#             self.index += 1
#             return value
#         raise StopIteration
    
#     def __getitem__(self, item: int):
#         if item < 0 and item > len(self.conteiner):
#             raise IndexError
#         return self.conteiner[item]
     
#     def __setitem__(self, key: int, value: Banknote):
#         if key < 0 and key > len(self.conteiner):
#             raise IndexError
#         self.conteiner[key] = value


# b = Banknote(100)
# c = Banknote(100)
# w = Wallet(1000, 2000, 3000, 4000)
# # if w:
# #     print("yes")
# # else:
# #     print("no")
# # # print(10 in w)
# # print(len(w))
# # print(w())
# # for i in w:
# #     print(i)
# # print(w[0])
# w[0] = 100
# print(w)

# class Baseclass:
#     def test(self):
#         print("Baseclass")

# class Mixin:
#     def testing(self):
#         print("Mixin")

# class Myclass(Mixin, Baseclass):
#     pass

# obj = Myclass()
# obj.test()
# obj.testing()
class Entity:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

class SquareMixin:
    def add_size(self, size_x):
        self.size_x = size_x
        self.size_y = size_x

    def perimeter(self):
        return self.size_x * self.size_x
    
    def square(self):
        return self.size_x * self.size_x
    
class SquareEntity(SquareMixin, Entity):
    pass
square = SquareEntity(5, 4)
square.add_size(500)
print(square.size_x)
print(square.size_y)
print(square.square())
print(square.perimeter())

