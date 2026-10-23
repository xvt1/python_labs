#task 1
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         return self.name
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#
#     def info(self):
#         return f'Учень: {self.name}, група: {self.group}'
#
# anna = Student('Anna', 'IT-10')#СОВПАДЄНІЄ І ПОКи Що
# neAnna = Student('Anna Ivanenko','IT-10')
#
# print(anna.info())
# print(neAnna.info())

#task 2
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         return f"Ім'я {self.name}"
#
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#
#     def info(self):
#         return f'Учень: {self.name}, група: {self.group}'
#
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#
#     def info(self):
#         return f'Викладач:{self.name} предмет:{self.subject}'
#
# l = [Person("Ivan Komarov"), Student("Anna Ivanenko", "IT-10"), Teacher("Olena Kovalenko", "Python")]
#
# for i in l:
#     print(i.info())

#task 3
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         return f"Ім'я {self.name}"
#
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#
#     def info(self):
#         return f'Учень: {self.name}, група: {self.group}'
#
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#
#     def info(self):
#         return f'Викладач:{self.name} предмет:{self.subject}'
# class Course:
#     def __init__(self, title, teacher):
#         self.teacher = teacher
#         self.title = title
#         self.students = []
#     def add_student(self, student):
#         if student not in self.students:
#             self.students.append(student)
#
#
#     def remove_student(self, student):
#         if student in self.students:
#             self.students.remove(student)
#
#
#     def info(self):
#         for i in range(len(self.students)):
#             print(f'{i+1}.{self.students[i].info()}')
# c = Course("Python,","Ivan Komarov")
# c.add_student(Student("Sophie pe4enka","IT-10"))
# c.add_student(Student("Anna Ivanenko","IT-10")) #совпадєніє
# c.add_student(Student("Veronika Sixsevenova","IT-10"))
# c.add_student(Student("Maria Karandash","IT-10"))
# c.info()

#task 4
import os
class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        return f"Ім'я {self.name}"

class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group
        self.grades = []

    def add_grade(self, grade):
        if grade >= 1 or grade <= 12:
            self.grades.append(grade)
    def average(self):
        return sum(self.grades) / len(self.grades)

    def info(self):
        return f'Учень: {self.name}, група: {self.group}'

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def info(self):
        return f'Викладач:{self.name} предмет:{self.subject}'

class Course:
    def __init__(self, title, teacher):
        self.teacher = teacher
        self.title = title
        self.students = []
        self.load_date()

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)


    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def finde_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def add_grade_to_student(self,name, grade):
            s = self.finde_student(name)
            if s != None:
                s.add_grade(grade)

    def show_rating(self):
        studentsAverage = []
        for student in self.students:
            studentsAverage.append(student.average())
        return studentsAverage.sort()

    def save_date(self):
        with open('course_data.txt', 'w', encoding='utf-8') as f:
            for student in self.students:
                parts = student.info().split(",")
                name = parts[0].split(":")[1].strip()
                group = parts[1].split(":")[1].strip()

                f.write(f'{name};{group};{student.grades}\n')
                print(f'{name};{group};{student.grades}\n')

    def load_date(self):
        if os.path.exists("course_data.txt"):
            with open("course_data.txt", "r", encoding="utf-8") as f:
                for i in f.readlines():
                    parts = i.split(";")
                    self.students.append(Student(parts[0], parts[1]))
                    f1 = parts[2]
                    f1 = f1[:-1]
                    f1 = f1[1:]
                    f1 = f1.split(",")
                    for i in f1:
                        i = i.strip()
                        if i.isdigit():
                            self.add_grade_to_student(parts[0], int(i))

    def info(self):
        for i in range(len(self.students)):
            print(f'{i+1}.{self.students[i].info()}')

def main():
    c = Course("Python", "Ivan Komarov")


if __name__ == '__main__':
    main()

#4 пункт не дороблено.... я його планую в суботу робити...