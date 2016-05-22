---
layout: episode
title: "Conditionals"
teaching: 5
exercises: 10
questions:
- "How can programs make decisions?"
objectives:
- "Correctly write programs that use if and else statements and simple Boolean expressions (without logical operators)."
- "Trace the execution of unnested conditionals and conditionals inside loops."
keypoints:
- FIXME
---
In the course of programming, we may find that we need our code to make a
choice.  This choice may be to execute or not execute a certain task or to
execute one or a subset of multiple tasks.  We can often use **conditional**
statements in order to direct our program in these ways.  Conditional statements
are often referred to as "if" statements, since their syntax involves the
keyword "if" in python and many other languages.  Their general structure looks
like:

~~~
if statement_1:
    task_to_be_done_if_statement_1_is_true
~~~
{: .source python}

In the above code, the indented line, `task_to_be_done_if_statement_1_is_true`,
will only be executed if the content of statement_1 evaluates to true.  What if
we want a task to be executed if statement_1 is false?  We can use the "else"
keyword in conjunction with "if" (sometimes referred to as an "if-else"
statement).

~~~
if statement_1:
    task_to_be_done_if_statement_1_is_true
else:
    task_to_be_done_if_statement_1_is_false
~~~
{: .source}

For example, we might use the comparator `>`, as in the following:

~~~
water_temp = 120 
pressure = 1

if water_temp > 100:
    print("Boiling")
else:
    print("Not boiling")
~~~
{: .source}

I can also more complex conditional statements with boolean operators
like **and** and **or**, and use comparators like "<", ">"

~~~
water_temp = 30
pressure = 1

if water_temp < 100 and water_temp > 0:
    state = "liquid"

print("The water is currently ", state)
~~~
{: .source}

> ## Trimming Values
> 
> Fill in the blanks so that this program trims the data
> by replacing all values less than zero with zero
> and all values greater than one with one.
> 
> ~~~
> original = [-1.5, 0.2, 0.4, 0.0, 1.3, 0.4]
> result = ____
> for value in original:
>     if ____:
>         result.append(0.0)
>     elif ____:
>         result.append(1.0)
>     else:
>         result.append(____)
> print(result)
> ~~~
> {: .source}
> 
> ~~~
> [0.0, 0.2, 0.4, 0.0, 1.0, 0.4]
> ~~~
> {: .output}
{: .challenge}

> ## Processing Small Files
> 
> Modify this program so that it only processes files with fewer than 50 records.
> 
> ~~~
> import glob
> import pandas as pd
> for filename in glob.glob('data/*.csv'):
>     contents = pd.read_csv(filename)
>     ____:
>         print(filename,len(contents))
> ~~~
> {: .source}
{: .challenge}

> ## Initializing
> 
> Modify this program so that it finds the largest and smallest values in the list
> no matter what the range of values originally is.
> 
> ~~~
> values = [...some test data...]
> smallest, largest = None, None
> for v in values:
>     if ____:
>         smallest, largest = v, v
>     ____:
>         smallest = min(____, v)
>         largest = max(____, v)
> print(smallest, largest)
> ~~~
> {: .source}
> 
> What are the advantages and disadvantages of using this method
> to find the range of the data?
{: .challenge}

> ## Tracing Execution
> 
> What does this program print?
> 
> ~~~
> pressure = 71.9
> if pressure 50.0:
>     pressure = 25.0
> elif pressure <= 50.0:
>     pressure = 0.0
> print(pressure)
> ~~~
{: .challenge}
