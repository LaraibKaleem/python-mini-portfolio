# conditional_statements.py
# Author: Laraib Kaleem
# Python Beginner Portfolio - Conditional Statements

# 1️⃣ if statement
x = 10
if x > 5:
    print("x is greater than 5")

# 2️⃣ if-else statement
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is less than or equal to 5")

# 3️⃣ if-elif-else statement
z = 7
if z > 10:
    print("z is greater than 10")
elif z > 5:
    print("z is greater than 5 but less than or equal to 10")
else:
    print("z is 5 or less")

# 4️⃣ Nested if statements
a = 8
if a > 5:
    if a % 2 == 0:
        print("a is greater than 5 and even")

# 5️⃣ Using logical operators
b = 12
if b > 5 and b < 15:
    print("b is between 5 and 15")

if b < 5 or b > 10:
    print("b is less than 5 or greater than 10")

if not b == 10:
    print("b is not equal to 10")
