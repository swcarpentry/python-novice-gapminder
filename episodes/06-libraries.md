---
layout: episode
title: "Libraries"
teaching: 5
exercises: 5
questions:
- "How can I use software that other people have written?"
- "How can I find out what that software does?"
objectives:
- "Explain what software libraries are and why programmers create and use them."
- "Write programs that import and use libraries from Python's standard library."
- "Find and read documentation for standard libraries interactively (in the interpreter) and online."
keypoints:
- FIXME
---
FIXME: lesson content.

> ## Locating the Right Library
> 
> You want to select a random value from your data:
> ~~~
> ids = [1, 2, 3, 4, 5, 6]
> ~~~ 
> 
> 1. What [standard library](https://docs.python.org/3/library/index.html) 
>    would you most expect to help? 
> 2. Which function would you select from that library? Are there alternatives?
{: .challenge}

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
> {: .source}
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
> {: .source}
{: .challenge}
