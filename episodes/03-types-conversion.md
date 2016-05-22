---
layout: episode
title: "Data Types and Type Conversion"
teaching: 5
exercises: 5
questions:
- "What kinds of data do programs store?"
- "How can I convert one type to another?"
objectives:
- "Explain key differences between integers and floating point numbers."
- "Explain key differences between numbers and character strings."
- "Use built-in functions to convert between integers, floating point numbers, and strings."
keypoints:
- FIXME
---
### Words

*   Text handling is a strength of Python, we call a sequence of characters a `str` or string.
*   Python doesn't understand what the string means, it sees it as a sequence of characters.

~~~
# create a string and assign it to a variable
question = 'The meaning of life'
~~~
{: .source}

### Numbers

*   Numeric values are either `int` or `float`.
*   The difference is `int`, or integer, is a whole number value and a `float`, or floating point number, is a number with a decimal point.
*   "Use integers for counting and floats for measuring."

~~~
# Create a int and a float.
answer = 42
precisely = 42.7
~~~
{: .source}

### Types

Let's use the `type` function to check:

~~~
question = 'The meaning of life'
type(question)
~~~
{: .source}
~~~
<class 'str'>
~~~
{: .output}

~~~
answer = 42
type(answer)
~~~
{: .source}
~~~
<class 'int'>
~~~
{: .output}

~~~
precisely = 42.7
type(precisely)
~~~
{: .source}
~~~
<class 'float'>
~~~
{: .output}

*   Can you include numeric values in strings?

> ## Choose a Type
> 
> What type of value (integer, floating point number, or character string)
> would you use to represent each of the following?
> 
> 1. Number of days since the start of the year.
> 2. Time elapsed since the start of the year.
> 3. Serial number of a piece of lab equipment.
> 4. A lab specimen's age.
> 5. Current population of a city.
> 6. Average population of a city over time.
{: .challenge}

> ## Division Types
> 
> The `//` operator returns the whole-number result of division,
> while the '%' operator returns the remainder from division:
> 
> ~~~
> print('5 // 3:', 5//3)
> print('5 % 3:', 5%3)
> ~~~
> {: .source}
> 
> ~~~
> 5 // 3: 1
> 5 % 3: 2
> ~~~
> {: .output}
> 
> If `num_subjects` is the number of subjects taking part in a study,
> and `num_per_survey` is the number that can take part in a single survey,
> write an expression that calculates the number of surveys needed
> to reach everyone once.
{: .challenge}

> ## Strings to Numbers
> 
> `float` will convert a string to a floating point number,
> and `int` will convert a floating point number to an integer:
> 
> ~~~
> print("string to float:", float("3.4"))
> print("float to int:", int(3.4))
> ~~~
> {: .source}
> 
> ~~~
> 3.4
> 3
> ~~~
> {: .output}
> 
> Given that,
> what do you expect this program to do?
> What does it actually do?
> Why do you think it does that?
> 
> ~~~
> print("fractional string to int:", int("3.4"))
> ~~~
> {: .source}
{: .challenge}

> ## Arithmetic with Different Types
> 
> Which of the following will print 2.0?
> Note: there may be more than one right answer.
> 
> ~~~
> first = 1.0
> second = "1"
> third = "1.1"
> ~~~
> {: .source}
> 
> 1. `first + float(second)`
> 2. `float(second) + float(third)`
> 3. `first + int(third)`
> 4. `first + int(float(third))`
> 5. `int(first) + int(float(third))`
> 6. `2.0 * second`
> 
> Answer: A and D
{: .challenge}
