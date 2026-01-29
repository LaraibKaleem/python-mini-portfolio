# oop_basics.py
# Author: Laraib Kaleem
# Python Beginner Portfolio - OOP Basics

# 1️⃣ Class and Object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Student Name: {self.name}, Age: {self.age}")

# Create object
student1 = Student("Laraib", 24)
student1.info()

# 2️⃣ Inheritance
class SchoolStudent(Student):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def details(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

student2 = SchoolStudent("Ali", 15, "9th Grade")
student2.details()
