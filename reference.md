---
title: 'Reference'
---

## Reference

## [Running and Quitting](episodes/01-run-quit.md)

- Python files have the `.py` extension.
- Can be written in a text file or a [Jupyter Notebook][jupyter].
  - Jupyter notebooks have the extension `.ipynb`
  - Jupyter notebooks can be opened from [Anaconda](https://docs.continuum.io/anaconda/install) or through the command line by entering `$ jupyter notebook`
    - Markdown and HTML are allowed in markdown cells for documenting code.

## [Variables and Assignment](episodes/02-variables.md)

- Variables are stored using `=`.
  - Strings are defined in quotations `'...'`.
  - Integers and floating point numbers are defined without quotations.
- Variables can contain letters, digits, and underscores `_`.
  - Cannot start with a digit.
  - Variables that start with underscores should be avoided.
- Use `print(...)` to display values as text.
- Can use indexing on strings.
  - Indexing starts at 0.
  - Position is given in square brackets `[position]` following the variable name.
  - Take a slice using `[start:stop]`. This makes a copy of part of the original string.
    - `start` is the index of the first element.
    - `stop` is the index of the element after the last desired element.
- Use `len(...)` to find the length of a variable or string.

## [Data Types and Type Conversion](episodes/03-types-conversion.md)

- Each value has a type. This controls what can be done with it.
  - `int` represents an integer
  - `float` represents a floating point number.
  - `str` represents a string.
- To determine a variables type, use the built-in function `type(...)`, including the variable name in the parenthesis.
- Modifying strings:
  - Use `+` to concatenate strings.
  - Use `*` to repeat a string.
  - Numbers and strings cannot be added to on another.
    - Convert string to integer: `int(...)`.
    - Convert integer to string: `str(...)`.

## [Built-in Functions and Help](episodes/04-built-in.md)

- To add a comment, place `#` before the thing you do not with to be executed.
- Commonly used built-in functions:
  - `min()` finds the smallest value.
  - `max()` finds the largest value.
  - `round()` rounds off a floating point number.
  - `help()` displays documentation for the function in the parenthesis.
    - Other ways to get help include holding down `shift` and pressing `tab` in Jupyter Notebooks.

## [Libraries](episodes/06-libraries.md)

- Importing a library:
  - Use `import ...` to load a library.
  - Refer to this library by using `module_name.thing_name`.
    - `.` indicates 'part of'.
- To import a specific item from a library: `from ... import ...`
- To import a library using an alias: `import ... as ...`
- Importing the math library: `import math`
  - Example of referring to an item with the module's name: `math.cos(math.pi)`.
- Importing the plotting library as an alias: `import matplotlib as mpl`

## [Reading Tabular Data into DataFrames](episodes/07-reading-tabular.md)

- Use the pandas library to do statistics on tabular data. Load with `import pandas as pd`.
  - To read in a csv: `pd.read_csv()`, including the path name in the parenthesis.
    - To specify a column's values should be used as row headings: `pd.read_csv('path', index_col='column name')`, where path and column name should be replaced with the relevant values.
- To get more information about a DataFrame, use `DataFrame.info`, replacing `DataFrame` with the variable name of your DataFrame.
- Use `DataFrame.columns` to view the column names.
- Use `DataFrame.T` to transpose a DataFrame.
- Use `DataFrame.describe` to get summary statistics about your data.

## [Pandas DataFrames](episodes/08-data-frames.md)

- Select data using `[i,j]`
  - To select by entry position: `DataFrame.iloc[..., ...]`
    - This is inclusive of everything except the final index.
  - To select by entry label: `DataFrame.loc[..., ...]`
    - Can select multiple rows or columns by listing labels.
    - This is inclusive to both ends.
  - Use `:` to select all rows or columns.
- Can also select data based on values using `True` and `False`. This is a Boolean mask.
  - `mask = subset > 10000`
  - We can then use this to select values.
- To use a select-apply-combine operation we use `data.apply(lambda x: x > x.mean())` where `mean()` can be any operation the user would like to be applied to x.

## [Plotting](episodes/09-plotting.md)

- The most widely used plotting library is `matplotlib`.
  - Usually imported using `import matplotlib.pyplot as plt`.
  - To plot we use the command `plt.plot(time, position)`.
  - To create a legend use `plt.legend(['label1', 'label2'], loc='upper left')`
    - Can also define labels within the plot statements by using `plt.plot(time, position, label='label')`. To make the legend show up, use `plt.legend()`
  - To label x and y axis `plt.xlabel('label')` and `plt.ylabel('label')` are used.
- Pandas DataFrames can be used to plot by using `DataFrame.plot()`. Any operations that can be used on a DataFrame can be applied while plotting.
  - To plot a bar plot `data.plot(kind='bar')`

```python
import matplotlib.puplot as plot
plt.plot(time, position, label='label')
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.legend()
```

## [Lists](episodes/11-lists.md)

- Defined within `[...]` and separated by `,`.
  - An empty list can be created by using `[]`.
- Can use `len(...)` to determine how many values are in a list.
- Can index just as done in previous lessons.
  - Indexing can be used to reassign values `list_name[0] = newvalue`.
- To add an item to a list use `list_name.append()`, with the item to append in the parenthesis.
- To combine two lists use `list_name_1.extend(list_name_2)`.
- To remove an item from a list use `del list_name[index]`.

## [For Loops](episodes/12-for-loops.md)

- Start a for loop with `for number in [1, 2, 3]:`, with the following lines indented.
  - `[1, 2, 3]` is considered the collection.
  - `number` is the loop variable.
  - The action following the collection is the body.
- To iterate over a sequence of numbers use `range(start, end)`

```python
for number in range(0,5):
    print(number)
```

## [Conditionals](episodes/13-conditionals.md)

- Defined similarly to a loop, using `if variable conditional value:`.
  - For example, `if variable > 5:`.
- Use `elif:` for additional tests.
- Use `else:` for when if statement is not true.
- Can combine more than one conditional by using `and` or `or`.
- Often used in combination with for loops.
- Conditions that can be used:
  - `==` equal to.
  - `>=` greater than or equal to.
  - `<=` less than or equal to.
  - `>` greater than.
  - `<` less than.

```python
for m in [3, 6, 7, 2, 8]:
    if m > 5:
        print(m, 'is large')
    elif m == 5:
        print(m, 'is 5')
    else:
        print(m, 'is small')
```

## [Looping Over Data Sets](episodes/14-looping-data-sets.md)

- Use a for loop: `for filename in [file1, file2]:`
- To find a set of files using a pattern use `glob.glob`
  - Must import first using `import glob`.
  - `*` indicates "match zero or more characters"
  - `?` indicates "match exactly one character"
    - For example: `glob.glob(*.txt)` will find all files that end with `.txt` in the current directory.
- Combine these by writing a loop using: `for filename in glob.glob(*.txt):`

```python
for filename in glob.glob(*.txt):
  data = pd.read_csv(filename)
```

## [Writing Functions](episodes/16-writing-functions.md)

- Define a function using `def function_name(parameters):`. Replace `parameters` with the variables to use when the function is executed.
- Run by using `function_name(parameters)`.
- To return a result to the caller use `return ...` in the function.

```python
def add_numbers(a, b):
    result = a + b
    return result

add_numbers(1, 4)
```

## [Variable Scope](episodes/17-scope.md)

- A local variable is defined in a function and can only be seen and used within that function.
- A global variable is defined outside of a function and can be seen or used anywhere after definition.

## [Programming Style](episodes/18-style.md)

- Document your code.
- Use clear and meaningful variable names.
- Follow [the PEP8 style guide](https://www.python.org/dev/peps/pep-0008) when setting up your code.
- Use assertions to check for internal errors.
- Use docstrings to provide help.

## Glossary

Arguments
:     Values passed to functions.

Array
:     A container holding elements of the same type.

Boolean
:     An object composed of `True` and `False`.

DataFrame
:     The way Pandas represents a table; a collection of series.

Element
:     An item in a list or an array. For a string, these are the individual characters.

Function
:     A block of code that can be called and re-used elsewhere.

Global variable
:     A variable defined outside of a function that can be used anywhere.

Index
:     The position of a given element.

Jupyter Notebook
:     Interactive coding environment allowing a combination of code and markdown.

Library
:     A collection of files containing functions used by other programs.

Local Variable
:     A variable defined inside of a function that can only be used inside of that function.

Mask
:     A boolean object used for selecting data from another object.

Method
:     An action tied to a particular object. Called by using `object.method`.

Modules
:     The files within a library containing functions used by other programs.

Parameters
:     Variables used when executing a function.

Series
:     A Pandas data structure to represent a column.

Substring
:     A part of a string.

Variables
:     Names for values.




