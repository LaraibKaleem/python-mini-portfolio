# libraries_packages_modules.py
# Author: Laraib Kaleem
# Python Beginner Portfolio - Libraries, Packages, Modules

# 1️⃣ Using built-in module
import math
print("Square root of 16:", math.sqrt(16))
print("Factorial of 5:", math.factorial(5))

# 2️⃣ Using your own module
# Suppose my_module.py exists with a function greet()
# import my_module
# print(my_module.greet("Laraib"))

# 3️⃣ Using external library (NumPy)
try:
    import numpy as np
    arr = np.array([1, 2, 3])
    print("NumPy Array:", arr)
except ImportError:
    print("NumPy not installed. Run 'pip install numpy' to install.")

# 4️⃣ Using external library (Pandas)
try:
    import pandas as pd
    data = pd.DataFrame({'Name': ['Laraib', 'Ali'], 'Age': [23, 25]})
    print("Pandas DataFrame:\n", data)
except ImportError:
    print("Pandas not installed. Run 'pip install pandas' to install.")

#4️⃣ Installing External Libraries
#Use pip to install external libraries:
#pip install numpy
#pip install pandas
