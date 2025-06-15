[Contents](../Contents.md) \| [Previous (3.4 Modules)](04_Modules.md) \| [Next (3.6 Design Discussion)](06_Design_discussion.md)

# 3.5 Main Module

This section introduces the concept of a main program or main module.

### Main Functions

In many programming languages, there is a concept of a *main* function or method.

```c
// c / c++
int main(int argc, char *argv[]) {
    ...
}
```

```java
// java
class myprog {
    public static void main(String args[]) {
        ...
    }
}
```

This is the first function that executes when an application is launched.

### Python Main Module

Python has no *main* function or method.  Instead, there is a *main*
module. The *main module* is the source file that runs first.

```bash
bash % python3 prog.py
...
```

Whatever file you give to the interpreter at startup becomes *main*. It doesn't matter the name.

### `main` Check

It is standard practice for modules that run as a main script to use this convention:

```python
# prog.py
...
if __name__ == '__main__':
    # Running as the main program ...
    statements
    ...
```

Statements enclosed inside the `if` statement become the *main* program.

### Main programs vs. library imports

Any Python file can either run as main or as a library import:

```bash
bash % python3 prog.py # Running as main
```

```python
import prog   # Running as library import
```

In both cases, `__name__` is the name of the module.  However, it will only be set to `__main__` if
running as main.

Usually, you don't want statements that are part of the main program
to execute on a library import.  So, it's common to have an `if-`check
in code that might be used either way.

```python
if __name__ == '__main__':
    # Does not execute if loaded with import ...
```

### Command Line Tools

Python is often used for command-line tools

```bash
bash % python3 report.py portfolio.csv prices.csv
```

It means that the scripts are executed from the shell /
terminal. Common use cases are for automation, background tasks, etc.

### Standard I/O

Standard Input / Output (or stdio) are files that work the same as normal files.

```python
sys.stdout
sys.stderr
sys.stdin
```

By default, print is directed to `sys.stdout`.  Input is read from
`sys.stdin`.  Tracebacks and errors are directed to `sys.stderr`.

Be aware that *stdio* could be connected to terminals, files, pipes, etc.

```bash
bash % python3 prog.py > results.txt
# or
bash % cmd1 | python3 prog.py | cmd2
```

### Environment Variables

Environment variables are set in the shell.

```bash
bash % setenv NAME dave
bash % setenv RSH ssh
bash % python3 prog.py
```

`os.environ` is a dictionary that contains these values.

```python
import os

name = os.environ['NAME'] # 'dave'
```

Changes are reflected in any subprocesses later launched by the program.

### Program Exit

Program exit is handled through exceptions.

```python
raise SystemExit
raise SystemExit(exitcode)
raise SystemExit('Informative message')
```

An alternative.

```python
import sys
sys.exit(exitcode)
```

A non-zero exit code indicates an error.

### The `#!` line

On Unix, the `#!` line can launch a script as Python.
Add the following to the first line of your script file.

```python
#!/usr/bin/env python3
# prog.py
...
```

It requires the executable permission.

```bash
bash % chmod +x prog.py
# Then you can execute
bash % prog.py
... output ...
```

*Note: The Python Launcher on Windows also looks for the `#!` line to indicate language version.*

## Exercises

### Exercise 3.15: Making Scripts

Modify the `report.py` and `pcost.py` programs so that they can
execute as a script on the command line and add to each the `main` function:

```bash
bash $ python3 report.py Data/portfolio.csv Data/prices.csv
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84

bash $ python3 pcost.py Data/portfolio.csv
Total cost: 44671.15
```

[Contents](../Contents.md) \| [Previous (3.4 Modules)](04_Modules.md) \| [Next (3.6 Design Discussion)](06_Design_discussion.md)
