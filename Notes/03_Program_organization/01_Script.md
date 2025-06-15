[Contents](../Contents.md) \| [Previous (2.6 Object Model)](../02_Working_with_data/06_Objects.md) \| [Next (3.2 More on Functions)](02_More_functions.md)

# 3.1 Scripting

In this part we look more closely at the practice of writing Python
scripts.

### What is a Script?

A *script* is a program that runs a series of statements and stops.

```python
# program.py

statement1
statement2
statement3
...
```

We have mostly been writing scripts to this point.

### A Problem

If you write a useful script, it will grow in features and
functionality.  You may want to apply it to other related problems.
Over time, it might become a critical application.  And if you don't
take care, it might turn into a huge tangled mess.  So, let's get
organized.

### Defining Things

Names must always be defined before they get used later.

```python
def square(x):
    return x*x

a = 42
b = a + 2     # Requires that `a` is defined

z = square(b) # Requires `square` and `b` to be defined
```

**The order is important.**
You almost always put the definitions of variables and functions near the top.

### Defining Functions

It is a good idea to put all of the code related to a single *task* all in one place.
Use a function.

```python
def read_prices(filename):
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

A function also simplifies repeated operations.

```python
oldprices = read_prices('oldprices.csv')
newprices = read_prices('newprices.csv')
```

### Function Definition

Functions can be *defined* in any order.

```python
def foo(x):
    bar(x)

def bar(x):
    statements

# OR
def bar(x):
    statements

def foo(x):
    bar(x)
```

Functions must only be defined prior to actually being *used* (or called) during
program execution.

```python
foo(3)        # foo must be defined already
```

Stylistically, it is probably more common to see functions defined in
a *bottom-up* fashion.

### Bottom-up Style

Functions are treated as building blocks.
The smaller/simpler blocks go first.

```python
# myprogram.py
def foo(x):
    ...

def bar(x):
    ...
    foo(x)          # Defined above
    ...

def spam(x):
    ...
    bar(x)          # Defined above
    ...

spam(42)            # Code that uses the functions appears at the end
```

Later functions build upon earlier functions.  Again, this is only
a point of style.  The only thing that matters in the above program
is that the call to `spam(42)` go last.

### Function Design

Ideally, functions should be a *black box*.
They should only operate on passed inputs and avoid global variables
and mysterious side-effects.  Your main goals: *Modularity* and *Predictability*.

## Exercises

In section 2, you wrote a program called `report.py` that printed out
a report showing the performance of a stock portfolio.  This program
consisted of some functions. For example:

```python
def read_portfolio(filename: Path) -> List[Dict[str, Any]]:
    """
    Read a stock portfolio CSV file into a list of Stock namedtuples.

    Args:
        filename (Path): Path to the CSV file with portfolio data.
    
    Returns:
        Dict[str, Any]: A list of Stock dictinaries with the keys name, shares, and price.
    """
    portfolio = []
    with filename.open("rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                 'name'   : record['name'],
                 'shares' : int(record['shares']),
                 'price'   : float(record['price'])
            }
            portfolio.append(stock)

    return portfolio
...
```

However, there were also portions of the program that just performed a
series of scripted calculations.  This code appeared near the end of
the program. For example:

```python
...

# Output the header
print(' '.join([f'{header:>10s}' for header in TableRow._fields]))
print(f'{"---------- "*len(TableRow._fields)}')

# Print the rows
for row in make_report(portfolio, prices):
    print(f'{row.name:>10s} {row.shares:>10d} {row.price:>10.2f} {row.change:>10.2f}')
...
```

In this exercise, we’re going take this program and organize it a
little more strongly around the use of functions.

### Exercise 3.1: Structuring a program as a collection of functions

Modify your `report.py` program so that all major operations,
including calculations and output, are carried out by a collection of
functions. Specifically:

* Create a function `print_report(report)` that prints out the report.
* Change the last part of the program so that it is nothing more than a series of function calls and no other computation.

### Exercise 3.2: Creating a top-level function for program execution

Take the last part of your program and package it into a single
function `portfolio_report(portfolio_filename, prices_filename)`.
Have the function work so that the following function call creates the
report as before:

```python
portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
```

In this final version, your program will be nothing more than a series
of function definitions followed by a single function call to
`portfolio_report()` at the very end (which executes all of the steps
involved in the program).

By turning your program into a single function, it becomes easy to run
it on different inputs.  For example, try these statements
interactively after running your program:

```python
>>> portfolio_report('Data/portfolio2.csv', 'Data/prices.csv')
... look at the output ...
>>> files = ['Data/portfolio.csv', 'Data/portfolio2.csv']
>>> for name in files:
        print(f'{name:-^43s}')
        portfolio_report(name, 'Data/prices.csv')
        print()

... look at the output ...
>>>
```

### Commentary

Python makes it very easy to write relatively unstructured scripting code
where you just have a file with a sequence of statements in it. In the
big picture, it's almost always better to utilize functions whenever
you can.  At some point, that script is going to grow and you'll wish
you had a bit more organization.  Also, a little known fact is that Python
runs a bit faster if you use functions.

[Contents](../Contents.md) \| [Previous (2.6 Object Model)](../02_Working_with_data/06_Objects.md) \| [Next (3.2 More on Functions)](02_More_functions.md)