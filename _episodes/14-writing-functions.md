---
title: "Writing Functions"
teaching: 10
exercises: 15
questions:
- "How can I create my own functions?"
objectives:
- "Explain and identify the difference between function definition and function call."
- "Write a function that takes a small, fixed number of arguments and produces a single result."
keypoints:
- "Break programs down into functions to make them easier to understand."
- "Define a function using `def` with a name, parameters, and a block of code."
- "Defining a function does not run it."
- "Arguments in call are matched to parameters in definition."
- "Functions may return a result to their caller using `return`."
---
## Break programs down into functions to make them easier to understand.

*   Human beings can only keep a few items in working memory at a time.
*   Understand larger/more complicated ideas by understanding and combining pieces.
    *   Components in a machine.
    *   Lemmas when proving theorems.
*   Functions serve the same purpose in programs.
    *   *Encapsulate* complexity so that we can treat it as a single "thing".
*   Also enables *re-use*.
    *   Write one time, use many times.

## Define a function using `def` with a name, parameters, and a block of code.

*   Begin the definition of a new function with `def`.
*   Followed by the name of the function.
    *   Must obey the same rules as variable names.
*   Then *parameters* in parentheses.
    *   Empty parentheses if the function doesn't take any inputs.
    *   We will discuss this in detail in a moment.
*   Then a colon.
*   Then an indented block of code.

~~~
def print_greeting():
    print('Hello!')
~~~
{: .python}

## Defining a function does not run it.

*   Defining a function does not run it.
    *   Like assigning a value to a variable.
*   Must call the function to execute the code it contains.

~~~
print_greeting()
~~~
{: .python}
~~~
Hello!
~~~
{: .output}

## Arguments in call are matched to parameters in definition.

*   Functions are most useful when they can operate on different data.
*   Specify *parameters* when defining a function.
    *   These become variables when the function is executed.
    *   Are assigned the arguments in the call (i.e., the values passed to the function).

~~~
def print_date(year, month, day):
    joined = str(year) + '/' + str(month) + '/' + str(day)
    print(joined)

print_date(1871, 3, 19)
~~~
{: .python}
~~~
1871/3/19
~~~
{: .output}

