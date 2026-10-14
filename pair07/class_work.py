

# print("Створення файлу")
#
# with open ('hello.txt',"w",encoding="utf-8") as file:
#     file.write("Аня обіцяє вчитись!\n")
#
#r - читання має вже існувати
#w - записування
#a - додає контент в кінець якщо файл не сторююван то він його створює
#x - створює новий файл, але якщо є вже файл то буде помилка

import os

if not os.path.exists("text.txt"):
    with open("text.txt","w", encoding="utf-8") as f:
        f.write("Python  - популярна мова програмування.\n")
        f.write("Python  - використовується для роботи з данними.\n")
        f.write("Файли дозволяють зберігати інформацію \n")
        f.write("Python  вимагає практики. \n")
        f.write("Сьогодні ми працюємо з текстовими файлами.\n")

if not os.path.exists("numbers.txt"):
    with open("numbers.txt", "w", encoding="utf-8") as f:
        f.write("12\n8\n25\n4\n\n16\n")

if not os.path.exists("students.txt"):
    with open("students.txt","w", encoding="utf-8") as f:
        f.write("Ivanenko Anna;91\n")
        f.write("Leshechenko Ivan;76\n")
        f.write("Komarova Sophie; 97\n")
        f.write("Bondarenko Illya;84\n")


if not os.path.exists("grades.csv"):
    with open("grades.csv","w", encoding="utf-8") as f:
        f.write("Anna;Python;11\n")
        f.write("Anna;Math;10\n")
        f.write("Ivan;Python;6\n")
        f.write("Ivan;Math;5\n")
        f.write("Sophie;Python;11\n")
        f.write("Sophie;Math;12\n")
        f.write("Illya;Python;9\n")
        f.write("Illya;Math;8\n")


# with open("text.txt","r", encoding="utf-8") as file:
#     text = file.read()
# print(text)

# with - автоматично закриває файл після завершення його роботи
#
# with open("log.txt","w", encoding="utf-8") as file:
#     file.write("Перший запуск\n")
#     file.write("Другий запуск\n")
# with open("log.txt","w", encoding="utf-8") as file:
#     file.write("Другий запуск, перший видалено\n")
# with open("log.txt","a", encoding="utf-8") as file:
#     file.write("Новий запис додаємо у кінець\n")
# with open("log.txt","r", encoding="utf-8") as file:
#     text = file.read()
#     print(text)
# #способи читання
# with open("text.txt","r", encoding="utf-8") as file:
#     text = file.read()
# print(f'read -> {type(text)}, count -> {len(text)} ')

# with open("text.txt","r", encoding="utf-8") as file:
#     line1 = file.readline()#наступний рядок
#     line2 = file.readline()
#     other_line1 = file.readlines()#список з усіх рядків які ще не були прочитані
# print(line1)
# print(line2)
# print(other_line1)
#
# with open("text.txt","r", encoding="utf-8") as file:
#     lines = file.readlines()
# print(other_line1)
# print(other_line1[0] if lines else 'Файл порожній')

# #перебір файлу
#
with open("text.txt","r", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        clean_line = line.strip()
        print(f'number: {number}, line: {clean_line}')
#
# #розпакування
#
# line = "Ivanenko Anna;91\n"
# clean_line = line.strip()
# name, score = clean_line.split(";")
# print(f'name: {name}, score: {score}')
#
# numbers = []
#
# with open("numbers.txt","r", encoding="utf-8") as file:
#     for line in file:
#         numbers.append(int(line.strip()))
# print(f'numbers: {numbers}')
#
# students = []
#
# with open("students.txt","r", encoding="utf-8") as f:
#     for line in f:
#         name, score = line.split(";")
#         students.append([name,int(score)])
# print(students)

#csv
# grades = []
# with open("grades.csv","r", encoding="utf-8") as f:
#     for line in f:
#         name, subject, score = line.strip().split(";")
#         grades.append([name, subject, score])
# print(grades)