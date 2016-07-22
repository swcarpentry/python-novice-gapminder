---
title: "The Call Stack"
teaching: 10
exercises: 15
questions:
- "How do function calls actually work?"
objectives:
- "Identify local and global variables."
- "Identify parameters as local variables."
- "Trace values in non-recursive nested function calls."
keypoints:
- "The scope of a variable is the part of a program that can 'see' that variable."
- "Python keeps track of variables during function calls using a call stack."
---
## The scope of a variable is the part of a program that can 'see' that variable.

*   There are only so many sensible names for variables.
*   People using functions shouldn't have to worry about
    what variable names the author of the function used.
*   People writing functions shouldn't have to worry about
    what variable names the function's caller uses.
*   The part of a program in which a variable is visible is called its *scope*.

~~~
pressure = 103.9

def adjust(t):
    temperature = t * 1.43 / pressure
    return temperature
~~~
{: .python}

*   `pressure` is a *global variable*.
    *   Defined outside any particular function.
    *   Visible everywhere.
*   `t` and `temperature` are *local variables* in `adjust`.
    *   Defined in the function.
    *   Not visible in the main program.
    *   Remember: a function parameter is a variable
        that is automatically assigned a value when the function is called.

~~~
print('adjusted:', adjust(0.9))
print('temperature after call:', temperature)
~~~
{: .python}
~~~
adjusted: 0.01238691049085659
~~~
{: .output}
~~~
Traceback (most recent call last):
  File "/Users/swcarpentry/foo.py", line 8, in <module>
    print('temperature after call:', temperature)
NameError: name 'temperature' is not defined
~~~
{: .error}

## Python keeps track of variables during function calls using a call stack.

*   Every time a function is called, Python:
    *   Creates a new *stack frame* to hold its variables.
    *   Puts this on top of a *call stack*.
*   A function can only see:
    *   The top frame of the stack (i.e., the one created for it).
    *   The bottom frame (holding the global variables).
    *   And *not* the intermediate frames (holding variables for other active calls).

~~~
def double(x):
    result = 2 * x
    return result

def double_cube(x):
    value = x ** 3
    result = double(value)
    return result

x = 4
result = double_cube(x)
print('final result:', result)
~~~
{: .python}
~~~
final result: 128
~~~
{: .output}

> ## Stacking and Unstacking
>
> Trace the values on the call stack during the execution of the following program:
>
> ~~~
> def double(x):
>     result = 2 * x
>     return result
>
> def cube(x):
>     result = x ** 3
>     return result
>
> x = 4
> result = double(cube(x))
> print('final result:', result)
> ~~~
> {: .python}
{: .challenge}

> ## Local and Global Variable Use
>
> Trace the values of all variables in this program as it is executed.
> (Use '---' as the value of variables before and after they exist.)
>
> ~~~
> limit = 100
>
> def clip(value):
>     return min(max(0.0, value), limit)
>
> value = -22.5
> print(clip(value))
> ~~~
> {: .source}
{: .challenge}
