

# Python Operators
Python operators are symbols used to perform operations on variables and values.
They are categorized into several types:

**1️⃣ Arithmetic Operators**
| Operator | Description         | Example       |
| -------- | ------------------- | ------------- |
| `+`      | Addition            | `5 + 3 = 8`   |
| `-`      | Subtraction         | `5 - 3 = 2`   |
| `*`      | Multiplication      | `5 * 3 = 15`  |
| `/`      | Division (float)    | `5 / 2 = 2.5` |
| `//`     | Floor Division      | `5 // 2 = 2`  |
| `%`      | Modulus (remainder) | `5 % 2 = 1`   |
| `**`     | Exponent            | `2 ** 3 = 8`  |

**2️⃣ Comparison Operators**
| Operator | Description              | Example          |
| -------- | ------------------------ | ---------------- |
| `==`     | Equal to                 | `5 == 5 → True`  |
| `!=`     | Not equal to             | `5 != 3 → True`  |
| `>`      | Greater than             | `5 > 3 → True`   |
| `<`      | Less than                | `5 < 3 → False`  |
| `>=`     | Greater than or equal to | `5 >= 5 → True`  |
| `<=`     | Less than or equal to    | `5 <= 3 → False` |

**3️⃣ Logical Operators**
| Operator | Description             | Example                  |
| -------- | ----------------------- | ------------------------ |
| `and`    | True if both are True   | `True and False → False` |
| `or`     | True if any one is True | `True or False → True`   |
| `not`    | Inverts Boolean         | `not True → False`       |

**4️⃣ Assignment Operators**
| Operator | Description         | Example                |
| -------- | ------------------- | ---------------------- |
| `=`      | Assign value        | `x = 5`                |
| `+=`     | Add and assign      | `x += 3 → x = x + 3`   |
| `-=`     | Subtract and assign | `x -= 2 → x = x - 2`   |
| `*=`     | Multiply and assign | `x *= 4 → x = x * 4`   |
| `/=`     | Divide and assign   | `x /= 2 → x = x / 2`   |
| `%=`     | Modulus and assign  | `x %= 3 → x = x % 3`   |
| `**=`    | Exponent and assign | `x **= 2 → x = x ** 2` |

**5️⃣ Membership Operators**
| Operator | Description                              | Example                   |
| -------- | ---------------------------------------- | ------------------------- |
| `in`     | True if value exists in sequence         | `'a' in 'cat' → True`     |
| `not in` | True if value does not exist in sequence | `'b' not in 'cat' → True` |

**6️⃣ Identity Operators**
| Operator | Description             | Example      |
| -------- | ----------------------- | ------------ |
| `is`     | True if same object     | `x is y`     |
| `is not` | True if not same object | `x is not y` |

# Strings
Strings are sequences of characters used to store text. In Python, strings are enclosed in single quotes '...' or double quotes "...".

**1️⃣ Accessing Strings**
**Indexing:** Access a single character by position (0-based index)
**Slicing:** Access a substring

**2️⃣ String Operations**
| Operation     | Example               | Result           |
| ------------- | --------------------- | ---------------- |
| Concatenation | `"Hello " + "World"`  | `"Hello World"`  |
| Repetition    | `"Hi! " * 3`          | `"Hi! Hi! Hi! "` |
| Length        | `len("Python")`       | `6`              |
| Membership    | `'y' in "Python"`     | `True`           |
| Not in        | `'z' not in "Python"` | `True`           |

**3️⃣ Common String Methods**
| Method         | Example                     | Result          |
| -------------- | --------------------------- | --------------- |
| `upper()`      | `"hello".upper()`           | `"HELLO"`       |
| `lower()`      | `"HELLO".lower()`           | `"hello"`       |
| `capitalize()` | `"python".capitalize()`     | `"Python"`      |
| `title()`      | `"hello world".title()`     | `"Hello World"` |
| `strip()`      | `"  hello  ".strip()`       | `"hello"`       |
| `replace()`    | `"Python".replace("P","J")` | `"Jython"`      |
| `split()`      | `"a,b,c".split(",")`        | `['a','b','c']` |
| `join()`       | `",".join(['a','b','c'])`   | `"a,b,c"`       |


