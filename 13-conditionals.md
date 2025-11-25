---
title: Conditionals
teaching: 10
exercises: 15
---

::::::::::::::::::::::::::::::::::::::: objectives

- Correctly write programs that use if and else statements and simple Boolean expressions (without logical operators).
- Trace the execution of unnested conditionals and conditionals inside loops.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can programs do different things for different data?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Use `if` statements to control whether or not a block of code is executed.

- An `if` statement (more properly called a *conditional* statement)
  controls whether some block of code is executed or not.
- Structure is similar to a `for` statement:
  - First line opens with `if` and ends with a colon
  - Body containing one or more statements is indented (usually by 4 spaces)

```python
mass = 3.54
if mass > 3.0:
    print(mass, 'is large')

mass = 2.07
if mass > 3.0:
    print (mass, 'is large')
```

```output
3.54 is large
```

## Conditionals are often used inside loops.

- Not much point using a conditional when we know the value (as above).
- But useful when we have a collection to process.

```python
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 3.0:
        print(m, 'is large')
```

```output
3.54 is large
9.22 is large
```

## Use `else` to execute a block of code when an `if` condition is *not* true.

- `else` can be used following an `if`.
- Allows us to specify an alternative to execute when the `if` *branch* isn't taken.

```python
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 3.0:
        print(m, 'is large')
    else:
        print(m, 'is small')
```

```output
3.54 is large
2.07 is small
9.22 is large
1.86 is small
1.71 is small
```

## Use `elif` to specify additional tests.

- May want to provide several alternative choices, each with its own test.
- Use `elif` (short for "else if") and a condition to specify these.
- Always associated with an `if`.
- Must come before the `else` (which is the "catch all").

```python
masses = [3.54, 2.07, 9.22, 1.86, 1.71]
for m in masses:
    if m > 9.0:
        print(m, 'is HUGE')
    elif m > 3.0:
        print(m, 'is large')
    else:
        print(m, 'is small')
```

```output
3.54 is large
2.07 is small
9.22 is HUGE
1.86 is small
1.71 is small
```

## Conditions are tested once, in order.

- Python steps through the branches of the conditional in order, testing each in turn.
- So ordering matters.

```python
grade = 85
if grade >= 90:
    print('grade is A')
elif grade >= 80:
    print('grade is B')
elif grade >= 70:
    print('grade is C')
```

```output
grade is B
```

- Does *not* automatically go back and re-evaluate if values change.

```python
velocity = 10.0
if velocity > 20.0:
    print('moving too fast')
else:
    print('adjusting velocity')
    velocity = 50.0
```

```output
adjusting velocity
```

- Often use conditionals in a loop to "evolve" the values of variables.

```python
velocity = 10.0
for i in range(5): # execute the loop 5 times
    print(i, ':', velocity)
    if velocity > 20.0:
        print('moving too fast')
        velocity = velocity - 5.0
    else:
        print('moving too slow')
        velocity = velocity + 10.0
print('final velocity:', velocity)
```

```output
0 : 10.0
moving too slow
1 : 20.0
moving too slow
2 : 30.0
moving too fast
3 : 25.0
moving too fast
4 : 20.0
moving too slow
final velocity: 30.0
```

## Create a table showing variables' values to trace a program's execution.

<table>
  <tr>   <td><strong>i</strong></td>   <td>0</td>   <td>.</td>   <td>1</td>   <td>.</td>   <td>2</td>   <td>.</td>   <td>3</td>   <td>.</td>   <td>4</td>   <td>.</td>
  </tr>
  <tr>   <td><strong>velocity</strong></td>   <td>10.0</td>   <td>20.0</td>   <td>.</td>   <td>30.0</td>   <td>.</td>   <td>25.0</td>   <td>.</td>   <td>20.0</td>   <td>.</td>   <td>30.0</td>
  </tr>
</table>

- The program must have a `print` statement *outside* the body of the loop
  to show the final value of `velocity`,
  since its value is updated by the last iteration of the loop.

:::::::::::::::::::::::::::::::::::::::::  callout

## Compound Relations Using `and`, `or`, and Parentheses

Often, you want some combination of things to be true.  You can combine
relations within a conditional using `and` and `or`.  Continuing the example
above, suppose you have

