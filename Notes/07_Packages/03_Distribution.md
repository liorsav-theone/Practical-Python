[Contents](../Contents.md) \| [Previous (9.2 Third Party Packages)](02_Third_party.md) \| [Next (The End)](TheEnd.md)

# 9.3 Distribution

At some point you might want to give your code to someone else, possibly just a co-worker.
This section gives the most basic technique of doing that.   For more detailed
information, you'll need to consult the Python Packaging User Guide.

### Creating a setup.py file

Add a `setup.py` file to the top-level of your project directory.

```python
# setup.py
import setuptools

setuptools.setup(
    name="porty",
    version="0.0.1",
    author="Your Name",
    author_email="you@example.com",
    description="Practical Python Code",
    packages=setuptools.find_packages(),
)
```

### Creating MANIFEST.in

If there are additional files associated with your project, specify them with a `MANIFEST.in` file.
For example:

```txt
# MANIFEST.in
include *.csv
```

Put the `MANIFEST.in` file in the same directory as `setup.py`.

### Creating a source distribution

To create a distribution of your code, use the `setup.py` file.  For example:

```bash
bash % python setup.py sdist
```

This will create a `.tar.gz` or `.zip` file in the directory `dist/`.  That file is something
that you can now give away to others.

### Installing your code

Others can install your Python code using `pip` in the same way that they do for other
packages.  They simply need to supply the file created in the previous step.
For example:

```bash
bash % python -m pip install porty-0.0.1.tar.gz
```

### Installing Packages in Editable Mode (`-e`)

When you're actively developing a Python project, installing your package in editable mode can significantly simplify your workflow. Editable installations allow you to make changes to your codebase and have those changes immediately reflected without needing to reinstall the package each time.

To install your package interactively (editable mode), use the following command:

```bash
pip install -e .
```

Here's what this command does:

* The `-e` or `--editable` flag tells `pip` to install your package as a symbolic link rather than copying files.
* The `.` refers to the current directory containing your `setup.py` file.

Now, when you modify your source code, the changes will automatically take effect in your environment.

#### Example

If your project's structure is:

```bash
my_project/
├── setup.py
└── my_package/
    └── __init__.py
```

Run this in your terminal:

```bash
pip install -e .
```

Now, changes made inside `my_package` immediately reflect when you import and use it, greatly speeding up your development and testing cycles.

### Commentary

The steps above describe the absolute most minimal basics of creating
a package of Python code that you can give to another person.  In
reality, it can be much more complicated depending on third-party
dependencies, whether or not your application includes foreign code
(i.e., C/C++), and so forth.  Covering that is outside the scope of
this course.  We've only taken a tiny first step.

## Exercises

### Exercise 9.5:  Make a package

Take the `porty-app/` code you created for Exercise 9.3 and see if you
can recreate the steps described here.  Specifically, add a `setup.py`
file and a `MANIFEST.in` file to the top-level directory.
Create a source distribution file by running `python setup.py sdist`.

As a final step, see if you can install your package into a Python
virtual environment.

[Contents](../Contents.md) \| [Previous (9.2 Third Party Packages)](02_Third_party.md) \| [Next (The End)](TheEnd.md)
