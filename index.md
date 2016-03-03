# Python for Novice Research Programmers

## Stage 0 - Assumptions

*   Audience
    *   Graduate students in numerate disciplines from cosmology to economics
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
        *   In particular, must not require knowledge of shell or version control
    *   Use the Jupyter Notebook
        *   Authentic tool used by many instructors
        *   There isn't really an alternative
        *   And means that even people who have seen a bit of Python before will probably learn something
*   Data
    *   Use the gapminder data throughout
    *   But break into multiple files by continent
        *   To make display of output from examples tidier (use Australia/New Zealand, which is only two lines)
        *   And allow examples showing use of multiple data sets
*   Focus on Pandas instead of NumPy
    *   Makes lesson usable by both Data Carpentry and Software Carpentry
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
*   See also:
    *   http://nsoontie.github.io/2015-03-05-ubc/novice/python/Pandas-Lesson.html

## Stage 1 - Desired Results

### Goals

1.  Get learners to the stage decribed in the "Software" section of
    "[Good Enough Practices in Scientific Computing][good-enough]".
    *   Missing items are in **bold**
    *   Goals
        1.  Make it easy for people (including your future self) to understand and (re)use your code
        2.  Modular, comprehensible, reusable, and testable all come together
    *   Rules
        1.  Every analysis step is represented textually (complete with parameter values)
        2.  Every program or script has a brief explanatory comment at the start
        3.  Programs of all kinds (including "scripts") are broken into functions
        4.  No duplication
        5.  Functions and variables have meaningful names
        6.  **Dependencies and requirements are explicit (e.g., a requirements.txt file)**
        7.  Commenting/uncommenting are not routinely used to control program behavior
        8.  Use a simple example or test data set to run to tell if it's working at all and whether it gives a known correct output for a simple known input
        9.  Submit code to a reputable DOI-issuing repository upon submission of paper, just like data
2.  Enable them to make sense of other onlines tutorials and resources

### Summative Assessment

*   Midpoint: plot bar chart showing average GDP per continent
*   Final: debug and extend a short multi-function program to handle data laid out differently

### Essential Questions

*   How do I read, analyze, and visualize a tabular data set?
*   How do I process multiple data sets?
*   How do I tell if my program is working correctly?
*   How do I fix it when it's not?
*   How do I find and use software other people have written instead of writing my own?

### Learners Will Be Able To...

*   Run code interactively
*   Run code saved in a file
*   Write single-condition `if` statements
*   Convert between basic data types (integer, float, string)
*   Call built-in functions
*   Use `help` and online documentation
*   Import a library using an alias
*   Call something from an imported library
*   Read tabular data into an array or data frame
*   Do collective operations on arrays and data frames
*   Create simple plots of data in arrays and data frames
*   Interpret common error messages
*   Track down bugs by running small tests of program modules
*   Write non-recursive functions taking a fixed number of named parameters
*   Create literate programs in the Jupyter Notebook

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
*   What a variable is
*   How assignment works
*   What integers, floats, strings, and data frames are
*   How a `for` loop executes
*   What a list is and how to index one
*   How `if`/`else` executes
*   The difference between defining and calling a function
*   What a call stack is
*   How local variables are created and scoped
*   Where to find documentation on standard libraries

## Stage 2 - Learning Plan

### Running and Quitting Interactively

*   Teaching: 15 min (because setup issues)
*   Exercises: 0 min (accounted for in teaching time - no separate exercise)
    *   Run the Notebook
    *   Create a few Markdown cells (just formatted)
    *   Create and execute a Python cell that prints 1+2 (to show that cells can be executed)

### Variables and Assignment

*   Teaching: 5 min
*   Exercises: 5 min
    *   Trace behavior of swapping values of two variables using an intermediate variable
    *   Calculate elapsed time in seconds using named values for seconds per minute, etc.

### Data Types and Type Conversion

*   Teaching: 5 min
*   Exercises: 5 min
    *   Predict result types (or errors) of various operations
    *   Add conversion functions to broken code to make it work

### Built-in Functions (and Methods) and Help

*   Teaching: 10 min
    *   Include re-running cells and re-running all
*   Exercises: 10 min
    *   Chain calculations with max and min
    *   Find a useful method using help(str)
    *   Parsons Problem to achieve specific results with string methods

### Error Messages

*   Teaching: 5 min (review of error messages seen to date)
*   Exercises: 10 min
    *   Identify causes of common errors (but don't actually fix)

### Libraries (Including Aliases)

*   Teaching: 5 min
*   Exercises: 5 min
    *   Operations with math library
    *   Look things up in the python.org docs

### *Coffee: 15 min*

### Reading Tabular Data

*   Teaching: 5 min
*   Exercises: 10 min (because some people will have trouble finding the data set's path)
    *   Read one continent's subset of gapminder CSV data
*   Callout:
    *   How to read data from Excel spreadsheets via export to CSV

### Pandas Data Frames

*   Teaching: 10 min
*   Exercises: 10 min
    *   Create data frame manually
    *   Select individual values
    *   Select various subsets of data
    *   Normalize values (scale to 0..1)

### Plotting

*   Teaching: 10 min (to show a variety of plots and debug display problems)
*   Exercises: 10 min
    *   Plot normalized change in GDP over time (tweaking provided code)

### For Loops

*   Teaching: 10 min
    *   Do *not* explicitly introduce lists
*   Exercises: 10 min
    *   Reverse a string by repeated append
    *   Manually trace execution of loop

### Looping Over Data Sets

*   Teaching: 5 min (use `glob` to get filenames)
*   Exercises: 15 min
    *   Count rows of each data set
    *   Check number of columns in each data set is the same

### Lists

*   Teaching: 5 min (show what `glob` produces and do a few operations on lists)
*   Exercises: 5 min
    *   Toy examples of lists, indexing, etc.

### *Lunch: 60 min*

### Conditionals

*   Teaching: 5 min (show conditionals inside loop)
*   Exercises: 10 min
    *   Count vowels
    *   Report badly-sized files inside loop

### Writing Functions

*   Teaching: 10 min
*   Exercises: 15 min
    *   Check size of a single data file
    *   Check sizes of all data files in a directory
        *   Write new function using previous function

### Documentation

*   Teaching: 5 min
*   Exercises: 5 min
    *   Add docstrings to functions written earlier

### *Coffee: 15 min*

### Defensive Programming

*   Teaching: 5 min (introduce assertions)
*   Exercises: 10 min
    *   Critique a badly-written 20-line program

### Debugging

*   Teaching: 10 min (divide and conquer)
*   Exercises: 10 min
    *   Debug three-function program

### Programming Style

*   Teaching: 10 min (present checklist)
*   Exercises: 10 min
    *   Do a code review

### Wrap-Up

*   Teaching: 10 min
    *   Where to look next
*   Exercises: 0 min

[good-enough]: https://github.com/swcarpentry/good-enough-practices-in-scientific-computing
