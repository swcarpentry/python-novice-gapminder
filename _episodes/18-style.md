---
title: "Programming Style"
teaching: 15
exercises: 15
questions:
- "How can I make my programs more readable?"
- "How do most programmers format their code?"
- "How can programs check their own operation?"
objectives:
- "Provide sound justifications for basic rules of coding style."
- "Refactor one-page programs to make them more readable and justify the changes."
- "Use Python community coding standards (PEP-8)."
keypoints:
- "Follow standard Python style in your code."
- "Use docstrings to provide online help."
---

## Coding style

Coding style helps us to understand the code better. It helps to maintain and change the code.
Python relies strongly on coding style, as we may notice by the indentation we apply to lines to define different blocks of code.
Python proposes a standard style through one of its first Python Enhancement Proposals (PEP), [PEP8](https://www.python.org/dev/peps/pep-0008), and highlight the importance of readability in the [Zen of Python](https://www.python.org/dev/peps/pep-0020).

We may highlight some points:
*   document your code
*   use clear, meaningful variable names
*   use white-space, *not* tabs, to indent lines


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
*   [Google style guide on Python](https://google.github.io/styleguide/pyguide.html) 
    supports the use of PEP8 and extend the coding style to more specific structure of 
    a Python code, which may be interesting also to follow.

## Use assertions to check for internal errors.

Assertions are a simple, but powerful method for making sure that the context in which your code is executing is as you expect.

~~~
def calc_bulk_density(mass, volume):
    '''Return dry bulk density = powder mass / powder volume.'''
    assert volume > 0
    return mass / volume
~~~
{: .language-python}

If the assertion is `False`, the Python interpreter raises an `AssertionError` runtime exception. The source code for the expression that failed will be displayed as part of the error message. To ignore assertions in your code run the interpreter with the '-O' (optimize) switch. Assertions should contain only simple checks and never change the state of the program. For example, an assertion should never contain an assignment.

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
    return sum(values) / len(values)

help(average)
~~~
{: .language-python}
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
> {: .language-python}
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
> {: .language-python}
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
> {: .language-python}
> > ## Solution
> >
> > ~~~
> > def middle(a, b, c):
> >     '''Return the middle value of three.
> >     Assumes the values can actually be compared.'''
> >     values = [a, b, c]
> >     values.sort()
> >     return values[1]
> > ~~~
> > {: .language-python}
> {: .solution}
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
> n = 10
> s = 'et cetera'
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
> {: .language-python}
>
> > ## Solution
> >
> > Here's one solution.
> >
> > ~~~
> > def string_machine(input_string, iterations):
> >     """
> >     Takes input_string and generates a new string with -'s and *'s
> >     corresponding to characters that have identical adjacent characters
> >     or not, respectively.  Iterates through this procedure with the resultant
> >     strings for the supplied number of iterations.
> >     """
> >     print(input_string)
> >     old = input_string
> >     for i in range(iterations):
> >         new = ''
> >         # iterate through characters in previous string
> >         for j in range(len(input_string)):
> >             left = j-1
> >             right = (j+1)%len(input_string) # ensure right index wraps around
> >             if old[left]==old[right]:
> >                 new += '-'
> >             else:
> >                 new += '*'
> >         print(new)
> >         # store new string as old
> >         old = new
> >
> > string_machine('et cetera', 10)
> > ~~~
> > {: .language-python}
> > 
> > ~~~
> > et cetera
> > *****-***
> > ----*-*--
> > ---*---*-
> > --*-*-*-*
> > **-------
> > ***-----*
> > --**---**
> > *****-***
> > ----*-*--
> > ---*---*-
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}
