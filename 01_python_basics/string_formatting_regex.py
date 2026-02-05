
# 🐍 `string_formatting_regex.py`
# Author: Laraib Kaleem
# Python Beginner Portfolio - Regression

name = "Laraib"
age = 23

print("\n--- String Formatting ---")
print("Name: %s" % name)
print("Age: %d" % age)
print("Price: %.2f" % price)
print(f"My name is {name} and I am {age}")
print("My name is {} and I am {}".format(name, age))
print("My name is %s and I am %d" % (name, age))

# -------------------------
# Regular Expressions
# -------------------------
import re

print("\n--- Regex Examples ---")

text = "My score is 95 and email is test@gmail.com"

# Find numbers
numbers = re.findall(r"\d+", text)
print("Numbers:", numbers)

# Extract email
emails = re.findall(r"\s+@\s+", text)
print("Emails:", emails)

# Replace digits
clean = re.sub(r"\d+", "", text)
print("Removed numbers:", clean)
