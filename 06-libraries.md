---
layout: lesson
subtitle: Libraries
---
> ## Learning Objectives
>
> * Learner will explain what software libraries are
>   and why programmers create and use them.
> * Learner will write programs that import and use libraries from Python's standard library.
> * Learner can find and read documentation for standard libraries
>   interactively (in the interpreter) and online.
{: .objectives}

FIXME: lesson content.

> ## Exploring the Math Library
>
> 1. What function from the `math` library can you use to calculate a square root
>    *without* using `sqrt`?
> 2. Since the library contains this function, why does `sqrt` exist?
{: .challenge}

> ## When Is Help Available?
>
> When a colleague of yours types `help(math)`,
> Python tells him:
>
> ~~~
> NameError: name 'math' is not defined
> ~~~
> {: .error}
>
> What has he forgotten to do?
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
{: .challenge}
