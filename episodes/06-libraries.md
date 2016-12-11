---
title: "Libraries"
teaching: 10
exercises: 10
questions:
- "How can I use software that other people have written?"
- "How can I find out what that software does?"
objectives:
- "Explain what software libraries are and why programmers create and use them."
- "Write programs that import and use libraries from Python's standard library."
- "Find and read documentation for standard libraries interactively (in the interpreter) and online."
keypoints:
- "Most of the power of a programming language is in its libraries."
- "A program must import a library in order to use it."
- "Use `help` to find out more about a library's contents."
- "Import specific items from a library to shorten programs."
- "Create an alias for a library when importing it to shorten programs."
---
## Most of the power of a programming language is in its libraries.

*   A *library* is a collection of functions that can be used by other programs.
    *   May also contain data values (e.g., numerical constants).
    *   Library's contents are supposed to be related, but there's no way to enforce that.
*   Python's [standard library][stdlib] is installed with it.
*   Many additional libraries are available from [PyPI][pypi] (the Python Package Index).
*   We will see later how to write new libraries.

## A program must import a library in order to use it.

*   Use `import` to load a library into a program's memory.
*   Then refer to things from the library as `library_name.thing_name`.
    *   Python uses `.` to mean "part of".

~~~
import math

print('pi is', math.pi)
print('cos(pi) is', math.cos(math.pi))
~~~
{: .python}
~~~
pi is 3.141592653589793
cos(pi) is -1.0
~~~
{: .output}

*   Have to refer to each item with the library's name.
    *   `math.cos(pi)` won't work: the reference to `pi`
        doesn't somehow "inherit" the function's reference to `math`.

## Use `help` to find out more about a library's contents.

*   Works just like help for a function.

~~~
help(math)
~~~
{: .python}
~~~
Help on module math:

NAME
    math

MODULE REFERENCE
    http://docs.python.org/3.5/library/math

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(...)
        acos(x)

        Return the arc cosine (measured in radians) of x.
⋮ ⋮ ⋮
~~~
{: .output}

## Import specific items from a library to shorten programs.

*   Use `from...import...` to load only specific items from a library.
*   Then refer to them directly without library name as prefix.

~~~
from math import cos, pi

print('cos(pi) is', cos(pi))
~~~
{: .python}
~~~
cos(pi) is -1.0
~~~
{: .output}

## Create an alias for a library when importing it to shorten programs.

*   Use `import...as...` to give a library a short *alias* while importing it.
*   Then refer to items in the library using that shortened name.

~~~
import math as m

print('cos(pi) is', m.cos(m.pi))
~~~
{: .python}
~~~
cos(pi) is -1.0
~~~
{: .output}

*   Commonly used for libraries that are frequently used or have long names.
    *   E.g., `matplotlib` plotting library is often aliased as `mpl`.
*   But can make programs harder to understand,
    since readers must learn your program's aliases.

> ## Exploring the Math Library
>
> 1. What function from the `math` library can you use to calculate a square root
>    *without* using `sqrt`?
> 2. Since the library contains this function, why does `sqrt` exist?
>
> > ## Solution
> >
> > 1. You could use the `pow` function to raise a number of interest to the power
> >    of 1/2. To find the square root of 9, you would write `math.pow(9, 1/2)`.
> > 2. To make the code more clear and easy to understand.
> {: .solution}
{: .challenge}

> ## Locating the Right Library
>
> You want to select a random character from a string:
>
> ~~~
> bases = 'ACTTGCTTGAC'
> ~~~
> {: .python}
>
> 1. What [standard library][stdlib] would you most expect to help?
> 2. Which function would you select from that library? Are there alternatives?
>
> > ## Solution
> >
> > 1. The [random library](randomlib)
> > 2. The string has 11 characters, each having a positional index from 0 to 10.
> >    You could use `random.randrange` (or the alias `random.randint` if you
> >    find that easier to remember) to get a random integer between 0 and 10, and
> >    then pick out the character at that position:
> >
> >    ~~~
> >    random_index = random.randrange(len(bases))
> >    bases[random_index]
> >    ~~~
> >    {: .python}
> >
> >    or at one line:
> >
> >    ~~~
> >    bases[random.randrange(len(bases))]
> >    ~~~
> >    {: .python}
> >
> >    Perhaps you found the `random.sample` function? It allows for slightly
> >    less typing:
> >
> >    ~~~
> >    random.sample(bases, 1)
> >    ~~~
> >    {: .python}
> >
> >    Note that this function returns a list of values. We will learn about
> >    lists in episode 11.
> >
> >    There's also other functions you could use, but with more convoluted
> >    code as a result.
> {: .solution}
{: .challenge}

> ## When Is Help Available?
>
> When a colleague of yours types `help(math)`,
> Python reports an error:
>
> ~~~
> NameError: name 'math' is not defined
> ~~~
> {: .error}
>
> What has your colleague forgotten to do?
>
> > ## Solution
> >
> > Importing the math library (`import math`)
> {: .solution}
{: .challenge}

> ## Importing With Aliases
>
> 1. Fill in the blanks so that the program below prints `90.0`.
> 2. Rewrite the program so that it uses `import` *without* `as`.
> 3. Which form do you find easier to read?
>
> ~~~
> import math as m
> angle = ____.degrees(____.pi / 2)
> print(____)
> ~~~
> {: .python}
>
> > ## Solution
> >
> > ~~~
> > import math as m
> > angle = m.degrees(m.pi / 2)
> > print(angle)
> > ~~~
> > {: .python}
> >
> > can bewritten as
> >
> > ~~~
> > import math
> > angle = math.degrees(math.pi / 2)
> > print(angle)
> > ~~~
> > {: .python}
> >
> > Since you just wrote the code and are familiar with it, you might actually
> > find the first version easier to read. But when trying to read a huge piece
> > of code written by someone else, or when getting back to your own huge piece
> > of code after several months, non-abbreviated names are often easier, expect
> > where there are clear abbreviation conventions.
> {: .solution}
{: .challenge}

> ## Importing Specific Items
>
> 1. Fill in the blanks so that the program below prints `90.0`.
> 2. Do you find this easier to read than preceding versions?
> 3. Why *would't* programmers always use this form of `import`?
>
> ~~~
> ____ math import ____, ____
> angle = degrees(pi / 2)
> print(angle)
> ~~~
> {: .python}
>
> > ## Solution
> >
> > ~~~
> > from math import degrees, pi
> > angle = degrees(pi / 2)
> > print(angle)
> > ~~~
> > {: .python}
> >
> > Most likely you find this version easier to read since it's less dense.
> > The main reason not to use this form of import is to avoid name clashes.
> > For instance, you wouldn't import `degrees` this way if you also wanted to
> > use the name `degrees` for a variable or function of your own. Or if you
> > were to also import a function named `degrees` from another library.
> {: .solution}
{: .challenge}

> ## Reading Error Messages
>
> 1. Read the code below and try to identify what the errors are without running it.
> 2. Run the code, and read the error message. What type of error is it?
>
> ~~~
> from math import log
> log(0)
> ~~~
> {: .python}
>
> > ## Solution
> >
> > 1. The logarithm of `x` is only defined for `x > 0`, so 0 is outside the
> >    domain of the function.
> > 2. You get an error of type "ValueError", indicating that the function
> >    received an inappropriate argument value. The additional message
> >    "math domain error" makes it clearer what the problem is.
> {: .solution}
{: .challenge}

[pypi]: https://pypi.python.org/pypi/
[stdlib]: https://docs.python.org/3/library/
