
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

