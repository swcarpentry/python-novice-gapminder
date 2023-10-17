---
title: Lesson Design
---

:::::::::::::::::::::::::::::::::::::::::  callout

## Help Wanted

**We are filling in the exercises [below](#stage-3-learning-plan)
in order to make the lesson plan more concrete.
Contributions (both in the form of pull requests with filled-in exercises,
and comments on specific exercises, ordering, and timings) are greatly appreciated.**


::::::::::::::::::::::::::::::::::::::::::::::::::

## Process Used

> Michael Pollan's advice if he taught R or Python programming:
> 
> 1. Write code.
> 2. Not too much.
> 3. Mostly plots.
> 
> — [Michael Koontz](https://twitter.com/_mikoontz/status/758021742078025728)
> {: .quotation}

This lesson was developed using a slimmed-down variant of the "Understanding by Design" process.
The main sections are:

1. Assumptions about audience, time, etc.
  (The current draft also includes some conclusions and decisions in this
  section - that should be refactored.)

2. Desired results:
  overall goals, summative assessments at half-day granularity, what learners
  will be able to do, what learners will know.

3. Learning plan:
  each episode has a heading that summarizes what will be covered,
  then estimates time that will be spent on teaching and on exercises,
  while the exercises are given as bullet points.

## Stage 1: Assumptions

- Audience
  - Graduate students in numerate disciplines from cosmology to archaeology
  - Who have manipulated data in spreadsheets and with interactive tools like SAS
  - But have *not* programmed beyond CPD (copy-paste-despair)
- Constraints
  - One full day 09:00-16:30
    - 06:15 class time
    - 0:45 lunch
    - 0:30 total for two coffee breaks
  - Learners use native installs on their own machines
    - May use VMs or cloud resources at instructor's discretion
    - But must keep native local install as an option
  - No dependence on other Carpentry modules
    - In particular, does not require knowledge of shell or version control
  - Use the Jupyter Notebook
    - Authentic tool used by many instructors
    - There isn't really an alternative
    - And means that even people who have seen a bit of Python before
      will probably learn something
- Motivating Example
  - Creating 2D plots suitable for inclusion in papers
  - Appeals to almost everyone
  - Makes lesson usable by both Carpentries
    - And means that even people who have seen a bit of Python before
      will probably learn something
- Data
  - Use the gapminder data throughout
  - But break into multiple files by continent
    - To make display of output from examples tidier
      (e.g., use Australia/New Zealand, which is only two lines)
    - And allow examples showing use of multiple data sets
- Focus on Pandas instead of NumPy
  - Makes lesson usable by both Data Carpentry and Software Carpentry
  - Genuine novices are likely to want data analysis
  - And people with some prior experience:
    - will accept data analysis as an authentic task,
    - and are unlikely to have encountered Pandas,
      so they'll still get something useful out of the lesson
- Challenges will mostly *not* be "write this code from scratch"
  - Want lots of short exercises that can reliably be finished in allotted time
  - So use MCQs, fill-in-the-blanks, Parsons Problems, "tweak this code", etc.

## Stage 2: Desired Results

### Questions

How do I...

- ...read tabular data?
- ...plot a single vector of values?
- ...create a time series plot?
- ...create one plot for each of several data sets?
- ...get extra data from a single data set for plotting?
- ...write programs I can read and re-use in future?

### Skills

I can...

- ...write short scripts using loops and conditionals.
- ...write functions with a fixed number of parameters that return a single result.
- ...import libraries using aliases and refer to those libraries' contents.
- ...do simple data extraction and formatting using Pandas.

### Concepts

I know...

- ...that a program is a piece of lab equipment that implements an analysis
  - Needs to be validated/calibrated before/during use
  - Makes analysis reproducible, reviewable, shareable
- ...that programs are written for people, not for computers
  - Meaningful variable names
  - Modularity for readability as well as re-use
  - No duplication
  - Document purpose and use
- ...that there is no magic: the programs they use are no different
  in principle from those they build
- ...how to assign values to variables
- ...what integers, floats, strings, NumPy arrays, and Pandas dataframes are
- ...how to trace the execution of a `for` loop
- ...how to trace the execution of `if`/`else` statements
- ...how to create and index lists
- ...how to create and index NumPy arrays
- ...how to create and index Pandas dataframes
- ...how to create time series plots
- ...the difference between defining and calling a function
- ...where to find documentation on standard libraries
- ...how to find out what else scientific Python offers

## Stage 3: Learning Plan

### Summative Assessment

- Midpoint: create time-series plot for each file in a directory.
- Final: extract data from Pandas dataframe
  and create comparative multi-line time series plot.

### [Running and Quitting Interactively](../episodes/01-run-quit.md) (9:00)

- Teaching: 15 min (because setup issues)
  - Launch the Jupyter Notebook, create new notebooks, and exit the Notebook.
  - Create Markdown cells in a notebook.
  - Create and run Python cells in a notebook.
- Challenges: 0 min (accounted for in teaching time - no separate exercise)
  - Creating lists in Markdown
  - What is displayed when several expressions are put in a single cell?
  - Change an existing cell from code to Markdown
  - Rendering LaTeX-style equations

### [Variables and Assignment](../episodes/02-variables.md) (9:15)

- Teaching: 10 min
  - Write programs that assign scalar values to variables and perform calculations with those values.
  - Correctly trace value changes in programs that use scalar assignment.
- Challenges: 10 min
  - Trace execution of code swapping two values using an intermediate variable.
  - Predict final values of variables after several assignments.
  - What happens if you try to index a number?
  - Which is a better variable name, `m`, `min`, or `minutes`?
  - What do the following slice expressions produce?

### [Data Types and Type Conversion](../episodes/03-types-conversion.md) (09:35)

- Teaching: 10 min
  - Explain key differences between integers and floating point numbers.
  - Explain key differences between numbers and character strings.
  - Use built-in functions to convert between integers, floating point numbers, and strings.
- Challenges: 10 min
  - What type of value is 3.4?
  - What type of value is 3.25 + 4?
  - What type of value would you use to represent:
    - Number of days since the start of the year.
    - Time elapsed since the start of the year.
    - Etc.
  - How can you use `//` (integer division) and `%` (modulo)?
  - What does `int("3.4")` do?
  - Given these float, int, and string values, which expressions will print a particular result?
  - What do you expect `1+2j + 3` to produce?

### [Built-in Functions and Help](../episodes/04-built-in.md) (09:55)

- Teaching: 15 min
  - Explain the purpose of functions.
  - Correctly call built-in Python functions.
  - Correctly nest calls to built-in functions.
  - Use help to display documentation for built-in functions.
  - Correctly describe situations in which SyntaxError and NameError occur.
- Challenges: 10 min
  - Explain the order of operations in the following complex expression.
  - What will each nested combination of `min` and `max` calls produce?
  - Why don't `max` and `min` return `None` when given no arguments?
  - Given what we have seen so far,
    what index expression will get the last character in a string?

### [Coffee](../episodes/05-coffee.md): 15 min (10:20)

### [Libraries](../episodes/06-libraries.md) (10:35)

- Teaching: 10 min
  - Explain what software libraries are and why programmers create and use them.
  - Write programs that import and use libraries from Python's standard library.
  - Find and read documentation for standard libraries interactively (in the interpreter) and online.
- Challenges: 10 min
  - Which function from the standard math library could you use to calculate a square root?
  - What library would you use to select a random value from data?
  - If `help(math)` produces an error, what have you forgotten to do?
  - Fill in the blanks in code below so that the import statement and program run.

### [Reading Tabular Data](../episodes/07-reading-tabular.md) (10:55)

- Teaching: 10 min
  - Import the Pandas library.
  - Use Pandas to load a simple CSV data set.
  - Get some basic information about a Pandas DataFrame.
- Challenges: 10 min
  - Read the data for the Americas and display its summary statistics.
  - What do `.head` and `.tail` do?
  - What string(s) should you pass to `read_csv` to read files from other directories?
  - How can you *write* CSV data?

### [DataFrames](../episodes/08-data-frames.md) (11:15)

- Teaching: 15 min
  - Select individual values from a Pandas dataframe.
  - Select entire rows or entire columns from a dataframe.
  - Select a subset of both rows and columns from a dataframe in a single operation.
  - Select a subset of a dataframe by a single Boolean criterion.
- Challenges: 15 min
  - Write an expression to find the Per Capita GDP of Serbia in 2007.
  - What rule governs what is (or isn't) included in numerical and named slices in Pandas?
  - What does each line in the following short program do?
  - What do `idxmin` and `idxmax` do?
  - Write expressions to get the GDP per capita for all countries in 1982,
    for all countries *after* 1985,
    etc.
  - Given the way its borders have changed since 1900,
    what would you do if asked to create a table of GDP per capita for Poland
    for the Twentieth Century?

### [Plotting](../episodes/09-plotting.md) (11:45)

- Teaching: 15 min
  - Create a time series plot showing a single data set.
  - Create a scatter plot showing relationship between two data sets.
- Exercise: 15 min
  - Fill in the blanks to plot the minimum GDP per capita over time for European countries.
  - Modify the example to create a scatter plot of GDP per capita in Asian countries.
  - Explain what each argument to `plot` does in the following example.

### [Lunch](../episodes/10-lunch.md) (12:15): 45 min

### [Lists](../episodes/11-lists.md) (13:00)

- Teaching: 10 min
  - Explain why programs need collections of values.
  - Write programs that create flat lists, index them, slice them, and modify them through assignment and method calls.
- Challenges: 10 min
  - Fill in the blanks so that the program produces the output shown.
  - How large are the following slices?
  - What do negative index expressions print?
  - What does a "stride" in a slice do?
  - How do slices treat out-of-range bounds?
  - What are the differences between sorting these two ways?
  - What is the difference between `new = old` and `new = old[:]`?

### [Loops](../episodes/12-for-loops.md) (13:20)

- Teaching: 10 min
  - Explain what for loops are normally used for.
  - Trace the execution of a simple (unnested) loop and correctly state the values of variables in each iteration.
  - Write for loops that use the Accumulator pattern to aggregate values.
- Challenges: 15 min
  - Is an indentation error a syntax error or a runtime error?
  - Trace which lines of this program are executed in what order.
  - Fill in the blanks in this program so that it reverses a string.
  - Fill in the blanks in this series of examples to get practice accumulating values.
  - Reorder and indent these lines to calculate the cumulative sum of the list values.

### [Looping Over Data Sets](13-looping-data-sets) (13:45)

- Teaching: 5 min
  - Be able to read and write globbing expressions that match sets of files.
  - Use glob to create lists of files.
  - Write for loops to perform operations on files given their names in a list.
- Challenges: 10 min
  - Which filenames are *not* matched by this glob expression?
  - Modify this program so that it prints the number of records in the shortest file.
  - Write a program that reads and plots all of the regional data sets.

### [Writing Functions](14-writing-functions) (14:00)

- Teaching: 10 min
  - Explain and identify the difference between function definition and function call.
  - Write a function that takes a small, fixed number of arguments and produces a single result.
- Challenges: 15 min
  - This code defines and calls a function - what does it print when run?
  - Explain why this short program prints things in the order it does.
  - Fill in the blanks to create a function that finds the minimum value in a data file.
  - Fill in the blanks to create a function that finds the first negative value in a list.
    What does your function do if the list is empty?
  - Why is it sometimes useful to pass arguments by naming the corresponding parameters?
  - Fill in the blanks and turn this short piece of code into a function.

### [Variable Scope](15-scope) (14:25)

- Teaching: 10 min
  - Identify local and global variables.
  - Identify parameters as local variables.
  - Read a traceback and determine the file, function, and line number on which the error occurred.
- Challenges: 10 min
  - Trace the changes to the values in this program,
    being careful to distinguish local from global values.

### [Coffee](16-coffee) (14:45): 15 min

### [Conditionals](17-conditionals) (15:00)

- Teaching: 10 min
  - Correctly write programs that use if and else statements and simple Boolean expressions (without logical operators).
  - Trace the execution of unnested conditionals and conditionals inside loops.
- Challenges: 15 min
  - Trace the execution of this conditional statement.
  - Fill in the blanks so that this function replaces negative values with zeroes.
  - Modify this program so that it only processes files with fewer than 50 records.
  - Modify this program so that it always finds the largest and smallest values in a list
    no matter what the list's values are.

### [Programming Style](../episodes/18-style.md) (15:25)

- Teaching: 15 min
  - How can I make my programs more readable?
  - How do most programmers format their code?
  - How can programs check their own operation?
- Challenges: 15 min
  - Which lines in this code will be available as online help?
  - Turn the comments in this program into docstrings.
  - Rewrite this short program to be more readable.

### [Wrap-Up](../episodes/19-wrap.md) (15:55)

- Teaching: 20 min
  - Name and locate scientific Python community sites for software, workshops, and help.
- Challenges: 0 min
  - None.

### [Feedback](../episodes/20-feedback.md) (16:15)

- Teaching: 0 min
- Challenges: 15 min
  - Collect feedback

### Finish (16:30)


