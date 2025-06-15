[Contents](../Contents.md) \| [Previous (1.5 Lists)](05_Lists.md) \| [Next (1.7 Functions)](07_Functions.md)

# 1.6 File Management

Let’s talk about working with files. This is something you’ll do often—whether reading config files, processing logs, or generating output. Python has excellent built-in support for file I/O, and it's best to adopt modern, readable idioms from the start.

### File Input and Output

Open a file.

```python
f = open('foo.txt', 'rt')     # Open for reading (text)
g = open('bar.txt', 'wt')     # Open for writing (text)
```

Read all of the data.

```python
data = f.read()

# Read only up to 'maxbytes' bytes
data = f.read([maxbytes])
```

Write some text.

```python
g.write('some text')
```

Close when you are done.

```python
f.close()
g.close()
```

Files should be properly closed and it's an easy step to forget.
Thus, the preferred approach is to use the `with` statement like this.

```python
with open(filename, 'rt') as file:
    # Use the file `file`
    ...
    # No need to close explicitly
...statements
```

This automatically closes the file when control leaves the indented code block.

### File Reading and Writing Idioms (with `pathlib`)

In modern Python code, the `pathlib` module provides a more intuitive and object-oriented way to work with files and directories.
It is now the **preferred** method over older approaches using `open()` and string-based file paths.

Here’s how to read a text file:

```python
from pathlib import Path

file_path = Path("example.txt")
content = file_path.read_text()
print(content)
```

Writing to a file is just as simple:

```python
from pathlib import Path

output_path = Path("output.txt")
output_path.write_text("This is some output text.")
```

### File Iteration

You can also iterate over the lines of a file using `open()` if needed:

```python
from pathlib import Path

with Path("example.txt").open("r") as f:
    for line in f:
        print(line.strip())
```

This ensures the file is properly closed after reading and handles large files efficiently.

### Creating and Checking Paths

`pathlib` makes it easier to manipulate paths, check if files exist, or create directories:

```python
from pathlib import Path

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

if data_dir.exists():
    print("Directory exists!")

log_file = data_dir / "log.txt"
log_file.write_text("Starting new log file.")
```

## Exercises

These exercises depend on a file `Data/portfolio.csv`.  The file
contains a list of lines with information on a portfolio of stocks.
It is assumed that you are working in the `practical-python/Work/`
directory.  If you're not sure, you can find out where Python thinks
it's running by doing this:

```python
>>> import os
>>> os.getcwd()
'/Users/beazley/Desktop/practical-python/Work' # Output vary
>>>
```

### Exercise 1.26: File Preliminaries

First, try reading the entire file all at once as a big string:

```python
>>> from pathlib import Path
>>> data = Path('Data/portfolio.csv').read_text()

>>> data
'name,shares,price\n"AA",100,32.20\n"IBM",50,91.10\n"CAT",150,83.44\n"MSFT",200,51.23\n"GE",95,40.37\n"MSFT",50,65.10\n"IBM",100,70.44\n'
>>> print(data)
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>>
```

In the above example, it should be noted that Python has two modes of
output.  In the first mode where you type `data` at the prompt, Python
shows you the raw string representation including quotes and escape
codes.  When you type `print(data)`, you get the actual formatted
output of the string.

Although reading a file all at once is simple, it is often not the
most appropriate way to do it—especially if the file happens to be
huge or if contains lines of text that you want to handle one at a
time.

To read a file line-by-line, use a for-loop like this:

```python
>>> with Path('Data/portfolio.csv').open('rt') as f:
        for line in f:
            print(line, end='')

name,shares,price
"AA",100,32.20
"IBM",50,91.10
...
>>>
```

When you use this code as shown, lines are read until the end of the
file is reached at which point the loop stops.

On certain occasions, you might want to manually read or skip a
*single* line of text (e.g., perhaps you want to skip the first line
of column headers).

```python
>>> f = Path('Data/portfolio.csv').open('rt')
>>> headers = next(f)
>>> headers
'name,shares,price\n'
>>> for line in f:
    print(line, end='')

"AA",100,32.20
"IBM",50,91.10
...
>>> f.close()
>>>
```

`next()` returns the next line of text in the file. If you were to call it repeatedly, you would get successive lines.
However, just so you know, the `for` loop already uses `next()` to obtain its data.
Thus, you normally wouldn’t call it directly unless you’re trying to explicitly skip or read a single line as shown.

Once you’re reading lines of a file, you can start to perform more processing such as splitting.
For example, try this:

```python
>>> from pathlib import Path
>>> with Path('Data/portfolio.csv').open('rt') as f:
...     headers = next(f).split(",")
...     print(headers)
...     for line in f:
...         row = line.split(",")
...         print(row)
...
['name', 'shares', 'price\n']
['"AA"', '100', '32.20\n']
['"IBM"', '50', '91.10\n']...
```

### Exercise 1.27: Reading a data file

Now that you know how to read a file, let’s write a program to perform a simple calculation.

The columns in `portfolio.csv` correspond to the stock name, number of
shares, and purchase price of a single stock holding.  Write a program called
`pcost.py` that opens this file, reads all lines, and calculates how
much it cost to purchase all of the shares in the portfolio.

*Hint: to convert a string to an integer, use `int(s)`. To convert a string to a floating point, use `float(s)`.*

Your program should print output such as the following:

```bash
Total cost 44671.15
```

### Exercise 1.28: Other kinds of "files"

What if you wanted to read a non-text file such as a gzip-compressed
datafile?  The builtin `open()` function won’t help you here, but
Python has a library module `gzip` that can read gzip compressed
files.

Try it:

```python
>>> import gzip
>>> with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')

... look at the output ...
>>>
```

Note: Including the file mode of `'rt'` is critical here.  If you forget that,
you'll get byte strings instead of normal text strings.

[Contents](../Contents.md) \| [Previous (1.5 Lists)](05_Lists.md) \| [Next (1.7 Functions)](07_Functions.md)
