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

This lesson is meant to be used in both [Data Carpentry][dc-website] and [Software Carpentry][swc-website] workshops.
It's also meant to serve as a worked example in [instructor training][instructor-training] of how to develop a new lesson.
To that end,
the outline below was developed using a slimmed-down variant of the "Understanding by Design" process.
The main sections are:

1.  Assumptions about audience, time, etc.
    (The current draft also includes some conclusions and decisions in this section - that should be refactored.)

2.  Desired results:
    overall goals, summative assessments at half-day granularity, what learners will be able to do, what learners will know.

3.  Learning plan:
    each episode has a heading that summarizes what will be covered,
    then estimates time that will be spent on teaching and on exercises,
    while the exercises are given as bullet points.

## Stage 1 - Assumptions

*   Audience
    *   Graduate students in numerate disciplines from cosmology to archaeology
    *   Who understand very basic statistics (mean, standard deviation, correlation coefficient)
    *   And have manipulated data in spreadsheets and with interactive tools like SAS
    *   But have *not* programmed beyond CPD (copy-paste-despair)
*   Constraints
    *   One full day 09:00-17:00
        *   06:30 teaching time
        *   1:00 for lunch
        *   0:30 total for two coffee breaks
    *   Learners use native installs on their own machines
        *   May use VMs or cloud resources at instructor's discretion
        *   But must keep native local install as an option
    *   No dependence on other Carpentry modules
        *   In particular, does not require knowledge of shell or version control
    *   Use the Jupyter Notebook
        *   Authentic tool used by many instructors
        *   There isn't really an alternative
        *   And means that even people who have seen a bit of Python before will probably learn something
*   Motivating Example
    *   Creating 2D plots suitable for inclusion in papers
    *   Appeals to almost everyone
    *   Makes lesson usable by both Carpentries
*   Data
    *   Use the gapminder data throughout
    *   But break into multiple files by continent
        *   To make display of output from examples tidier
            (use Australia/New Zealand, which is only two lines)
        *   And allow examples showing use of multiple data sets
*   Focus on Pandas instead of NumPy
    *   Genuine novices are likely to want data analysis
    *   And people with some prior experience:
        *   will accept data analysis as an authentic task
        *   And are unlikely to have encountered Pandas,
            so they'll still get something useful out of the lesson
*   Exercises will mostly *not* be "write this code from scratch"
    *   Want lots of short exercises that can reliably be finished in allotted time
    *   So use MCQs, fill-in-the-blanks, Parsons Problems, "tweak this code", etc.
*   Lesson materials
    *   Notes for instructors and self-study will be written in Markdown
        *   We've tried writing/maintaining lessons as Notebooks...
    *   Learners will be provided with one Notebook per episode containing exercises

## Stage 2 - Desired Results

### Goals

Learners can...

*   ...write short scripts using loops and conditionals.
*   ...write functions with a fixed number of parameters that return a single result
    by extracting and encapsulating code from longer scripts.
*   ...import libraries using aliases and refer to those libraries' contents.
*   ...do simple data extraction and formatting using NumPy and Pandas.
*   ...read tabular data and plot it.

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
*   That there is no magic: the programs they use are no different in principle from those they build
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

<<<<<<< HEAD
### Running and Quitting Interactively (9:00)

*   Teaching: 15 min (because setup issues)
*   Exercises: 0 min (accounted for in teaching time - no separate exercise)
    *   Run the Notebook
    *   Create a few Markdown cells
    *   Create and execute a Python cell that prints 1+2

### Variables and Assignment (9:15)

#### Teaching: 10 min

*   Basic assignment of a value.
*   What kind of thing is it?
*   Can assign results of computation and use a variable on the right to assign to the left.

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

*   Use meaningful names for variables.  For example, time

~~~
minutes = 3
seconds = 12
seconds = seconds + minutes*60
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

### NumPy Arrays (9:35)

*   Teaching: 15 min
*   Exercises: 10 min
    *   Read CSV data into array
    *   Calculate statistics on rows and columns

### Plotting Vectors (10:00)

*   Teaching: 10 min
*   Exercise: 10 min
    *   Load single-column CSV and create plot

### Plotting Time Series (10:20)

*   Teaching: 10 min
*   Exercise: 10 min
    *   Read and plot two-column data set (year and value)

### Coffee: 15 min (10:40)

### Lists (10:55)

#### Teaching: 15 min

*   A list is a collection of values.
*   Can be strings, numbers, or a mix.
*   Written inside `[]` with values separated by `,`.

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

Q: Given what we saw earlier about indexing NumPy arrays,
   what do you expect these two expressions do?

1.  `continents[:2]`
2.  `continents[1:]`

Q: How would you get a list of all CSV files in the `data` directory?
   What would your answer produce if the `data` directory was empty?

A:

1.  `glob.glob('data/*.csv')`
2.  An empty list.

Q: Write a single expression to produce the number of CSV files in the `data` directory.

A: `len(glob.glob('data/*.csv'))`

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

### Loops (11:20)

*   Teaching: 15 min
*   Exercises: 15 min
    *   Filter a list of files (a simple alternative to `glob`)

### Combining Ideas (11:50)

*   Teaching: 5 min
*   Exercise: 15 min
    *   Produce one plot for each data file in a directory

### Lunch: 60 min (12:10)

### Writing Functions (13:10)

*   Teaching: 20 min
*   Exercises: 20 min
    *   Extract and encapsulate "plot this file"

### Conditionals (13:50)

