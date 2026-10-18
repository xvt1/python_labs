# book = {
#     'title': 'Кобзар',
#     'Avtor': 'Тарас Шевченко',
#     'copiess': 15
# }
# print(book)
#
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def available(self):
#         return self.pages > 0
#
# book1 = Book("Kobzar", "Тарас Шевченко", 10)
# book2 = Book("Kobzar", "", 20)
#
# print(book1.title, book1.author, book1.pages)
# print(book2)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

rectangle = Rectangle(100,200)
area = rectangle.area()
print(area)

print(area > 10000)

