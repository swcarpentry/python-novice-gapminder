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
- "A program must import a library module in order to use it."
- "Use `help` to learn about the contents of a library module."
- "Import specific items from a library to shorten programs."
- "Create an alias for a library when importing it to shorten programs."
---
## Most of the power of a programming language is in its libraries.

*   A *library* is a collection of files (called *modules*) that contains
    functions for use by other programs.
    *   May also contain data values (e.g., numerical constants), classes and other data structures.
*   [Modules][python-modules] can be organized in (sub-)directories, 
    being called then (sub-)[packages][python-packages].
*   The Python [standard library][stdlib] is an extensive suite of modules that comes
    with Python itself.
*   Many additional libraries are available from [PyPI][pypi] (the Python Package Index).
*   We will see later how to write new libraries.

### How to know which library provides the functionality we need?

Documentation. And google.

*   It all starts with at before mentioned Python's [standard library][stdlib], 
    have a glance there to see what is available by default with your Python distribution.
*   [Browse PyPI][pypi-browse] packages if have an idea of the subject the funcitonality you need fits.
*   When googling for a funcionality, be explicit on what you want, chances are
    your question has already been answered in a community site (e.g, StackOverflow)
    or a blog. For example, suppose you have a huge data file to read and you want
    to have a glance on it at first, explicit search for "how to sample large data file in python"
    and see how well the internet answers you, with many alternatives to explore.
*   Follow newsletter, blogs that explore Python libraries, [Python Modules of the Week][pymotw]
    is a good one, for instance.

> ## Libraries, modules and packages
>
> A library is a collection of modules and packages, but the terms are often used
> interchangeably. There is no restriction on the number of modules or packages
> a library may contain, neither how it should be organized. By all means,
> a library/modules/packages will eventually provide a data structure, function
> or class to be used by your code.
{: .callout}


## Very first step to use a library: *import* it.

*   Use `import` to load a library module/package into a program's namespace.
*   Then refer to things from the module as `module_name.thing_name`.
    *   Python uses `.` to mean "part of".
*   Using `math`, one of the modules in the standard library:

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

*   Have to refer to each item with the module's name.
    *   `math.cos(pi)` won't work: the reference to `pi`
        doesn't somehow "inherit" the function's reference to `math`.

## Use `help` to learn about the contents of a library module.

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

## Import specific items from a library module to shorten programs.

*   Use `from ... import ...` to load only specific items from a library module.
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

## Create an alias for a library module when importing it to shorten programs.

*   Use `import ... as ...` to give the import an *alias*.
    An alias may be useful for two reasons:
    *   to shorten the imported module's name
    *   to avoid confusion or overwriting when importing modules with the same name
*   Then refer to items in the library using the *alias*.

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

> ## Exploring the Math Module
>
> 1. What function from the `math` module can you use to calculate a square root
>    *without* using `sqrt`?
> 2. Since the library contains this function, why does `sqrt` exist?
>
> > ## Solution
> > 1. Using `help(math)` we see that we've got `pow(x,y)` in addition to `sqrt(x)`
> > 2. The `sqrt(x)` function (like much of the `math` library) has it's origins in
> >    C's math library. Consequently, it might be somewhat faster than `pow(x,y)`.
> >    Also, it might be more readable than `pow(x, 0.5)` when implementing equations.
> >    However, `sqrt(x)` doesn't support negative arguments.
> {: .solution}
{: .challenge}

> ## Locating the Right Module
>
> You want to select a random character from a string:
>
> ~~~
> bases = 'ACTTGCTTGAC'
> ~~~
> {: .python}
>
> 1. Which [standard library][stdlib] module could help you?
> 2. Which function would you select from that module? Are there alternatives?
> 3. Try to write a program that uses the function.
>
> > ## Solution
> >
> > The [random module](randommod) seems like it could help you.
> >
> > The string has 11 characters, each having a positional index from 0 to 10.
> > You could use `random.randrange` function (or the alias `random.randint`
> > if you find that easier to remember) to get a random integer between 0 and
> > 10, and then pick out the character at that position:
> >
> > ~~~
> > from random import randrange
> >
> > random_index = random.randrange(len(bases))
> > print(bases[random_index])
> > ~~~
> > {: .python}
> >
> > or more compactly:
> >
> > ~~~
> > from random import randrange
> >
> > print(bases[random.randrange(len(bases))])
> > ~~~
> > {: .python}
> >
> > Perhaps you found the `random.sample` function? It allows for slightly
> > less typing:
> >
> > ~~~
> > from random import sample
> >
> > print(sample(bases, 1)[0])
> > ~~~
> > {: .python}
> >
> > Note that this function returns a list of values. We will learn about
> > lists in episode 11.
> >
> > There's also other functions you could use, but with more convoluted
> > code as a result.
> {: .solution}
{: .challenge}


> ## Jigsaw Puzzle (Parson's Problem) Programming Example
> 
> Rearrange the following statements so that a random
> DNA base is printed.  Not all statements may be needed.  Feel free to use/add 
> intermediate variables. 
>
> ~~~
> bases="ACTTGCTTGAC"
> import math
> import random
> len(bases)
> len(bases)+1
> math.floor(s1)
> math.ceil(s1)
> print("random base ",bases[])
> random.random()*l
> ~~~
{: .challenge}

> ## When is a module's help available?
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
> > Importing the math module (`import math`)
> {: .solution}
{: .challenge}

> ## Importing with aliases
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
> > can be written as
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

> ## There are many ways to import libraries!
>
> Match the following print statements with the appropriate library calls.
> 
> Print commands:
>
> 1. `print("sin(pi/2) =",sin(pi/2))`
> 2. `print("sin(pi/2) =",m.sin(m.pi/2))`
> 3. `print("sin(pi/2) =",math.sin(math.pi/2))`
>
> Library calls:
>
> 1. `from math import sin,pi`
> 2. `import math`
> 3. `import math as m`
> 4. `from math import *`
>
> > ## Solution
> >
> > 1. Library calls 1 and 4. In order to directly refer to `sin` and `pi` without
> >    the library name as prefix, you need to use the `from ... import ...`
> >    statement. Whereas library call 1 specifically imports the two functions
> >    `sin` and `pi`, library call 4 imports all functions in the `math` module.
> > 2. Library call 3. Here `sin` and `pi` are referred to with a shortened library
> >    name `m` instead of `math`. Library call 3 does exactly that using the
> >    `import ... as ...` syntax - it creates an alias for `math` in the form of
> >    the shortened name `m`.
> > 3. Library call 2. Here `sin` and `pi` are referred to with the regular library
> >    name `math`, so the regular `import ...` call suffices.
> {: .solution}
{: .challenge}

> ## Importing specific items
>
> 1. Fill in the blanks so that the program below prints `90.0`.
> 2. Do you find this version easier to read than preceding ones?
> 3. Why *wouldn't* programmers always use this form of `import`?
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
[python-modules]: https://docs.python.org/3/tutorial/modules.html
[python-packages]: https://docs.python.org/3/tutorial/modules.html#packages
[pypi-browse]: https://pypi.python.org/pypi?%3Aaction=browse
[pymotw]: https://pymotw.com/3/
[randommod]: https://docs.python.org/3/library/random.html
