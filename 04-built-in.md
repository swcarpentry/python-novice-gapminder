---
layout: lesson
subtitle: Built-in Functions (and Methods) and Help
teaching: 10
exercises: 10
---
> ## Learning Objectives
>
> * Learner will explain the purpose of functions.
> * Learner will correctly call built-in Python functions such as `len`, `max`, and `min`.
> * Learner will correctly nest calls to built-in functions.
> * Learner will use `help` to display documentation for built-in functions.
{: .objectives}

FIXME: lesson content.

### Functions

Lets use Python's maths functions to calculate a mean or average

```python
a = 2
b = 7
c = 4
average = a + b + c / 3
average
```

Oops! I forgot that division happens before addition. Can you see the mistake?

```python
a = 2
b = 7
c = 4
average = (a + b + c) / 3
average
```

If we wanted to just know the answer in round numbers we could convert the floating point number to an integer
```python
whole = int(average)
whole
```

Rounding it to 2 decimal places would be a bit trickier. 

### Built in Functions

Python has common tasks already built in and rounding numbers is one of them.

```python
round(average)
```

The function has parenthesis after it. The variable we want to perform the function on is inside them. The default behaviour is to round to whole numbers. If we wanted to round to 2 decimal places, we need to stipulate that with a second value inside the parenthesis.

```python
round(average,2)
```

### Getting Help

In the Jupyter notebook we can get help on functions in a couple of ways. Place the cursor inside the parenthesis of the function, hold down `shift` and press `tab`. Notice they are close together on the left side of the keyboard.

Typing a function name with a question mark after it will bring up the documentation.
  
```python
round?
```

The third way is to use the help function. This will work at any python prompt, rather than just in the Jupyter Notebook like the first two examples.

```python
help(round)
```

  Now that you know how to get help, try out `len()`,`sum()`,`min()` and `max()`.

## What Happens When
{: .challenge}

1. Explain in simple terms the order of operations in the following program:
   when does the addition happen, when does the subtraction happen,
   when is each function called, etc.
2. What is the final value of `radiance`?

~~~
radiance = 1.0
radiance = max(2.0 + min(radiance, 1.1 * radiance - 0.5))
~~~
{: .python}

## Spot the Difference
{: .challenge}

1. Predict what each of the `print` statements in the program below will print.
2. Does `max(len(rich), poor)` run or produce an error message?
   If it runs, does its result make any sense?

~~~
rich = "gold"
poor = "tin"
print(max(rich, poor))
print(max(len(rich), len(poor)))
~~~
{: .python}

## Getting Help
{: .challenge}

Use `help` to determine what the function `round` does,
and write a program to round 3.141592653 to 3, 4, and 5 significant digits.
Do you agree with the answers?
