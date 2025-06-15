[Contents](../Contents.md) \| [Previous (6.2 Anonymous Functions)](04_Anonymous_function.md) \| [Next (6.6 Decorators)](06_Function_decorators.md)

# 6.5 Returning Functions

This section introduces the idea of using functions to create other functions.

### Introduction

Consider the following function.

```python
def add(x, y):
    def do_add():
        print('Adding', x, y)
        return x + y
    return do_add
```

This is a function that returns another function.

```python
>>> a = add(3,4)
>>> a
<function do_add at 0x6a670>
>>> a()
Adding 3 4
7
```

### Local Variables

Observe how the inner function refers to variables defined by the outer
function.

```python
def add(x, y):
    def do_add():
        # `x` and `y` are defined above `add(x, y)`
        print('Adding', x, y)
        return x + y
    return do_add
```

Further observe that those variables are somehow kept alive after
`add()` has finished.

```python
>>> a = add(3,4)
>>> a
<function do_add at 0x6a670>
>>> a()
Adding 3 4      # Where are these values coming from?
7
```

### Closures

When an inner function is returned as a result, that inner function is known as a *closure*.

```python
def add(x, y):
    # `do_add` is a closure
    def do_add():
        print('Adding', x, y)
        return x + y
    return do_add
```

*Essential feature: A closure retains the values of all variables
 needed for the function to run properly later on.*   Think of a
closure as a function plus an extra environment that holds the values
of variables that it depends on.

### Using Closures

Closure are an essential feature of Python. However, their use if often subtle.
Common applications:

* Use in callback functions.
* Delayed evaluation.
* Decorator functions (later).

### Delayed Evaluation

Consider a function like this:

```python
def after(seconds, func):
    import time
    time.sleep(seconds)
    func()
```

Usage example:

```python
def greeting():
    print('Hello Guido')

after(30, greeting)
```

`after` executes the supplied function... later.

Closures carry extra information around.

```python
def add(x, y):
    def do_add():
        print(f'Adding {x} + {y} -> {x+y}')
    return do_add

def after(seconds, func):
    import time
    time.sleep(seconds)
    func()

after(30, add(2, 3))
# `do_add` has the references x -> 2 and y -> 3
```

### Code Repetition

Closures can also be used as technique for avoiding excessive code repetition.
You can write functions that make code.

## Exercises

Intentionally left blank, just skip.

[Contents](../Contents.md) \| [Previous (6.4 Anonymous Functions)](04_Anonymous_function.md) \| [Next (6.6 Decorators)](06_Function_decorators.md)
