---
layout: episode
title: "Error Messages"
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
FIXME: multiple prerequisites missing (reorder?)

* Indexing not yet described, (quickly described below for strings)
* File IO not yet described, (quickly described below)
* Multi-level trace backs probably require some knowledge of functions to understand
* Many of the challenges require knowledge of defining functions
* The "Identifying Variable Name Errors" challenge requires knowledge of for loops and conditionals
* The "Identifying Item Errors" challenge requires knowledge of lists

FIXME: does not yet describe tracebacks

FIXME: does not yet describe multi-level tracebacks

FIXME: Overview times should be updated once lesson content more finalized.

### SyntaxError
* This type of error indicates that the python interpreter does not understand the instructions you have given it.
* Syntax Errors are also sometimes refereed to as parsing errors.
* This could be for a number of reasons for example, a missing opening or closing bracket.
* Can you spot the syntax error in the code below?

~~~
print ("hello world"
~~~
{: .source}

* The resulting error message might help you find it

~~~
  File "<ipython-input-6-d1cc229bf815>", line 1
    print ("hello world"
                        ^
SyntaxError: unexpected EOF while parsing
~~~
{: .output}

* This syntax error indicates that there is a problem on first line of the given file ("line 1").
* In this case the "ipython-input" section of the file name tells us that we are working with input into IPython. IPython is an interactive python interpreter used by jupyter notebooks to run python code entered into the notebook cells.
* The "-6-" part of the file name indicates that the error occurred in the 6th cell of our jupyter notebook.
* Next the message contains the problem line of code, indicating with a "^" where the problem is within the line.
* Our error is caused when the Python interpreter reaches the end of the cell before it finds the expected closing bracket, ")".

### IndentationError
* Python uses indentation to group sections of code together and expects changes in indentation to coincide with certain keywords and syntax, which will be discussed more later.
* If the indentation changes in a way that the python interpreter does not expect, an indentation error occurs.
* The follow code will create an indentation error.

~~~
firstName="Jon"
  lastName="Smith"
~~~
{: .source}

~~~
  File "<ipython-input-7-f65f2962bf9c>", line 2
    lastName="Smith"
    ^
IndentationError: unexpected indent
~~~
{: .output}

* The resulting error message again tells us exactly where the error occurs.
* This error can be fixed by removing the extra spaces at the begging of line 2 of our jupyter notebook cell 7.

### NameError
* Name errors occur when a "name" is not found. This could be the name of a variable or function that has not yet been defined.

~~~
print(myName)
myName="Eric"
~~~
{: .source}

~~~
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-10-b0a8aa832076> in <module>()
----> 1 print(myName)
      2 myName="Eric"

NameError: name 'myName' is not defined
~~~
{: .output}

* The Python interpreter reads statements from top to bottom in sequence.
* In the above code the variable `myName` is defined after the print function which prints it.
* When the line `print(myName)` is executed `myName` is not known by the python interpreter and a `NameError` is encountered.

### Accessing a String by Index
FIXME: should string indexing be described before hand? Or is it better here?

* We have seen that string variables can have a length.
* The length of a string is the number of characters making up that string including spaces and other characters you might not see, referred as "white space".
* The individual characters of a string can be accessed using the "[ ]" notation, for example

~~~
myName="Eric"
print(myName[2])
~~~
{: .source}

~~~
i
~~~
{: .output}

* Indexing starts at 0 so that `print(myName[0])` produces "E" and `print(myName[3])` produces "c"
* What happens if the index given for `myName` is not between 0 and 3 inclusive?
* Try

~~~
print(myName[-1])
~~~
{: .source}

~~~
c
~~~
{: .output}

* That worked because you can also index from the back of the string with the last character referenced by '-1', the second last character as '-2' and so on.
* What about an index of 4?

### IndexError
~~~
myName="Eric"
print(myName[4])
~~~
{: .source}

~~~
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-29-5f5b5bde32ce> in <module>()
      1 myName="Eric"
----> 2 print(myName[4])

IndexError: string index out of range
~~~
{: .output}

* An Index error occurs when the given index does not correspond to an element in a sequence.
* In the above example, an index of 4 is past the end of the string and does not correspond to any character in the string.


### Files

#### Writing to a File

FIXME: should File IO be described before hand? Or is it better here?

* Strings can be written to files on your computer.

~~~
outputFile=open("my_name.txt",'w')
outputFile.write(myName)
outputFile.close()
~~~
{: .source}

* The first line above creates a new file "my_name.txt" and opens it for writing ('w').
* The second line writes the variable `myName` to the file
* The third line closes the file. It is a good habit to close files when done working with them.

#### Reading from a File
* This file can then be read in with

~~~
inputFile=open("my_name.txt",'r')
myNameAgain=inputFile.read()
inputFile.close()
print(myNameAgain)
~~~
{: .source}

~~~
Eric
~~~
{: .output}

* This code opens the "my_name.txt" file for reading ('r') and sets the variable `myNameAgain` equal to the content of the file.
* It then closes it and prints out the `myNameAgain` variable.
* What would happen if we tried to open a file for reading which didn't exist?

### FileNotFoundError
* This error occurs when attempting to read from a file which does not already exist

~~~
inputFile=open("no_file.txt",'r')
~~~
{: .source}

* Provided the file "no_file.txt" does not already exist the following error will occur

~~~
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-38-7ddeb8db68ca> in <module>()
----> 1 inputFile=open("no_file.txt",'r')

FileNotFoundError: [Errno 2] No such file or directory: 'no_file.txt'
~~~
{: .output}

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
