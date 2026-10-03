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

# 🔀 Conditional Statements

- **Conditional statements** → We ask a question and then answer it based on whether the condition is `True` or `False`.

## Comparison Operators

The symbols used for comparison are:

```text
==    Equal to
!=    Not equal to
>     Greater than
>=    Greater than or equal to
<     Less than
<=    Less than or equal to
```

---

## `if`

- **`if`** → Used to ask a question or check a condition.

Example:

```python
if x < y:
    print("x is smaller")
```

- `x < y` → **Boolean expression**
- A Boolean expression has a **yes or no answer**, represented as `True` or `False`.

---

## Boolean (`bool`)

- **`bool`** → A datatype that means **True or False**.
- Boolean values are represented as:
  - `True`
  - `False`
- The first letter is always **capital** in Python.

Example:

```python
x = True
y = False
```

---

## Indentation

- **Indentation** → Spaces at the beginning of a line that tell Python that the line belongs to the previous block of code.
- The indented code is executed only when the condition is `True`.

Example:

```python
if x < y:
    print("x is smaller")
```

Here, `print()` is indented, so it belongs to the `if` block.

---

## `:`

- `:` → Used to represent the **start of a block of code**.
- **Indentation** tells Python what is inside that block.

Example:

```python
if x < y:
    print("x is smaller")
```

Here:

- `:` → Starts the block.
- Indentation → Shows what is inside the block.

---

# 🔁 `if`, `elif` and `else`

`if`, `elif` and `else` are **keywords** in Python.

## `if`

- `if` → Checks a condition.
- Multiple `if` statements are independent, so **all the `if` statements will be checked until the end of the code**.

Example:

```python
if x > 0:
    print("Positive")

if x < 10:
    print("Less than 10")
```

Both conditions can be checked.

---

## `elif`

- `elif` → Means **"else if"**.
- When using an `if`/`elif` chain, Python stops checking the remaining conditions once it finds a `True` condition.

Example:

```python
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
```

Once one condition is `True`, the remaining `elif` conditions are not checked.

---

## `else`

- `else` → Runs when **all the conditions above it are `False`**.
- It runs by default when none of the previous conditions are satisfied.

Example:

```python
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
```

---

# 🔗 Logical Operators

- **`and`** and **`or`** are keywords used for combining conditions.

### `and`

Both conditions must be `True`.

```python
if x > 0 and x < 10:
    print("x is between 0 and 10")
```

### `or`

At least one condition must be `True`.

```python
if x < 0 or x > 10:
    print("x is outside the range")
```

---

## Python's Special Comparison Feature

- Python has a special feature where instead of writing two conditions and comparing them using `and` or `or`, we can sometimes combine the comparisons directly.

Example:

```python
if 0 < x < 10:
    print("x is between 0 and 10")
```

This is equivalent to:

```python
if x > 0 and x < 10:
    print("x is between 0 and 10")
```

---

# 🔢 Parity

- **Parity** → Whether a number is **even or odd**.

## Modulus Operator `%`

- `%` → **Modulus operator**.
- It gives the **remainder** when one number is divided by another.

Example:

```python
10 % 3
```

Output:

```text
1
```

Because when `10` is divided by `3`, the remainder is `1`.

---

## Even Numbers

- An **even number** is a number that is divisible by `2` and gives a remainder of `0`.

Example:

```python
10 % 2
```

Output:

```text
0
```

Therefore, `10` is even.

### Checking whether a number is even or odd

```python
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

# 🐍 Pythonic

- **Pythonic** → A term used by the Python community to describe code that follows the style, principles and idioms that are considered natural and readable in Python.

- Python has many syntaxes that are closely related to **human language and English**, making Python code relatively easy to read compared with many other programming languages.

---

# 🔀 Match-Case

- **`match`** → A keyword similar to `switch` in other programming languages.
- Python uses **`case`** inside a `match` statement.

Example:

```python
match number:
    case 1:
        print("One")
    case 2:
        print("Two")
```

---

## Default Case: `_`

- When we don't have a matching `case`, or we want a **default value**, we use `_`.

Example:

```python
match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Something else")
```

- `_` → Acts as the default/wildcard case in this context.

### `break` and `default`

- In Python's `match` statement, we **do not need to use `break`** after each case like in traditional `switch` statements.
- We also use `_` instead of a `default` keyword.

---

# 📌 Conditional Statements — Quick Revision

| Concept | Meaning |
|---|---|
| `if` | Checks a condition |
| `elif` | Checks another condition if previous condition is false |
| `else` | Runs when all previous conditions are false |
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `>=` | Greater than or equal to |
| `<` | Less than |
| `<=` | Less than or equal to |
| `and` | Both conditions must be true |
| `or` | At least one condition must be true |
| `bool` | Boolean datatype |
| `True` | Boolean true value |
| `False` | Boolean false value |
| `%` | Modulus/remainder operator |
| `match` | Used for pattern matching |
| `case` | Defines a pattern/case inside `match` |
| `_` | Default/wildcard case in `match` |
| `:` | Starts a block |
| Indentation | Defines what belongs to a block |
