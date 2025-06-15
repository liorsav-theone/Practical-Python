[Contents](../Contents.md) \| [Prev (5.2 Classes and Objects)](../05_Object_model/02_Classes_encapsulation.md) \| [Next (6.2 Variable Arguments)](02_Variable_arguments.md)

# Paydantic

Pydantic is a powerful Python library that leverages type hints
to help you easily validate and serialize (convert to a standard format such as a dictionary or JSON)
your data according to a description of the data structure (sometimes called a 'schema'). This
makes your code more robust, readable, concise, and easier to
debug. Pydantic also integrates well with many popular static
typing tools and IDEs, which allows you to catch issues with your data structure descriptions
before running your code.

### Using Models

Pydantic’s primary way of defining data schemas is through models.
A Pydantic model is an object, similar to a Python dataclass,
that defines and stores data about an entity with annotated fields.
Unlike dataclasses, Pydantic’s focus is centered around automatic
data parsing, validation, and serialization.

### Working With Pydantic BaseModels

In your code, you process CSV files into Stock objects.
The steps you take to serialize the stock object are:
    - Separate the columns that interest you in the CSV files
    - Try to cast the value of each column to the correct type
    - Set the members of the Stock object.
Those 3 steps can be done seamlessly inside Pydantic models.

To create a pydantic model, first update your Stock class to inherit from pydantic's `BaseModel`:

```python
from pydantic import BaseModel

class Stock(BaseModel):
    """
    Represents a stock holding with a name, number of shares, and price per share.
    """
```

Then, you define the names and expected types of your Stock fields via annotations.

```python
from pydantic import BaseModel

class Stock(BaseModel):
    """
    Represents a stock holding with a name, number of shares, and price per share.
    """
    name: str
    shares: int
    price: float
```

When Pydantic instantiates the `Stock` object, it will validate that each member given can be casted to the given type.

The simplest way to create an `Stock` object is to instantiate it as you would any other Python object.

```python
>>> from stock import Stock
>>> Stock(name="IBM", shares='33', price=10.24)
Stock(name='IBM', shares=33, price=10.24)
```

In this block, you import `Stock` and create an object with all of the required `Stock` fields.
Pydantic successfully validates and coerces the fields you passed in, and it creates a valid `Stock` object.
Notice how Pydantic automatically converts your shares string into an int.

Next, look at how Pydantic responds when you try to pass invalid data to an `Stock` instance:

```python
>>> from stock import Stock
>>> Stock(name=True, shares='55.42', price='Too much')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "site-packages\pydantic\main.py", line 212, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pydantic_core._pydantic_core.ValidationError: 3 validation errors for Stock
name
  Input should be a valid string [type=string_type, input_value=True, input_type=bool]
    For further information visit https://errors.pydantic.dev/2.9/v/string_type
shares
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='55.42', input_type=str]
    For further information visit https://errors.pydantic.dev/2.9/v/int_parsing
price
  Input should be a valid number, unable to parse string as a number [type=float_parsing, input_value='Too much', input_type=str]
    For further information visit https://errors.pydantic.dev/2.9/v/float_parsing
```

In this example, you created an `Stock` object with invalid data fields.
Pydantic gives you a detailed error message for each field, telling you what was expected, what was received, and where you can go to learn more about the error.

### Json Integration

Pydantic’s BaseModel is equipped with a suite of methods that make it easy to create models from other objects, such as dictionaries and JSON.
For example, you can also serialize Pydantic models as dictionaries and JSON:

```python
>>> stock = Stock(name="IBM", shares=33, price=10.24)  
>>> stock.model_dump()
{'name': 'IBM', 'shares': 33, 'price': 10.24}
>>> stock.model_dump_json() 
'{"name":"IBM","shares":33,"price":10.24}'
```

Here, you use .model_dump() and .model_dump_json() to convert your stock model to a dictionary and JSON string, respectively.

