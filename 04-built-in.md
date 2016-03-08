---
layout: lesson
subtitle: Built-in Functions (and Methods) and Help
---
> ## Learning Objectives
>
> * Learner will explain the purpose of functions.
> * Learner will correctly call built-in Python functions such as `len`, `max`, and `min`.
> * Learner will correctly nest calls to built-in functions.
> * Learner will use `help` to display documentation for built-in functions.
{: .objectives}

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
> radiance = max(2.0 + min(radiance, 1.1 * radiance - 0.5))
> ~~~
> {: .python}
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
> {: .python}
{: .challenge}

> ## Getting Help
>
> Use `help` to determine what the function `round` does,
> and write a program to round 3.141592653 to 3, 4, and 5 significant digits.
> Do you agree with the answers?
{: .challenge}
