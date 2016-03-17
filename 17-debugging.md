---
layout: lesson
subtitle: Debugging
teaching: 10
exercises: 10
---
> ## Learning Objectives
>
> * Learner will diagnose bugs in short functions containing simple logic errors.
> * Learner will correct simple logic errors in short functions.
{: .objectives}

FIXME: lesson content.

## Finding Neighbors
{: .challenge}

This function is supposed to find the minimum value adjacent to (but not in) a specified location in an array.
For what inputs does it produce the wrong answer?
How can it be repaired?

~~~
def any_negative_neighbors(array, i, j, use_diagonals):
    '''
    Return True if any neighbors of (i,j) are negative, or False if none are.
    Only check diagonal neighbors if use_diagonals is True.
    '''

    width, height = array.shape

    if i > 0 and array[i-1, j] < 0: return True
    if i < width and array[i+1, j] < 0: return True
    if j > 0 and array[i, i-1] < 0: return True
    if j < width and array[i, j+1] < 0: return True

    if not use_diagonals: return False

    if i > 0 and j > 0 and array[i-1, j-1] < 0: return True
    if i > 0 and j < width and array[i-1, j+1] < 0: return True
    if i < width and j > 0 and array[i+1, j-1] < 0: return True
    if i < width and j < height and array[i+1, j+1] < 0: return True
~~~
{: .python}
