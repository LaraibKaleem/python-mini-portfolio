# strings.py
# Author: Laraib Kaleem
# Python Beginner Portfolio - Strings

# 1️⃣ Creating Strings
string1 = 'Hello'
string2 = "Python"
string3 = """This
is a multi-line
string"""
print(string1, string2)
print(string3)

# 2️⃣ Accessing Strings
text = "Python"
print("Indexing:", text[0], text[-1])
print("Slicing:", text[1:4], text[:4], text[2:])

# 3️⃣ String Operations
print("Concatenation:", "Hello " + "World")
print("Repetition:", "Hi! " * 3)
print("Length:", len(text))
print("Membership:", 'y' in text)
print("Not in:", 'z' not in text)

# 4️⃣ String Methods
sample = "  hello world  "
print("Upper:", sample.upper())
print("Lower:", sample.lower())
print("Capitalize:", sample.capitalize())
print("Title:", sample.title())
print("Strip:", sample.strip())
print("Replace:", "Python".replace("P","J"))
print("Split:", "a,b,c".split(","))
print("Join:", ",".join(['a','b','c']))

# 5️⃣ String Formatting
name = "Laraib"
age = 23
print(f"My name is {name} and I am {age} years old.") # f-string
print("My name is {} and I am {} years old.".format(name, age)) # format()
print("My name is %s and I am %d years old." % (name, age)) # % formatting

# 6️⃣ String Indexing 
print("\nIndexing\n")
print("First character:", text[0])
print("Second character:", text[1])
print("Last character:", text[-1])
print("Indexing:", text[0], text[-1])

# 7️⃣ String Slicing 
print("\nSlicing\n")
print("Copy string:", text[:])
print("First word:", text[0:6])
print("Second word:", text[7:])
print("Start to 6:", text[:6])
print("Step slicing:", text[::2])
print("Every second character:", text[::2])
print("Reverse string:", text[::-1])
print("Partial reverse:", text[5:0:-1])
print("\nNegative Slicing: Last 5 characters:", text[-5:])






