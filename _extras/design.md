---
layout: page
title: "Lesson Design"
permalink: /design/
---

> ## Help Wanted
>
> **We are filling in the exercises [below](#stage-3---learning-plan)
> in order to make the lesson plan more concrete.
> Contributions (both in the form of pull requests with filled-in exercises,
> and comments on specific exercises, ordering, and timings) are greatly appreciated.**
{: .callout}

## Process Used

This lesson was developed using a slimmed-down variant of the "Understanding by Design" process.
The main sections are:

1.  Assumptions about audience, time, etc.
    (The current draft also includes some conclusions and decisions in this 
    section - that should be refactored.)

2.  Desired results:
    overall goals, summative assessments at half-day granularity, what learners 
    will be able to do, what learners will know.

3.  Learning plan:
    each episode has a heading that summarizes what will be covered,
    then estimates time that will be spent on teaching and on exercises,
    while the exercises are given as bullet points.

## Stage 1 - Assumptions

*   Audience
    *   Graduate students in numerate disciplines from cosmology to archaeology
    *   Who have manipulated data in spreadsheets and with interactive tools like SAS
    *   But have *not* programmed beyond CPD (copy-paste-despair)
*   Constraints
    *   One full day 09:00-16:30
        *   06:15 class time
        *   0:45 lunch
        *   0:30 total for two coffee breaks
    *   Learners use native installs on their own machines
        *   May use VMs or cloud resources at instructor's discretion
        *   But must keep native local install as an option
    *   No dependence on other Carpentry modules
        *   In particular, does not require knowledge of shell or version control
    *   Use the Jupyter Notebook
        *   Authentic tool used by many instructors
        *   There isn't really an alternative
        *   And means that even people who have seen a bit of Python before
            will probably learn something
*   Motivating Example
    *   Creating 2D plots suitable for inclusion in papers
    *   Appeals to almost everyone
    *   Makes lesson usable by both Carpentries
        *   And means that even people who have seen a bit of Python before 
            will probably learn something
*   Data
    *   Use the gapminder data throughout
    *   But break into multiple files by continent
        *   To make display of output from examples tidier
            (e.g., use Australia/New Zealand, which is only two lines)
        *   And allow examples showing use of multiple data sets
*   Focus on Pandas instead of NumPy
    *   Makes lesson usable by both Data Carpentry and Software Carpentry
    *   Genuine novices are likely to want data analysis
    *   And people with some prior experience:
        *   will accept data analysis as an authentic task,
        *   and are unlikely to have encountered Pandas,
            so they'll still get something useful out of the lesson
*   Exercises will mostly *not* be "write this code from scratch"
    *   Want lots of short exercises that can reliably be finished in allotted time
    *   So use MCQs, fill-in-the-blanks, Parsons Problems, "tweak this code", etc.

## Stage 2 - Desired Results

### Goals

Learners can...

*   ...write short scripts using loops and conditionals.
*   ...write functions with a fixed number of parameters that return a single result.
*   ...import libraries using aliases and refer to those libraries' contents.
*   ...do simple data extraction and formatting using Pandas.

### Summative Assessment

*   Midpoint: create time-series plot for each file in a directory.
*   Final: extract data from Pandas data frame
    and create comparative multi-line time series plot.

### Essential Questions

How do I...

*   ...read tabular data?
*   ...plot a single vector of values?
*   ...create a time series plot?
*   ...create one plot for each of several data sets?
*   ...extra data from a single data set for plotting?
*   ...write programs I can read and re-use in future?

### Learners Will Know...

*   That a program is a piece of lab equipment that implements an analysis
    *   Needs to be validated/calibrated before/during use
    *   Makes analysis reproducible, reviewable, shareable
*   That programs are written for people, not for computers
    *   Meaningful variable names
    *   Modularity for readability as well as re-use
    *   No duplication
    *   Document purpose and use
*   That there is no magic: the programs they use are no different 
    in principle from those they build
*   How to assign values to variables
*   What integers, floats, strings, NumPy arrays, and Pandas data frames are
*   How to trace the execution of a `for` loop
*   How to trace the execution of `if`/`else` statements
*   How to create and index lists
*   How to create and index NumPy arrays
*   How to create and index Pandas data frames
*   How to create time series plots
*   The difference between defining and calling a function
*   Where to find documentation on standard libraries
*   How to find out what else scientific Python offers

## Stage 3 - Learning Plan

### Running and Quitting Interactively (9:00)

#### Teaching: 15 min (because setup issues)

* Launch the Jupyter Notebook, create new notebooks, and exit the Notebook.
* Create Markdown cells in a notebook.
* Create and run Python cells in a notebook.

#### Exercises: 0 min (accounted for in teaching time - no separate exercise)

> ## Creating Lists in Markdown
>
> Create a nested list in a Markdown cell in a notebook that looks like this:
>
> 1.  Get funding.
> 2.  Do work.
>     *   Design experiment.
>     *   Collect data.
>     *   Analyze.
> 3.  Write up.
> 4.  Publish.
{: .challenge}

> ## More Math
>
> What is displayed when a Python cell in a notebook that contains several calculations is executed?
> For example, what happens when this cell is executed?
>
> ~~~
> 7 * 3
> 2 + 1
> ~~~
> {: .source}
{: .challenge}

> ## Change an Existing Cell from Code to Markdown
>
> What happens if you write some Python in a code cell and then you switch it to a Markdown cell?
> For example,
> put the following in a code cell:
>
> ~~~
> x = 6 * 7 + 12
> print(x)
> ~~~
> {: .python}
>
> And then run it with shift+return to be sure that it works as a code cell.
> Now go back to the cell and use escape+M to switch the cell to Markdown
> and "run" it with shift+return.
> What happened and how might this be useful?
{: .challenge}

> ## Mathematics
>
> Standard Markdown (such as we're using for these notes) won't render equations,
> but the Notebook will.
> Create a new Markdown cell
> and enter the following:
>
> ~~~
> $\Sigma_{i=1}^{N} 2^{-i} \approx 1$
> ~~~
> {: .source}
>
> (It's probably easier to copy and paste.)
> What does it display?
> What do you think the underscore `_`, circumflex `^`, and dollar sign `$` do?
{: .challenge}

### Variables and Assignment (9:15)

#### Teaching: 10 min

* Write programs that assign scalar values to variables and perform calculations with those values.
* Correctly trace value changes in programs that use scalar assignment.

~~~
a = 3
print(a)
type(a)
a = a + 60
print(a)
~~~
{: .python}

*   Things can change type and operators can change 'meaning'

~~~
a = 'gdp.csv'
print(a)
type(a)
a = 'data/' + a
print(a)
~~~
{: .python}

*   Indexing a string

~~~
print(a[0])
print(a[-1])
print(a[5:8])
~~~
{: .python}

Q:  If you set `a = 123`, then what happens if you try to get the second digit?
A:  Numbers are not stored in the written representation, so they can't be
    treated like strings.

~~~
a = 123
print(a[1])
~~~
{: .python}

*   Use meaningful names for variables.

~~~
minutes = 3
seconds = 12
seconds = seconds + minutes * 60
print(seconds)
~~~
{: .python}

#### Exercises: 10 min

Q: What kind of thing is 3.4?

A:

~~~
min = 3.25
type(3.25)
~~~
{: .python}

Q: What kind of thing is `3.25 + 4`?

~~~
test = 3.25 + 4
type(test)
type(3.25 + 4)
~~~
{: .python}

Q: Which is a better variable name, `min` or `minutes`?
   Why?
   (Hint: what else might `min` stand for?)

A: `minutes` is better because `min` might mean something like "minimum"
   (and actually does in Python, but we haven't seen that yet).

Q: Which of the following would you rather inherit from someone who is leaving the lab?

   1. `ts = m * 60 + s`
   2. `tot_sec = min * 60 + sec`
   3. `total_seconds = minutes * 60 + seconds`

A: #3.

Q: Trace the behavior of three-step swapping
   by drawing a table to show the values of each variable after each line:

~~~
temp = left
left = right
right = temp
~~~
{: .python}

Q: Create a variable for minutes and set it to 6.35.
   Convert the minutes into seconds and print the result.
   Then print the result *without* storing the number of seconds in a variable.

A:

~~~
minutes = 6.35
seconds = 6.35 * 60
print(seconds)
~~~
{: .python}

~~~
print(6.35 * 60)
~~~
{: .python}

### Data Types and Type Conversion (09:35)

*   Teaching: 10 min

* Explain key differences between integers and floating point numbers.
* Explain key differences between numbers and character strings.
* Use built-in functions to convert between integers, floating point numbers, and strings.

*   Exercises: 10 min

Q: What type of value (integer, floating point number, or character string)
   would you use to represent each of the following?

1. Number of days since the start of the year.
2. Time elapsed since the start of the year.
3. Serial number of a piece of lab equipment.

Q: `float` will convert a string to a floating point number, and `int`
   will convert a floating point number to an integer: Given that,
   what do you expect this program to do?  What does it actually do?
   Why do you think it does that?

`print("fractional string to int:", int("3.4"))`

### Built-in Functions and Help (09:55)

#### Teaching: 10 min

* Explain the purpose of functions.
* Correctly call built-in Python functions.
* Correctly nest calls to built-in functions.
* Use help to display documentation for built-in functions.

#### Exercises: 10 min

Q: explain the order of operations in the second line below:

~~~
radiance = 1.0
radiance = max(2.1, 2.0 + min(radiance, 1.1 * radiance - 0.5))
~~~

Q: Why don't `max` and `min` return `None` when they are given no arguments?

### Error Messages (10:15)

#### Teaching: 5 min

* Read a traceback and determine the file, function, and line number on which the error occurred, the type of error, and the error message.
* Correctly describe situations in which SyntaxError, IndentationError, and NameError occur.

#### Exercise: 10 min

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

### Coffee: 15 min (10:30)

### Libraries (Including Aliases) (10:45)

#### Teaching: 10 min

* Explain what software libraries are and why programmers create and use them.
* Write programs that import and use libraries from Python's standard library.
* Find and read documentation for standard libraries interactively (in the interpreter) and online.

#### Exercises: 10 min

> ## Exploring the Math Library
>
> 1. What function from the `math` library can you use to calculate a square root
>    *without* using `sqrt`?
> 2. Since the library contains this function, why does `sqrt` exist?
{: .challenge}

> ## Importing With Aliases
>
> 1. Fill in the blanks so that the program below prints `90.0`.
> 2. Rewrite the program so that it uses `import` *without* `as`.
> 3. Which form do you find easier to read?
>
> ~~~
> import math as m
> angle = ____.degrees(____.pi / 2)
> print(____)
> ~~~
> {: .source}
{: .challenge}

### Reading Tabular Data (11:05)

#### Teaching: 5 min

* Import the Pandas library.
* Use Pandas to load a simple CSV data set.
* Get some basic information about a Pandas Data frame.

#### Exercises: 10 min

> ## Reading Other Data
>
> Read the data in `gapminder_gdp_americas.csv`
> (which should be in the same directory as `gapminder_gdp_oceania.csv`)
> into a variable called `americas`
> and display its summary statistics.
{: .challenge}

> ## Inspecting Data.
>
> After reading the data for the Americas,
> use `help(americas.head)` and `help(americas.tail)`
> to find out what `DataFrame.head` and `DataFrame.tail` do.
>
> 1.  What method call will display the first three rows of this data?
> 2.  What method call will display the last three columns of this data?
>     (Hint: you may need to change your view of the data.)
{: .challenge}

### Data Frames (11:20)

#### Teaching: 15 min

* Select individual values from a Pandas data frame.
* Select entire rows or entire columns from a data frame.
* Select a subset of both rows and columns from a data frame in a single operation.
* Select a subset of a data frame by a single Boolean criterion.

#### Exercises: 15 min

Q: Write an expression to find the Per Capita GDP of Serbia in 2007.

Do the two statements below produce the same output?
Based on this,
what rule governs what is included (or not) in numerical slices and named slices in Pandas?

~~~
print(data.ix[0:2, 0:2])
print(data.ix['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])
~~~
{: .python}

> ## Practice with Selection
>
> Assume Pandas has been imported and the Gapminder GDP data for Europe has been loaded.
> Write an expression to select each of the following:
>
> 1.  GDP per capita for all countries in 1982.
> 2.  GDP per capita for Denmark for all years.
> 3.  GDP per capita for all countries for years *after* 1985.
> 4.  GDP per capita for each country in 2007 as a multiple of 
>     GDP per capita for that country in 1952.
{: .challenge}

### Plotting (11:50)

#### Teaching: 10 min

- "Create a time series plot showing a single data set."
- "Create a scatter plot showing relationship between two data sets."

#### Exercise: 15 min

> ## Minima and Maxima
>
> Fill in the blanks below to plot the minimum GDP per capita over time
> for all the countries in Europe.
> Modify it again to plot the maximum GDP per capita over time for Europe.
>
> ~~~
> data_europe = pandas.read_csv('data/gapminder_gdp_europe.csv')
> data_europe.____.plot(label='min')
> data_europe.____
> plt.legend(loc='best')
> ~~~
> {: .python}
{: .challenge}

### Lunch (12:15): 45 min

### Lists and Indexing (13:00)

#### Teaching: 10 min

* Explain why programs need collections of values.
* Write programs that create flat lists, index them, slice them, and modify them through assignment and method calls.

~~~
continents = ['Africa', 'Europe']
print(continents)
primes = [1, 2, 3, 7, 11]
print(primes)
~~~
{: .python}

*   Use the built-in function `len` to find out how long the list is.

~~~
len(primes)
~~~
{: .python}

*   Use an index to specify a single value in a list.
*   List indexes start at 0, so `list[1]` is actually the *second* value in the list.

~~~
print(continents[1])
~~~
{: .python}

*   The type of the list is `list`, but the types of the values may vary.

~~~
mixed = [1, "is not prime"]
type(mixed)
type(mixed[0])
type(mixed[1])
~~~
{: .python}

*   Cannot ask for values that do not exist.
    *   Unlike some languages, Python doesn't fill in a default.

~~~
print(continents[2])
~~~
{: .python}

*   Negative indexes count backward from the end of the list.

~~~
print(primes[-1])
~~~
{: .python}

*   Can change values in a list by assigning to them (just like regular variables).

~~~
americas = ['South', 'Norht'] # oops, typo
americas[1] = 'North'
print(americas)
~~~
{: .python}

*   The empty list contains no values.
    *   Like zero for numbers or the empty string for text.

~~~
empty = []
type(empty)
print(empty)
~~~
{: .python}

*   Can enlarge a list by appending values to it.

~~~
continents.append('Oceania')
print(continents)
~~~
{: .python}

*   Use the `glob` library to get a list of filenames matching a pattern.

~~~
import glob

files = glob.glob('*.txt')
print(files)
type(files)
~~~
{: .python}

#### Exercises: 10 min

> ## Slicing
>
> What does the following program print?
>
> ~~~
> element = 'carbon'
> print('element[1:3] is:', element[1:3])
> ~~~
> {: .python}
> ~~~
> element[1:3] is: ar
> ~~~
> {: .output}
>
> 1.  What does `thing[low:high]` do?
> 2.  What does `thing[low:]` (without a value after the colon) do?
> 3.  What does `thing[:high]` (without a value before the colon) do?
> 4.  What does `thing[:]` (just a colon) do?
{: .challenge}

> ## Fill in the Blanks
>
> Fill in the blanks so that the program below produces the output shown.
>
> ~~~
> values = ____
> values.____(1)
> values.____(3)
> values.____(5)
> print('first time:', values)
> values = values[____]
> print('second time:', values)
> ~~~
> {: .python}
>
> ~~~
> first time: [1, 3, 5]
> second time: [3, 5]
> ~~~
> {: .output}
{: .challenge}

> ## How Large is a Slice?
>
> If 'low' and 'high' are both non-negative integers,
> how long is the list `values[low:high]`?
{: .challenge}

Q: What does program A print?
   What does program B print?
   In simple terms, explain the difference between `sorted(letters)` and `letters.sort()`.

<div class="row">
  <div class="col-md-6" markdown="1">
~~~
# Program A
letters = list('gold')
result = sorted(letters)
print('letters is', letters, 'and result is', result)
~~~
{: .python}
  </div>
  <div class="col-md-6" markdown="1">
~~~
# Program B
letters = list('gold')
result = letters.sort()
print('letters is', letters, 'and result is', result)
~~~
{: .python}
  </div>
</div>

Q: What does program A print?
   What does program B print?
   In simple terms, explain the difference between `new = old` and `new = old[:]`.

<div class="row">
  <div class="col-md-6" markdown="1">
~~~
# Program A
old = list('gold')
new = old      # simple assignment
new[0] = 'D'
print('new is', new, 'and old is', old)
~~~
{: .python}
  </div>
  <div class="col-md-6" markdown="1">
~~~
# Program B
old = list('gold')
new = old[:]   # assigning a slice
new[0] = 'D'
print('new is', new, 'and old is', old)
~~~
{: .python}
  </div>
</div>

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

### Loops (13:20)

#### Teaching: 10 min

* Explain what for loops are normally used for.
* Trace the execution of a simple (unnested) loop and correctly state the values of variables in each iteration.
* Write for loops that use the Accumulator pattern to aggregate values.

#### Exercises: 15 min

> ## Tracing Execution
>
> Create a table showing the numbers of the lines that are executed when this program runs,
> and the values of the variables after each line is executed.
>
> ~~~
> total = 0
> for char in "tin":
>     total = total + 1
> ~~~
> {: .python}
{: .challenge}

> ## Reversing a String
>
> Fill in the blanks in the program below so that it prints "nit"
> (the reverse of the original character string "tin").
>
> ~~~
> original = "tin"
> result = ____
> for char in original:
>     result = ____
> print(result)
> ~~~
> {: .python}
{: .challenge}

> ## Practice Accumulating
>
> Fill in the blanks in each of the programs below
> to produce the indicated result.
>
> ~~~
> # Total length of the strings in the list: ["red", "green", "blue"] => 12
> total = 0
> for word in ["red", "green", "blue"]:
>     ____ = ____ + len(word)
> print(total)
> ~~~
> {: .python}
>
> ~~~
> # List of word lengths: ["red", "green", "blue"] => [3, 5, 4]
> lengths = ____
> for word in ["red", "green", "blue"]:
>     lengths = lengths.____(____)
> print(lengths)
> ~~~
> {: .python}
>
> ~~~
> # Concatenate all words: ["red", "green", "blue"] => "redgreenblue"
> words = ["red", "green", "blue"]
> result = ____
> for ____ in ____:
>     ____
> print(result)
> ~~~~
> {: .python}
>
> ~~~
> # Create acronym: ["red", "green", "blue"] => "RGB"
> # write the whole thing
> ~~~
> {: .python}
{: .challenge}

> ## Cumulative Sum
>
> Reorder and properly indent the lines of code below
> so that they print an array with the cumulative sum of data.
> The result should be `[1, 3, 5, 10]`.
>
> ~~~
> cumulative += [sum]
> for number in data:
> cumulative = []
> sum += number
> print(cumulative)
> data = [1,2,2,5]
> ~~~
> {: .python}
{: .challenge}

> ## Indentation Errors
>
> What kind of error does Python report
> when we try to run the following program?
>
> ~~~
> for char in 'helium':
> print char
> ~~~
> {: .python}
>
> Is this a syntax error or a runtime error?
{: .challenge}

### Looping Over Data Sets (13:45)

#### Teaching: 5 min

* Be able to read and write globbing expressions that match sets of files.
* Use glob to create lists of files.
* Write for loops to perform operations on files given their names in a list.

#### Exercise: 10 min

> ## Determining Matches
>
> Which of these files is *not* matched by the expression `glob.glob('data/*as*.csv')`?
>
> 1. `data/gapminder_gdp_africa.csv`
> 2. `data/gapminder_gdp_americas.csv`
> 3. `data/gapminder_gdp_asia.csv`
> 4. 1 and 2 are not matched.
{: .challenge}

> ## Maximum File Size
>
> Modify this program so that it prints the number of records in
> the file that has the fewest records.
>
> ~~~
> fewest = ____
> for filename in glob.glob('data/*.csv'):
>     fewest = ____
> print('smallest file has', fewest, 'records')
> ~~~
> {: .source}
{: .challenge}

> ## Comparing Data
>
> Write a short program that reads in the regional data sets
> and plots the average GDP per capita for each region over time
> in a single chart.
{: .challenge}

### Writing Functions (14:00)

#### Teaching: 10 min

* Explain and identify the difference between function definition and function call.
* Write a function that takes a small, fixed number of arguments and produces a single result.

#### Exercises: 15 min

> ## Encapsulation
>
> Fill in the blanks to create a function that takes a single filename as an argument,
> loads the data in the file named by the argument,
> and returns the minimum value in that data.
>
> ~~~
> import pandas
>
> def min_in_data(____):
>     data = ____
>     return ____
> ~~~
> {: .source}
{: .challenge}

> ## Find the First
>
> Fill in the blanks to create a function that takes a list of numbers as an argument
> and returns the first negative value in the list.
> What does your function do if the list is empty?
>
> ~~~
> def first_negative(values):
>     for v in ____:
>         if ____:
>             return ____
> ~~~
> {: .python}
{: .challenge}

### Variable Scope (14:25)

#### Teaching: 10 min

* Identify local and global variables.
* Identify parameters as local variables.

#### Exercises: 10 min

> ## Local and Global Variable Use
>
> Trace the values of all variables in this program as it is executed.
> (Use '---' as the value of variables before and after they exist.)
>
> ~~~
> limit = 100
>
> def clip(value):
>     return min(max(0.0, value), limit)
>
> value = -22.5
> print(clip(value))
> ~~~
> {: .source}
{: .challenge}

### Coffee (14:45): 15 min

### Conditionals (15:00)

#### Teaching: 10 min

* Correctly write programs that use if and else statements and simple Boolean expressions (without logical operators).
* Trace the execution of unnested conditionals and conditionals inside loops.

#### Exercises: 15 min

> ## Tracing Execution
>
> What does this program print?
>
> ~~~
> pressure = 71.9
> if pressure 50.0:
>     pressure = 25.0
> elif pressure <= 50.0:
>     pressure = 0.0
> print(pressure)
> ~~~
> {: .source}
{: .challenge}

> ## Processing Small Files
>
> Modify this program so that it only processes files with fewer than 50 records.
>
> ~~~
> import glob
> import pandas
> for filename in glob.glob('data/*.csv'):
>     contents = pandas.read_csv(filename)
>     ____:
>         print(filename, len(contents))
> ~~~
> {: .source}
{: .challenge}

### Programming Style (15:25)

#### Teaching: 15 min

* How can I make my programs more readable?
* How do most programmers format their code?
* How can programs check their own operation?

#### Exercises: 15 min

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

### Wrap-Up (15:55)

#### Teaching: 20 min

- "What have we learned?"
- "What else is out there and where do I find it?"

#### Exercises: 0 min

### Feedback (16:15)

#### Teaching: 00 min

#### Exercises: 15 min

### Finish (16:30)
