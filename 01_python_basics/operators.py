# operators.py
# Author: Laraib Kaleem
# Python Beginner Portfolio - Operators

# 1️⃣ Arithmetic Operators
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# 2️⃣ Comparison Operators
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater or Equal:", a >= b)
print("Less or Equal:", a <= b)

# 3️⃣ Logical Operators
x = True
y = False
print("Logical AND:", x and y)
print("Logical OR:", x or y)
print("Logical NOT:", not x)

# 4️⃣ Assignment Operators
c = 5
c += 3   # c = c + 3
print("c += 3:", c)
c *= 2   # c = c * 2
print("c *= 2:", c)

# 5️⃣ Membership Operators
name = "Python"
print("'P' in name:", 'P' in name)
print("'x' not in name:", 'x' not in name)

# 6️⃣ Identity Operators
a_list = [1, 2, 3]
b_list = a_list
c_list = [1, 2, 3]
print("a_list is b_list:", a_list is b_list)       # True
print("a_list is c_list:", a_list is c_list)       # False
print("a_list is not c_list:", a_list is not c_list)  # True
