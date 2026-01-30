# data_structures.py
# Author: Laraib Kaleem
# Python Beginner Portfolio - Data Structures

# 1️⃣ List
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)
print("First fruit:", fruits[0])
fruits.append("orange")
fruits.remove("banana")
print("Updated List:", fruits)

# 2️⃣ Tuple
colors = ("red", "green", "blue")
print("Tuple:", colors)
print("Second color:", colors[1])
# colors[1] = "yellow"  # ❌ Error: tuples are immutable

# 3️⃣ Set
numbers = {1, 2, 3, 3}
print("Set:", numbers)  # duplicates removed
numbers.add(4)
numbers.remove(2)
print("Updated Set:", numbers)

# 4️⃣ Dictionary
person = {"name": "Laraib", "age": 23}
print("Dictionary:", person)
print("Name:", person["name"])
person["age"] = 24
person["city"] = "Islamabad"
print("Updated Dictionary:", person)

# 5️⃣ Common operations
# List access and modification
fruits[0] = "mango"
print("Modified List:", fruits)

# Set: membership test
print("Is 3 in numbers?", 3 in numbers)

# Dictionary keys and values
print("Keys:", person.keys())
print("Values:", person.values())
