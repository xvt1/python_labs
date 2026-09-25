#1
# a = int(input())
#
# if a % 2 == 0:
#     print("parne")
# else:
#     print("ne parne")

#2
# a = int(input("Ведіть свій вік: "))
# if a >= 18:
#     print("Ви повнолітній!")
# else:
#     print("Ви неповнолітній!")

#3
# a = int(input("Ведіть радіус кола:"))
# r = a*2*3.14
# s = 3.14*a**2
# print("Довжина кола: " + str(r))
# print("Площа кола: " + str(s))

#4
# a,b = map(int,input("Ведіть 2 числа через пробіл").split())
#
# if (a > b):
#     print(a)
# else:
#     print(b)

#2
# x,y = map(int,input("Ведіть координати точки через пробіл: ").split())
# if x > 0 and y > 0:
#     print("1 chvert")
# elif x < 0 and y > 0:
#     print("2 chvert")
# elif x < 0 and y < 0:
#     print("3 chvert")
# elif x > 0 and y < 0:
#     print("4 chvert")

#3
# a = int(input("Ведіть свій вік до 120 років: "))
#
# if(a < 120):
#     last_digit = a % 10
#     if last_digit == 1 and a != 11:
#         print(str(a) + " рік")
#     elif last_digit == 2 or last_digit == 3 or last_digit == 4 and a != 12 and a != 13:
#         print(str(a) + " роки")
#     elif last_digit > 5 or last_digit < 9 or last_digit == 0 or a == 12 or a == 13 or a == 14 or a == 11:
#         print(str(a) + " років")
#ФІНАЛЬНЕ СУПЕР ДУПЕР ЗАВДАННЯ
n = int(input("Ведіть кількість поїздок: "))
k = int(input("Кількість штук в 1 пачці: "))
p1 = int(input("Ведіть вартість одного квитка: "))
p2 = int(input("Ведіть вартість пачкі: "))
if(n > 0 and k > 0 and p1 > 0 and p2 > 0 and n < 10000 and k < 10000 and p1 <  10000 and p2 < 10000):
    a = n*p1
    b = n//k
    c = n % k

    d = b*p2 + c*p1
    e = (b + 1) * p2

    result = min(a, d, e)
    print(result)
else:
    print("Числа не виконують умову задачі")