---
title: Variable Scope
teaching: 10
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

- Identify local and global variables.
- Identify parameters as local variables.
- Read a traceback and determine the file, function, and line number on which the error occurred, the type of error, and the error message.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How do function calls actually work?
- How can I determine where errors occurred?

::::::::::::::::::::::::::::::::::::::::::::::::::

## The scope of a variable is the part of a program that can 'see' that variable.

- There are only so many sensible names for variables.
- People using functions shouldn't have to worry about
  what variable names the author of the function used.
- People writing functions shouldn't have to worry about
  what variable names the function's caller uses.
- The part of a program in which a variable is visible is called its *scope*.

```python
pressure = 103.9

def adjust(t):
    temperature = t * 1.43 / pressure
    return temperature
```

- `pressure` is a *global variable*.
  - Defined outside any particular function.
  - Visible everywhere.
- `t` and `temperature` are *local variables* in `adjust`.
  - Defined in the function.
  - Not visible in the main program.
  - Remember: a function parameter is a variable
    that is automatically assigned a value when the function is called.

```python
print('adjusted:', adjust(0.9))
print('temperature after call:', temperature)
```

```output
adjusted: 0.01238691049085659
```

```error
Traceback (most recent call last):
  File "/Users/swcarpentry/foo.py", line 8, in <module>
    print('temperature after call:', temperature)
NameError: name 'temperature' is not defined
```

:::::::::::::::::::::::::::::::::::::::  challenge

## Local and Global Variable Use

Trace the values of all variables in this program as it is executed.
(Use '---' as the value of variables before and after they exist.)

```python
limit = 100

def clip(value):
    return min(max(0.0, value), limit)

value = -22.5
print(clip(value))
```

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Reading Error Messages

Read the traceback below, and identify the following:

1. How many levels does the traceback have?
2. What is the file name where the error occurred?
3. What is the function name where the error occurred?
4. On which line number in this function did the error occur?
5. What is the type of error?
6. What is the error message?

```error
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-2-e4c4cbafeeb5> in <module>()
      1 import errors_02
----> 2 errors_02.print_friday_message()

/Users/ghopper/thesis/code/errors_02.py in print_friday_message()
     13
     14 def print_friday_message():
---> 15     print_message("Friday")

/Users/ghopper/thesis/code/errors_02.py in print_message(day)
      9         "sunday": "Aw, the weekend is almost over."
     10     }
---> 11     print(messages[day])
     12
     13

KeyError: 'Friday'
```

:::::::::::::::  solution

## Solution

1. Three levels.
2. `errors_02.py`
3. `print_message`
4. Line 11
5. `KeyError`. These errors occur when we are trying to look up a key that does not exist (usually in a data
  structure such as a dictionary). We can find more information about the `KeyError` and other built-in exceptions
  in the [Python docs](https://docs.python.org/3/library/exceptions.html#KeyError).
6. `KeyError: 'Friday'`
  
  

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- The scope of a variable is the part of a program that can 'see' that variable.

::::::::::::::::::::::::::::::::::::::::::::::::::


