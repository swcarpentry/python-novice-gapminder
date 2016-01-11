# Python for Novice Research Programmers

## Stage 0 - Assumptions

*   Audience
    *   Graduate students in numerate disciplines
    *   Understand very basic statistics (mean, correlation)
    *   Have manipulated data in spreadsheets and interactive tools like SAS
    *   Have _not_ programmed beyond CPD (copy-paste-despair)
*   Requirements
    *   Full day: 6.5 hours
    *   Learners use their own machines
    *   No dependence on other Carpentry modules
        *   In particular, no knowledge of shell or version control
    *   Will _not_ depend on Jupyter Notebook
        *   What to use instead?
        *   How to get learners' filenames into programs?
*   Data
    *   Use the gapminder data throughout
    *   Break into multiple files by continent

## Stage 1 - Desired Results

### Goals

*   Get learners to the stage decribed in the "Software" section of
    "[Good Enough Practices in Scientific Computing][good-enough]".
*   Enable them to make sense of other onlines tutorials and resources

### Understandings

Students will understand that...

*   A program is a piece of lab equipment that implements an analysis
    *   Needs to be validated/calibrated before/during use
    *   Makes analysis reproducible, reviewable, shareable
*   Programs are written for people, not for computers
    *   Meaningful variable names
    *   Modularity for readability as well as re-use
    *   No duplication
    *   Document purpose and use
*   There is no magic: the programs they use are no different in principle from those they build

### Essential Questions

*   How do I read, analyze, and visualize a tabular data set?
*   How do I process multiple data sets?
*   How do I tell if my program is working correctly?
*   How do I fix it when it's not?
*   How do I find and use software other people have written instead of writing my own?

### Learners Will Know...

*   What a variable is
*   How assignment works
*   What integers, floats, strings, lists, arrays, and data frames are
*   How a `for` loop executes
*   How `if`/`else` executes
*   The difference between defining and calling a function
*   What a call stack is
*   How local variables are created and scoped
*   Where to find documentation on standard libraries

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

## Stage 2 - Assessment

### Running and Quitting Interactively

*   Teaching: 5 min
*   Exercises: 10 min (because setup issues)
    *   Run an interactive Python interpreter, print 1+2, exit the interpreter

### Variables and Assignment

*   Teaching: 5 min
*   Exercises: 5 min
    *   Trace behavior of swapping (`a, b = b, a` the old fashioned way) with an intermediate variable
    *   Calculate elapsed time in seconds using named values for seconds per minute, etc.

### Data Types and Type Conversion

*   Teaching: 5 min
*   Exercises: 5 min
    *   predict result types (or errors) of various operations
    *   add conversion functions to broken code to make it work

### Built-in Functions (and Methods) and Help

*   Teaching: 5 min
*   Exercises: 5 min
    *   chain calculations with max and min
    *   find a useful method using help(str)
    *   Parsons Problem to achieve specific results with string methods

### Libraries (Including Aliases)

*   Teaching: 10 min
*   Exercises: 10 min
    *   operations with math library
    *   look things up in the python.org docs

### Collective Operations (on NumPy Arrays)

*   Teaching: 10 min
*   Exercises: 10 min
    *   scale array values to 0..1

### Reading Tabular Data

*   Teaching: 5 min (hard part is changing directory, so may need to introduce os library)
*   Exercises: 5 min
    *   read gapminder CSV with NumPy

### Plotting

*   Teaching: 10 min (to show a variety of plots and debug display problems)
*   Exercises: 5 min
    *   plot normalized change in GDP over time (tweaking provided code)

### Running Saved Programs

*   Teaching: 10 min (setup issues again)
*   Exercises:
    *   save plotting code in file and run that (input filename hard-coded)
    *   FIXME: how to get filename into script without editing?

### For Loops

*   Teaching: 15 min (do *not* introduce lists)
*   Exercises: 10 min
    *   reverse a string by repeated append
    *   trace execution of loop

### Lists

*   Teaching: 10 min
*   Exercises: 10 min
    *   indexing exercises
    *   conversion from list to string and back
    *   sum values in a list

### Looping Over Data Sets

*   Teaching: 10 min (use glob to get filenames)
*   Exercises: 15 min
    *   count rows of each data set
    *   check number of columns in each data set is the same

### Error Messages

*   Teaching: 10 min (review of error messages seen to date)
*   Exercises: 10 min
    *   diagnose and fix small programs with errors (some syntax, some runtime)

### Conditionals

*   Teaching: 15 min (inside loop)
*   Exercises: 15 min
    *   count vowels
    *   check sizes of data files inside a loop

### Writing Functions

*   Teaching: 15 min
*   Exercises: 15 min
    *   check size of a single data file
    *   check sizes of all data files in a directory (directory name given as arg)

### The Call Stack and Variable Scoping

*   Teaching: 15 min
*   Exercises: 20 min
    *   trace and draw execution of functions calling functions

### Documentation

*   Teaching: 10 min
*   Exercises: 10 min
    *   add docstrings to functions written earlier

### Programming Style

*   Teaching: 15 min (mostly to introduce checklist)
*   Exercises: 15 min
    *   clean up badly-written 20-line program

### Debugging

*   Teaching: 10 min (divide and conquer)
*   Exercises: 15 min
    *   debug one-page program

### Defensive Programming

*   Teaching: 5 min
*   Exercises: 10 min
    *   add assertions to functions based on docstrings

### Testing

*   Teaching: 15 min
*   Exercises: 15 min
    *   write Nose tests for the functions in the one-page program above

### Jupyter Notebook

*   Teaching: 15 min
*   Exercises: 20 min
    *   build a multi-part script with documentation in the Notebook

## Stage 3 - Learning Plan

[good-enough]: https://github.com/swcarpentry/good-enough-practices-in-scientific-computing
