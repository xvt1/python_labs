#task 1
# from math import *
# import random
#
# def circleArea(radius):
#     area = ceil((pi * radius ** 2)*100)/100
#     return area
#
# def hypotenuse(a, b):
#     с = ceil(sqrt(a ** 2 + b ** 2) * 100) / 100
#     return с
#
# def needPackages(items,packages):
#     needPackages = ceil((items / packages))
#     return needPackages
#
# #тест для перевірки площи круга(перевірка функції circleArea())
# def test1():
#     if(circleArea(5) == 78.54):
#         print("test 1 (r = 5): Passed")
#     else:
#         print("test 1 (r = 5): Failed")
#
#     if(circleArea(0) == 0.0):
#         print("test 1(r = 0): Passed")
#     else:
#         print("test 1(r = 0): Failed")
#
# #тест для перевірки
# def test2():
#     if(hypotenuse(6, 8) == 10):
#         print("test 2 (6,8): Passed")
#     else:
#         print("test 2 (6,8): Failed")
#
# #тест для перервірки функції needPackages()
# def test3():
#     if(needPackages(25,6) == 5):
#         print("test 3 (25,6): Passed")
#     else:
#         print("test 3 (25,6): Failed")
#
# #запуск всіх тестів для перевірки
# def startTests():
#     test1()
#     test2()
#     test3()
# startTests()
#
# def main():
#     r = int(input("Ведість Радіус: "))
#     a, b = map(int, input("Ведіть катети через кому(Приклад: 6,8): ").split(","))
#     items = int(input("Вкажіть к-сть предметів: "))
#     packages = int(input("Ведіть к-сть в упаковці: "))
#     print(f'Площа круга: {circleArea(r)}')
#     print(f'Гіпотенуза: {hypotenuse(a, b)}')
#     print(f'Потрібно упаковок: {needPackages(items, packages)}')
#
# if __name__ == '__main__':
#     main()
# import random
# import statistics
#
# def generateGrades(n):
#     grades = []
#     for i in range(n):
#         grades.append(random.randint(1,12))
#     return grades
#
# def findGradesDiapson(grades):
#     g = 0
#     for i in grades:
#         if i > 9 and i < 13:
#             g += 1
#     return g
#
#
# def test2():
#     test_grades = [9, 10, 11, 12]
#
#     result = findGradesDiapson(test_grades)
#
#     if result == 3:
#         print("Test 2 (Diapason): Passed")
#     else:
#         print(f"Test 2 (Diapason): Failed! Очікували 3, але функція повернула {result}")
#
#
# def test1():
#     grades = generateGrades(10)
#     if len(grades) == 10:
#         print("Test 1 (10): Passed")
#     passedNumbers = 0
#     for i in range(len(grades)):
#         if grades[i] > 0 and grades[i] < 13:
#             passedNumbers += 1
#     if passedNumbers == len(grades):
#         print("Test 1 (grades): Passed")
#     else:
#         print("Test 1 (grades): Failed")
#
# def main():
#     n = int(input("N = "))
#     grades = generateGrades(n)
#     print(f'Оцінки: {grades}')
#     print(f'Min: {min(grades)}')
#     print(f'Max: {max(grades)}')
#     print(f'Середнє: {statistics.mean(grades)}')
#     print(f'Медіана: {statistics.median(grades)}')
#     print(f'Оцінок від 10-12: {findGradesDiapson(grades)}')
#
# if __name__ == '__main__':
#     test1()
#     test2()
#     main()
# import datetime
#
# def current_date(date_str):
#     year, month, day = date_str.split('-')
#     return datetime.date(int(year), int(month), int(day))
#
# def days_until_day(day1,day2):
#     diferent = day1 - day2
#     return diferent.days
#
# def test2():
#     date1 = current_date('2008-10-30')
#     date2 = current_date('2008-11-31')
#     if(days_until_day(date1,date2) == 31):
#         print("Test 1: Passed")
#     else:
#         print("Test 1: Failed")
#
# def test1():
#     if(current_date('2000-01-01') == datetime.date(2000, 1, 1)):
#         print("Test 1 : Passed")
#     else:
#         print("Test 1 : Failed")
#
# def main():
#     date = input("Ведіть сьогоднішу дату(Наприклад 2026-12-31): ")
#     days = days_until_day(current_date(date),datetime.date.today())
#     if(days < 0):
#         print(f'Пройшло днів: {abs(days)}')
#     elif(days > 0):
#         print(f'До події залишилося: {days}')
#     elif(days == 0):
#         print(f'цей день сьогодні')
#
# if __name__ == '__main__':
#     test1()
#     test2()
#     main()

