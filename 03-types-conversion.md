---
layout: lesson
subtitle: Data Types and Type Conversion
teaching: 5
exercises: 5
---
> ## Learning Objectives
>
> * Learner will explain key differences between integers and floating point numbers.
> * Learner will explain key differences between numbers and character strings.
> * Learner will use built-in functions to convert between integers, floating point numbers, and strings.
{: .objectives}

Text handling is a strength of Python, we call a sequence of characters a `str` or string. Python doesn't understand what the string means, it sees it as a sequence of characters.

```python
# create a string and assign it to a variable
question = 'The meaning of life'
```

Numeric values are either `int` or `float`. The difference is `int`, or integer, is a whole number value and a `float`, or floating point number, is a number with a decimal point.

```python
#create a int and a float
answer = 42
precisely = 42.7
```

Let's use the `type()` function to check

```python
question = 'The meaning of life'
type(question)
```
```python
answer = 42
type(answer)
```
```python
precisely = 42.7
type(precisely)
```

Can you include numeric values in strings?

## Choose a Type
{: .challenge}

What type of value (integer, floating point number, or character string)
would you use to represent each of the following?

1. Number of days since the start of the year.
2. Time elapsed since the start of the year.
3. Serial number of a piece of lab equipment.
4. A lab specimen's age.
5. Current population of a city.
6. Average population of a city over time.

## Division Types
{: .challenge}

The `//` operator returns the whole-number result of division,
while the '%' operator returns the remainder from division:

~~~
print('5 // 3:', 5//3)
print('5 % 3:', 5//3)
~~~
{: .python}

~~~
5 // 3: 1
5 % 3: 2
~~~
{: .output}

If `num_subjects` is the number of subjects taking part in a study,
and `num_per_survey` is the number that can take part in a single survey,
write an expression that calculates the number of surveys needed
to reach everyone once.

## Strings to Numbers
{: .challenge}

`float` will convert a string to a floating point number,
and `int` will convert a floating point number to an integer:

~~~
print("string to float:", float("3.4"))
print("float to int:", int(3.4))
~~~
{: .python}

~~~
3.4
3
~~~
{: .output}

Given that,
what do you expect this program to do?
What does it actually do?
Why do you think it does that?

~~~
print("fractional string to int:", int("3.4"))
~~~
{: .python}

## Arithmetic with Different Types
{: .challenge}

Which of the following will print 2.0?
Note: there may be more than one right answer.

~~~
first = 1.0
second = "1"
third = "1.1"
~~~
{: .python}

1. `first + float(second)`
2. `float(second) + float(third)`
3. `first + int(third)`
4. `first + int(float(third))`
5. `int(first) + int(float(third))`
6. `2.0 * second`

> Answer: A and D
{: .solution}
