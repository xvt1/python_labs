# a = 12 # int
# b = 12.4 # float
# c = "hello" #str
# d = True #False Bool
#
# print(a + b)

# a = int(input("введи перше число: "))
# b = int(input("введи друге число: "))
#
# print(int(a)+int(b)) #конкатенація - скелюваня двох або більше str частин
# print(a + b)
#
# int()
# float()
# str()
# bool()

# + -
# *    /   %   \\
# **

# +
# print("hello" * 2)

# a = int(input("#1"))
# b = int(input("#2"))
# c = int(input("#3"))

a,b,c = map(int,input("Введи три числа через пробіл: ").split())
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
else:
    print("a == b == c")

#<=
#>=

# if a > b:
#     if a > c:
#         print(a)
#     else:
#         print(c)
# elif b > a:
#     if b > c:
#         print(b)
#     else:
#         print(c)
# elif c > a:
#     if c > b:
#         print(c)
#     else:
#         print(b)
# else:
#     print("a == b == c")
# max()