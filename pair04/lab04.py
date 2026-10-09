#task 1
# digits = [12, 3, 4, 14, -12, 5, 10, 16, -4]
#
# plus = []
# minus = []
# parni = []
# kratni = []
#
# for i in digits:
#     if i > 0:
#         plus.append(i)
#     if i < 0:
#         minus.append(i)
#     if i % 2 == 0:
#         parni.append(i)
#     if i % 3 == 0:
#         kratni.append(i)
# print("Додатні: ",plus)
# print("Від'ємні: ",minus)
# print("Парні: ",parni)
# print("Кратні 3: ",kratni)
# print("Min: " + str(min(digits)) + ";", "Max: " + str(max(digits))+ ";","Sum: " + str(sum(digits)) + ";", "Average: " + str(round((sum(digits)/len(digits)), 2)))

#task 2
# group1 = {'Anna','Ivan','Olha'}
# group2 = {'Ivan','Maksym','Olha'}
#
# print("Спільні: " + ", ".join(sorted(group1 & group2)))
# print("Тільки group1: " + ", ".join(sorted(group1 - group2)))
# print("Тільки group2: " + ", ".join(sorted(group2 - group1)))
# print("Усі: " + ", ".join(sorted(group1 | group2)))

#task 3
# catalog = {"milk": 48, "tea": 75, "bread": 30, "coffee": 150}
#
#
# def add_or_update(name, price):
#     old_price = catalog.get(name)
#     if old_price is None:
#         print("Товар " + name + " додано")
#     else:
#         print("Ціну товару " + name + " змінено: " + str(old_price) + " -> " + str(price) + " грн")
#     catalog[name] = price
#
#
# def find_product(name):
#     price = catalog.get(name)
#     if price is None:
#         print("Товар не знайдено")
#     else:
#         print(name + " - " + str(price) + " грн")
#
#
# def show_in_range(low, high):
#     kilkist = 0
#     for name, price in catalog.items():
#         if price >= low and price <= high:
#             print(name + " - " + str(price) + " грн")
#             kilkist = kilkist + 1
#     if kilkist == 0:
#         print("У цьому діапазоні товарів немає")
#
#
# def read_number(text):
#     while True:
#         a = input(text).strip()
#         if a.replace(".", "", 1).isdigit():
#             if a.count(".") == 0:
#                 return int(a)
#             else:
#                 return float(a)
#         elif a.startswith("-") and a[1:].replace(".", "", 1).isdigit():
#             print("Ціна не може бути від'ємною")
#         else:
#             print("Введіть число")
#
#
# while True:
#     print()
#     print("1 - Додати/змінити товар")
#     print("2 - Знайти товар за назвою")
#     print("3 - Товари в ціновому діапазоні")
#     print("0 - Вихід")
#     choice = input("Ваш вибір: ").strip()
#
#     if(choice == "1"):
#         name = input("Назва товару: ").strip()
#         if name == "":
#             print("Назва не може бути порожньою")
#         else:
#             price = read_number("Ціна: ")
#             add_or_update(name, price)
#     elif(choice == "2"):
#         name = input("Назва товару: ").strip()
#         find_product(name)
#     elif(choice == "3"):
#         low = read_number("Мінімальна ціна: ")
#         high = read_number("Максимальна ціна: ")
#         if low > high:
#             temp = low
#             low = high
#             high = temp
#         show_in_range(low, high)
#     elif(choice == "0"):
#         break
#     else:
#         print("Невірний вибір")

#task 4
group_info = ('10-IT', '2026/2027')
journal = {}


def read_grades():
    while True:
        a = input("Введіть 5 оцінок через пробіл: ")
        chastyny = a.split()
        grades = []
        pomylka = False
        for p in chastyny:
            if p.isdigit():
                grades.append(int(p))
            elif p[0] == "-" and p[1:].isdigit():
                grades.append(int(p))
            else:
                pomylka = True

        if pomylka == True:
            print("Оцінки мають бути цілими числами")
        elif len(grades) != 5:
            print("Має бути рівно 5 оцінок")
        else:
            dobre = True
            for g in grades:
                if g < 1 or g > 12:
                    dobre = False
            if dobre == True:
                return grades
            else:
                print("Оцінки мають бути в діапазоні 1–12")


def average(grades):
    suma = 0
    for g in grades:
        suma = suma + g
    return suma / len(grades)


def add_student():
    name = input("ПІБ учня: ").strip()
    if name == "":
        print("ПІБ не може бути порожнім")
    else:
        if name in journal:
            print("Такий учень уже є, оцінки буде замінено")
        journal[name] = read_grades()


def show_journal():
    print(group_info[0] + " - " + group_info[1])
    for name in journal:
        ocinky = ""
        for g in journal[name]:
            ocinky = ocinky + str(g) + " "
        print(name + ": " + ocinky)


def show_averages():
    for name in journal:
        print(name + " - " + str(round(average(journal[name]), 1)))


def show_rating():
    imena = []
    for name in journal:
        imena.append(name)

    for i in range(len(imena)):
        for j in range(len(imena) - 1):
            if average(journal[imena[j]]) < average(journal[imena[j + 1]]):
                temp = imena[j]
                imena[j] = imena[j + 1]
                imena[j + 1] = temp

    mistse = 1
    for name in imena:
        print(str(mistse) + ". " + name + " - " + str(round(average(journal[name]), 1)))
        mistse = mistse + 1


def show_best():
    best = 0
    for name in journal:
        if average(journal[name]) > best:
            best = average(journal[name])
    for name in journal:
        if average(journal[name]) == best:
            print("Найкращий результат: " + name + " - " + str(round(best, 1)))


while True:
    print()
    print("1 - Додати учня")
    print("2 - Показати журнал")
    print("3 - Середній бал кожного учня")
    print("4 - Рейтинг учнів")
    print("5 - Учень з найвищим середнім балом")
    print("0 - Вихід")
    choice = input("Ваш вибір: ").strip()

    if(choice == "1"):
        add_student()
    elif(choice == "2"):
        if len(journal) == 0:
            print("Журнал порожній")
        else:
            show_journal()
    elif(choice == "3"):
        if len(journal) == 0:
            print("Журнал порожній")
        else:
            show_averages()
    elif(choice == "4"):
        if len(journal) == 0:
            print("Журнал порожній")
        else:
            show_rating()
    elif(choice == "5"):
        if len(journal) == 0:
            print("Журнал порожній")
        else:
            print(group_info[0] + " - " + group_info[1])
            show_best()
    elif(choice == "0"):
        break
    else:
        print("Невірний вибір")















