---
title: "Programming Style"
teaching: 10
exercises: 15
questions:
- "How can I make my programs more readable?"
- "How do most programmers format their code?"
objectives:
- "Provide sound justifications for basic rules of coding style."
- "Refactor one-page programs to make them more readable and justify the changes."
- "Use Python community coding standards (PEP-8)."
keypoints:
- "Follow standard Python style in your code."
- "Use docstrings to provide online help."
---
## Follow standard Python style in your code.

*   [PEP8](https://www.python.org/dev/peps/pep-0008):
    a style guide for Python that discusses topics such as how you should name variables,
    how you should use indentation in your code,
    how you should structure your `import` statements,
    etc.
    Adhering to PEP8 makes it easier for other Python developers to read and understand your code,
    and to understand what their contributions should look like.
    The [PEP8 application and Python library](https://pypi.python.org/pypi/pep8)
    can check your code for compliance with PEP8.

*   [numpydoc](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt):
    a standard for API documentation through docstrings used by NumPy, SciPy,
    and many other Python scientific computing pacakges.
    Adhering to numpydoc helps ensure that users and developers 
    will know how to use your Python package,
    either for their own analyses or as a component of their own Python packages.
    If you use numpydoc,
    you can also use existing tools such as [Sphinx](http://sphinx-doc.org/)
    to automatically generate HTML documentation for your API.

*   [Semantic Versioning](http://semver.org/):
    a standard describing how to define versions of your software
    no matter what language it's written in.
    Using Semantic Versioning makes it easy for other developers to understand
    what is guaranteed to stay the same and what might change across versions of your software.

## Use docstrings to provide online help.

*   If the first thing in a function is a character string
    that is not assigned to a variable,
    Python attaches it to the function as the online help.
*   Called a *docstring* (short for "documentation string").

~~~
def average(values):
    "Return average of values, or None if no values are supplied."

    if len(values) == 0:
        return None
    return sum(values) / average(values)

help(average)
~~~
{: .python}
~~~
Help on function average in module __main__:

average(values)
    Return average of values, or None if no values are supplied.
~~~
{: .output}

> ## Multiline Strings
>
> Often use *multiline strings* for documentation.
> These start and end with three quote characters (either single or double)
> and end with three matching characters.
>
> ~~~
> """This string spans
> multiple lines.
>
> Blank lines are allowed."""
> ~~~
> {: .python}
{: .callout}

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

> ## Clean Up This Code
>
> 1. Read this short program and try to predict what it does.
> 2. Run it: how accurate was your prediction?
> 3. Refactor the program to make it more readable.
>    Remember to run it after each change to ensure its behavior hasn't changed.
> 4. Compare your rewrite with your neighbor's.
>    What did you do the same?
>    What did you do differently, and why?
>
> ~~~
> import sys
> n = int(sys.argv[1])
> s = sys.argv[2]
> print(s)
> i = 0
> while i < n:
>     # print('at', j)
>     new = ''
>     for j in range(len(s)):
>         left = j-1
>         right = (j+1)%len(s)
>         if s[left]==s[right]: new += '-'
>         else: new += '*'
>     s=''.join(new)
>     print(s)
>     i += 1
> ~~~
> {: .source}
>
> Here's one solution.
>
> ~~~
> def string_machine(input_string, iterations):
>     """
>     Takes input_string and generates a new string with -'s and *'s
>     corresponding to characters that have identical adjacent characters
>     or not, respectively.  Iterates through this procedure with the resultant
>     strings for the supplied number of iterations.
>     """
>     print(input_string)
>     old = input_string
>     for i in range(iterations):
>         new = ''
>         # iterate through characters in previous string
>         for j in range(len(s)):
>             left = j-1
>             right = (j+1)%len(s) # ensure right index wraps around
>             if old[left]==old[right]:
>                 new += '-'
>             else:
>                 new += '*'
>         print(new)
>         # store new string as old
>         old = new
>
> string_machine('et cetera', 10)
> ~~~
> {: .source}
{: .challenge}

> ## Finding Neighbors
>
> This function is supposed to find the minimum value adjacent to 
> (but not in) a specified location in an array.
> For what inputs does it produce the wrong answer?
> How can it be repaired?
>
> ~~~
> def any_negative_neighbors(array, i, j, use_diagonals):
>     '''
>     Return True if any neighbors of (i,j) are negative, or False if none are.
>     Only check diagonal neighbors if use_diagonals is True.
>     '''
>
>     width, height = array.shape
>
>     if i > 0 and array[i-1, j] < 0: return True
>     if i < width and array[i+1, j] < 0: return True
>     if j > 0 and array[i, i-1] < 0: return True
>     if j < width and array[i, j+1] < 0: return True
>
>     if not use_diagonals: return False
>
>     if i > 0 and j > 0 and array[i-1, j-1] < 0: return True
>     if i > 0 and j < width and array[i-1, j+1] < 0: return True
>     if i < width and j > 0 and array[i+1, j-1] < 0: return True
>     if i < width and j < height and array[i+1, j+1] < 0: return True
> ~~~
> {: .source}
{: .challenge}