*   Via [Twitter](https://twitter.com/minisciencegirl/status/693486088963272705):
    `()` contains the ingredients for the function
    while the body contains the recipe.

## Functions may return a result to their caller using `return`.

*   Use `return ...` to give a value back to the caller.
*   May occur anywhere in the function.
*   But functions are easier to understand if `return` occurs:
    *   At the start to handle special cases.
    *   At the very end, with a final result.

~~~
def average(values):
    if len(values) == 0:
        return None
    return sum(values) / len(values)
~~~
{: .python}

~~~
a = average([1, 3, 4])
print('average of actual values:', a)
~~~
{: .python}
~~~
2.6666666666666665
~~~
{: .output}

~~~
print('average of empty list:', average([]))
~~~
{: .python}
~~~
None
~~~
{: .output}

*   Remember: [every function returns something]({{ page.root }}/04-built-in/).
*   A function that doesn't explicitly `return` a value automatically returns `None`.

~~~
result = print_date(1871, 3, 19)
print('result of call is:', result)
~~~
{: .python}
~~~
1871/3/19
result of call is: None
~~~
{: .output}

> ## Identifying Syntax Errors
>
> 1. Read the code below and try to identify what the errors are
>    *without* running it.
> 2. Run the code and read the error message.
>    Is it a `SyntaxError` or an `IndentationError`?
> 3. Fix the error.
> 4. Repeat steps 2 and 3 until you have fixed all the errors.
>
> ~~~
> def another_function
>   print("Syntax errors are annoying.")
>    print("But at least python tells us about them!")
>   print("So they are usually not too hard to fix.")
> ~~~
> {: .python}
>
> > ## Solution
> >
> > ~~~
> > def another_function():
> >   print("Syntax errors are annoying.")
> >   print("But at least Python tells us about them!")
> >   print("So they are usually not too hard to fix.")
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Definition and Use
>
> What does the following program print?
>
> ~~~
> def report(pressure):
>     print('pressure is', pressure)
>
> print('calling', report, 22.5)
> ~~~
> {: .python}
> > ## Solution
> >
> > ~~~
> > calling <function report at 0x7fd128ff1bf8> 22.5
> > ~~~ 
> > {: .output}
> >
> > A function call always needs parenthesis, otherwise you get memory address of the function object. So, if we wanted to call the function named report, and give it the value 22.5 to report on, we could have our function call as follows
> > ~~~
> > print("calling")
> > report(22.5)
> > ~~~
<{: .solution}
{: .challenge}


> ## Order of Operations
>
> The example above:
>
> ~~~
> result = print_date(1871, 3, 19)
> print('result of call is:', result)
> ~~~
> {: .python}
>
> printed:
> ~~~
> 1871/3/19
> result of call is: None
> ~~~
> {: .output}
>
> Explain why the two lines of output appeared in the order they did.
>
> What's wrong in this example?
> ~~~
> result = print_date(1871,3,19)
>
> def print_date(year, month, day):
>    joined = str(year) + '/' + str(month) + '/' + str(day)
>    print(joined)
> ~~~
> {: .python}
> 
{: .challenge}

> ## Encapsulation
>
> Fill in the blanks to create a function that takes a single filename as an argument,
> loads the data in the file named by the argument,
> and returns the minimum value in that data.
>
> ~~~
> import pandas
>
> def min_in_data(____):
>     data = ____
>     return ____
> ~~~
> {: .python}
{: .challenge}

> ## Find the First
>
> Fill in the blanks to create a function that takes a list of numbers as an argument
> and returns the first negative value in the list.
> What does your function do if the list is empty?
>
> ~~~
> def first_negative(values):
>     for v in ____:
>         if ____:
>             return ____
> ~~~
> {: .python}
{: .challenge}

> ## Calling by Name
>
> What does this short program print?
>
> ~~~
> def print_date(year, month, day):
>     joined = str(year) + '/' + str(month) + '/' + str(day)
>     print(joined)
>
> print_date(day=1, month=2, year=2003)
> ~~~
> {: .python}
>
> 1.  When have you seen a function call like this before?
> 2.  When and why is it useful to call functions this way?
> {: .python}
{: .challenge}

> ## Encapsulate of If/Print Block
>
> The code below will run on a label-printer for chicken eggs.  A digital scale will report a chicken egg mass (in grams) to the computer and then the computer will print a label.  
>
> Please re-write the code so that the if-block is folded into a function.
>
> ~~~
>  import random
>  for i in range(10):
>
>     # simulating the mass of a chicken egg
>     # the (random) mass will be 70 +/- 20 grams
>     mass=70+20.0*(2.0*random.random()-1.0)
>
>     print(mass)
>    
>     #egg sizing machinery prints a label
>     if(mass>=85):
>        print("jumbo")
>     elif(mass>=70):
>        print("large")
>     elif(mass<70 and mass>=55):
>        print("medium")
>     else:
>        print("small")
> ~~~
> {: .python}
>
>
> The simplified program  follows.  What function definition will make it functional?
>
> ~~~
>  # revised version
>  import random
>  for i in range(10):
>
>     # simulating the mass of a chicken egg
>     # the (random) mass will be 70 +/- 20 grams
>     mass=70+20.0*(2.0*random.random()-1.0)
>
>     print(mass,print_egg_label(mass))    
>
> ~~~
> {: .python}
>
>
> 1. Create a function definition for `print_egg_label()` that will work with the revised program above.  Note, the function's return value will be signifigant. Sample output might be `71.23 large`.
> 2.  A dirty egg might have a mass of more than 90 grams, and a spoiled or broken egg will probably have a mass that's less than 50 grams.  Modify your `print_egg_label()` function to account for these error conditions. Sample output could be `25 too light, probably spoiled`.
>
{: .challenge}

> ## Encapsulating Data Analysis
>
> Assume that the following code has been executed:
>
> ~~~
> import pandas
>
> df = pandas.read_csv('gapminder_gdp_asia.csv', index_col=0)
> japan = df.ix['Japan']
> ~~~
> {: .python}
>
> 1. Complete the statements below to obtain the average GDP for Japan
>    across the years reported for the 1980s.
>
> ~~~
> year = 1983
> gdp_decade = 'gdpPercap_' + str(year // ____)
> avg = (japan.ix[gdp_decade + ___] + japan.ix[gdp_decade + ___]) / 2
> ~~~
> {: .python}
>
> 2. Abstract the code above into a single function.
>
> ~~~
> def avg_gdp_in_decade(country, continent, year):
>     df = pd.read_csv('gapminder_gdp_'+___+'.csv',delimiter=',',index_col=0)
>     ____
>     ____
>     ____
>     return avg
> ~~~
> {: .python}
>
> 3. How would you generalize this function
>    if you did not know beforehand which specific years occurred as columns in the data?
>    For instance, what if we also had data from years ending in 1 and 9 for each decade?
>    (Hint: use the columns to filter out the ones that correspond to the decade,
>    instead of enumerating them in the code.)
>
> > ## Solution
> >
> > 1.
> >
> > ~~~
> > year = 1983
> > gdp_decade = 'gdpPercap_' + str(year // 10)
> > avg = (japan.ix[gdp_decade + '2'] + japan.ix[gdp_decade + '7']) / 2
> > ~~~
> > {: .python}
> >
> > 2.
> >
> > ~~~
> > def avg_gdp_in_decade(country, continent, year):
> >     df = pd.read_csv('gapminder_gdp_' + continent + '.csv', index_col=0)
> >     c = df.ix[country]
> >     gdp_decade = 'gdpPercap_' + str(year // 10)
> >     avg = (c.ix[gdp_decade + '2'] + c.ix[gdp_decade + '7'])/2
> >     return avg
> > ~~~
> > {: .python}
> >
> > 3. We need to loop over the reported years
> >    to obtain the average for the relevant ones in the data.
> >
> > ~~~
> > def avg_gdp_in_decade(country, continent, year):
> >     df = pd.read_csv('gapminder_gdp_' + continent + '.csv', index_col=0)
> >     c = df.ix[country]
> >     gdp_decade = 'gdpPercap_' + str(year // 10)
> >     total = 0.0
> >     num_years = 0
> >     for yr_header in c.index: # c's index contains reported years
> >         if yr_header.startswith(gdp_decade):
> >             total = total + c.ix[yr_header]
> >             num_years = num_years + 1
> >     return total/num_years
> > ~~~
> > {: .python}
> {: .solution}

> ## Simulating a dynamical system
>
> In mathematics, a [dynamical system](https://en.wikipedia.org/wiki/Dynamical_system) is a system in which a function describes the time dependence of a point in a geometrical space.  Canonical example of a dynamical system is a system called the [logistic map](https://en.wikipedia.org/wiki/Logistic_map).
>
>
> 1. Define a function called `logistic_map` that takes two inputs: `X`, representing the state of the system at time _t_, and a parameter `r`. This function should return a value representing the state of the system at time _t+1_.
>
> 2. Using a `for` loop, iterate the `logistic_map` function defined in part 1 starting from an initial condition of 0.5 for `T=10`, `100`, and `1000` periods. Store the intermediate results in a list so that after the `for` loop terminates you have accumulated a sequence of values representing the state of the logistic map at time _t=0,1,...,T_.
>
> 3. Encapsulate the logic of your `for` loop into a function called `iterate` that takes the initial condition as its first input, the parameter `T` as its second input and the parameter `r` as its third input. The function should return the list of values representing the state of the logistic map at time _t=0,1,...,T_.
>
>
> > ## Solution
> >
> > 1.
> >
> > ~~~
> > def logistic_map(X, r):
> >     return r * X * (1 - X)
> > ~~~
> > {: .python}
> >
> > 2.
> >
> > ~~~
> > initial_condition = 0.5
> > T = 10
> > r = 1.0
> > trajectory = [initial_condition]
> > for t in range(1, T):
> >     trajectory[t] = logistic_map(trajectory[t-1], r)
> > ~~~
> > {: .python}
> >
> > 3.
> > ~~~
> > def iterate(initial_condition, T, r):
> >     trajectory = [initial_condition]
> >     for t in range(1, T):
> >         trajectory[t] = logistic_map(trajectory[t-1], r)
> >     return trajectorys
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}
