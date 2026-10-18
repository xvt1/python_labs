#task 1
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#     def info(self):
#         print(f'{self.width} × {self.height}: площа = {self.area()}, периметр = {self.perimeter()}')
#
# rectangle1 = Rectangle(5, 3).info()
# rectangle2 = Rectangle(10, 4).info()
#task 2
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#
#     def add_grade(self, grade):
#         if grade > 0 and grade <= 12:
#             self.grades.append(grade)
#         else:
#             print(f'Оцінка {grade} не додається')
#     def average(self):
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)
#     def __str__(self):
#         return f'{self.name}: {self.grades}, середній = {round(self.average(),2)}'
# student1 = Student('Ivan Petrenko')
# student1.add_grade(10)
# student1.add_grade(12)
# student1.add_grade(15)
# student1.add_grade(9)
# print(student1)
#task 3
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#
#     def add_grade(self, grade):
#         if grade > 0 and grade <= 12:
#             self.grades.append(grade)
#         else:
#             print(f'Оцінка {grade} не додається')
#     def average(self):
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)
#     def __str__(self):
#         return f'{self.name}: {self.grades}, середній = {round(self.average(),2)}'
#
# students = [
#     Student("Anna", [5,10,2,2,7]),
#     Student("Ivan", [5,10,12,12,7]),
#     Student("Olha", [12,11,11,11,11]),
#     Student("Nika", [12,11,11,11,11]),
#     Student("Sacha", [12,11,11,11,11]),
# ]
# studentsBestScore = []
# def findTheBestResult(score):
#     for student in students:
#         if student.average() == score:
#             studentsBestScore.append(student.name)
#     return studentsBestScore
#
# averageScore = []
#
# for student in students:
#     print(f'{student.name} - {student.average()}')
#     averageScore.append(student.average())
#
# print(f'Найкращий результат: {",".join(findTheBestResult(max(averageScore)))} - {max(averageScore)}')

#4
# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self,amount):
#         if amount <= 0:
#             print("Поповнення має бути більше за 0")
#         else:
#             self.balance += amount
#
#     def withdraw(self,amount):
#         if amount <= 0:
#             print("Зняття коштів має бути більшим за нуль")
#         elif amount > self.balance:
#             print("На рахунку не вистачає коштів")
#         else:
#             self.balance -= amount
#
#     def info(self):
#         print(f'{self.owner}: баланс: {self.balance}')
#
# ivan = BankAccount('Ivan',1000)
# ivan.deposit(500)
# ivan.withdraw(300)
# ivan.withdraw(2000)
# olha = BankAccount('Olha',700)
# olha.withdraw(200)
# olha.deposit(100)
#
# ivan.info()
# olha.info()