---
layout: lesson
subtitle: Documentation
teaching: 5
exercises: 5
---
> ## Learning Objectives
>
> * Learner will correctly identify portions of source code that will be displayed as online help,
>   and in particular distinguish docstrings from comments.
> * Learner will write short docstrings for functions.
{: objectives}

FIXME: lesson content.

## What Will Be Shown?
{: .challenge}

Highlight the lines in the code below that will be available as online help.
Are there lines that should be made available, but won't be?
Will any lines produce a syntax error or a runtime error?

~~~
"Find maximum edit distance between multiple sequences."
# This finds the maximum distance between all sequences.

def overall_max(sequences):
    '''Determine overall maximum edit distance.'''

    highest = 0
    for left in sequences:
        for right in sequences:
            '''Avoid checking sequence against itself.'''
            if left != right:
                this = edit_distance(left, right)
                highest = max(highest, this)

    # Report.
    return highest
~~~
{: .python}

# Document This
{: .challenge}

Turn the comment on the following function into a docstring
and check that `help` displays it properly.

~~~
def middle(a, b, c):
    # Return the middle value of three.
    # Assumes the values can actually be compared.
    values = [a, b, c]
    values.sort()
    return values[1]
~~~
{: .python}