While Pydantic already validated these fields and converted your model to JSON, whoever uses this JSON downstream won’t know that shares needs to be a valid int and name needs to be a string. To solve this, you can create a JSON schema from your `Stock` model.

JSON schemas tell you what fields are expected and what values are represented in a JSON object. You can think of this as the JSON version of your `Stock` class definition. Here’s how you generate a JSON schema for `Stock`:

```python
>>> stock.model_json_schema()
{
    'description': 'Represents a stock holding with a name, number of shares, and price per share.', 
    'properties': {
        'name': {
            'title': 'Name', 
            'type': 'string'
        }, 
        'shares': {
            'title': 'Shares', 
            'type': 'integer'
        }, 
        'price': {
            'title': 'Price', 
            'type': 'number'
        }
    }, 
    'required': ['name', 'shares', 'price'], 
    'title': 'Stock', 
    'type': 'object'
}
```

When you call .model_json_schema(), you get a dictionary representing your model’s JSON schema.
You also see information about how your fields should be formatted. For instance, according to this JSON schema, shares is expected to be an integer and name is expected to be a string.

You can convert your JSON schema to a JSON string using json.dumps(), which enables just about **any programming language** to validate JSON objects produced by your `Stock` model. In other words, not only can Pydantic validate incoming data and serialize it as JSON, but it also provides other programming languages with the information they need to validate your model’s data via JSON schemas.

### Using Fields for Customization and Metadata

So far, your `Stock` model validates the data type of each field and ensures that inputs conform to expected formats. However, in many practical applications, you need more precise control over what constitutes valid data. For example:

- You may want to ensure that `price` is a positive float.
- You might want `shares` to be greater than zero.
- You probably don’t want someone to create a `Stock` with an empty string for a name.

These constraints aren’t about data *type*, but rather about data *validity*. This is where Pydantic's `Field` class comes in.

#### What is `Field`?

`Field` is a helper function provided by Pydantic that lets you attach metadata and validation rules to model attributes. It is the recommended way to express additional requirements for your fields without writing custom validators.

A typical usage might look like this:

```python
from pydantic import Field

shares: int = Field(gt=0, description="Number of shares")
```

Here are some of the most useful arguments you can pass to `Field`:

| Argument      | Purpose                                                                 |
|---------------|-------------------------------------------------------------------------|
| `default`     | Default value if the field is not set.                                  |
| `gt`          | Value must be strictly greater than this                                |
| `ge`          | Value must be greater than or equal to this                             |
| `lt`          | Value must be strictly less than this                                   |
| `le`          | Value must be less than or equal to this                                |
| `min_length`  | Minimum string length                                                   |
| `max_length`  | Maximum string length                                                   |
| `description` | A human-readable description                                            |
| `example`     | A suggested example value                                               |

This is not a complete list. To learn more about `Field` parameters, visit the Pydantic official documentation or use the help(Field).

#### Updated `Stock` Example

Let’s revisit our `Stock` model and add some proper constraints using `Field`:

```python
from pydantic import BaseModel, Field

class Stock(BaseModel):
    name: str = Field(min_length=1, description="Stock symbol")
    shares: int = Field(gt=0, description="Number of shares")
    price: float = Field(gt=0.0, description="Price per share")
```

This updated model ensures the following:

- The `name` field cannot be an empty string.
- The `shares` field must be a positive integer.
- The `price` field must be a positive float.

This is all done without writing a single line of custom validation logic—Pydantic handles it automatically.

#### Example: Passing Invalid Data

What happens when we try to create a stock with invalid input?

```python
stock = Stock(name="", shares=-10, price=-1.5)
```

Pydantic will immediately raise a `ValidationError` with detailed output like this:

```python
pydantic_core._pydantic_core.ValidationError: 3 validation errors for Stock
name
  String should have at least 1 character [type=string_too_short, input_value='', input_type=str]
    For further information visit https://errors.pydantic.dev/2.9/v/string_too_short
shares
  Input should be greater than 0 [type=greater_than, input_value=-10, input_type=int]
    For further information visit https://errors.pydantic.dev/2.9/v/greater_than
price
  Input should be greater than 0 [type=greater_than, input_value=-1.5, input_type=float]
    For further information visit https://errors.pydantic.dev/2.9/v/greater_than
```

