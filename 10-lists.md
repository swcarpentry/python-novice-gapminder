---
layout: lesson
subtitle: Lists
teaching: 5
exercises: 10
---
> ## Learning Objectives
>
> * Learner will explain why programs need collections of values.
> * Learner will correctly explain each adjective in
>   "a mutable ordered collection of heterogeneous values".
> * Learner will write programs that create flat lists,
>   index them,
>   slice them,
>   and modify them through assignment and method calls.
{: .objectives}

FIXME: lesson content.

## From Strings to Lists and Back
{: .challenge}

Given this:

~~~
print('string to list:', list('tin'))
print('list to string:', ''.join(['g', 'o', 'l', 'd']))
~~~
{: .python}

~~~
['t', 'i', 'n']
'gold'
~~~
{: .output}

1. Explain in simple terms what `list("some string")` does.
2. What does `'-'.join(['x', 'y'])` generate?

## Indexing
{: .challenge}

What does the following program print?

~~~
values = [1, 3, 5, 7, 9]
print(values[values[0]])
~~~
{: .python}

## Fill in the Blanks
{: .challenge}

Fill in the blanks so that the program below produces the output shown.

~~~
values = ____
values.____(1)
values.____(3)
values.____(5)
print('first time:', values)
values = values[____]
print('second time:', values)
~~~
{: .python}

~~~
first time: [1, 3, 5]
second time: [3, 5]
~~~
{: .output}

## How Large is a Slice?
{: .challenge}

If 'low' and 'high' are both non-negative integers,
how long is the list `values[low:high]`?

## In Simple Terms
{: .challenge}

Assuming `values` is a list,
explain in simple terms what `del values[-1]` does.
