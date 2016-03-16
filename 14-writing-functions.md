---
layout: lesson
subtitle: Writing Functions
teaching: 10
exercises: 15
---
> ## Learning Objectives
>
> * Learner will explain and identify the difference between function *definition* and function *call*.
> * Learner will write a function that takes a small, fixed number of arguments and producing a single result.
> * Learner will correctly identify local and global variable use in a function.
{: .objectives}

FIXME: lesson content.

FIXME: [elegant explanation of functions](https://twitter.com/minisciencegirl/status/693486088963272705):
() contains the ingredients for the function while the body contains the recipe.

## Definition and Use
{: .challenge}

What does the following program print?

~~~
def report(pressure):
    print('pressure is', pressure)

print('calling', report, 22.5)

## Encapsulation
{: .challenge}

Fill in the blanks to create a function
that takes a single filename as an argument,
loads the data in the file named by the argument,
and returns the minimum value in that data.

~~~
import pandas as pd

def min_in_data(____):
    data = ____
    return ____
~~~
{: .python}

## Local and Global Variable Use
{: .challenge}

Trace the values of all variables in this program as it is executed.
(Use '---' as the value of variables before and after they exist.)

~~~
limit = 100

def clip(value):
    return min(max(0.0, value), limit)

value = -22.5
print(clip(value))
~~~
{: .python}
