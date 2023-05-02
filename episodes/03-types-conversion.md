---
title: Data Types and Type Conversion
teaching: 10
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

- Explain key differences between integers and floating point numbers.
- Explain key differences between numbers and character strings.
- Use built-in functions to convert between integers, floating point numbers, and strings.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- What kinds of data do programs store?
- How can I convert one type to another?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Every value has a type.

- Every value in a program has a specific type.
- Integer (`int`): represents positive or negative whole numbers like 3 or -512.
- Floating point number (`float`): represents real numbers like 3.14159 or -2.5.
- Character string (usually called "string", `str`): text.
  - Written in either single quotes or double quotes (as long as they match).
  - The quote marks aren't printed when the string is displayed.

## Use the built-in function `type` to find the type of a value.

- Use the built-in function `type` to find out what type a value has.
- Works on variables as well.
  - But remember: the *value* has the type --- the *variable* is just a label.

```python
print(type(52))
```

```output
<class 'int'>
```

```python
fitness = 'average'
print(type(fitness))
```

```output
<class 'str'>
```

## Types control what operations (or methods) can be performed on a given value.

- A value's type determines what the program can do to it.

```python
print(5 - 3)
```

```output
2
```

```python
print('hello' - 'h')
```

```error
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-67f5626a1e07> in <module>()
----> 1 print('hello' - 'h')

TypeError: unsupported operand type(s) for -: 'str' and 'str'
```

## You can use the "+" and "\*" operators on strings.

- "Adding" character strings concatenates them.

```python
full_name = 'Ahmed' + ' ' + 'Walsh'
print(full_name)
```

```output
Ahmed Walsh
```

- Multiplying a character string by an integer *N* creates a new string that consists of that character string repeated  *N* times.
  - Since multiplication is repeated addition.

```python
separator = '=' * 10
print(separator)
```

```output
==========
```

## Strings have a length (but numbers don't).

- The built-in function `len` counts the number of characters in a string.

```python
print(len(full_name))
```

```output
11
```

- But numbers don't have a length (not even zero).

```python
print(len(52))
```

```error
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-f769e8e8097d> in <module>()
----> 1 print(len(52))

TypeError: object of type 'int' has no len()
```

## Must convert numbers to strings or vice versa when operating on them. {#convert-numbers-and-strings}

- Cannot add numbers and strings.

```python
print(1 + '2')
```

```error
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-fe4f54a023c6> in <module>()
----> 1 print(1 + '2')

TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

- Not allowed because it's ambiguous: should `1 + '2'` be `3` or `'12'`?
- Some types can be converted to other types by using the type name as a function.

```python
print(1 + int('2'))
print(str(1) + '2')
```

```output
3
12
```

## Can mix integers and floats freely in operations.

- Integers and floating-point numbers can be mixed in arithmetic.
  - Python 3 automatically converts integers to floats as needed.

```python
print('half is', 1 / 2.0)
print('three squared is', 3.0 ** 2)
```

```output
half is 0.5
three squared is 9.0
```

## Variables only change value when something is assigned to them.

- If we make one cell in a spreadsheet depend on another,
  and update the latter,
  the former updates automatically.
- This does **not** happen in programming languages.

```python
variable_one = 1
variable_two = 5 * variable_one
variable_one = 2
print('first is', variable_one, 'and second is', variable_two)
```

```output
first is 2 and second is 5
```

- The computer reads the value of `variable_one` when doing the multiplication,
  creates a new value, and assigns it to `variable_two`.
- Afterwards, the value of `variable_two` is set to the new value and *not dependent on `variable_one`* so its value
  does not automatically change when `variable_one` changes.

:::::::::::::::::::::::::::::::::::::::  challenge

## Fractions

What type of value is 3.4?
How can you find out?

:::::::::::::::  solution

## Solution

It is a floating-point number (often abbreviated "float").
It is possible to find out by using the built-in function `type()`.

```python
print(type(3.4))
```

```output
<class 'float'>
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Automatic Type Conversion

What type of value is 3.25 + 4?

:::::::::::::::  solution

## Solution

It is a float:
integers are automatically converted to floats as necessary.

```python
result = 3.25 + 4
print(result, 'is', type(result))
```

```output
7.25 is <class 'float'>
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Choose a Type

What type of value (integer, floating point number, or character string)
would you use to represent each of the following?  Try to come up with more than one good answer for each problem.  For example, in  # 1, when would counting days with a floating point variable make more sense than using an integer?

1. Number of days since the start of the year.
2. Time elapsed from the start of the year until now in days.
3. Serial number of a piece of lab equipment.
4. A lab specimen's age
5. Current population of a city.
6. Average population of a city over time.

:::::::::::::::  solution

## Solution

The answers to the questions are:

1. Integer, since the number of days would lie between 1 and 365.
2. Floating point, since fractional days are required
3. Character string if serial number contains letters and numbers, otherwise integer if the serial number consists only of numerals
4. This will vary! How do you define a specimen's age? whole days since collection (integer)? date and time (string)?
5. Choose floating point to represent population as large aggregates (eg millions), or integer to represent population in units of individuals.
6. Floating point number, since an average is likely to have a fractional part.
  
  

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Division Types

In Python 3, the `//` operator performs integer (whole-number) floor division, the `/` operator performs floating-point
division, and the `%` (or *modulo*) operator calculates and returns the remainder from integer division:

