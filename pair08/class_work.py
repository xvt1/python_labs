# while True:
#     try:
#         grade = int(input("Enter your grade 1... 12: "))
#         if grade < 1 or grade > 12:
#             raise ValueError("Grade must be between 1 and 12")
#         print("Your grade is ", grade)
#         break
#     except ValueError as error:
#         print(f'Error: {error}')
from pptx import parts

# def int_input(message):
#     while True:
#         try:
#             return int(input(message))
#         except ValueError:
#             print('Please enter a number.')
# count = int_input("Please enter your count: ")
# print(count)
#
# def input_grade():
#     while True:
#         try:
#             grade = input("Enter your grade 1-12: ")
#             if grade < 1 or grade > 12:
#                 raise ValueError("Grade must be between 1 and 12")
#             return grade
#         except ValueError as error:
#             print(error)
# grade = input_grade()
# print("Прийнято", grade)

# students = ["Anna","Ivan", "Sophyie"]
#
# try:
#     index = int(input("Enter index of student: "))
#     print(students[index])
# except ValueError:
#     print("Invalid index")
# except IndexError:
#     print("nema takogo elementa")

# price = {
#     "apple":100,
#     "banana":200,
#     "mango":300,
# }
#
# product = input("Enter product name : ")
# # try:
# #     print(f'Ціна: {price[product]}')
# # except KeyError:
# #     print("Такого товарау немає")
#
# price = price.get(product,"немає у наявності")
# print(price)
#
# try:
#     with open("data.txt","r",encoding="utf-8") as file:
#         data = file.read()
#         print(data)
#

#
# line = 'Anna;60'
#
# parts = line.split(';')
#
# if(len(parts) != 2):
#     print('error')
# else:
#     name = parts[0]
#     grade = parts[1]
#
#     try:
#         score = int(grade)
#         if(score < 0 or score > 100):
#             raise ValueError('score must be between 0 and 100')
#     except ValueError as error:
#         print('error')
#     else:
#         print(f'Запис правильний {name}: {score}')
#
#
#
#

# lines = [
#     'Anna;90',
#     'Ivan;hello'
#     'Matvey;99'
# ]
#
#
# for line_number,line in enumerate(lines,start=1):
#     parts = line.strip().split(';')
#
#     if len(parts) != 2:
#         print(f'Рядок: {line_number}: пропущено через неправильний формат \n {line}')
#         continue
#     name = parts[0]
#     grade = parts[1]
#
#     try:
#         grade = int(grade)
#     except ValueError:
#         print(f'Рядок {line_number},пропущенно: бал не є числом')
#         continue
#     print("Правильний запис: ", name, grade)
#