# Data Types Folder
This folder contains Python related to:
- Converting between data types (int, float, str, bool)  
- Type casting (explicit & implicit conversion)  

**Files:**
- `convert_data_types.py` → Practical examples of converting variables between types  
- `type_casting.py` → Demonstrates type casting and implicit conversions

Implicit vs Explicit Type Conversion in Python- **Key Differences Table**

| Feature           | Implicit Conversion  | Explicit Conversion                        |
| ----------------- | -------------------- | ------------------------------------------ |
| Who converts?     | Python automatically | Programmer manually                        |
| Also called       | Type Coercion        | Type Casting                               |
| Risk of data loss | No                   | Yes (possible)                             |
| Example           | `int → float`        | `"100" → int`                              |
| Syntax            | No function needed   | Uses `int()`, `float()`, `str()`, `bool()` |


**✅ Python Data Type Conversion Table**

| From Type         | To Type   | Example Code    | Result   | Explanation                        |
| ----------------- | --------- | --------------- | -------- | ---------------------------------- |
| String → Integer  | `int()`   | `int("100")`    | `100`    | Converts numeric string to integer |
| String → Float    | `float()` | `float("10.5")` | `10.5`   | Converts numeric string to float   |
| String → Boolean  | `bool()`  | `bool("Hello")` | `True`   | Non-empty string is True           |
| String → Boolean  | `bool()`  | `bool("")`      | `False`  | Empty string is False              |
| Integer → String  | `str()`   | `str(100)`      | `"100"`  | Converts integer to text (string)  |
| Integer → Float   | `float()` | `float(10)`     | `10.0`   | Converts integer to decimal number |
| Integer → Boolean | `bool()`  | `bool(10)`      | `True`   | Non-zero numbers are True          |
| Integer → Boolean | `bool()`  | `bool(0)`       | `False`  | Zero is False                      |
| Float → String    | `str()`   | `str(3.5)`      | `"3.5"`  | Converts float number to text      |
| Float → Integer   | `int()`   | `int(10.9)`     | `10`     | Removes decimal part (no rounding) |
| Float → Boolean   | `bool()`  | `bool(2.7)`     | `True`   | Non-zero float is True             |
| Float → Boolean   | `bool()`  | `bool(0.0)`     | `False`  | Zero float is False                |
| Boolean → Integer | `int()`   | `int(True)`     | `1`      | True becomes 1                     |
| Boolean → Integer | `int()`   | `int(False)`    | `0`      | False becomes 0                    |
| Boolean → Float   | `float()` | `float(True)`   | `1.0`    | True becomes 1.0                   |
| Boolean → Float   | `float()` | `float(False)`  | `0.0`    | False becomes 0.0                  |
| Boolean → String  | `str()`   | `str(True)`     | `"True"` | Converts boolean to text           |
| Boolean → String  | `str()`   | `str(False)`    | `"False"`| Converts boolean to text           |


# Python Data Structures
Python has several built-in data structures to store and organize data efficiently:

**1️⃣ List**
Ordered, mutable, allows duplicates
Defined using square brackets [ ]

**2️⃣ Tuple**
Ordered, immutable, allows duplicates
Defined using parentheses ( )

**3️⃣ Set**
Unordered, mutable, no duplicates
Defined using curly braces { } or set()

**4️⃣ Dictionary**
Unordered, mutable, key-value pairs
Defined using curly braces {key: value}

**🔹 Common Operations**
| Data Structure | Add                    | Remove                  | Access                 |
| -------------- | ---------------------- | ----------------------- | ---------------------- |
| List           | `append()`, `insert()` | `remove()`, `pop()`     | `list[index]`          |
| Tuple          | ❌ Immutable            | ❌ Immutable             | `tuple[index]`         |
| Set            | `add()`                | `remove()`, `discard()` | ❌ Indexing not allowed |
| Dictionary     | `dict[key] = value`    | `del dict[key]`         | `dict[key]`            |

