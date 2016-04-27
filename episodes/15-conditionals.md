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
FIXME: lesson content.

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
>         print filename,len(contents)
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
