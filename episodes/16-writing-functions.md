---
title: Writing Functions
teaching: 10
exercises: 15
---

::::::::::::::::::::::::::::::::::::::: objectives

- Explain and identify the difference between function definition and function call.
- Write a function that takes a small, fixed number of arguments and produces a single result.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can I create my own functions?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Break programs down into functions to make them easier to understand.

- Human beings can only keep a few items in working memory at a time.
- Understand larger/more complicated ideas by understanding and combining pieces.
  - Components in a machine.
  - Lemmas when proving theorems.
- Functions serve the same purpose in programs.
  - *Encapsulate* complexity so that we can treat it as a single "thing".
- Also enables *re-use*.
  - Write one time, use many times.

## Define a function using `def` with a name, parameters, and a block of code.

- Begin the definition of a new function with `def`.
- Followed by the name of the function.
  - Must obey the same rules as variable names.
- Then *parameters* in parentheses.
  - Empty parentheses if the function doesn't take any inputs.
  - We will discuss this in detail in a moment.
- Then a colon.
- Then an indented block of code.

```python
def print_greeting():
    print('Hello!')
    print('The weather is nice today.')
    print('Right?')
```

## Defining a function does not run it.

- Defining a function does not run it.
  - Like assigning a value to a variable.
- Must call the function to execute the code it contains.

```python
print_greeting()
```

```output
Hello!
```

## Arguments in a function call are matched to its defined parameters.

- Functions are most useful when they can operate on different data.
- Specify *parameters* when defining a function.
  - These become variables when the function is executed.
  - Are assigned the arguments in the call (i.e., the values passed to the function).
  - If you don't name the arguments when using them in the call, the arguments will be matched to
    parameters in the order the parameters are defined in the function.

```python
def print_date(year, month, day):
    joined = str(year) + '/' + str(month) + '/' + str(day)
    print(joined)

print_date(1871, 3, 19)
```

```output
1871/3/19
```

Or, we can name the arguments when we call the function, which allows us to
specify them in any order and adds clarity to the call site; otherwise as
one is reading the code they might forget if the second argument is the month
or the day for example.

```python
print_date(month=3, day=19, year=1871)
```

```output
1871/3/19
```

