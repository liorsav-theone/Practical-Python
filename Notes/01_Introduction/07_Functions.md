[Contents](../Contents.md) \| [Previous (1.6 Files)](06_Files.md) \| [Next (2.0 Working with Data)](../02_Working_with_data/00_Overview.md)

# 1.7 Functions

As your programs start to get larger, you'll want to get organized.  This section
briefly introduces functions and library modules.  Error handling with exceptions is also introduced.

### Custom Functions

Use functions for code you want to reuse. Here is a function definition:

```python
def sumcount(n: int) -> int:
    """
    Calculate the sum of the first `n` positive integers.

    Args:
        n (int): A non-negative integer representing the upper bound.

    Returns:
        int: The sum of integers from 1 to `n`. Returns 0 if `n` <= 0.
    """
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total
```

To call a function.

```python
a = sumcount(100)
```

A function is a series of statements that perform some task and return a result.
The `return` keyword is needed to explicitly specify the return value of the function.

### Type Hints

Python supports optional type hints, which make your code more readable and help
with tooling, autocompletion, and catching bugs early using static analysis
tools like `mypy`.

Here’s how to add type hints to a simple function:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

- name: str indicates that name should be a string.
- -> str tells us that the function returns a string.

Type hints don’t change how your code runs — they are completely optional at
runtime. But they’re a best practice in production code, especially when writing
shared tools or working with structured data (e.g., using pydantic).

You can also annotate variables:

```python
count: int = 0
users: list[str] = []
```

But this is rarely used and not recommended.

If you're not sure about a type or want flexibility, use Any from the typing module:

```python
from typing import Any

def debug_print(value: Any) -> None:
    print(value)
```

### Docstrings

A **docstring** is a special string placed immediately after a function, class,
or module definition. It serves as built-in documentation and is accessible with
`help()` or in editors like VS Code.

Here’s a function with a docstring:

```python
def greet(name: str) -> str:
    """Return a greeting string for the given name."""
    return f"Hello, {name}"
```

You can write more detailed multi-line docstrings using triple quotes:

```python
def divide(a: float, b: float) -> float:
    """
    Divide two numbers and return the result.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    return a / b
```

Clear, concise docstrings make your code easier to maintain and understand —
especially in shared tools or utility libraries.

### Library Functions

Python comes with a large standard library.
Library modules are accessed using `import`.
For example:

```python
import math
x = math.sqrt(10)

import urllib.request
u = urllib.request.urlopen('http://www.python.org/')
data = u.read()
```

We will cover libraries and modules in more detail later.

### Errors and exceptions

Functions report errors as exceptions.  An exception causes a function to abort and may
cause your entire program to stop if unhandled.

Try this in your python REPL.

```python
>>> int('N/A')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'N/A'
>>>
```

For debugging purposes, the message describes what happened, where the error occurred,
and a traceback showing the other function calls that led to the failure.

### Catching and Handling Exceptions

Exceptions can be caught and handled.

To catch, use the `try - except` statement.

```python
for line in file:
    fields = line.split(',')
    try:
        shares = int(fields[1])
    except ValueError:
        print("Couldn't parse", line)
    ...
```

The name `ValueError` must match the kind of error you are trying to catch.

