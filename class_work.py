# Приклад 1. Виведення 1..N циклом for
# n = int(input('N = '))
# for i in range(1, n + 1):
#     print(i)
# Приклад 2. Те саме циклом while
# n = int(input('N = '))
# i = 1
# while i <= n:
#     print(i)
#     i += 1
# Приклад 3. Сума і середнє чисел 1..N
# n = int(input('N = '))
# total = 0
# for i in range(1, n + 1):
#     total += i
# print('Сума:', total)
# print('Середнє:', total / n)
# Приклад 4. Факторіал
# n = int(input('N = '))
# result = 1
# for i in range(1, n + 1):
#     result *= i
# print('Факторіал:', result)
# Приклад 5. Сума чисел за умовою
# n = int(input('N = '))
# total = 0
# for i in range(1, n + 1):
#     if i % 3 == 0:
#         total += i
# print('Сума:', total)
# Приклад 6. range() з різними параметрами
# print(list(range(5)))
# print(list(range(2, 8)))
# print(list(range(10, 1, -2)))
# Приклад 7. Аналіз цифр числа
# n = int(input('N = '))
# count = 0
# total = 0
# max_digit = 0
# while n > 0:
#     digit = n % 10
#     count += 1
#     total += digit
#     if digit > max_digit:
#         max_digit = digit
#     n //= 10
# print('Кількість:', count)
# print('Сума цифр:', total)
# print('Найбільша цифра:', max_digit)
# Приклад 8. break: введення до команди завершення
# while True:
#     value = input("Введіть число або 'stop': ")
#     if value == 'stop':
#         break
# print('Введено:', value)
# Приклад 9. continue: пропуск недопустимих значень
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
# print(i)
# Приклад 10. Вкладені цикли: таблиця множення
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i * j, end='\t')
#     print()
# Приклад 11. Прямокутник символами
# width = int(input('Ширина: '))
# height = int(input('Висота: '))
# for row in range(height):
#     for col in range(width):
#         print('*', end='')
#     print()
# Приклад 12. Дільники числа
# n = int(input('N = '))
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)