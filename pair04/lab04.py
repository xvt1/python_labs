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
# print("Віж'ємні: ",minus)
# print("Парні: ",parni)
# print("Картні 3: ",kratni)
# print("Min: " + str(min(digits)) + ";", "Max: " + str(max(digits))+ ";","Sum:" + str(sum(digits)) + ";", "Averange: " + str(round((sum(digits)/len(digits)), 2)) + ";")

#task 2
# group1 = set
# group2 = set
# group1 = {'Anna','Ivan','Olha'}
# group2 = {'Ivan','Maksym','Olha'}
#
# all = ""
# spilni = ""
#
# for x in group1 | group2:
#     all = all + " "+ x
#
# for y in group1 & group2:
#     spilni = spilni + " "+ y
#
# onlyingp1 = group1 - group2
# onlyingp2 = group2 - group1
#
# for x in onlyingp1:
#     onlyingp1 = x
# for x in onlyingp2:
#     onlyingp2 = x
#
# print("Спільні: " + spilni)
# print("Тільки group1: ", onlyingp1)
# print("Тільки group2: ", onlyingp2)
# print("Усі: " + all)

#task 3
# catalog = {"milk": 48, "tea": 75, "bread": 30, "coffee": 150}
#
#
# def add_or_update(name, price):
#     if catalog.get(name) is None:
#         print(f"Товар {name} додано")
#     else:
#         print(f"Ціну товару {name} змінено: {catalog[name]} -> {price} грн")
#     catalog[name] = price
#
#
# def find_product(name):
#     price = catalog.get(name)
#     if price is None:
#         print("Товар не знайдено")
#     else:
#         print(f"{name} — {price} грн")
#
#
# def show_in_range(low, high):
#     found = False
#     for name, price in catalog.items():
#         if low <= price <= high:
#             print(f"{name} — {price} грн")
#             found = True
#     if not found:
#         print("У цьому діапазоні товарів немає")
#
#
# def read_number(text):
#     while True:
#         try:
#             value = float(input(text))
#             if value < 0:
#                 print("Ціна не може бути від'ємною")
#                 continue
#             return int(value) if value.is_integer() else value
#         except ValueError:
#             print("Введіть число")
#
#
# while True:
#     print("\n1 - Додати/змінити товар")
#     print("2 - Знайти товар за назвою")
#     print("3 - Товари в ціновому діапазоні")
#     print("0 - Вихід")
#     choice = input("Ваш вибір: ").strip()
#
#     if choice == "1":
#         name = input("Назва товару: ").strip()
#         if not name:
#             print("Назва не може бути порожньою")
#             continue
#         add_or_update(name, read_number("Ціна: "))
#     elif choice == "2":
#         find_product(input("Назва товару: ").strip())
#     elif choice == "3":
#         low = read_number("Мінімальна ціна: ")
#         high = read_number("Максимальна ціна: ")
#         if low > high:
#             low, high = high, low
#         show_in_range(low, high)
#     elif choice == "0":
#         break
#     else:
#         print("Невірний вибір")

#task 4
group_info = ('10-IT', '2026/2027')
journal = {}


def read_grades():
    while True:
        parts = input("Введіть 5 оцінок через пробіл: ").split()
        try:
            grades = [int(p) for p in parts]
        except ValueError:
            print("Оцінки мають бути цілими числами")
            continue
        if len(grades) != 5:
            print("Має бути рівно 5 оцінок")
        elif not all(1 <= g <= 12 for g in grades):
            print("Оцінки мають бути в діапазоні 1–12")
        else:
            return grades


def average(grades):
    return sum(grades) / len(grades)


def add_student():
    name = input("ПІБ учня: ").strip()
    if not name:
        print("ПІБ не може бути порожнім")
        return
    if name in journal:
        print("Такий учень уже є, оцінки буде замінено")
    journal[name] = read_grades()


def show_journal():
    print(f"{group_info[0]} — {group_info[1]}")
    if not journal:
        print("Журнал порожній")
        return
    for name, grades in journal.items():
        print(f"{name}: {' '.join(map(str, grades))}")


def show_averages():
    for name, grades in journal.items():
        print(f"{name} — {average(grades):.1f}")


def show_rating():
    ranking = sorted(journal.items(), key=lambda item: average(item[1]), reverse=True)
    for place, (name, grades) in enumerate(ranking, start=1):
        print(f"{place}. {name} — {average(grades):.1f}")


def show_best():
    best_avg = max(average(g) for g in journal.values())
    for name, grades in journal.items():
        if average(grades) == best_avg:
            print(f"{name} — {best_avg:.1f}")


while True:
    print("\n1 - Додати учня")
    print("2 - Показати журнал")
    print("3 - Середній бал кожного учня")
    print("4 - Рейтинг учнів")
    print("5 - Учень з найвищим середнім балом")
    print("0 - Вихід")
    choice = input("Ваш вибір: ").strip()

    if choice == "1":
        add_student()
    elif choice in ("2", "3", "4", "5"):
        if not journal:
            print("Журнал порожній")
        elif choice == "2":
            show_journal()
        elif choice == "3":
            show_averages()
        elif choice == "4":
            show_rating()
        else:
            print(f"{group_info[0]} — {group_info[1]}")
            show_best()
    elif choice == "0":
        break
    else:
        print("Невірний вибір")















