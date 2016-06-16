---
layout: episode
title: "For Loops"
teaching: 10
exercises: 10
questions:
- "How can I make a program do many things?"
objectives:
- "Explain what for loops are normally used for."
- "Trace the execution of a simple (unnested) loop and correctly state the values of variables in each iteration."
- "Write for loops that use the Accumulator pattern to aggregate values."
keypoints:
- FIXME
---
FIXME: lesson content.

> ## Tracing Execution
>
> Create a table showing the numbers of the lines that are executed when this program runs,
> and the values of the variables after each line is executed.
>
> ~~~
> total = 0
> for char in "tin":
>     total = total + 1
> ~~~
> {: .source}
{: .challenge}

> ## Reversing a String
>
> Fill in the blanks in the program below so that it prints "nit"
> (the reverse of the original character string "tin").
>
> ~~~
> original = "tin"
> result = ____
> for char in original:
>     result = ____
> print(result)
> ~~~
> {: .source}
{: .challenge}

> ## Cumulative sum
>
> Reorder and properly indent the following program so that it prints an array with the cumulative sum of data.
> (should print [1,3,5,10]).
>
> ~~~
> cumulative += [sum]
> for number in data:
> cumulative = []
> sum += number
> print(cumulative)
> data = [1,2,2,5]
> ~~~
> {: .source}
{: .challenge}

> ## Looping through Dictionaries
>
> So far, we've seen two ways to loop through objects in Python. 
> Looping through a *string* iterates through character by character.
> Looping through a *list* iterates through item by item. 
> We can also loop through python *dictionaries*. 
> The default looping behavior iterates through each key in the dictionary.
> 
> ~~~ {.python}
> d = {'apples': 0.49, 'oranges': 0.99, 'pears': 1.49, 'bananas': 0.32}
> #default looping
> for key in d:
>    print key, d[key]
> ~~~
> 
> Knowing this, use a for loop to calculate how much it'll cost you 
> to buy 2 pieces of each fruit.
