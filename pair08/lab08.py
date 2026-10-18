#task 1
# def plus(a, b):
#     return a + b
#
#
# def minus(a, b):
#     return a - b
#
#
# def dilenya(a, b):
#     if b == 0:
#         return "Помилка: на нуль ділити не можна."
#     else:
#         return a / b
#
# def mnozenya(a, b):
#     return a*b
#
# a = input("A: ")
# b = input("B: ")
# operator = input("Операція: ")
#
# try:
#     a = float(a)
#     b = float(b)
# except ValueError:
#     print("Помилка a,b мають бути числами")
# else:
#     if operator == "+":
#         print(plus(a, b))
#     elif operator == "-":
#         print(minus(a, b))
#     elif operator == "/":
#         print(dilenya(a, b))
#     elif operator == "*":
#         print(mnozenya(a, b))
#     else:
#         print("такого оператора немає")

#task 2

# def input_grade():
#     while True:
#         inp = input("Оцінка: ")
#
#         try:
#             try:
#                 number = int(inp)
#             except ValueError:
#                 print("Помилка: потрібно ввести ціле число.")
#                 continue
#
#             if not (1 <= number <= 12):
#                 raise ValueError("Помилка: оцінка повинна бути від 1 до 12.")
#
#             return number
#         except ValueError as e:
#             print(e)
#
# grade = input_grade()
# print(f"Прийнято: {grade}")

#task 3
# students = [
#     "Аня",#совпадєніє
#     "Влад",
#     "Саша",
#     "Вероніка",
#     "Софія"
# ]
# subjects = {
#     "Математика": 8,
#     "Англійська": 12,
#     "Інформатика": 12,
#     "Фізкультура": 10
# }
#
# def findeStudent(index):
#     try:
#         return students[index]
#     except IndexError:
#         return("Помилка: учня з таким індексом немає.")
#
# def findSubject(subject):
#     try:
#         return subjects[subject.lower().strip().capitalize()]
#     except KeyError:
#         return("Предмета з таким індексом немає")
#
# methondFinde = input("1 - учень, 2 - предмет: ")
# try:
#     methondFinde = int(methondFinde)
#     if methondFinde == 1:
#         inx = input("Індекс: ")
#         try:
#             inx = int(inx)
#             print(findeStudent(inx))
#         except ValueError:
#             print("має бути числом")
#     elif methondFinde == 2:
#         subject = input("Ведіть назву предмету: ")
#         print(findSubject(subject))
#
#     else:
#         raise ValueError("Виберіть режим 1 - учень, 2 - предмет")
# except ValueError as e:
#     print(e)
#
#task 4

import os

clear_line = []
countPassed = 0
countSkipped = 0
try:
    with open("students.txt","r", encoding="utf-8") as f:
        for number,line in enumerate(f,start=1):

            if not ";" in line.strip():
                print(f'Рядок {number} пропущено: немає розділового знаку')
                countSkipped += 1
                continue
            parts = line.split(';')
            try:
                parts[1] = int(parts[1])
                if parts[1] < 0 or parts[1] > 100:
                    print(f'Рядок {number} пропущено: бал поза діапазоном')
                    countSkipped += 1
                elif len(parts) == 2:
                    clear_line.append((parts[1], f"{parts[0]};{parts[1]}\n"))
                    countPassed += 1
                elif len(parts) > 2:
                    countSkipped += 1
                    print(f'Рядок {number} пропущено: більше двух значень')
            except ValueError:
                print(f'Рядок {number} пропущено: бал не є числом')
                countSkipped += 1
        clear_line.sort(key=lambda x: x[0], reverse=True)
        with open("report.txt", "w", encoding="utf-8") as f:
            for i,g in clear_line:
                f.write(g)
    print("створено report.txt")
    print(f'Правильних записів: {countPassed}')
    print(f'Пропущено: {countSkipped}')
except FileNotFoundError:
    print("Файла немає")