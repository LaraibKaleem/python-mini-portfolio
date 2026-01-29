# functions.py
# Author: Laraib Kaleem
# Python Beginner Portfolio - Functions

# 1️⃣ Simple function
def greet(name):
    print(f"Hello, {name}!")

greet("Laraib")

# 2️⃣ Function with return
def add(a, b):
    return a + b

result = add(5, 10)
print("Sum:", result)

# 3️⃣ Default parameters
def greet_default(name="Guest"):
    print(f"Hello, {name}!")

greet_default()
greet_default("Laraib")

# 4️⃣ Arbitrary arguments (*args, **kwargs)
def info(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

info(1, 2, 3, name="Laraib", age=24)
