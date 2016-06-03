---
layout: episode
title: "Lists"
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

> ## Creating Lists
>
>  Multiple values can be stored in lists:
>
> ~~~
> objectives = ['Create lists.', 'Extract items from lists.','Modify lists.']
>
> print(type(objectives))
> ~~~
>{: .source}
>
> ~~~
> <class 'list'>
> ~~~
> {: .output}

> Sometimes we are not sure how many values we will have so we can start with an empty list and fill it sequentially.
>
> ~~~
> objectives = []
> print(objectives)
> objectives.append("Create lists.")
> print(objectives)
> objectives.append('Extract items from lists.')
> print(objectives)
> objectives.append('Modify lists.')
> print(objectives)
> ~~~
> {: .source}
>
> ~~~
> []
> ['Create lists.']
> ['Create lists.','Extract items from lists.']
> ['Create lists.','Extract items from lists.','Modify lists.']
> ~~~
> {: .output}

> Lists can also contain different types of values:
>
> ~~~
> objectives = [1, 'Create lists.', 2, 'Extract items from lists.', 3, 'Modify lists.']
> ~~~
> {: .source}




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
> print(values[0])
> print(values[1:3])
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


> ## Working with the End
>
> 1. Assuming `values` is a list,
> explain in simple terms what `del values[-1]` does.
> 2. How can you display all elements but the last one without changing `values`?
{: .challenge}

> ## Stepping through a List
>  
> What if we want to sequentially go through the elements of a list in a particular manner?
> Discuss the output of the following commands:
>
> ~~~
> values = [1,2,3,4,5,6,7]
> values[::2]
> values[::-1]
> ~~~
> {: .source}
>
> How can you extract a list of the even numbers from `values`?
{: .challenge}


> ## Dealing with Bounds
>
> Explain how python is handling out-of-bound indices by trying these commands:
>
> ~~~
> values[0:20]
> values[-1:3]
> ~~~
> {: .source}
{: .challenge}
