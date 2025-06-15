[Contents](../Contents.md) \| [Prev (6.2 Variable Arguments)](02_Variable_arguments.md) \| [Next (6.4 Anonymous Function)](04_Anonymous_function.md)

# Into To YAML

YAML is a portable and widely used data serialization format.
Unlike the more compact JSON or verbose XML formats, YAML
emphasizes human readability with block indentation, which
should be familiar to most Python programmers.

While Python comes with *batteries included*,it lacks
built-in support for YAML. Still, you can read and write
YAML documents in Python by installing a third-party library,
such as PyYAML.

### Crash Course in YAML

YAML, which rhymes with camel, is a recursive acronym that
stands for YAML Ain’t Markup Language because it’s not a markup language!
YAML was originally meant to simplify Extensible Markup Language (XML),
but in reality, it has a lot more in common with JavaScript Object Notation (JSON).
In fact, it’s a superset of JSON.

If you’re familiar with XML or JSON, then you might be wondering what
YAML brings to the table. All three are major data interchange formats,
which share some overlapping features. For example, they’re all text
based and more or less human readable.
At the same time, they differ in many respects, which you’ll find out next.

Now have a look at a sample document expressed in all three data formats but representing the same person. You can click to expand the collapsible sections and reveal data serialized in those formats:

#### XML

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<person firstName="John" lastName="Doe">
    <dateOfBirth>1969-12-31</dateOfBirth>
    <married>true</married>
    <spouse>
        <person firstName="Jane" lastName="Doe">
            <dateOfBirth/> <!- This is a comment -->
        </person>
    </spouse>
</person>
```

#### JSON

```json
{
    "person": {
        "dateOfBirth": "1969-12-31",
        "firstName": "John",
        "lastName": "Doe",
        "married": true,
        "spouse": {
            "dateOfBirth": null,
            "firstName": "Jane",
            "lastName": "Doe"
        }
    }
}
```

#### YAML

```yaml
person:
  dateOfBirth: 1969-12-31
  firstName: John
  lastName: Doe
  married: true
  spouse:
    dateOfBirth: null  # This is a comment
    firstName: Jane
    lastName: Doe
```

At first glance, XML appears to have the most intimidating syntax, which adds a lot of noise. JSON greatly improves the situation in terms of simplicity, but it still buries information beneath mandatory delimiters. On the other hand, YAML uses Python-style block indentation to define the structure, making it look clean and straightforward. The downside is that you can’t collapse whitespace to reduce size when transferring messages over the wire.

### Practical Uses of YAML

As noted earlier, YAML is mostly praised for its readability, which makes it perfect for storing all kinds of configuration data in a human-readable format. It became especially popular among DevOps engineers, who’ve built automation tools around it.

### Loading YAML Documents in Python

To read YAML files in Python, you typically use the `PyYAML` library combined with Python's convenient file handling tools. The general workflow involves opening a YAML file, parsing its contents, and converting it into Python data structures, usually dictionaries.

Consider the following YAML content saved in a file named example.yaml:

```yaml
person:
  name: John Doe
  age: 30
  married: true
  children:
    - Alice
    - Bob
```

You can load this YAML file into Python like this:

```python
>>> from pathlib import Path
>>> import yaml
>>> yaml_content = Path("example.yaml").read_text()
>>> data = yaml.safe_load(yaml_content)
>>> data
{'person': {'name': 'John Doe', 'age': 30, 'married': True, 'children': ['Alice', 'Bob']}}
```

### Simple Integration with Pydantic

Integrating YAML with Pydantic is straightforward: you load your YAML data into a dictionary using PyYAML, then directly feed this dictionary into a Pydantic model. This allows you to effortlessly leverage Pydantic’s powerful data validation and serialization features with YAML configurations.

## Exercises

Let's experiment with YAML files and learn how to integrate them seamlessly into our Python code.

### Exercises 6.7

Add the following function to the fileparse.py file:

```python

def parse_yaml(lines: Any) -> Dict[Any, Any]:
```

Implement this function with logic that parses YAML file contents into a Python dictionary.

Although this function might seem short and straightforward, encapsulating YAML parsing logic here ensures that `fileparse.py` serves as a centralized module containing all the necessary functions to parse different file types. This practice promotes clean and maintainable code, making future parsing tasks simpler and consistent.

### Exercises 6.8

Use your new function to read the `stock.yaml` file and convert its contents into a `Stock` object:

```python
>>> from fileparse import parse_yaml
>>> from pathlib import Path
>>> with Path('Data/stock.yaml').open('rt') as f:
...    stock = Stock(**prase_yaml(f))
...
>>> stock
<<< See the output >>>
```

Using this code, modify it to read the `portfolio.yaml` fils and create a `Portfolio` object.

[Contents](../Contents.md) \| [Prev (6.2 Variable Arguments)](02_Variable_arguments.md) \| [Next (6.4 Anonymous Function)](04_Anonymous_function.md)
