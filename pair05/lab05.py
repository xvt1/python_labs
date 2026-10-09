#task 1
# def rectangle_area(shyryna, vysota):
#     return shyryna * vysota
#
# def triangle_area(osnova, vysota):
#     return osnova * vysota / 2
#
# def circle_area(r):
#     pi = 3.14159
#     return pi * r ** 2
#
# def main():
#     a = input("Оберіть фігуру (прямокутник, трикутник, круг): ")
#     figura = a.strip().lower().replace(" ", "")
#
#     if(figura == "прямокутник"):
#         shyryna = float(input("Ширина: "))
#         vysota = float(input("Висота: "))
#         print("Площа прямокутника:", rectangle_area(shyryna, vysota))
#     elif(figura == "трикутник"):
#         osnova = float(input("Основа: "))
#         vysota = float(input("Висота: "))
#         print("Площа трикутника:", triangle_area(osnova, vysota))
#     elif(figura == "круг"):
#         r = float(input("Радіус: "))
#         print("Площа круга:", circle_area(r))
#     else:
#         print("Такої фігури немає")
#
# if __name__ == '__main__':
#     main()
#task 2
# def is_prime(n):
#     if n < 2:
#         return False
#
#     dil = 0
#     for i in range(1,n+1):
#         if n % i == 0:
#            dil += 1
#     return dil == 2
#
# def divisors(n):
#     dilnyky = []
#     for i in range(1,n+1):
#         if n % i == 0:
#             dilnyky.append(i)
#     return dilnyky
#
# def digit_sum(n):
#     chyslo = str(n)
#     tsyfry = []
#     for i in range(len(chyslo)):
#         tsyfry.append(int(chyslo[i]))
#     return sum(tsyfry)
#
# def main():
#     n = int(input('Введіть натуральне число: '))
#     if n < 1:
#         print('Число має бути натуральним')
#         return
#
#     if is_prime(n):
#         proste = 'так'
#     else:
#         proste = 'ні'
#     print(f'Просте число: {proste}')
#     print(f'Дільники: {divisors(n)}')
#     print(f'Сума цифр: {digit_sum(n)}')
#
# if __name__ == '__main__':
#     main()
#task 3
# def average(ocinky):
#     s = sum(ocinky)
#     serednie = s/len(ocinky)
#     return serednie
# def minimum(ocinky):
#     m = min(ocinky)
#     return m
# def maximum(ocinky):
#     m = max(ocinky)
#     return m
#
# def count_above(ocinky, porig):
#     kilkist = 0
#     for ocinka in ocinky:
#         if ocinka > porig:
#             kilkist += 1
#     return kilkist
#
# def main():
#     ocinky = [10,8,12,9,11]
#     porig = 9
#     print(f'Оцінки: {ocinky}')
#     print(f'Поріг: {porig}')
#     print(f'Середній бал: {average(ocinky)}')
#     print(f'Мінімальна: {minimum(ocinky)}')
#     print(f'Максимальна: {maximum(ocinky)}')
#     print(f'Вище {porig}: {count_above(ocinky, porig)}')
#
# if(__name__ == "__main__"):
#     main()
#task 4
def has_min_length(parol, min_dovzhyna=8):
    return len(parol) >= min_dovzhyna

def has_digit(parol):
    for symvol in parol:
        if symvol.isdigit():
            return True
    return False

def has_upper(parol):
    for symvol in parol:
        if symvol.isupper():
            return True
    return False

def has_lower(parol):
    for symvol in parol:
        if symvol.islower():
            return True
    return False

def has_special(parol):
    for symvol in parol:
        if not symvol.isalnum():
            return True
    return False

def validate_password(parol):
    pomylky = []
    if not has_min_length(parol):
        pomylky.append("менше 8 символів")
    if not has_digit(parol):
        pomylky.append("немає цифри")
    if not has_upper(parol):
        pomylky.append("немає великої літери")
    if not has_lower(parol):
        pomylky.append("немає малої літери")
    if not has_special(parol):
        pomylky.append("немає спеціального символу")
    return len(pomylky) == 0, pomylky

def main():
    parol = input("Password: ")
    nadiynyi, pomylky = validate_password(parol)
    if nadiynyi:
        print("Пароль надійний.")
    else:
        print("Пароль не відповідає вимогам.")
        print("Не виконано: " + ", ".join(pomylky))

if(__name__ == "__main__"):
    main()
