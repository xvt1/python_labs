class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return self.name
class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group
    def info(self):
        return f'{self.name} {self.group}'


student = Student("Anna","10IT")
person = Person("John")
print(student.name)
print(student.group)
print(person.info())
