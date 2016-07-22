---
title: "Defensive Programming"
teaching: 10
exercises: 15
questions:
- "What sorts of things frequently go wrong in programs?"
- "How can I make my programs more robust?"
objectives:
- "Diagnose corner cases in simple programs."
- "Write assertions with informative messages that test for corner cases in simple programs."
keypoints:
- FIXME
---
## Fail early, fail loudly.

*   "All programs are wrong, but some programs are useful."
*   Python reports syntax errors when it reads the source code.
*   Can report runtime errors for things that can't possibly be right.
    *   Division by zero, index out of bounds.
*   But it cannot know how your data should be handled.
*   Want to detect and report the problem:
    *   As soon as it occurs (so that you don't have to trace back through hundreds of lines).
    *   Loudly and clearly: a *silent error* is worse than one you know about.

## Can use `if`, `print`, and `sys.exit` to detect and report errors.

~~~
import sys

def average(values):
    if len(values) == 0:
        print('Error in average: no values supplied')
        sys.exit(1)

    return sum(values) / len(values)
~~~
{: .python}

*   But it doesn't give the caller a chance to handle the error in a different way.
*   And doesn't integrate with graphical user interfaces, web programs,
    and other things that might not want you to print.
*   And gets in the way of reading the "happy path" through the code.

## Use `assert` to check internal correctness.

*   The `assert` statement checks whether a condition is true.
    *   "This must be true here or something has gone wrong."
*   Like `if`, but signals an error instead of controlling a block of code.
*   By default, Python stops the program and displays the error,
    along with a *traceback* of the call stack
    to help you figure out what went wrong.

~~~
import sys

def average(values):
    assert len(values) > 0, 'No values supplied'
    return sum(values) / len(values)
~~~
{: .python}

*   Easier to read.
*   A standard way to do things
    (much better than a dozen libraries each reporting errors in different ways).
*   Sometimes called "runnable documentation".
    *   Python checks while the program executes.
    *   Human readers can see what you expect of your program.

## Practice defensive programming.

*   When fixing bug,
    add assertions to make sure they don't reoccur.

~~~
def kelvin_to_celsius(k):
    assert k >= 0.0, 'Temperature in Kelvin cannot be negative'
    return FIXME
~~~
{: .python}

*   Add assertions when writing code in the first place
    to check for errors you have made or seen in the past.

## Practice test-driven development.

*   Write assertions *before* writing functions
    to help you figure out what those functions should do.
*   Encourages you to:
    *   Think about how the function is supposed to behave.
    *   See how usable the function will be before it's written.
*   The assertions are a "contract".
    *   Specify what the function does without specifying how.
    *   A good way to communicate with other programmers when developing software together.

~~~
assert count_leading_zeros([]) == 0
assert count_leading_zeros([0]) == 1
assert count_leading_zeros([0, 1]) == 1
assert count_leading_zeros([0, 1, 0]) == 1
assert count_leading_zeros([0, 0, 1]) == 2
assert count_leading_zeros([1, 0]) == 0
~~~
{: .python}

> ## Is This Needed?
>
> The `os` library contains a function called `os.path.exists(path)`
> that returns `True` if the file or directory identified by `path` exists,
> and `False` if it does not.
> A colleague of yours routinely uses it to check whether a file exists
> before trying to open it:
>
> ~~~
> ...
> assert os.path.exists(filename), 'File {0} not found'.format(filename)
> reader = open(filename, 'r')
> ...
> ~~~
> {: .source}
>
> Should you adopt this practice?
> Why or why not?
{: .challenge}

> ## Finding Corner Cases
>
> 1. Under what circumstances will the following function fail with an error?
> 2. Under what circumstances will it return something other than what the user would expect?
>
> ~~~
> def find_two_smallest(values):
>     "Find the two smallest values in a list."
>
>     copy = values[:]
>     copy.sort()
>     return copy[:2]
> ~~~
> {: .source}
{: .challenge}

> ## Test-Driven Development.
>
> 1. Explain in simple language what `run_starts` function is supposed to do.
> 2. Fill in the blanks in the function definition so that all of the assertions succeed.
> 3. For what input(s) could different users reasonably expect this function to return different values?
>    I.e., where could reasonable people still disagree about the function's behavior?
> 4. Add one or more assertions to test for each situation identified above.
>
> ~~~
> def run_starts(values):
>
>     if values == []:
>         ____
>
>     result = []
>     previous = values[0] + 1
>     for v in values:
>         if v < previous:
>             ____
>             previous = ____
>
>     return result
>
> assert run_starts([]) == []
> assert run_starts([1]) == [1]
> assert run_starts([1, 2]) == [1]
> assert run_starts([1, 2, 1]) == [1, 1]
> assert run_starts([1, 2, 3, 2, 3]) == [1, 2]
> assert run_starts([2, 3, 4, 0, 5, 7, 4, 6]) == [2, 0, 4]
> ~~~
> {: .source}
{: .challenge}
