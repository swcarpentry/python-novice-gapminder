---
title: "Variables and Assignment"
teaching: 5
exercises: 5
questions:
- "How can I store data in programs?"
objectives:
- "Correctly identify integers, floats, and strings, and explain their intended uses."
- "Write programs that assign scalar values to variables and perform calculations with those values."
- "Correctly trace value changes in programs that use scalar assignment."
keypoints:
- FIXME
---
## Use variables to store values.

*   Variables are names for values.
*   In Python the `=` symbol assigns the value on the right to the name on the left.
*   The variable is created when a value is assigned to it.
*   Here's Python that assigns an age to a variable `age`
    and a name in quotation marks to a variable `first_name`.

~~~
age = 42
first_name = 'Ahmed'
~~~
{: .python}

*   Variable names:
    *   cannot start with a digit
    *   cannot contain spaces, quotation marks, or other punctuation
    *   *may* contain an underscore (typically used to separate words in long variable names)
*   Underscores at the start like `__alistairs_real_age` have a special meaning
    so we won't do that until we understand the convention.

## Use `print` to display values.

*   Python has a built-in function called `print` that prints things as text.
*   Call the function (i.e., tell Python to run it) by using its name.
*   Provide values to the function (e.g., things to print) in parentheses.

~~~
print(first_name, 'is', age, 'years old')
~~~
{: .python}
~~~
Ahmed is 42 years old
~~~
{: .output}

*   `print` automatically puts a single space between items to separate them.
*   And wraps around to a new line at the end.

## Variables persist between cells.

*   Variables defined in one cell exist in all following cells.
*   Notebook cells are just a way to organize a program:
    as far as Python is concerned,
    all of the source code is one long set of instructions.

## Variables must be created before they are used.

*   If a variable doesn't exist yet, or if the name has been mis-spelled,
    Python reports an error.
    *   Unlike some languages, which "guess" a default value.

~~~
print(last_name)
~~~
{: .python}
~~~
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-c1fbb4e96102> in <module>()
----> 1 print(last_name)

NameError: name 'last_name' is not defined
~~~
{: .error}

*   The last line of an error message is usually the most informative.
*   We will look at error messages in detail [later]({{ site.github.url }}/05-error-messages/).

## Python is case-sensitive.

*   Python thinks that upper- and lower-case letters are different,
    so `Name` and `name` are different variables.
*   Again,
    there are conventions around using upper-case letters at the start of variable names
    so we will use lower-case letters for now.

## Use meaningful variable names.

*   Python doesn't care what you call variables as long as they obey the rules
    (alphanumeric characters and the underscore).

~~~
flabadab = 42
ewr_422_yY = 'Ahmed'
print(ewr_422_yY, 'is', flabadab, 'years old')
~~~
{: .python}

*   Use meaningful variable names to help other people understand what the program does.
*   The most important "other person" is your future self.

## Variables can be used in calculations.

*   We can use variables in calculations just as if they were values.

~~~
age = age + 3
print('Age in three years:', age)
~~~
{: .python}
~~~
Age in three years: 45
~~~
{: .output}

## Every value has a type.

*   Every value in a program has a specific type.
*   Integer (`int`): counting numbers like 3 or -512.
*   Floating point number (`float`): fractional numbers like 3.14159 or -2.5.
    *   Integers are used to count, floats are used to measure.
*   Character string (usually just called "string", `str`): text.
    *   Written in either single quotes or double quotes (as long as they match).
    *   The quotation marks aren't printed when the string is displayed.

## Values know their type.

*   Use the built-in function `type` to find out what type a value has.
*   Works on variables as well.
    *   But remember: the *value* has the type --- the *variable* is just a label.

~~~
print(type(52))
~~~
{: .python}
~~~
<class 'int'>
~~~
{: .output}

~~~
fitness = 'average'
print(type(fitness))
~~~
{: .python}
~~~
<class 'str'>
~~~
{: .output}

## Types control what operations can be done on values.

*   A value's type determines what the program can do to it.

~~~
print(5 - 3)
~~~
{: .python}
~~~
2
~~~
{: .output}

~~~
print('hello' - 'h')
~~~
{: .python}
~~~
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-67f5626a1e07> in <module>()
----> 1 print('hello' - 'h')

TypeError: unsupported operand type(s) for -: 'str' and 'str'
~~~
{: .error}

## Strings can be added and multiplied.

*   "Adding" character strings concatenates them.

~~~
full_name = 'Ahmed' + ' ' + 'Walsh'
print(full_name)
~~~
{: .python}
~~~
Ahmed Walsh
~~~
{: .output}

*   Multiplying a character string by an integer replicates it.
    *   Since multiplication is just repeated addition.

~~~
separator = '=' * 10
print(separator)
~~~
{: .python}
~~~
==========
~~~
{: .output}

## Strings have a length (but numbers don't).

*   The built-in function `len` counts the number of characters in a string.

~~~
print(len(full_name))
~~~
{: .python}
~~~
11
~~~
{: .output}

*   But numbers don't have a length (not even zero).

~~~
print(len(52))
~~~
{: .python}
~~~
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-f769e8e8097d> in <module>()
----> 1 print(len(52))

TypeError: object of type 'int' has no len()
~~~
{: .error}

## Sometimes need to convert values explicitly before operating on them.

*   Cannot add numbers and strings.

~~~
print(1 + 'A')
~~~
{: .python}
~~~
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-fe4f54a023c6> in <module>()
----> 1 print(1 + '2')

TypeError: unsupported operand type(s) for +: 'int' and 'str'
~~~
{: .error}

*   Not allowed because it's ambiguous: should `1 + '2'` be `3` or `'12'`?
*   Use the name of a type as a function to convert a value to that type.

~~~
print(1 + int('2'))
print(str(1) + '2')
~~~
{: .python}
~~~
3
12
~~~
{: .output}

## Variables only change value when something is assigned to them.

*   If we make one cell in a spreadsheet depend on another, and update the latter, the former updates automatically.
*   This does *not* happen in programming languages.

~~~
first = 1
second = 5 * first
first = 2
print('first is', first, 'and second is', second)
~~~
{: .python}
~~~
first is 2 and second is 5
~~~
{: .output}

*   The computer reads the value of `first` when doing the multiplication, creates a new value, and assigns it to `second`.
*   After that, `second` does not remember where it came from.

> ## Swapping Values
>
> Draw a table showing the values of the variables in this program
> after each statement is executed.
> In simple terms, what do the last three lines of this program do?
>
> ~~~
> lowest = 1.0
> highest = 3.0
> temp = lowest
> lowest = highest
> highest = temp
> ~~~
> {: .source}
{: .challenge}

> ## Predicting Values
>
> What is the final value of `position` in the program below?
> (Try to predict the value without running the program,
> then check your prediction.)
>
> ~~~
> initial = "left"
> position = initial
> initial = "right"
> ~~~
> {: .source}
{: .challenge}