This makes it very easy to enforce quality and correctness in the data your scripts or applications rely on.
You can also leverage this for auto-generated documentation or command-line input parsing with tools like FastAPI or Typer, though these are out of scope for now.
In summary, `Field()` is one of the simplest and most powerful ways to improve data integrity in your Python programs.

### Working With Validators

Up to this point, you’ve used Pydantic’s `BaseModel` to validate model fields with predefined types, and you incorporated `Field` to further customize your validation. While you can get pretty far with `BaseModel` and `Field` alone, for more complicated validation scenarios that require custom logic, you’ll need to use Pydantic validators.

With validators, you can execute just about any validation logic that you can express in a function. You’ll see how to do this next.

### Validating Models and Fields

Continuing with the Stock example, suppose you have a policy that you cannot have any shares in the FAANG stocks. Any time you create a new Stock object, you need to make sure the stock is not for Meta (META), Amazon (AMZN), Apple (AAPL), Netflix (NFLX); And Alphabet (GOOG). To handle this, you could add a regex pattern on the name field. However, this seems very complex and requires an understanding of regex.

A better solution is to use a Pydantic field validator. Field validators allow you to apply custom validation logic to your `BaseModel` fields by adding class methods to your model. To enforce that all stocks are not named any of the FAANG names, you can add the following `Field` validator to your `Stock` model:

```python
from pydantic import BaseModel, Field, field_validator

class Stock(BaseModel):
    name: str = Field(min_length=1, description="Stock symbol")
    shares: int = Field(gt=0, description="Number of shares")
    price: float = Field(gt=0.0, description="Price per share")

    @field_validator("name")
    @classmethod
    def check_valid_age(cls, name: str) -> str:
        if name in ["META", "AMZN", "AAPL", "NFLX", "GOOG"]:
            raise ValueError("Stock name cannot be one of the FAANG stocks.")

        return name
```

The syntax you see here is not simple. It uses both function decorators and method decorators, which are explained later in this course.

Now if we try to create a Stock it will enforce the names and will raise an error if needed:

```python
>>> Stock(name="META", shares=15, price=15.45) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "pydantic\main.py", line 212, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pydantic_core._pydantic_core.ValidationError: 1 validation error for Stock
name
  Value error, Stock name cannot be one of the FAANG stocks. [type=value_error, input_value='META', input_type=str]
    For further information visit https://errors.pydantic.dev/2.9/v/value_error
```

As you can imagine, Pydantic’s field_validator() enables you to arbitrarily customize field validation. However, field_validator() won’t work if you want to compare multiple fields to one another or validate your model as a whole. For this, you’ll need to use model validators.

### Models Validators

Suppose you buy only stocks whose total worth is more than 50 USD. Because of this, a stock doesn't qualify if its price times the shares is smaller than 50. You can use Pydantic’s model_validator() to enforce this constraint:

```python
from typing import Self
from pydantic import BaseModel, Field, field_validator, model_validator

class Stock(BaseModel):
    name: str = Field(min_length=1, description="Stock symbol")
    shares: int = Field(gt=0, description="Number of shares")
    price: float = Field(gt=0.0, description="Price per share")

    @field_validator("name")
    @classmethod
    def check_valid_age(cls, name: str) -> str:
        if name in ["META", "AMZN", "AAPL", "NFLX", "GOOG"]:
            raise ValueError("Stock name cannot be one of the FAANG stocks.")

        return name
    
    @model_validator(mode="after")
    def check_it_worth(self) -> Self:
        if self.shares * self.price < 50:
            raise ValueError(
                "Stock total price must be higher than 50"
            )
        return self
```

To see your new model validator in action, check out this example:

