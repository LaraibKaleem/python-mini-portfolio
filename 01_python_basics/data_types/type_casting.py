# type_casting_examples.py
# Author: Laraib Kaleem
# Python Beginner Portfolio - Type Casting Examples

# Explicit casting
x = 5       # int
y = float(x) # convert to float
print("Explicit casting int->float:", y, "Type:", type(y))

# Implicit casting
a = 10      # int
b = 5.5     # float
c = a + b   # int + float = float
print("Implicit casting int+float:", c, "Type:", type(c))

# Converting string to number
num_str = "123"
num_int = int(num_str)
print("String to int:", num_int, "Type:", type(num_int))

num_float = float(num_str)
print("String to float:", num_float, "Type:", type(num_float))

# Converting number to string
num = 456
num_s = str(num)
print("Number to string:", num_s, "Type:", type(num_s))