- Via [Twitter](https://twitter.com/minisciencegirl/status/693486088963272705):
  `()` contains the ingredients for the function
  while the body contains the recipe.

## Functions may return a result to their caller using `return`.

- Use `return ...` to give a value back to the caller.
- May occur anywhere in the function.
- But functions are easier to understand if `return` occurs:
  - At the start to handle special cases.
  - At the very end, with a final result.

```python
def average(values):
    if len(values) == 0:
        return None
    return sum(values) / len(values)
```

```python
a = average([1, 3, 4])
print('average of actual values:', a)
```

```output
average of actual values: 2.6666666666666665
```

```python
print('average of empty list:', average([]))
```

```output
average of empty list: None
```

- Remember: [every function returns something](04-built-in.md).
- A function that doesn't explicitly `return` a value automatically returns `None`.

```python
result = print_date(1871, 3, 19)
print('result of call is:', result)
```

```output
1871/3/19
result of call is: None
```

:::::::::::::::::::::::::::::::::::::::  challenge

## Identifying Syntax Errors

1. Read the code below and try to identify what the errors are
  *without* running it.
2. Run the code and read the error message.
  Is it a `SyntaxError` or an `IndentationError`?
3. Fix the error.
4. Repeat steps 2 and 3 until you have fixed all the errors.

```python
def another_function
  print("Syntax errors are annoying.")
   print("But at least python tells us about them!")
  print("So they are usually not too hard to fix.")
```

:::::::::::::::  solution

## Solution

```python
def another_function():
  print("Syntax errors are annoying.")
  print("But at least Python tells us about them!")
  print("So they are usually not too hard to fix.")
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Definition and Use

What does the following program print?

```python
def report(pressure):
    print('pressure is', pressure)

print('calling', report, 22.5)
```

:::::::::::::::  solution

## Solution

```output
calling <function report at 0x7fd128ff1bf8> 22.5
```

A function call always needs parenthesis, otherwise you get memory address of the function object. So, if we wanted to call the function named report, and give it the value 22.5 to report on, we could have our function call as follows

```python
print("calling")
report(22.5)
```

```output
calling
pressure is 22.5
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Order of Operations

1. What's wrong in this example?
  
  ```python
  result = print_time(11, 37, 59)
  
  def print_time(hour, minute, second):
     time_string = str(hour) + ':' + str(minute) + ':' + str(second)
     print(time_string)
  ```

2. After fixing the problem above, explain why running this example code:
  
  ```python
  result = print_time(11, 37, 59)
  print('result of call is:', result)
  ```
  
  gives this output:
  
  ```output
  11:37:59
  result of call is: None
  ```

3. Why is the result of the call `None`?

:::::::::::::::  solution

## Solution

1. The problem with the example is that the function `print_time()` is defined *after* the call to the function is made. Python
  doesn't know how to resolve the name `print_time` since it hasn't been defined yet and will raise a `NameError` e.g.,
  `NameError: name 'print_time' is not defined`

2. The first line of output `11:37:59` is printed by the first line of code, `result = print_time(11, 37, 59)` that binds the value
  returned by invoking `print_time` to the variable `result`. The second line is from the second print call to print the contents
  of the `result` variable.

3. `print_time()` does not explicitly `return` a value, so it automatically returns `None`.

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Encapsulation

Fill in the blanks to create a function that takes a single filename as an argument,
loads the data in the file named by the argument,
and returns the minimum value in that data.

```python
import pandas as pd

def min_in_data(____):
    data = ____
    return ____
```

:::::::::::::::  solution

## Solution

```python
import pandas as pd

def min_in_data(filename):
    data = pd.read_csv(filename)
    return data.min()
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Find the First

Fill in the blanks to create a function that takes a list of numbers as an argument
and returns the first negative value in the list.
What does your function do if the list is empty? What if the list has no negative numbers?

```python
def first_negative(values):
    for v in ____:
        if ____:
            return ____
```

:::::::::::::::  solution

## Solution

```python
def first_negative(values):
    for v in values:
        if v < 0:
            return v
```

If an empty list or a list with all positive values is passed to this function, it returns `None`:

```python
my_list = []
print(first_negative(my_list))
```

```output
None
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Calling by Name

Earlier we saw this function:

```python
def print_date(year, month, day):
    joined = str(year) + '/' + str(month) + '/' + str(day)
    print(joined)
```

We saw that we can call the function using *named arguments*, like this:

```python
print_date(day=1, month=2, year=2003)
```

1. What does `print_date(day=1, month=2, year=2003)` print?
2. When have you seen a function call like this before?
3. When and why is it useful to call functions this way?

:::::::::::::::  solution

## Solution

1. `2003/2/1`
2. We saw examples of using *named arguments* when working with the pandas library. For example, when reading in a dataset
  using `data = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')`, the last argument `index_col` is a
  named argument.
3. Using named arguments can make code more readable since one can see from the function call what name the different arguments
  have inside the function. It can also reduce the chances of passing arguments in the wrong order, since by using named arguments
  the order doesn't matter.
  
  

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Encapsulation of an If/Print Block

The code below will run on a label-printer for chicken eggs.  A digital scale will report a chicken egg mass (in grams)
to the computer and then the computer will print a label.

```python
import random
for i in range(10):

    # simulating the mass of a chicken egg
    # the (random) mass will be 70 +/- 20 grams
    mass = 70 + 20.0 * (2.0 * random.random() - 1.0)

    print(mass)

    # egg sizing machinery prints a label
    if mass >= 85:
        print("jumbo")
    elif mass >= 70:
        print("large")
    elif mass < 70 and mass >= 55:
        print("medium")
    else:
        print("small")
```

The if-block that classifies the eggs might be useful in other situations,
so to avoid repeating it, we could fold it into a function, `get_egg_label()`.
Revising the program to use the function would give us this:

```python
# revised version
import random
for i in range(10):

    # simulating the mass of a chicken egg
    # the (random) mass will be 70 +/- 20 grams
    mass = 70 + 20.0 * (2.0 * random.random() - 1.0)

    print(mass, get_egg_label(mass))

```

1. Create a function definition for `get_egg_label()` that will work with the revised program above.  Note that the `get_egg_label()` function's return value will be important. Sample output from the above program would be `71.23 large`.
2. A dirty egg might have a mass of more than 90 grams, and a spoiled or broken egg will probably have a mass that's less than 50 grams.  Modify your `get_egg_label()` function to account for these error conditions. Sample output could be `25 too light, probably spoiled`.

:::::::::::::::  solution

## Solution

```python
def get_egg_label(mass):
    # egg sizing machinery prints a label
    egg_label = "Unlabelled"
    if mass >= 90:
        egg_label = "warning: egg might be dirty"
    elif mass >= 85:
        egg_label = "jumbo"
    elif mass >= 70:
        egg_label = "large"
    elif mass < 70 and mass >= 55:
        egg_label = "medium"
    elif mass < 50:
        egg_label = "too light, probably spoiled"
    else:
        egg_label = "small"
    return egg_label
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Encapsulating Data Analysis

Assume that the following code has been executed:

```python
import pandas as pd

data_asia = pd.read_csv('data/gapminder_gdp_asia.csv', index_col=0)
japan = data_asia.loc['Japan']
```

1. Complete the statements below to obtain the average GDP for Japan
  across the years reported for the 1980s.
  
  ```python
  year = 1983
  gdp_decade = 'gdpPercap_' + str(year // ____)
  avg = (japan.loc[gdp_decade + ___] + japan.loc[gdp_decade + ___]) / 2
  ```

2. Abstract the code above into a single function.
  
  ```python
  def avg_gdp_in_decade(country, continent, year):
      data_countries = pd.read_csv('data/gapminder_gdp_'+___+'.csv',delimiter=',',index_col=0)
      ____
      ____
      ____
      return avg
  ```

3. How would you generalize this function
  if you did not know beforehand which specific years occurred as columns in the data?
  For instance, what if we also had data from years ending in 1 and 9 for each decade?
  (Hint: use the columns to filter out the ones that correspond to the decade,
  instead of enumerating them in the code.)

:::::::::::::::  solution

## Solution

1. The average GDP for Japan across the years reported for the 1980s is computed with:
  
  ```python
  year = 1983
  gdp_decade = 'gdpPercap_' + str(year // 10)
  avg = (japan.loc[gdp_decade + '2'] + japan.loc[gdp_decade + '7']) / 2
  ```

2. That code as a function is:
  
  ```python
  def avg_gdp_in_decade(country, continent, year):
      data_countries = pd.read_csv('data/gapminder_gdp_' + continent + '.csv', index_col=0)
      c = data_countries.loc[country]
      gdp_decade = 'gdpPercap_' + str(year // 10)
      avg = (c.loc[gdp_decade + '2'] + c.loc[gdp_decade + '7'])/2
      return avg
  ```

3. To obtain the average for the relevant years, we need to loop over them:
  
  ```python
  def avg_gdp_in_decade(country, continent, year):
      data_countries = pd.read_csv('data/gapminder_gdp_' + continent + '.csv', index_col=0)
      c = data_countries.loc[country]
      gdp_decade = 'gdpPercap_' + str(year // 10)
      total = 0.0
      num_years = 0
      for yr_header in c.index: # c's index contains reported years
          if yr_header.startswith(gdp_decade):
              total = total + c.loc[yr_header]
              num_years = num_years + 1
      return total/num_years
  ```

The function can now be called by:

```python
avg_gdp_in_decade('Japan','asia',1983)
```

```output
20880.023800000003
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Simulating a dynamical system

In mathematics, a [dynamical system](https://en.wikipedia.org/wiki/Dynamical_system) is a system
in which a function describes the time dependence of a point in a geometrical space. A canonical
example of a dynamical system is the [logistic map](https://en.wikipedia.org/wiki/Logistic_map),
a growth model that computes a new population density (between  0 and 1) based on the current
density. In the model, time takes discrete values 0, 1, 2, ...

1. Define a function called `logistic_map` that takes two inputs: `x`, representing the current
  population (at time `t`), and a parameter `r = 1`. This function should return a value
  representing the state of the system (population) at time `t + 1`, using the mapping function:
  
  `f(t+1) = r * f(t) * [1 - f(t)]`

2. Using a `for` or `while` loop, iterate the `logistic_map` function defined in part 1, starting
  from an initial population of 0.5, for a period of time `t_final = 10`. Store the intermediate
  results in a list so that after the loop terminates you have accumulated a sequence of values
  representing the state of the logistic map at times `t = [0,1,...,t_final]` (11 values in total).
  Print this list to see the evolution of the population.

3. Encapsulate the logic of your loop into a function called `iterate` that takes the initial
  population as its first input, the parameter `t_final` as its second input and the parameter
  `r` as its third input. The function should return the list of values representing the state of
  the logistic map at times `t = [0,1,...,t_final]`. Run this function for periods `t_final = 100`
  and `1000` and print some of the values. Is the population trending toward a steady state?

:::::::::::::::  solution

## Solution

1.
  ```python
  def logistic_map(x, r):
      return r * x * (1 - x)
  ```

2.
  ```python
  initial_population = 0.5
  t_final = 10
  r = 1.0
  population = [initial_population]

  for t in range(t_final):
      population.append( logistic_map(population[t], r) )
  ```

3.
  ```python
  def iterate(initial_population, t_final, r):
      population = [initial_population]
      for t in range(t_final):
          population.append( logistic_map(population[t], r) )
      return population
  
  for period in (10, 100, 1000):
      population = iterate(0.5, period, 1)
      print(population[-1])
  ```

  ```output
  0.06945089389714401
  0.009395779870614648
  0.0009913908614406382
  ```
  
  The population seems to be approaching zero.
  
  

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::  callout

## Using Functions With Conditionals in Pandas

Functions will often contain conditionals.  Here is a short example that
will indicate which quartile the argument is in based on hand-coded values
for the quartile cut points.

```python
def calculate_life_quartile(exp):
    if exp < 58.41:
        # This observation is in the first quartile
        return 1
    elif exp >= 58.41 and exp < 67.05:
        # This observation is in the second quartile
       return 2
    elif exp >= 67.05 and exp < 71.70:
        # This observation is in the third quartile
       return 3
    elif exp >= 71.70:
        # This observation is in the fourth quartile
       return 4
    else:
        # This observation has bad data
       return None

calculate_life_quartile(62.5)
```

```output
2
```

That function would typically be used within a `for` loop, but Pandas has
a different, more efficient way of doing the same thing, and that is by
*applying* a function to a dataframe or a portion of a dataframe.  Here
is an example, using the definition above.

```python
data = pd.read_csv('data/gapminder_all.csv')
data['life_qrtl'] = data['lifeExp_1952'].apply(calculate_life_quartile)
```

There is a lot in that second line, so let's take it piece by piece.
On the right side of the `=` we start with `data['lifeExp']`, which is the
column in the dataframe called `data` labeled `lifExp`.  We use the
`apply()` to do what it says, apply the `calculate_life_quartile` to the
value of this column for every row in the dataframe.


::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Break programs down into functions to make them easier to understand.
- Define a function using `def` with a name, parameters, and a block of code.
- Defining a function does not run it.
- Arguments in a function call are matched to its defined parameters.
- Functions may return a result to their caller using `return`.

::::::::::::::::::::::::::::::::::::::::::::::::::


