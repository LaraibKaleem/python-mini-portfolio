# loops.py
# Author: Laraib Kaleem
# Python Beginner Portfolio - Loops

# 1️⃣ For loop
for i in range(5):
    print("For loop iteration:", i)

# 2️⃣ Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# 3️⃣ While loop
count = 0
while count < 5:
    print("While loop count:", count)
    count += 1

# 4️⃣ Break and Continue
for i in range(5):
    if i == 3:
        print("Breaking loop at i =", i)
        break
    if i == 1:
        print("Skipping iteration at i =", i)
        continue
    print("Loop i =", i)
