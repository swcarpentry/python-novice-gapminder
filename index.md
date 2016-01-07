# Python for Novice Research Programmers

## Stage 0 - Assumptions

*   Audience
    *   Graduate students in numerate disciplines
    *   Understand very basic statistics (mean, correlation)
    *   Have manipulated data in spreadsheets and interactive tools like SAS
    *   Have _not_ programmed beyond CPD (copy-paste-despair)
*   Requirements
    *   Full day: 18 x 20 minutes
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

## Stage 2 - Assessment

Running and Quitting Interactively
:   run an interactive Python interpreter; print 1+2; exit the interpreter

Variables and Assignment
:   trace behavior of swapping with intermediate variable; calculate elapsed time in seconds

Data Types and Type Conversion
:   predict types (or errors) of various operations; add conversion functions to broken code to make it work

Built-in Functions and Help
:   len (of strings); max

Libraries
:   operations with math library; python.org docs

Reading Tabular Data
:   read CSV with NumPy

Collective Operations
:   scale array values to 0..1

Plotting
:   plot differences between data sets

Running Saved Programs
:   FIXME: depends on tools

For Loops
:   reverse a string

Lists
:   create lists from lists

Looping Over Data Sets
:   process each file in a directory

Error Messages
:   diagnose and fix small programs with errors (some syntax, some runtime)

Conditionals
:   count vowels; check sizes of data files inside a loop

Writing Functions
:   check sizes of all data files in a directory (name given as arg)

The Call Stack and Variable Scoping
:   trace and draw execution of functions calling functions

Documentation
:   add docstrings to functions written earlier

Programming Style
:   clean up badly-written 20-line program

Debugging
:   debug one-page program by importing and then testing functions with small fabricated data

Testing
:   write Nose tests for the functions in the one-page program above

## Stage 3 - Learning Plan

[good-enough]: https://github.com/swcarpentry/good-enough-practices-in-scientific-computing
