class Student:
    def __init__(self, name, age, year):
        self.name = name
        self.age = age
        self.year = year
    def birth_year(self):
        print(2025 - self.age)

student = Student("Mark", 13, 7)
student2 = Student("David", 14, 8)

print(student2.name)
student2.birth_year()