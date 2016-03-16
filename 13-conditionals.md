---
layout: lesson
subtitle: Conditionals
teaching: 5
exercises: 10
---
> ## Learning Objectives
>
> * Learner will correctly write programs that use `if` and simple Boolean expressions
>   (without logical operators).
> * Learner will trace the execution of unnested conditionals
>   and conditionals inside loops.
{: .objectives}

FIXME: lesson content.

## Trimming Values
{: .challenge}

Fill in the blanks so that this program trims the data
by replacing all values less than zero with zero
and all values greater than one with one.

~~~
original = [-1.5, 0.2, 0.4, 0.0, 1.3, 0.4]
result = ____
for value in original:
    if ____:
        result.append(0.0)
    elif ____:
        result.append(1.0)
    else:
        result.append(____)
print(result)
~~~
{: .python}

~~~
[0.0, 0.2, 0.4, 0.0, 1.0, 0.4]
~~~
{: .output}

## Processing Small Files
{: .challenge}

Modify this program so that it only processes files with fewer than 50 records.

~~~
import glob
import pandas as pd
for filename in glob.glob('data/*.csv'):
    contents = pd.read_csv(filename)
    ____:
        FIXME: what to include as processing step?
~~~
{: .python}

## Initializing
{: .challenge}

Modify this program so that it finds the largest and smallest values in the list
no matter what the range of values originally is.

~~~
values = [...some test data...]
smallest, largest = None, None
for v in values:
    if ____:
        smallest, largest = v, v
    ____:
        smallest = min(____, v)
        largest = max(____, v)
print(smallest, largest)
~~~
{: .python}

What are the advantages and disadvantages of using this method
to find the range of the data?

## Tracing Execution
{: .challenge}

What does this program print?

~~~
pressure = 71.9
if pressure 50.0:
    pressure = 25.0
elif pressure <= 50.0:
    pressure = 0.0
print(pressure)
~~~
