[Contents](../Contents.md) \| [Previous (9.1 Packages)](01_Packages.md) \| [Next (9.3 Distribution)](03_Distribution.md)

# 9.2 Third Party Modules

Python has a large library of built-in modules (*batteries included*).

There are even more third party modules. Check them in the [Python Package Index](https://pypi.org/) or PyPi.
Or just do a Google search for a specific topic.

How to handle third-party dependencies is an ever-evolving topic with
Python.  This section merely covers the basics to help you wrap
your brain around how it works.

### The Module Search Path

`sys.path` is a directory that contains the list of all directories
checked by the `import` statement. Look at it:

```python
>>> import sys
>>> sys.path
... look at the result ...
>>>
```

If you import something and it's not located in one of those
directories, you will get an `ImportError` exception.

### Standard Library Modules

Modules from Python's standard library usually come from a location
such as `/usr/local/lib/python3.6'.  You can find out for certain
by trying a short test:

```python
>>> import re
>>> re
<module 're' from '/usr/local/lib/python3.6/re.py'>
>>>
```

Simply looking at a module in the REPL is a good debugging tip
to know about.  It will show you the location of the file.

### Third-party Modules

Third party modules are usually located in a dedicated
`site-packages` directory.   You'll see it if you perform
the same steps as above:

```python
>>> import numpy
>>> numpy
<module 'numpy' from '/usr/local/lib/python3.6/site-packages/numpy/__init__.py'>
>>>
```

Again, looking at a module is a good debugging tip if you're
trying to figure out why something related to `import` isn't working
as expected.

### Installing Modules

The most common technique for installing a third-party module is to use
`pip`.  For example:

```bash
bash % python3 -m pip install packagename
```

This command will download the package and install it in the `site-packages`
directory.

[Contents](../Contents.md) \| [Previous (9.1 Packages)](01_Packages.md) \| [Next (9.3 Distribution)](03_Distribution.md)
