---
layout: lesson
subtitle: Variables and Assignment
teaching: 5
exercises: 5
---
> ## Learning Objectives
>
> * Learner will write programs that assign scalar values to variables
>   and perform calculations with those values.
> * Learner will correctly trace value changes in programs that use scalar assignment.
{: .objectives}

### Variables

Variables are names for values. In Python the `=` symbol assigns the value on the right to the name on the left.

Enter code into a cell that assigns the value of your age to a variable `age` and your first name in quotation marks to a variable `first_name`

## Swapping Values
{: .challenge}

Draw a table showing the values of the variables in this program
after each statement is executed.
In simple terms, what do the last three lines of this program do?

~~~
lowest = 1.0
highest = 3.0
temp = lowest
lowest = highest
highest = temp
~~~
{: .python}

## Predicting Values
{: .challenge}

What is the final value of `position` in the program below?
(Try to predict the value without running the program,
then check your prediction.)

~~~
initial = "left"
position = initial
initial = "right"
~~~
{: .python}
