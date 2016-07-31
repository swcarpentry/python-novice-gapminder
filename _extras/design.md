---
layout: page
title: "Lesson Design"
permalink: /design/
---
## Process Used

This lesson was developed using a slimmed-down variant of the "Understanding by Design" process.
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
    *   Who are sighted
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
*   Exercises will mostly *not* be "write this code from scratch"
    *   Want lots of short exercises that can reliably be finished in allotted time
    *   So use MCQs, fill-in-the-blanks, Parsons Problems, "tweak this code", etc.
*   Lesson materials
    *   Notes for instructors and self-study will be written in Markdown
        *   We've tried writing/maintaining lessons as Notebooks...
    *   Learners will be provided with one Notebook per episode containing exercises

## Stage 1 - Desired Results

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

## Stage 2 - Learning Plan

*   Running and Quitting Interactively (9:00)
    *   Teaching: 15 min (because setup issues)
    *   Exercises: 0 min (accounted for in teaching time - no separate exercise)
        *   Run the Notebook
        *   Create a few Markdown cells
        *   Create and execute a Python cell that prints 1+2
*   Variables and Assignment (9:15)
    *   Teaching: 10 min
    *   Exercises: 10 min
        *   Trace behavior of three-step swapping
        *   Calculate elapsed time in seconds using named values for seconds per minute, etc.
*   NumPy Arrays (9:35)
    *   Teaching: 15 min
    *   Exercises: 10 min
        *   Read CSV data into array
        *   Calculate statistics on rows and columns
*   Plotting Vectors (10:00)
    *   Teaching: 10 min
    *   Exercise: 10 min
        *   Load single-column CSV and create plot
*   Plotting Time Series (10:20)
    *   Teaching: 10 min
    *   Exercise: 10 min
        *   Read and plot two-column data set (year and value)
*   Coffee: 15 min (10:40)
*   Lists (10:55)
    *   Teaching: 15 min (introduce `glob.glob`)
    *   Exercises: 10 min
        *   Count how many files match a given pattern
*   Loops (11:20)
    *   Teaching: 15 min
    *   Exercises: 15 min
        *   Filter a list of files (a simple alternative to `glob`)
*   Combining Ideas (11:50)
    *   Teaching: 5 min
    *   Exercise: 15 min
        *   Produce one plot for each data file in a directory
*   Lunch: 60 min (12:10)
*   Writing Functions (13:10)
    *   Teaching: 20 min
    *   Exercises: 20 min
        *   Extract and encapsulate "plot this file"
*   Conditionals (13:50)
    *   Teaching: 10 min
    *   Exercises: 15 min
        *   Resize picture so that either height or width is 100px
        *   Keep largest of three color values (conditional in loop)
*   Coffee: 15 min (14:15)
*   Programming Style (14:30)
    *   Teaching: 10 min
    *   Exercises: 10 min
        *   Add docstrings to functions written earlier
*   Data Frames (14:50)
    *   Teaching: 15 min
    *   Exercises: 15 min
        *   Read more complex data set and calculate statistics
*   Plotting Data Frames (15:20)
    *   Teaching: 15 min
    *   Exercises: 15 min
        *   Plot time series data from complex data set
*   Wrapping Up: 10 min (15:50)
