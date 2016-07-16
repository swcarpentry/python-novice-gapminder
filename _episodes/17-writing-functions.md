---
title: "Writing Functions"
teaching: 10
exercises: 15
questions:
- "How can I create my own functions?"
objectives:
- "Explain and identify the difference between function definition and function call."
- "Write a function that takes a small, fixed number of arguments and producing a single result."
- "Correctly identify local and global variable use in a function."
- "Correctly identify portions of source code that will be displayed as online help, and in particular distinguish docstrings from comments."
- "Write short docstrings for functions."
keypoints:
- FIXME
---
FIXME: lesson content.

FIXME: [elegant explanation of functions](https://twitter.com/minisciencegirl/status/693486088963272705):
() contains the ingredients for the function while the body contains the recipe.

> ## Definition and Use
>
> What does the following program print?
>
> ~~~
> def report(pressure):
>     print('pressure is', pressure)
>
> print('calling', report, 22.5)
{: .challenge}

> ## Encapsulation
>
> Fill in the blanks to create a function
> that takes a single filename as an argument,
> loads the data in the file named by the argument,
> and returns the minimum value in that data.
>
> ~~~
> import pandas as pd
>
> def min_in_data(____):
>     data = ____
>     return ____
> ~~~
> {: .source}
{: .challenge}

> ## What Will Be Shown?
>
> Highlight the lines in the code below that will be available as online help.
> Are there lines that should be made available, but won't be?
> Will any lines produce a syntax error or a runtime error?
>
> ~~~
> "Find maximum edit distance between multiple sequences."
> # This finds the maximum distance between all sequences.
>
> def overall_max(sequences):
>     '''Determine overall maximum edit distance.'''
>
>     highest = 0
>     for left in sequences:
>         for right in sequences:
>             '''Avoid checking sequence against itself.'''
>             if left != right:
>                 this = edit_distance(left, right)
>                 highest = max(highest, this)
>
>     # Report.
>     return highest
> ~~~
> {: .source}
{: .challenge}

> ## Document This
>
> Turn the comment on the following function into a docstring
> and check that `help` displays it properly.
>
> ~~~
> def middle(a, b, c):
>     # Return the middle value of three.
>     # Assumes the values can actually be compared.
>     values = [a, b, c]
>     values.sort()
>     return values[1]
> ~~~
> {: .source}
{: .challenge}
