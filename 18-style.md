---
title: Programming Style
teaching: 15
exercises: 15
---

::::::::::::::::::::::::::::::::::::::: objectives

- Provide sound justifications for basic rules of coding style.
- Refactor one-page programs to make them more readable and justify the changes.
- Use Python community coding standards (PEP-8).

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can I make my programs more readable?
- How do most programmers format their code?
- How can programs check their own operation?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Coding style

A consistent coding style helps others (including our future selves) read and understand code more easily. Code is read much more often than it is written, and as the [Zen of Python](https://www.python.org/dev/peps/pep-0020) states, "Readability counts".
Python proposed a standard style through one of its first Python Enhancement Proposals (PEP), [PEP8](https://www.python.org/dev/peps/pep-0008).

Some points worth highlighting:

- document your code and ensure that assumptions, internal algorithms, expected inputs, expected outputs, etc., are clear
- use clear, semantically meaningful variable names
- use white-space, *not* tabs, to indent lines (tabs can cause problems across different text editors, operating systems, and version control systems)

## Follow standard Python style in your code.

- [PEP8](https://www.python.org/dev/peps/pep-0008):
  a style guide for Python that discusses topics such as how to name variables,
  how to indent your code,
  how to structure your `import` statements,
  etc.
  Adhering to PEP8 makes it easier for other Python developers to read and understand your code, and to understand what their contributions should look like.
- To check your code for compliance with PEP8, you can use the [pycodestyle application](https://pypi.org/project/pycodestyle/) and tools like the [black code formatter](https://github.com/psf/black) can automatically format your code to conform to PEP8 and pycodestyle (a Jupyter notebook formatter also exists [nb\_black](https://github.com/dnanhkhoa/nb_black)).
- Some groups and organizations follow different style guidelines besides PEP8. For example, the [Google style guide on Python](https://google.github.io/styleguide/pyguide.html) makes slightly different recommendations. Google wrote an application that can help you format your code in either their style or PEP8 called [yapf](https://github.com/google/yapf/).
- With respect to coding style, the key is *consistency*. Choose a style for your project be it PEP8, the Google style, or something else and do your best to ensure that you and anyone else you are collaborating with sticks to it. Consistency within a project is often more impactful than the particular style used. A consistent style will make your software easier to read and understand for others and for your future self.

## Use assertions to check for internal errors.

Assertions are a simple but powerful method for making sure that the context in which your code is executing is as you expect.

```python
def calc_bulk_density(mass, volume):
    '''Return dry bulk density = powder mass / powder volume.'''
    assert volume > 0
    return mass / volume
```

If the assertion is `False`, the Python interpreter raises an `AssertionError` runtime exception. The source code for the expression that failed will be displayed as part of the error message. To ignore assertions in your code run the interpreter with the '-O' (optimize) switch. Assertions should contain only simple checks and never change the state of the program. For example, an assertion should never contain an assignment.

## Use docstrings to provide builtin help.

If the first thing in a function is a character string that is not assigned directly to a variable, Python attaches it to the function, accessible via the builtin help function. This string that provides documentation is also known as a *docstring*.

```python
def average(values):
    "Return average of values, or None if no values are supplied."

    if len(values) == 0:
        return None
    return sum(values) / len(values)

help(average)
```

```output
Help on function average in module __main__:

average(values)
    Return average of values, or None if no values are supplied.
```

:::::::::::::::::::::::::::::::::::::::::  callout

## Multiline Strings

Often use *multiline strings* for documentation.
These start and end with three quote characters (either single or double)
and end with three matching characters.

```python
"""This string spans
multiple lines.

Blank lines are allowed."""
```

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## What Will Be Shown?

Highlight the lines in the code below that will be available as online help.
Are there lines that should be made available, but won't be?
Will any lines produce a syntax error or a runtime error?

```python
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
```

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Document This

Use comments to describe and help others understand potentially unintuitive
sections or individual lines of code. They are especially useful to whoever
may need to understand and edit your code in the future, including yourself.

Use docstrings to document the acceptable inputs and expected outputs of a method
or class, its purpose, assumptions and intended behavior. Docstrings are displayed
when a user invokes the builtin `help` method on your method or class.

Turn the comment in the following function into a docstring
and check that `help` displays it properly.

```python
def middle(a, b, c):
    # Return the middle value of three.
    # Assumes the values can actually be compared.
    values = [a, b, c]
    values.sort()
    return values[1]
```

:::::::::::::::  solution

## Solution

```python
def middle(a, b, c):
    '''Return the middle value of three.
    Assumes the values can actually be compared.'''
    values = [a, b, c]
    values.sort()
    return values[1]
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Clean Up This Code

1. Read this short program and try to predict what it does.
2. Run it: how accurate was your prediction?
3. Refactor the program to make it more readable.
  Remember to run it after each change to ensure its behavior hasn't changed.
4. Compare your rewrite with your neighbor's.
  What did you do the same?
  What did you do differently, and why?

```python
n = 10
s = 'et cetera'
print(s)
i = 0
while i < n:
    # print('at', j)
    new = ''
    for j in range(len(s)):
        left = j-1
        right = (j+1)%len(s)
        if s[left]==s[right]: new = new + '-'
        else: new = new + '*'
    s=''.join(new)
    print(s)
    i += 1
```

:::::::::::::::  solution

## Solution

Here's one solution.

```python
def string_machine(input_string, iterations):
    """
    Takes input_string and generates a new string with -'s and *'s
    corresponding to characters that have identical adjacent characters
    or not, respectively.  Iterates through this procedure with the resultant
    strings for the supplied number of iterations.
    """
    print(input_string)
    input_string_length = len(input_string)
    old = input_string
    for i in range(iterations):
        new = ''
        # iterate through characters in previous string
        for j in range(input_string_length):
            left = j-1
            right = (j+1) % input_string_length  # ensure right index wraps around
            if old[left] == old[right]:
                new = new + '-'
            else:
                new = new + '*'
        print(new)
        # store new string as old
        old = new     

string_machine('et cetera', 10)
```

```output
et cetera
*****-***
----*-*--
---*---*-
--*-*-*-*
**-------
***-----*
--**---**
*****-***
----*-*--
---*---*-
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Follow standard Python style in your code.
- Use docstrings to provide builtin help.

::::::::::::::::::::::::::::::::::::::::::::::::::


