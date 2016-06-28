---
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

## Creating Lists

Multiple values can be stored in lists:

~~~
objectives = ['Create lists.', 'Extract items from lists.','Modify lists.']
print(type(objectives))
~~~
{: .source}

~~~
<class 'list'>
~~~
{: .output}

Sometimes we are not sure how many values we will have so we can start with an empty list and fill it sequentially.

~~~
objectives = []
print(objectives)
objectives.append("Create lists.")
print(objectives)
objectives.append('Extract items from lists.')
print(objectives)
objectives.append('Modify lists.')
print(objectives)
~~~
{: .source}

~~~
[]
['Create lists.']
['Create lists.','Extract items from lists.']
['Create lists.','Extract items from lists.','Modify lists.']
~~~
{: .output}

Lists can also contain different types of values:

~~~
objectives = [1, 'Create lists.', 2, 'Extract items from lists.', 3, 'Modify lists.']
~~~
{: .source}

## Accessing Multiple Values

If you want to take a slice from the beginning of a sequence, you can omit the first index in the range:

~~~
date = "Monday 4 January 2016"
day = date[0:6]
print("Using 0 to begin range:", day)
day = date[:6]
print("Omitting beginning index:", day)
~~~
{: .source}

~~~
Using 0 to begin range: Monday
Omitting beginning index: Monday
~~~
{: .output}

And equally, you can omit the ending index in the range to take a slice to the very end of the sequence:

~~~
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
sond = months[8:12]
print("With known last position:", sond)
sond = months[8:len(months)]
print("Using len() to get last entry:", sond)
sond = months[6:]
("Omitting ending index:", sond)
~~~
{: .source}

~~~
With known last position: ["sep", "oct", "nov", "dec"]
Using len() to get last entry: ["sep", "oct", "nov", "dec"]
Omitting ending index: ["sep", "oct", "nov", "dec"]
~~~
{: .output}

So far we've seen how to use slicing to take single blocks of successive entries from a sequence. But what if we want to take a subset of entries that aren't next to eachother in the sequence?

You can achieve this by providing a third argument to the range within the brackets, called the _step size_. The example below shows how you can take every third entry in a list:

~~~
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
subset = primes[0:12:3]
print("subset", subset)
~~~
{: .source}

~~~
subset [2, 7, 17, 29]
~~~
{: .output}

Notice that the slice taken begins with the first entry in the range, followed by entries taken at equally-spaced intervals (the steps) thereafter. If you wanted to begin the subset with the third entry, you would need to specify that as the starting point of the sliced range:

~~~
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
subset = primes[2:12:3]
print("subset", subset)
~~~
{: .source}

~~~
subset [5, 13, 23, 37]
~~~
{: .output}

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

> ## Stepping Through a List
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

> ## Non-continuous slices
> Use the step size argument to create a new string that contains only every other character in the string "In an octopus's garden in the shade"  
>
> ~~~
> beatles = "In an octopus's garden in the shade"
> ~~~
> {: .source}
> 
> ~~~
> I notpssgre ntesae
> ~~~
> {: .output}
{: .challenge}

>## Slicing correctly
> Given the list below, which option underneath will return the subset of list entries `['nothing', 'drive', 'away,', 'can', 'them', 'for', 'day.']` ?
>
>~~~
>bowie = ['Though', 'nothing', 'will', 'drive', 'them', 'away', 'we', 'can', 'beat', 'them', 'just', 'for', 'one', 'day']
>~~~
>{: .source}
>
>a) bowie[1,3,5,7,9,11,13]  
>b) bowie[::2]  
>c) bowie[1::2]  
>d) bowie[:2]
>{: .challenge}

