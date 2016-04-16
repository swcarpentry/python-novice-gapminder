---
layout: episode
title: Error Messages
teaching: 5
exercises: 10
questions:
- "What kind of errors can occur in programs?"
- "How can I identify errors when they occur?"
objectives:
- "Read a traceback and determine the file, function, and line number on which the error occurred, the type of error, and the error message."
- "Correctly describe situations in which SyntaxError, IndentationError, NameError, IndexError, and FileNotFoundError occur."
keypoints:
- FIXME
---
FIXME: lesson content.

> ## Reading Error Messages
> 
> Read the traceback below, and identify the following:
> 
> 1. How many levels does the traceback have?
> 2. What is the file name where the error occurred?
> 3. What is the function name where the error occurred?
> 4. On which line number in this function did the error occurr?
> 5. What is the type of error?
> 6. What is the error message?
> 
> ~~~
> ---------------------------------------------------------------------------
> KeyError                                  Traceback (most recent call last)
> <ipython-input-2-e4c4cbafeeb5> in <module>()
>       1 import errors_02
> ----> 2 errors_02.print_friday_message()
> 
> /Users/ghopper/thesis/code/errors_02.py in print_friday_message()
>      13
>      14 def print_friday_message():
> ---> 15     print_message("Friday")
> 
> /Users/ghopper/thesis/code/errors_02.py in print_message(day)
>       9         "sunday": "Aw, the weekend is almost over."
>      10     }
> ---> 11     print(messages[day])
>      12
>      13
> 
> KeyError: 'Friday'
> ~~~
> {: .error}
{: .challenge}

> ## Identifying Syntax Errors
> 
> 1. Read the code below and try to identify what the errors are
>    *without* running it.
> 2. Run the code and read the error message.
>    Is it a `SyntaxError` or an `IndentationError`?
> 3. Fix the error.
> 4. Repeat steps 2 and 3 until you have fixed all the errors.
> 
> ~~~
> def another_function
>   print("Syntax errors are annoying.")
>    print("But at least python tells us about them!")
>   print("So they are usually not too hard to fix.")
> ~~~
> {: .source}
{: .challenge}

> ## Identifying Variable Name Errors
> 
> 1. Read the code below and try to identify what the errors are
>    *without* running it.
> 2. Run the code and read the error message.
>    What type of `NameError` do you think this is?
>    Is it a string with no quotes, a misspelled variable, or a variable that should have been defined but was not?
> 3. Fix the error.
> 4. Repeat steps 2 and 3, until you have fixed all the errors.
> 
> ~~~
> for number in range(10):
>     # use a if the number is a multiple of 3, otherwise use b
>     if (Number % 3) == 0:
>         message = message + a
>     else:
>         message = message + "b"
> print(message)
> ~~~
> {: .source}
{: .challenge}

> ## Identifying Item Errors
> 
> 1. Read the code below and try to identify what the errors are
>    *without* running it.
> 2. Run the code, and read the error message. What type of error is it?
> 3. Fix the error.
> 
> ~~~
> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
> print('My favorite season is ', seasons[4])
> ~~~
> {: .source}
{: .challenge}
