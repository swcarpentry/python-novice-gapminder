---
title: Built-in Functions (and Methods) and Help
teaching: 10
exercises: 10
questions:
- "How can I use built-in functions?"
- "How can I find out what they do?"
objectives:
- "Explain the purpose of functions."
- "Correctly call built-in Python functions."
- "Correctly nest calls to built-in functions."
- "Use help to display documentation for built-in functions."
---
FIXME: lesson content.

> ## What Happens When
> 
> 1. Explain in simple terms the order of operations in the following program:
>    when does the addition happen, when does the subtraction happen,
>    when is each function called, etc.
> 2. What is the final value of `radiance`?
> 
> ~~~
> radiance = 1.0
> radiance = max(2.1, 2.0 + min(radiance, 1.1 * radiance - 0.5))
> ~~~
> {: .source}
{: .challenge}

> ## Spot the Difference
> 
> 1. Predict what each of the `print` statements in the program below will print.
> 2. Does `max(len(rich), poor)` run or produce an error message?
>    If it runs, does its result make any sense?
> 
> ~~~
> rich = "gold"
> poor = "tin"
> print(max(rich, poor))
> print(max(len(rich), len(poor)))
> ~~~
> {: .source}
{: .challenge}

> ## Getting Help
> 
> Use `help` to determine what the function `round` does,
> and write a program to round 3.141592653 to 3, 4, and 5 significant digits.
> Do you agree with the answers?
{: .challenge}