*   Teaching: 10 min
*   Exercises: 15 min
    *   Plot average if more than N records

### Coffee: 15 min (14:15)

### Programming Style (14:30)

*   Teaching: 10 min
*   Exercises: 10 min
    *   Add docstrings to functions written earlier

### Data Frames (14:50)

*   Teaching: 15 min
*   Exercises: 15 min
    *   Read more complex data set and calculate statistics

### Plotting Data Frames (15:20)

*   Teaching: 15 min
*   Exercises: 15 min
    *   Plot time series data from complex data set

### Wrapping Up: 10 min (15:50)

### Finish (16:00)
=======
The original step-by-step learning plan is included below.
It has been superseded by the content of the actual episodes,
but is included for reference.

*   Running and Quitting Interactively (09:00)
    *   Teaching: 15 min (because setup issues)
    *   Exercises: 0 min (accounted for in teaching time - no separate exercise)
        *   Run the Notebook
        *   Create a few Markdown cells
        *   Create and execute a Python cell that prints 1+2
*   Variables and Assignment (09:15)
    *   Teaching: 10 min
    *   Exercises: 10 min
        *   Trace behavior of swapping (`a, b = b, a` the old fashioned way) with an intermediate variable
        *   Calculate elapsed time in seconds using named values for seconds per minute, etc.
*   Data Types and Type Conversion (09:35)
    *   Teaching: 10 min
    *   Exercises: 10 min
        *   Predict result types (or errors) of various operations
        *   Add conversion functions to broken code to make it work
*   Built-in Functions (and Methods) and Help (09:55)
    *   Teaching: 10 min
    *   Exercises: 10 min
        *   Chain calculations with max and min
        *   Find a useful method using help(str)
        *   Parsons Problem to achieve specific results with string methods
*   Error Messages (10:15)
    *   Teaching: 10 min (review of error messages seen to date)
    *   Exercises: 10 min
        *   Diagnose and fix small errors (some syntax, some runtime)
*   Coffee: 15 min (10:35)
*   Libraries (Including Aliases) (10:50)
    *   Teaching: 10 min
    *   Exercises: 10 min
        *   Operations with math library
        *   Look things up in the python.org docs
*   Pandas Data Frames (11:10)
    *   Teaching: 10 min
    *   Exercises: 10 min
        *   Import Pandas
        *   Create and display a data frame
*   Reading Tabular Data (11:30)
    *   Teaching: 5 min
    *   Exercises: 5 min
        *   Read one continent's subset of gapminder CSV data
    *   Callout:
        *   How to read data from Excel spreadsheets via export to CSV
        *   How tor ead data from Excel spreadsheets directly (needs another library)
*   Collective Operations (11:40)
    *   Teaching: 10 min
    *   Exercises: 10 min
        *   Select various subsets of data
        *   Normalize values (scale to 0..1)
*   Lunch: 60 min (12:00)
*   Plotting (13:00)
    *   Teaching: 10 min (to show a variety of plots and debug display problems)
    *   Exercises: 10 min
        *   Plot normalized change in GDP over time (tweaking provided code)
*   For Loops (13:20)
    *   Teaching: 15 min (do *not* introduce lists)
    *   Exercises: 10 min
        *   Reverse a string by repeated append
        *   Trace execution of loop
*   Looping Over Data Sets (13:55)
    *   Teaching: 10 min (use glob to get filenames)
    *   Exercises: 15 min
        *   Count rows of each data set
        *   Check number of columns in each data set is the same
*   Lists (14:20)
    *   Teaching: 10 min
    *   Exercises: 10 min
        *   Indexing exercises
        *   Conversion from list to string and back
        *   Sum values in a list
*   Coffee: 15 min (14:40)
*   Conditionals (15:05)
    *   Teaching: 10 min (inside loop)
    *   Exercises: 15 min
        *   Count vowels
        *   Report badly-sized files inside loop
*   Writing Functions (15:30)
    *   Teaching: 15 min
    *   Exercises: 15 min
        *   Check size of a single data file
        *   Check sizes of all data files in a directory
            *   Write new function using previous function
*   Documentation (16:00)
    *   Teaching: 5 min
    *   Exercises: 10 min
        *   Add docstrings to functions written earlier
*   Programming Style (16:15)
    *   Teaching: 10 min (mostly to introduce checklist)
    *   Exercises: 15 min
        *   Clean up badly-written 20-line program
*   Debugging (16:40)
    *   Teaching: 10 min (divide and conquer)
    *   Exercises: 15 min
        *   Debug three-function program
*   Defensive Programming (17:05)
    *   Teaching: 5 min
    *   Exercises: 10 min
        *   Add assertions to functions based on docstrings
*   Programming with Arrays (17:20)
    *   Teaching: 10 min
    *   Exercises: 10 min
        *   More complicated array indexing
*   Wrap-Up (17:40)
    *   Teaching: 15 min
        *   Overview of key SciPy modules
        *   How to find and install libraries
        *   Running Python from the command line
        *   Other editing tools
    *   Exercises: 0 min
*   Finish (17:55)

[dc-website]: http://datacarpentry.org
[gapminder-data]: http://www.gapminder.org/data/
[good-enough]: https://github.com/swcarpentry/good-enough-practices-in-scientific-computing
[instructor-training]: https://swcarpentry.github.io/instructor-training/
[swc-website]: http://software-carpentry.org
>>>>>>> fb9ab5532d112674b1d202a7923c62703f968e17
