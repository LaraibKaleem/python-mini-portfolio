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
