---
title: "Built-in Functions and Help"
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
keypoints:
- "A function may take zero or more arguments."
- "Commonly-used built-in functions include `max`, `min`, and `round`."
- "Functions may only work for certain (combinations of) arguments."
- "Functions may have default values for some arguments."
- "Use the built-in function `help` to get help for a function."
- "The Jupyter Notebook has two ways to get help."
- "Every function returns something."
---
## A function may take zero or more arguments.

*   We have seen some functions already --- now let's take a closer look.
*   An *argument* is a value passed into a function.
*   `len` takes exactly one.
*   `int`, `str`, and `float` create a new value from an existing one.
*   `print` takes zero or more.
*   `print` with no arguments prints a blank line.
    *   Must always use parentheses, even if they're empty,
        so that Python knows a function is being called.

~~~
print('before')
print()
print('after')
~~~
{: .python}
~~~
before

after
~~~
{: .output}

## Commonly-used built-in functions include `max`, `min`, and `round`.

*   Use `max` to find the largest value of one or more values.
*   Use `min` to find the smallest.
*   Both work on character strings as well as numbers.
    *   "Larger" and "smaller" use (0-9, A-Z, a-z) to compare letters.

~~~
print(max(1, 2, 3))
print(min('a', 'A', '0'))
~~~
{: .python}
~~~
3
0
~~~
{: .output}

## Functions may only work for certain (combinations of) arguments.

*   `max` and `min` must be given at least one argument.
    *   "Largest of the empty set" is a meaningless question.
*   And they must be given things that can meaningfully be compared.

~~~
print(max(1, 'a'))
~~~
{: .python}
~~~
TypeError: unorderable types: str() > int()
~~~
{: .error}

## Functions may have default values for some arguments.

*   `round` will round off a floating-point number.
*   By default, rounds to zero decimal places.

~~~
round(3.712)
~~~
{: .python}
~~~
4
~~~
{: .output}

*   We can specify the number of decimal places we want.

~~~
round(3.712, 1)
~~~
{: .python}
~~~
3.7
~~~
{: .output}

## Use the built-in function `help` to get help for a function.

*   Every built-in function has online documentation.

~~~
help(round)
~~~
{: .python}
~~~
Help on built-in function round in module builtins:

round(...)
    round(number[, ndigits]) -> number

    Round a number to a given precision in decimal digits (default 0 digits).
    This returns an int when called with one argument, otherwise the
    same type as the number. ndigits may be negative.
~~~
{: .output}

## The Jupyter Notebook has two ways to get help.

*   Place the cursor inside the parenthesis of the function,
    hold down `shift`,
    and press `tab`.
*   Or type a function name with a question mark after it.

## Every function returns something.

*   Every function call produces some result.
*   If the function doesn't have a useful result to return,
    it usually returns the special value `None`.

~~~
result = print('example')
print('result of print is', result)
~~~
{: .python}
~~~
example
result of print is None
~~~
{: .output}

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

> ## Why Not?
>
> Why don't `max` and `min` return `None` when they are given no arguments?
{: .challenge}