```python
>>> Stock(name="IBM", shares="2", price=15) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "pydantic\main.py", line 212, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pydantic_core._pydantic_core.ValidationError: 1 validation error for Stock
  Value error, Stock total price must be higher than 50 [type=value_error, input_value={'name': 'IBM', 'shares': '2', 'price': 15}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.9/v/value_error
```

With model and field validators, you can implement just about any custom validation you can think of. You should now have a solid foundation to create Pydantic models for your own use cases

## Exercises

In those execrise we will adapt pydantic model and use thier funcitnality to simplfy our code base.

### Exercise 6.1: Update Stock Class

Update the `Stock` class to inherit pydantyic model and use its built-in features, including type validation and field description.
After this adaptation much of the class code is no longer needed as `pydantic` handles that for you.

Remove the following from your `Stock` code:

```python
    __slots__ = ('name', '_shares', 'price')

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name   = name
        self.shares = shares
        self.price  = price

    def __repr__(self) -> str:
        return f"Stock({self.name!r}, {self.shares!r}, {self.price!r})"
```

You can play a bit with your new Stock class in interactive mode, see how it reacts to diffrent inputs.

### Pydantic Challnage

Find a simple way to replace the following code:

```python

    @property
    def shares(self) -> int:
        """Get the number of shares."""
        return self._shares

    @shares.setter
    def shares(self, value: int) -> None:
        """Set the number of shares with type validation."""
        if not isinstance(value, int):
            raise TypeError("Shares must be an integer.")
        self._shares = value
```

### Exercise 6.2: Simplfy Report

Using pydantic models simplify much of the stock processing code.
Modify the `read_portfolio()` function in the `report.py` program so
that it does not use the `select` and `types` arguments of the `parse_csv`
function and instead pass the values as string to the `Stock` class.

However since pydantic models take no positinal arguments when created you must change the instance of each stock class to be

```python
    Stock(name=name_var, shares=shares_var, price=price_var) # valid
    Stock(name_var, shares_var, price_var) # invalid
```

Check if your code still works even with different CSV files:

```bash
python ..\Solutions\6\report.py .\Data\portfoliodate.csv .\Data\prices.csv txt
```

Notice how pydantic knows to ignore the extra columns and cast the types to the correct values.

### Exercise 6.3: List of Objects

Pydantic supports almost all types of Python objects, this means you can use it to validate a list member, a member that is an instance of another class, or even a member that is an instance of the same class that contains it.

In a new file named `portfolio.py`, add the following code:

```python
from stock import Stock
from typing import List
from pydantic import BaseModel, Field

class Portfolio(BaseModel):

    stocks: List[Stock] = Field(description="A list of stocks holding")

    @property
    def total_cost(self):
        return sum([s.cost for s in self.stocks])
```

This class holds a list of stocks, and can be used to quickly create multiple `Stocks` objects.

Open this file in interactive mode and try to create one instance of it with the following stocks members:

- 2 "IMB" stocks priced at 25.58 each.
- 16 "DD" stocks priced at 4.78 each.

```python
>>> stocks_list = [      
...     {
...         'name': 'IBM',
...         'shares': 2,
...         'price': 25.58
...     },
...     {
...         'name': 'DD',
...         'shares': 16,
...         'price': 4.78
...     }
... ]
>>> portfolio = Portfolio(stocks=stocks_list) 
>>> portfolio
... See what happens ...
```

### Commentary

Pydantic is an easy-to-use, fast, and widely-trusted data validation library in Python. You’ve gotten a broad overview of Pydantic, and now you have the knowledge and resources necessary to start using Pydantic in your own projects.

Pydantic is the backbone of any data validation program and is used widely in Matzov and particularly in our team.

[Contents](../Contents.md) \| [Prev (5.2 Classes and Objects)](../05_Object_model/02_Classes_encapsulation.md) \| [Next (6.2 Variable Arguments)](02_Variable_arguments.md)
