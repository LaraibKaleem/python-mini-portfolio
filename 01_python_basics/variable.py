# variable.py
# Author: Laraib Kaleem
# Python Beginner Portfolio - Python Basics

# 1️⃣ Creating variables
age = 25             # Integer
height = 5.7         # Float
name = "Laraib"      # String
is_student = True    # Boolean

# 2️⃣ Printing variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# 3️⃣ Multiple assignment
x, y, z = 10, 20, 30
print("x:", x, "y:", y, "z:", z)

# 4️⃣ Swapping variables
a = 5
b = 10
print("Before swap: a =", a, "b =", b)
a, b = b, a
print("After swap: a =", a, "b =", b)

# 5️⃣ Constants (convention: uppercase)
PI = 3.14159
GRAVITY = 9.8
print("Constants: PI =", PI, "Gravity =", GRAVITY)

# 6️⃣ Type casting (convert one type to another)
num_str = "100"
print("Before type casting:", num_str, "Type:", type(num_str))
num_int = int(num_str)
print("After type casting:", num_int, "Type:", type(num_int))
