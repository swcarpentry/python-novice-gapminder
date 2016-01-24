# Python for Novice Research Programmers

## Stage 0 - Assumptions

*   Audience
    *   Graduate students in numerate disciplines
    *   Understand very basic statistics (mean, correlation)
    *   Have manipulated data in spreadsheets and interactive tools like SAS
    *   Have _not_ programmed beyond CPD (copy-paste-despair)
*   Requirements
    *   Full day: 06:30
    *   Learners use their own machines
    *   No dependence on other Carpentry modules
        *   In particular, no knowledge of shell or version control
    *   Will introduce the Jupyter Notebook
        *   Authentic tool used by many instructors
        *   There isn't really an alternative
*   Data
    *   Use the gapminder data throughout
    *   Break into multiple files by continent
*   Pandas instead of NumPy
    *   Genuine novices are likely to want data analysis
    *   People with some prior experience:
        *   Will accept data analysis as an authentic task
        *   Are unlikely to have encountered Pandas,
            so they'll still get something useful out of the lesson

## Stage 1 - Desired Results

### Goals

1.  Get learners to the stage decribed in the "Software" section of
    "[Good Enough Practices in Scientific Computing][good-enough]".
    *   Goals
        1.  Make it easy for people (including your future self) to understand and (re)use your code
        2.  Modular, comprehensible, reusable, and testable all come together
    *   Rules
        1.  Every analysis step is represented textually (complete with parameter values)
        2.  Every program or script has a brief explanatory comment at the start
        3.  Programs of all kinds (including "scripts") are broken into functions that:
        4.  No duplication
        5.  Functions and variables have meaningful names
        6.  Dependencies and requirements are explicit (e.g., a requirements.txt file)
        7.  Commenting/uncommenting are not routinely used to control program behavior
        8.  Use a simple example or test data set to run to tell if it's working at all and whether it gives a known correct output for a simple known input
        9.  Submit code to a reputable DOI-issuing repository upon submission of paper, just like data
2.  Enable them to make sense of other onlines tutorials and resources

### Summative Assessment

FIXME:

1.  If we had a final exam for this, what would it be?
2.  If we had a mid-point exam, what would it be?

### Essential Questions

*   How do I read, analyze, and visualize a tabular data set?
*   How do I process multiple data sets?
*   How do I tell if my program is working correctly?
*   How do I fix it when it's not?
*   How do I find and use software other people have written instead of writing my own?

### Learners Will Be Able To...

*   Run code interactively
*   Run code saved in a file
*   Loop over a list
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
*   What integers, floats, strings, lists, arrays, and data frames are
*   How a `for` loop executes
*   How `if`/`else` executes
*   The difference between defining and calling a function
*   What a call stack is
*   How local variables are created and scoped
*   Where to find documentation on standard libraries

## Stage 2 - Assessment

### Running and Quitting Interactively

*   Teaching: 15 min (because setup issues)
*   Exercises: 0 min (accounted for in teaching time - no separate exercise)
    *   Run the Notebook
    *   Create a few Markdown cells
    *   Create and execute a Python cell that prints 1+2

### Variables and Assignment

*   Teaching: 5 min
*   Exercises: 5 min
    *   Trace behavior of swapping (`a, b = b, a` the old fashioned way) with an intermediate variable
    *   Calculate elapsed time in seconds using named values for seconds per minute, etc.

### Data Types and Type Conversion

*   Teaching: 5 min
*   Exercises: 5 min
    *   Predict result types (or errors) of various operations
    *   Add conversion functions to broken code to make it work

### Built-in Functions (and Methods) and Help

*   Teaching: 5 min
*   Exercises: 5 min
    *   Chain calculations with max and min
    *   Find a useful method using help(str)
    *   Parsons Problem to achieve specific results with string methods

### Error Messages

*   Teaching: 10 min (review of error messages seen to date)
*   Exercises: 10 min
    *   Diagnose and fix small errors (some syntax, some runtime)

### Libraries (Including Aliases)

*   Teaching: 5 min
*   Exercises: 5 min
    *   Operations with math library
    *   Look things up in the python.org docs

### Pandas Data Frames

*   Teaching: 10 min
*   Exercises: 10 min
    *   Import Pandas
    *   Create and display a data frame

### Reading Tabular Data

*   Teaching: 5 min
*   Exercises: 5 min
    *   Read one continent's subset of gapminder CSV data
*   Callout:
    *   How to read data from Excel spreadsheets via export to CSV
    *   How tor ead data from Excel spreadsheets directly (needs another library)

### Collective Operations

*   Teaching: 10 min
*   Exercises: 10 min
    *   Select various subsets of data
    *   Normalize values (scale to 0..1)

### Plotting

*   Teaching: 10 min (to show a variety of plots and debug display problems)
*   Exercises: 5 min
    *   Plot normalized change in GDP over time (tweaking provided code)

### For Loops

*   Teaching: 15 min (do *not* introduce lists)
*   Exercises: 10 min
    *   Reverse a string by repeated append
    *   Trace execution of loop

### Looping Over Data Sets

*   Teaching: 10 min (use glob to get filenames)
*   Exercises: 15 min
    *   Count rows of each data set
    *   Check number of columns in each data set is the same

### *Lunch Break*

### Lists

*   Teaching: 10 min
*   Exercises: 10 min
    *   Indexing exercises
    *   Conversion from list to string and back
    *   Sum values in a list

### Conditionals

*   Teaching: 10 min (inside loop)
*   Exercises: 15 min
    *   Count vowels
    *   Report badly-sized files inside loop

### Writing Functions

*   Teaching: 15 min
*   Exercises: 15 min
    *   Check size of a single data file
    *   Check sizes of all data files in a directory
        *   Write new function using previous function

### Documentation

*   Teaching: 5 min
*   Exercises: 10 min
    *   Add docstrings to functions written earlier

### Programming Style

*   Teaching: 10 min (mostly to introduce checklist)
*   Exercises: 15 min
    *   Clean up badly-written 20-line program

### Debugging

*   Teaching: 10 min (divide and conquer)
*   Exercises: 15 min
    *   Debug three-function program

### Defensive Programming

*   Teaching: 5 min
*   Exercises: 10 min
    *   Add assertions to functions based on docstrings

### Programming with Arrays

*   Teaching: 10 min
*   Exercises: 10 min
    *   More complicated array indexing

### Wrap-Up

*   Teaching: 25 min
    *   Overview of key SciPy modules
    *   How to find and install libraries
    *   Running Python from the command line
    *   Other editing tools
*   Exercises: 0 min

## Stage 3 - Learning Plan

[good-enough]: https://github.com/swcarpentry/good-enough-practices-in-scientific-computing
