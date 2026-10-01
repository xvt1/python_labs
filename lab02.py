#task 1
# n = int(input("Введіть число: "))
# s = 0
# k = 0
# j = 0
# for m in range(1, n+1):
#     if m % 3 == 0:
#         s = s + m
#         k = k + 1
#     elif m % 5 == 0:
#         s = s + m
#         k = k + 1
# j = s / k
# print("Кількість: ", k)
# print("Сума: ", s)
# print("Середнє: ", round(j, 2))
#task 4
# width = int(input("width="))
# height = int(input("height="))
# contur = input("контур=")
# inbox = input("всередині=")
# if(height > 3 and width > 3):
#     for i in range(height):
#         print("")
#         for j in range(width):
#             if(j == 0 or i == 0 or j == width-1 or i == height-1):
#                 print(contur, end="")
#             elif(j == width):
#                 print(contur, end="")
#             else:
#                 print(inbox, end="")
# else:
#     print("width та height мають бути більше 3")
#task 3
# n = int(input("Введіть N: "))
#
# res = []
# for i in range(1, n):
#     x = i
#     ok = True
#     while x > 0:
#         d = x % 10
#         if d != 0 and i % d != 0:
#             ok = False
#             break
#         x //= 10
#     if ok:
#         res.append(i)
#таск 2
# print(*res)
# n = int(input("Введіть N: "))
#
# if n == 0:
#     count = 1
#     total = 0
#     max_d = 0
#     min_d = 0
# else:
#     count = 0
#     total = 0
#     max_d = 0
#     min_d = 9
#     while n > 0:
#         d = n % 10
#         count += 1
#         total += d
#         if d > max_d:
#             max_d = d
#         if d < min_d:
#             min_d = d
#         n //= 10
#
# print("Кількість цифр:", count)
# print("Сума цифр:", total)
# print("Найбільша цифра:", max_d)
# print("Найменша цифра:", min_d)