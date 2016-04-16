---
layout: episode
title: Lists
teaching: 5
exercises: 10
questions:
- "How can I store multiple values?"
objectives:
- "Explain why programs need collections of values."
- "Correctly explain each adjective in 'a mutable ordered collection of heterogeneous values'."
- "Write programs that create flat lists, index them, slice them, and modify them through assignment and method calls."
keypoints:
- FIXME
---
FIXME: lesson content.

> ## From Strings to Lists and Back
> 
> Given this:
> 
> ~~~
> print('string to list:', list('tin'))
> print('list to string:', ''.join(['g', 'o', 'l', 'd']))
> ~~~
> {: .source}
> 
> ~~~
> ['t', 'i', 'n']
> 'gold'
> ~~~
> {: .output}
> 
> 1. Explain in simple terms what `list("some string")` does.
> 2. What does `'-'.join(['x', 'y'])` generate?
{: .challenge}

> ## Indexing
> 
> What does the following program print?
> 
> ~~~
> values = [1, 3, 5, 7, 9]
> print(values[values[0]])
> ~~~
> {: .source}
{: .challenge}

> ## Fill in the Blanks
> 
> Fill in the blanks so that the program below produces the output shown.
> 
> ~~~
> values = ____
> values.____(1)
> values.____(3)
> values.____(5)
> print('first time:', values)
> values = values[____]
> print('second time:', values)
> ~~~
> {: .source}
> 
> ~~~
> first time: [1, 3, 5]
> second time: [3, 5]
> ~~~
> {: .output}
{: .challenge}

> ## How Large is a Slice?
> 
> If 'low' and 'high' are both non-negative integers,
> how long is the list `values[low:high]`?
{: .challenge}

> ## In Simple Terms
> 
> Assuming `values` is a list,
> explain in simple terms what `del values[-1]` does.
{: .challenge}