```python
print('5 // 3:', 5 // 3)
print('5 / 3:', 5 / 3)
print('5 % 3:', 5 % 3)
```

```output
5 // 3: 1
5 / 3: 1.6666666666666667
5 % 3: 2
```

If `num_subjects` is the number of subjects taking part in a study,
and `num_per_survey` is the number that can take part in a single survey,
write an expression that calculates the number of surveys needed
to reach everyone once.

:::::::::::::::  solution

## Solution

We want the minimum number of surveys that reaches everyone once, which is
the rounded up value of `num_subjects/ num_per_survey`. This is
equivalent to performing a floor division with `//` and adding 1. Before
the division we need to subtract 1 from the number of subjects to deal with
the case where `num_subjects` is evenly divisible by `num_per_survey`.

```python
num_subjects = 600
num_per_survey = 42
num_surveys = (num_subjects - 1) // num_per_survey + 1

print(num_subjects, 'subjects,', num_per_survey, 'per survey:', num_surveys)
```

```output
600 subjects, 42 per survey: 15
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Strings to Numbers

Where reasonable, `float()` will convert a string to a floating point number,
and `int()` will convert a floating point number to an integer:

```python
print("string to float:", float("3.4"))
print("float to int:", int(3.4))
```

```output
string to float: 3.4
float to int: 3
```

If the conversion doesn't make sense, however, an error message will occur.

```python
print("string to float:", float("Hello world!"))
```

```error
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-5-df3b790bf0a2> in <module>
----> 1 print("string to float:", float("Hello world!"))

ValueError: could not convert string to float: 'Hello world!'
```

Given this information, what do you expect the following program to do?

What does it actually do?

Why do you think it does that?

```python
print("fractional string to int:", int("3.4"))
```

:::::::::::::::  solution

## Solution

What do you expect this program to do? It would not be so unreasonable to expect the Python 3 `int` command to
convert the string "3.4" to 3.4 and an additional type conversion to 3. After all, Python 3 performs a lot of other
magic - isn't that part of its charm?

```python
int("3.4")
```

```output
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-2-ec6729dfccdc> in <module>
----> 1 int("3.4")
ValueError: invalid literal for int() with base 10: '3.4'
```

However, Python 3 throws an error. Why? To be consistent, possibly. If you ask Python to perform two consecutive
typecasts, you must convert it explicitly in code.

```python
int(float("3.4"))
```

```output
3
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Arithmetic with Different Types

Which of the following will return the floating point number `2.0`?
Note: there may be more than one right answer.

```python
first = 1.0
second = "1"
third = "1.1"
```

1. `first + float(second)`
2. `float(second) + float(third)`
3. `first + int(third)`
4. `first + int(float(third))`
5. `int(first) + int(float(third))`
6. `2.0 * second`

:::::::::::::::  solution

## Solution

Answer: 1 and 4



:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Complex Numbers

Python provides complex numbers,
which are written as `1.0+2.0j`.
If `val` is a complex number,
its real and imaginary parts can be accessed using *dot notation*
as `val.real` and `val.imag`.

```python
a_complex_number = 6 + 2j
print(a_complex_number.real)
print(a_complex_number.imag)
```

```output
6.0
2.0
```

1. Why do you think Python uses `j` instead of `i` for the imaginary part?
2. What do you expect `1 + 2j + 3` to produce?
3. What do you expect `4j` to be?  What about `4 j` or `4 + j`?

:::::::::::::::  solution

## Solution

1. Standard mathematics treatments typically use `i` to denote an imaginary number. However, from media reports it
  was an early convention established from electrical engineering that now presents a technically expensive area to
  change. [Stack Overflow provides additional explanation and
  discussion.](https://stackoverflow.com/questions/24812444/why-are-complex-numbers-in-python-denoted-with-j-instead-of-i)
2. `(4+2j)`
3. `4j` and `Syntax Error: invalid syntax`. In the latter cases, `j` is considered a variable and the statement
  depends on if `j` is defined and if so, its assigned value.
  
  

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Every value has a type.
- Use the built-in function `type` to find the type of a value.
- Types control what operations can be done on values.
- Strings can be added and multiplied.
- Strings have a length (but numbers don't).
- Must convert numbers to strings or vice versa when operating on them.
- Can mix integers and floats freely in operations.
- Variables only change value when something is assigned to them.

::::::::::::::::::::::::::::::::::::::::::::::::::