It is often difficult to know exactly what kinds of errors might occur
in advance depending on the operation being performed.  For better or
for worse, exception handling often gets added *after* a program has
unexpectedly crashed (i.e., "oh, we forgot to catch that error. We
should handle that!").

### Raising Exceptions

To raise an exception, use the `raise` statement.

```python
raise RuntimeError('What a kerfuffle')
```

This will cause the program to abort with an exception traceback. Unless caught by a `try-except` block.

```bash
% python3 foo.py
Traceback (most recent call last):
  File "foo.py", line 21, in <module>
    raise RuntimeError("What a kerfuffle")
RuntimeError: What a kerfuffle
```

## Exercises

### Exercise 1.29: Defining a function

Try defining a simple function:

```python
>>> def greeting(name):
        print('Hello', name)

>>> greeting('Guido')
Hello Guido
>>> greeting('Paula')
Hello Paula
>>>
```

If the first statement of a function is a string, it serves as documentation.
Try typing a command such as `help(greeting)` to see it displayed.

### Exercise 1.30: Turning a script into a function

Take the code you wrote for the `pcost.py` program in [Exercise 1.27](06_Files.md)
and turn it into a function `portfolio_cost(filename)`.  This
function takes a filename as input, reads the portfolio data in that
file, and returns the total cost of the portfolio as a float.

To use your function, change your program so that it looks something
like this:

```python
def portfolio_cost(filename: Path) -> float:
    ...
    # Your code here
    ...

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
```

When you run your program, you should see the same output as before.
After you’ve run your program, you can also call your function
interactively by typing this:

```bash
bash $ python3 -i pcost.py
```

This will allow you to call your function from the interactive mode.

```python
>>> portfolio_cost('Data/portfolio.csv')
44671.15
>>>
```

Being able to experiment with your code interactively is useful for
testing and debugging.

### Exercise 1.31: Error handling

What happens if you try your function on a file with some missing fields?

```python
>>> portfolio_cost('Data/missing.csv')
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "pcost.py", line 11, in portfolio_cost
    nshares    = int(fields[1])
ValueError: invalid literal for int() with base 10: ''
>>>
```

At this point, you’re faced with a decision. To make the program work
you can either sanitize the original input file by eliminating bad
lines or you can modify your code to handle the bad lines in some
manner.

Modify the `pcost.py` program to catch the exception, print a warning
message, and continue processing the rest of the file.

### Exercise 1.32: Using a library function

Python comes with a large standard library of useful functions.  One
library that might be useful here is the `csv` module. You should use
it whenever you have to work with CSV data files.  Here is an example
of how it works:

```python
>>> import csv
>>> f = Path('Data/portfolio.csv').open("r")
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name', 'shares', 'price']
>>> for row in rows:
        print(row)

['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
>>> f.close()
>>>
```

One nice thing about the `csv` module is that it deals with a variety
of low-level details such as quoting and proper comma splitting.  In
the above output, you’ll notice that it has stripped the double-quotes
away from the names in the first column.

Modify your `pcost.py` program so that it uses the `csv` module for
parsing and try running earlier examples.

### Exercise 1.33: Reading from the command line

In the `pcost.py` program, the name of the input file was originally hardcoded:

```python
# pcost.py

def portfolio_cost(filename: Path) -> float:
    ...
    # Your code here
    ...

cost = portfolio_cost(Path("Data/portfolio.csv"))
print("Total cost:", cost)
```

That works fine for testing, but in real-world scripts you’ll often want to pass file paths or other settings via command-line arguments.

`argparse` is a built-in Python module used to create user-friendly command-line interfaces (CLIs). It allows your scripts to accept arguments and options from the command line, providing automatic help messages, input validation, and cleaner code.

A flexible approach is to use the argparse module. Try changing the bottom part of the program as follows:

```python
# pcost.py
import argparse
from pathlib import Path

def portfolio_cost(filename: Path) -> float:
    ...
    # Your code here
    ...

parser = argparse.ArgumentParser(description="Calculate the total cost of a portfolio file.")
parser.add_argument("filename", type=Path, help="Path to the input CSV file")
args = parser.parse_args()

cost = portfolio_cost(args.filename)
print("Total cost:", cost)
```

This version provides help messages and input validation. To run your script from the terminal:

```bash
bash % python3 pcost.py Data/portfolio.csv
Total cost: 44671.15
```

If you run the script without arguments or with -h, you’ll get a usage message like this:

```bash
bash % python3 pcost.py -h
usage: pcost.py [-h] filename

Calculate the total cost of a portfolio file.

positional arguments:
  filename    Path to the input CSV file

optional arguments:
  -h, --help  show this help message and exit
```

[Contents](../Contents.md) \| [Previous (1.6 Files)](06_Files.md) \| [Next (2.0 Working with Data)](../02_Working_with_data/00_Overview.md)
