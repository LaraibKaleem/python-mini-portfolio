# convert_data_types.py
# Author: Laraib Kaleem
# Python Beginner Portfolio - Convert Data Types

# 1️⃣ int to float
num_int = 10
type(num_int)
num_float = float(num_int)
print("int to float:", num_float, "Type:", type(num_float))

# 2️⃣ float to int
num_float2 = 9.8
type(num_float2)
num_int2 = int(num_float2)
print("float to int:", num_int2, "Type:", type(num_int2))

# 3️⃣ str to int
num_str = "100"
type(num_str)
num_int3 = int(num_str)
print("str to int:", num_int3, "Type:", type(num_int3))

# 4️⃣ int to str
num = 200
type(num)
num_str2 = str(num)
print("int to str:", num_str2, "Type:", type(num_str2))

# 5️⃣ bool conversion
print("bool(0):", bool(0))
print("bool(1):", bool(1))
print("bool(''):", bool(''))
print("bool('Hello'):", bool("Hello"))
