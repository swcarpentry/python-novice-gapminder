---
layout: episode
title: "Variables and Assignment"
teaching: 5
exercises: 5
questions:
- "How can I store data in programs?"
objectives:
- "Write programs that assign scalar values to variables and perform calculations with those values."
- "Correctly trace value changes in programs that use scalar assignment."
keypoints:
- FIXME
---
FIXME: lesson content.

The assignment of variables in Python is dynamic, this means that the type of data and memory are assigned when the objects/variables are created, for instance,

> ~~~
> x = 1
> ~~~

will assign an integer value to the variable `x`. However, if we assign

> ~~~
> x = 1.0
> ~~~

Python will assign a float value to the variable `x`. Once a variable is defined will remain in memory until the program python shell is alive. If you want to delete the variable you will do

> ~~~
> del x
> ~~~

and this command will delete the variable `x` just defined above. You can assign a variable the value of another variable,

> ~~~
> x = 10.0
> y = x
> ~~~

Now, `y` has the same value than `x`.

> ## Swapping Values
> 
> Draw a table showing the values of the variables in this program
> after each statement is executed.
> In simple terms, what do the last three lines of this program do?
> 
> ~~~
> lowest = 1.0
> highest = 3.0
> temp = lowest
> lowest = highest
> highest = temp
> ~~~
> {: .source}
{: .challenge}

> ## Predicting Values
> 
> What is the final value of `position` in the program below?
> (Try to predict the value without running the program,
> then check your prediction.)
> 
> ~~~
> initial = "left"
> position = initial
> initial = "right"
> ~~~
> {: .source}
{: .challenge}
