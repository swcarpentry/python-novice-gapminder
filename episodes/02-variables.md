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

### Variables

Variables are names for values. In Python the `=` symbol assigns the value on the right to the name on the left.

Enter code into a cell that assigns the value of your age to a variable `age` and your first name in quotation marks to a variable `first_name`

```python
age = 42
first_name = 'Alistair'
```

Variables names have a few rules

- They can't start with a number.
- They can't contain spaces, use underscores or hyphens instead.


Underscores at the start like `__alistairs_real_age` have a special meaning so we won't do that until we understand the convention.

*funny fact* - A double underscore is a `dunder`

### Upper and lower case letters

`Name` and `name` are different to Python.

Again there are conventions around using uppercase at the start of names so we'll use lowercase letters.

### Meaningful variable names

Python doesn't care what you call variables as long as they follow the rules. You can name your age `flabadap` and your first name `ewr-45-ada__wYYEDyebdb` but don't.... 

Try to use a meaningful variable name because it helps humans read the code. And by humans I really mean your future self.

### Using variables

Now we've created the age variable, we can do calculations with it

```python
#how old will you be in 3 years?

age = age + 3
age
```

We can also do maths with strings

```python
# create a last name variable
last_name = 'Walsh'

# now make a full name variable using the two parts

full_name = first_name + ' ' + last_name
full_name
```

- Can you use the `-` symbol to subtract a string?
- Can you multiply `*` a string by a number? 
- Another string?



### When are calculations performed?
We changed the value of `age` before to `age + 3`. Let's reassign our current age to `age` and create a `future_age` variable that uses `age` to calculate our future age in 15 years. 

```python
age = 42
future_age = age + 15
future_age
```

What happens if we change the value of `age` after we use it to calculate `future_age`? Does `future_age` update too?

```python
age = 42
future_age = age + 15
age = 100
future_age
```


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
