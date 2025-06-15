
[Contents](../Contents.md) \| [Previous (6.1 Pydantic)](01_Pydantic.md) \| [Next (6.3 YAML)](03_YAML.md)

# 6.2 Variable Arguments

This section covers variadic function arguments, sometimes described as
`*args` and `**kwargs`.

### Positional variable arguments (*args)

A function that accepts *any number* of arguments is said to use variable arguments.
For example:

```python
def f(x, *args):
    ...
```

Function call.

```python
f(1,2,3,4,5)
```

The extra arguments get passed as a tuple.

```python
def f(x, *args):
    # x -> 1
    # args -> (2,3,4,5)
```

### Keyword variable arguments (**kwargs)

A function can also accept any number of keyword arguments.
For example:

```python
def f(x, y, **kwargs):
    ...
```

Function call.

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

The extra keywords are passed in a dictionary.

```python
def f(x, y, **kwargs):
    # x -> 2
    # y -> 3
    # kwargs -> { 'flag': True, 'mode': 'fast', 'header': 'debug' }
```

### Combining both

A function can also accept any number of variable keyword and non-keyword arguments.

```python
def f(*args, **kwargs):
    ...
```

Function call.

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

The arguments are separated into positional and keyword components

```python
def f(*args, **kwargs):
    # args = (2, 3)
    # kwargs -> { 'flag': True, 'mode': 'fast', 'header': 'debug' }
    ...
```

This function takes any combination of positional or keyword
arguments.  It is sometimes used when writing wrappers or when you
want to pass arguments through to another function.

### Passing Tuples and Dicts

Tuples can be expanded into variable arguments.

```python
numbers = (2,3,4)
f(1, *numbers)      # Same as f(1,2,3,4)
```

Dictionaries can also be expanded into keyword arguments.

```python
options = {
    'color' : 'red',
    'delimiter' : ',',
    'width' : 400
}
f(data, **options)
# Same as f(data, color='red', delimiter=',', width=400)
```

## Exercises

### Exercise 6.4: A simple example of variable arguments

Try defining the following function:

```python
>>> def avg(x,*more):
        return float(x+sum(more))/(1+len(more))

>>> avg(10,11)
10.5
>>> avg(3,4,5)
4.0
>>> avg(1,2,3,4,5,6)
3.5
>>>
```

Notice how the parameter `*more` collects all of the extra arguments.

### Exercise 6.5: Passing tuple and dicts as arguments

Suppose you read some data from a file and obtained a dictionary such as
this:

```
>>> data = { 'name': 'GOOG', 'shares': 100, 'price': 490.1 }
>>>
```

Now, suppose you wanted to create a `Stock` object from this
data.  If you try to pass `data` directly, it doesn't work:

```
>>> from stock import Stock
>>> s = Stock(data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 4 arguments (2 given)
>>>
```

This is easily fixed using `**data` instead.  Try this:

```python
>>> s = Stock(**data)
>>> s
Stock('GOOG', 100, 490.1)
>>>
```

### Exercise 6.6: Creating a list of instances

In your `report.py` program, you created a list of instances
using code like this:

```python
    portfolio = [Stock(d['name'], d['shares'], d['price'])
                  for d in portdicts]
```

You can simplify that code using `Stock(**d)` instead.  Make that change.

[Contents](../Contents.md) \| [Previous (6.1 Pydantic)](01_Pydantic.md) \| [Next (6.3 YAML)](03_YAML.md)
