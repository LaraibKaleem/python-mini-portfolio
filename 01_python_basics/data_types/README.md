# Data Types Folder

This folder contains Python examples related to:

- Converting between data types (int, float, str, bool)  
- Type casting examples (explicit & implicit conversion)  

Files:

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

