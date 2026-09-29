# 🐍 Python-Learning

[Python Documentation](https://docs.python.org/)

---

## 🛠️ Basic Tools

### VS Code
**VS Code** → Text editor

### Terminal
**Terminal** → CLI → Command Line Interface

- `code file.py` → Creates a file named `file.py`
- `python file.py` → Runs the `file.py`
- `python` → Based on interpreter

---

# 🧩 Python Fundamentals

## Functions

- **Function** → A block of code that performs a particular task.
- Functions can be **built-in** or **user-defined**.
- Example: `print("hello")` → Used to print output on the screen.

### Arguments

- `"hello"` → **Argument**
- `input()` → Takes a string as an input value.

### Side Effect

- **Side effect** → Our output that appears after the execution of a program.
- It can be an **audio, visual output, or anything else**.

### Bug

- **Bug** → A mistake or error in a program.

### Return Value

- **Return value** → The output that a function returns.

---

## Variables

- **Variable** → Stores data/value in memory.
- `=` → Assignment operator.

---

## Comments

- **Comments** → Our notes that are not visible to the computer.

### Single-line Comments

```python
# This is a single-line comment
```

- `#` → Used for single-line comments.

### Multi-line Comments

```python
"""
for multi
line comments
"""
```

- `""" ... """` → Used for multi-line comments.

---

## Pseudocode

- **Pseudocode** → Expressing code in English or human language.

### Example

```python
name = input("Enter your name: ")
print("Hello, " + name)
print("Hello,", name)
```

### `+` vs `,`

- `+` → Printing one big argument by the help of `+` to add more things in it.
  - Requires space between arguments by the user.

- `,` → Taking multiple inputs together.
  - By default, a space is present between arguments.

---

# 🔤 Data Types

## String (`str`)

- **`str`** → Datatype for string.

---

## Integer (`int`)

- **`int`** → Integer datatype.
- `int` can also be used as a function in **type conversion**.

---

## Float (`float`)

- **`float`** → Decimal number.

---

# ➕ Operators

## Operators in Python

The basic operators are:

```text
+
-
*
/
%
```

- `+` → Addition
- `-` → Subtraction
- `*` → Multiplication
- `/` → Division
- `%` → Modulus

### Exponent

```python
x**2
```

- `x**2` → `x ^ 2`

---

# 💻 Python Interactive Mode

- **Interactive mode of Python** → When we type just `python` in the terminal, it shows `>>>`.
- We can perform or execute single-line codes as fast as possible.

Example:

```text
>>> 5 + 5
10
```

---

# 🔗 Concatenation

- **Concatenation** → Joining strings using `+`.

```python
str1 + str2
```

---

# ⚙️ Defining Functions

- `def` → Used to define/create a function.

Example:

```python
def hello():
    print("Hello")
```

---

# 📌 Parameters and Arguments

## Parameter

- **Parameter** → What value a function can take.
- Example: `(int)`

## Argument

- **Argument** → What value we pass to a function.
- Example: `(5)`

### Difference

```python
def square(x):      # x → parameter
    return x**2

square(5)           # 5 → argument
```

---

# ↩️ Escape Characters

- `\` → Escape character.
- Used for using different characters and not as Python syntax characters.

### New Line

- `\n` → New line character.
- `end = '\n'` → Ends a line with a new line.

---

# 📍 Positional and Named Parameters

## Positional Parameters

- **Positional parameters** → First parameter in `print`, then second, then third.
- They come in sequence and proper order.

## Named Parameters

- **Named parameters** → No order needed.
- Examples:
  - `sep`
  - `end`

---

# 📝 Format String

- **Format string** → Special string.

Example:

```python
print(f"Hello, {name}")
```

---

# 🔧 String Methods

## `str.strip()`

```python
str.strip()
```

- Removes whitespaces from a string.

---

## `str.capitalize()`

```python
str.capitalize()
```

- Capitalizes the first letter of the first word of the string.

---

## `str.title()`

```python
str.title()
```

- Capitalizes the first letter of each word of the string.

---

## `str.split(" ")`

```python
str.split(" ")
```

- Used to split a string into various substrings on the basis of whitespaces.

---

# 🛠️ Methods

- **Methods** → Built-in functions that have already defined values.

Examples:

```python
str.strip()
str.capitalize()
str.title()
str.split(" ")
```

---

# 🌐 Scope

- **Scope** → Anything defined in a block cannot be used outside that scope or block.

---

# 📚 Quick Revision

| Concept | Meaning |
|---|---|
| **Function** | Block of code that performs a particular task |
| **Variable** | Stores data/value in memory |
| **Argument** | Value passed to a function |
| **Parameter** | Value a function can take |
| **Return value** | Output returned by a function |
| **Bug** | Mistake or error in a program |
| **Pseudocode** | Code written in human language |
| **Concatenation** | Joining strings |
| **Scope** | Area where something can be accessed |
| **Method** | Built-in function associated with a value/object |
| **`def`** | Used to define/create a function |
| **`int`** | Integer datatype |
| **`float`** | Decimal number |
| **`str`** | String datatype |
| **`=`** | Assignment operator |
| **`\n`** | New line character |
| **`\`** | Escape character |
| **`+`** | Addition / string concatenation |
| **`%`** | Modulus |
| **`x**2`** | `x ^ 2` |