```python
mass     = [ 3.54,  2.07,  9.22,  1.86,  1.71]
velocity = [10.00, 20.00, 30.00, 25.00, 20.00]

i = 0
for i in range(5):
    if mass[i] > 5 and velocity[i] > 20:
        print("Fast heavy object.  Duck!")
    elif mass[i] > 2 and mass[i] <= 5 and velocity[i] <= 20:
        print("Normal traffic")
    elif mass[i] <= 2 and velocity[i] <= 20:
        print("Slow light object.  Ignore it")
    else:
        print("Whoa!  Something is up with the data.  Check it")
```

Just like with arithmetic, you can and should use parentheses whenever there
is possible ambiguity.  A good general rule is to *always* use parentheses
when mixing `and` and `or` in the same condition.  That is, instead of:

```python
if mass[i] <= 2 or mass[i] >= 5 and velocity[i] > 20:
```

write one of these:

```python
if (mass[i] <= 2 or mass[i] >= 5) and velocity[i] > 20:
if mass[i] <= 2 or (mass[i] >= 5 and velocity[i] > 20):
```

so it is perfectly clear to a reader (and to Python) what you really mean.


::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Tracing Execution

What does this program print?

```python
pressure = 71.9
if pressure > 50.0:
    pressure = 25.0
elif pressure <= 50.0:
    pressure = 0.0
print(pressure)
```

:::::::::::::::  solution

## Solution

```output
25.0
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Trimming Values

Fill in the blanks so that this program creates a new list
containing zeroes where the original list's values were negative
and ones where the original list's values were positive.

```python
original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
result = ____
for value in original:
    if ____:
        result.append(0)
    else:
        ____
print(result)
```

```output
[0, 1, 1, 1, 0, 1]
```

:::::::::::::::  solution

## Solution

```python
original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
result = []
for value in original:
    if value < 0.0:
        result.append(0)
    else:
        result.append(1)
print(result)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Processing Small Files

Modify this program so that it only processes files with fewer than 50 records.

```python
import glob
import pandas as pd
for filename in glob.glob('data/*.csv'):
    contents = pd.read_csv(filename)
    ____:
        print(filename, len(contents))
```

:::::::::::::::  solution

## Solution

```python
import glob
import pandas as pd
for filename in glob.glob('data/*.csv'):
    contents = pd.read_csv(filename)
    if len(contents) < 50:
        print(filename, len(contents))
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Initializing

Modify this program so that it finds the largest and smallest values in the list
no matter what the range of values originally is.

```python
values = [...some test data...]
smallest, largest = None, None
for v in values:
    if ____:
        smallest, largest = v, v
    ____:
        smallest = min(____, v)
        largest = max(____, v)
print(smallest, largest)
```

What are the advantages and disadvantages of using this method
to find the range of the data?

:::::::::::::::  solution

## Solution

```python
values = [-2,1,65,78,-54,-24,100]
smallest, largest = None, None
for v in values:
    if smallest is None and largest is None:
        smallest, largest = v, v
    else:
        smallest = min(smallest, v)
        largest = max(largest, v)
print(smallest, largest)
```

If you wrote `== None` instead of `is None`, that works too, but Python programmers always
write `is None` because of the special way `None` works in the language.

It can be argued that an advantage of using this method would be to make the code more readable.
However, a disadvantage is that this code is not efficient because within each iteration of the
`for` loop statement, there are two more loops that run over two numbers each (the `min` and
`max` functions). It would be more efficient to iterate over each number just once:

```python
values = [-2,1,65,78,-54,-24,100]
smallest, largest = None, None
for v in values:
    if smallest is None or v < smallest:
        smallest = v
    if largest is None or v > largest:
        largest = v
print(smallest, largest)
```

Now we have one loop, but four comparison tests. There are two ways we could improve it further:
either use fewer comparisons in each iteration, or use two loops that each contain only one
comparison test. The simplest solution is often the best:

```python
values = [-2,1,65,78,-54,-24,100]
smallest = min(values)
largest = max(values)
print(smallest, largest)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Use `if` statements to control whether or not a block of code is executed.
- Conditionals are often used inside loops.
- Use `else` to execute a block of code when an `if` condition is *not* true.
- Use `elif` to specify additional tests.
- Conditions are tested once, in order.
- Create a table showing variables' values to trace a program's execution.

::::::::::::::::::::::::::::::::::::::::::::::::::


