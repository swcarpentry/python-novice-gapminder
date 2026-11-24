---
title: Libraries
teaching: 10
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

- Explain what software libraries are and why programmers create and use them.
- Write programs that import and use modules from Python's standard library.
- Find and read documentation for the standard library interactively (in the interpreter) and online.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can I use software that other people have written?
- How can I find out what that software does?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Most of the power of a programming language is in its libraries.

- A *library* is a collection of files (called *modules*) that contains
  functions for use by other programs.
  - May also contain data values (e.g., numerical constants) and other things.
  - Library's contents are supposed to be related, but there's no way to enforce that.
- The Python [standard library][stdlib] is an extensive suite of modules that comes
  with Python itself.
- Many additional libraries are available from [PyPI][pypi] (the Python Package Index).
- We will see later how to write new libraries.

:::::::::::::::::::::::::::::::::::::::::  callout

## Libraries and modules

A library is a collection of modules, but the terms are often used
interchangeably, especially since many libraries only consist of a single
module, so don't worry if you mix them.


::::::::::::::::::::::::::::::::::::::::::::::::::

## A program must import a library module before using it.

- Use `import` to load a library module into a program's memory.
- Then refer to things from the module as `module_name.thing_name`.
  - Python uses `.` to mean "part of".
- Using `math`, one of the modules in the standard library:

```python
import math

print('pi is', math.pi)
print('cos(pi) is', math.cos(math.pi))
```

```output
pi is 3.141592653589793
cos(pi) is -1.0
```

- Have to refer to each item with the module's name.
  - `math.cos(pi)` won't work: the reference to `pi`
    doesn't somehow "inherit" the function's reference to `math`.

## Use `help` to learn about the contents of a library module.

- Works just like help for a function.

```python
help(math)
```

```output
Help on module math:

NAME
    math

MODULE REFERENCE
    http://docs.python.org/3/library/math

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
⋮ ⋮ ⋮
```

## Import specific items from a library module to shorten programs.

- Use `from ... import ...` to load only specific items from a library module.
- Then refer to them directly without library name as prefix.

```python
from math import cos, pi

print('cos(pi) is', cos(pi))
```

```output
cos(pi) is -1.0
```

## Create an alias for a library module when importing it to shorten programs.

- Use `import ... as ...` to give a library a short *alias* while importing it.
- Then refer to items in the library using that shortened name.

```python
import math as m

print('cos(pi) is', m.cos(m.pi))
```

```output
cos(pi) is -1.0
```

- Commonly used for libraries that are frequently used or have long names.
  - E.g., the `matplotlib` plotting library is often aliased as `mpl`.
- But can make programs harder to understand,
  since readers must learn your program's aliases.

:::::::::::::::::::::::::::::::::::::::  challenge

## Exploring the Math Module

1. What function from the `math` module can you use to calculate a square root
  *without* using `sqrt`?
2. Since the library contains this function, why does `sqrt` exist?

:::::::::::::::  solution

## Solution

1. Using `help(math)` we see that we've got `pow(x,y)` in addition to `sqrt(x)`,
  so we could use `pow(x, 0.5)` to find a square root.

2. The `sqrt(x)` function is arguably more readable than `pow(x, 0.5)` when
  implementing equations. Readability is a cornerstone of good programming, so it
  makes sense to provide a special function for this specific common case.
  
  Also, the design of Python's `math` library has its origin in the C standard,
  which includes both `sqrt(x)` and `pow(x,y)`, so a little bit of the history
  of programming is showing in Python's function names.
  
  

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Locating the Right Module

You want to select a random character from a string:

```python
bases = 'ACTTGCTTGAC'
```

1. Which [standard library][stdlib] module could help you?
2. Which function would you select from that module? Are there alternatives?
3. Try to write a program that uses the function.

:::::::::::::::  solution

## Solution

The [random module][randommod] seems like it could help.

