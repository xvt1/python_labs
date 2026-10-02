# name = "Dima"
# city = "Kyiv"
# message = "Hello world"
#
# #len - показує довжину рядка повертає к-сть символів
#
# print(len(message))
# print(name[0])
# print(name[-1])
# print(message[len(message)-1])

# text = input("")
# if len(text) > 0:
#     print(text[0])
# else:
#     print("Empty sentence")
# text = "Hello world"
# print(text[:2])
# print(text[2:])
# print(text[::2])
# print(text[::-1])

# text = "hello world"
# text2 = text.upper()#весь текст капсом
# print(text2)
# print(text2.lower()) #весь текст нижнім
# print(text.capitalize())#тіки перша літера великим
# print(text.title())#кожен слово через пробіл з великої
#
#
# text = "                 Python              programming          "
# print(text.lstrip())#видаляє пробіл зліва рядка
# print(text.rstrip())#видаляє пробіл зправа рядка
# print(text.strip())#видаляє пробіл зліва та справа але не в центрі

# login = "admin"
# user_login = input("Enter Username: ")
# if user_login.strip().lower() == login:
#     print("Login Successful")

# text = "Python"
#
# for char in text:
#     print(char)

# password = "123qwerty123"
# # print(password.isdigit())
# digits = 0
# letters = 0
# for char in password:
#     if char.isdigit():
#         digits += 1
#     if char.isalpha():
#         letters += 1
# print(f"numbers :{ digits} letters :  {letters}")
#
# print(password.isalpha())
# print(password.isdigit())
# print(password.isalnum())

# text = input("Enter a sentence: ").strip().lower()
# golocny = "аеєиіїоуюя"
# counter = 0
# for i in text:
#     if i in golocny:
#         counter += 1
# print(counter)


# text = "привіт                              світ"
# words = text.split()
# print(words)
#
# text_new = "+".join(words)
# print(text_new)

#
# text = "Python is easy to learn"
# new_text = text.replace("Python","JavaScript")
# print(new_text)
#
#
#
#
#
# word = "Дід "
#
# word_norm = word.strip().lower()
#
# if(word_norm == word_norm[::-1]):
#     print("поліндром")
# else:
#     print("непаліндром")
#
# text = "hello world"
#
# print(text.find("o"))
#
# print(text.count("l"))

# email = "test.rerrhe@gmail.com"
#
# if email.lower().endswith("@gmail.com"):
#     print("у тебе гуглівська пошта")
#