The string has 11 characters, each having a positional index from 0 to 10.
You could use the [`random.randrange`](https://docs.python.org/3/library/random.html#random.randrange)
or [`random.randint`](https://docs.python.org/3/library/random.html#random.randint) functions
to get a random integer between 0 and 10, and then select the `bases` character at that index:

```python
from random import randrange

random_index = randrange(len(bases))
print(bases[random_index])
```

or more compactly:

```python
from random import randrange

print(bases[randrange(len(bases))])
```

Perhaps you found the [`random.sample`](https://docs.python.org/3/library/random.html#random.sample) function?
It allows for slightly less typing but might be a bit harder to understand just by reading:

```python
from random import sample

print(sample(bases, 1)[0])
```

Note that this function returns a list of values. We will learn about
lists in [episode 11](11-lists.md).

The simplest and shortest solution is the [`random.choice`](https://docs.python.org/3/library/random.html#random.choice)
function that does exactly what we want:

```python
from random import choice

print(choice(bases))
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Jigsaw Puzzle (Parson's Problem) Programming Example

Rearrange the following statements so that a random
DNA base is printed and its index in the string.
Not all statements may be needed.  Feel free to use/add
intermediate variables.

```python
bases="ACTTGCTTGAC"
import math
import random
___ = random.randrange(n_bases)
___ = len(bases)
print("random base ", bases[___], "base index", ___)
```

:::::::::::::::  solution

## Solution

```python
import math 
import random
bases = "ACTTGCTTGAC" 
n_bases = len(bases)
idx = random.randrange(n_bases)
print("random base", bases[idx], "base index", idx)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## When Is Help Available?

When a colleague of yours types `help(math)`,
Python reports an error:

```error
NameError: name 'math' is not defined
```

What has your colleague forgotten to do?

:::::::::::::::  solution

## Solution

Importing the math module (`import math`)



:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Importing With Aliases

1. Fill in the blanks so that the program below prints `90.0`.
2. Rewrite the program so that it uses `import` *without* `as`.
3. Which form do you find easier to read?

```python
import math as m
angle = ____.degrees(____.pi / 2)
print(____)
```

:::::::::::::::  solution

## Solution

```python
import math as m
angle = m.degrees(m.pi / 2)
print(angle)
```

can be written as

```python
import math
angle = math.degrees(math.pi / 2)
print(angle)
```

Since you just wrote the code and are familiar with it, you might actually
find the first version easier to read. But when trying to read a huge piece
of code written by someone else, or when getting back to your own huge piece
of code after several months, non-abbreviated names are often easier, except
where there are clear abbreviation conventions.



:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## There Are Many Ways To Import Libraries!

Match the following print statements with the appropriate library calls.

Print commands:

1. `print("sin(pi/2) =", sin(pi/2))`
2. `print("sin(pi/2) =", m.sin(m.pi/2))`
3. `print("sin(pi/2) =", math.sin(math.pi/2))`

Library calls:

1. `from math import sin, pi`
2. `import math`
3. `import math as m`
4. `from math import *`

:::::::::::::::  solution

## Solution

1. Library calls 1 and 4. In order to directly refer to `sin` and `pi` without
  the library name as prefix, you need to use the `from ... import ...`
  statement. Whereas library call 1 specifically imports the two functions
  `sin` and `pi`, library call 4 imports all functions in the `math` module.
2. Library call 3. Here `sin` and `pi` are referred to with a shortened library
  name `m` instead of `math`. Library call 3 does exactly that using the
  `import ... as ...` syntax - it creates an alias for `math` in the form of
  the shortened name `m`.
3. Library call 2. Here `sin` and `pi` are referred to with the regular library
  name `math`, so the regular `import ...` call suffices.

**Note:** although library call 4 works, importing all names from a module using a wildcard
import is [not recommended][pep8-imports] as it makes it unclear which names from the module
are used in the code. In general it is best to make your imports as specific as possible and to
only import what your code uses. In library call 1, the `import` statement explicitly tells us
that the `sin` function is imported from the `math` module, but library call 4 does not
convey this information.



:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Importing Specific Items

1. Fill in the blanks so that the program below prints `90.0`.
2. Do you find this version easier to read than preceding ones?
3. Why *wouldn't* programmers always use this form of `import`?

```python
____ math import ____, ____
angle = degrees(pi / 2)
print(angle)
```

:::::::::::::::  solution

## Solution

```python
from math import degrees, pi
angle = degrees(pi / 2)
print(angle)
```

Most likely you find this version easier to read since it's less dense.
The main reason not to use this form of import is to avoid name clashes.
For instance, you wouldn't import `degrees` this way if you also wanted to
use the name `degrees` for a variable or function of your own. Or if you
were to also import a function named `degrees` from another library.



:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Reading Error Messages

1. Read the code below and try to identify what the errors are without running it.
2. Run the code, and read the error message. What type of error is it?

```python
from math import log
log(0)
```

:::::::::::::::  solution

## Solution

```output
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-1-d72e1d780bab> in <module>
      1 from math import log
----> 2 log(0)

ValueError: math domain error
```

1. The logarithm of `x` is only defined for `x > 0`, so 0 is outside the
  domain of the function.
2. You get an error of type `ValueError`, indicating that the function
  received an inappropriate argument value. The additional message
  "math domain error" makes it clearer what the problem is.
  
  

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

[stdlib]: https://docs.python.org/3/library/
[pypi]: https://pypi.python.org/pypi/
[randommod]: https://docs.python.org/3/library/random.html
[pep8-imports]: https://pep8.org/#imports


:::::::::::::::::::::::::::::::::::::::: keypoints

- Most of the power of a programming language is in its libraries.
- A program must import a library module in order to use it.
- Use `help` to learn about the contents of a library module.
- Import specific items from a library to shorten programs.
- Create an alias for a library when importing it to shorten programs.

::::::::::::::::::::::::::::::::::::::::::::::::::


