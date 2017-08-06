---
title: "Looping Over Data Sets"
teaching: 5
exercises: 10
questions:
- "How can I process many data sets with a single command?"
objectives:
- "Be able to read and write globbing expressions that match sets of files."
- "Use glob to create lists of files."
- "Write for loops to perform operations on files given their names in a list."
keypoints:
- "Use a `for` loop to process files given a list of their names."
- "Use `glob.glob` to find sets of files whose names match a pattern."
- "Use `glob` and `for` to process batches of files."
---

## Use a `for` loop to process files given a list of their names.

*   A filename is just a character string.
*   And lists can contain character strings.

~~~
import pandas
for filename in ['data/gapminder_gdp_africa.csv', 'data/gapminder_gdp_asia.csv']:
    data = pandas.read_csv(filename, index_col='country')
    print(filename, data.min())
~~~
{: .python}
~~~
data/gapminder_gdp_africa.csv gdpPercap_1952    298.846212
gdpPercap_1957    335.997115
gdpPercap_1962    355.203227
gdpPercap_1967    412.977514
⋮ ⋮ ⋮
gdpPercap_1997    312.188423
gdpPercap_2002    241.165877
gdpPercap_2007    277.551859
dtype: float64
data/gapminder_gdp_asia.csv gdpPercap_1952    331
gdpPercap_1957    350
gdpPercap_1962    388
gdpPercap_1967    349
⋮ ⋮ ⋮
gdpPercap_1997    415
gdpPercap_2002    611
gdpPercap_2007    944
dtype: float64
~~~
{: .output}

## Use `glob.glob` to find sets of files whose names match a pattern.

*   In Unix, the term "globbing" means "matching a set of files with a pattern".
*   The most common patterns are:
    *   `*` meaning "match zero or more characters"
    *   `?` meaning "match exactly one character"
*   Python contains the `glob` library to provide pattern matching functionality
*   The `glob` library contains a function also called `glob` to match file patterns
*   E.g., `glob.glob('*.txt')` matches all files in the current directory 
    whose names end with `.txt`.
*   Result is a (possibly empty) list of character strings.

~~~
import glob
print('all csv files in data directory:', glob.glob('data/*.csv'))
~~~
{: .python}
~~~
all csv files in data directory: ['data/gapminder_all.csv', 'data/gapminder_gdp_africa.csv', \
'data/gapminder_gdp_americas.csv', 'data/gapminder_gdp_asia.csv', 'data/gapminder_gdp_europe.csv', \
'data/gapminder_gdp_oceania.csv']
~~~
{: .output}

~~~
print('all PDB files:', glob.glob('*.pdb'))
~~~
{: .python}
~~~
all PDB files: []
~~~
{: .output}

## Use `glob` and `for` to process batches of files.

*   Helps a lot if the files are named and stored systematically and consistently
    so that simple patterns will find the right data.

~~~
for filename in glob.glob('data/*.csv'):
    data = pandas.read_csv(filename)
    print(filename, data['gdpPercap_1952'].min())
~~~
{: .python}
~~~
data/gapminder_all.csv 298.8462121
data/gapminder_gdp_africa.csv 298.8462121
data/gapminder_gdp_americas.csv 1397.717137
data/gapminder_gdp_asia.csv 331.0
data/gapminder_gdp_europe.csv 973.5331948
data/gapminder_gdp_oceania.csv 10039.59564
~~~
{: .output}

*   This includes all data, as well as per-region data.
*   Use a more specific pattern in the exercises to exclude the whole data set.
*   But note that the minimum of the entire data set is also the minimum of one of the data sets,
    which is a nice check on correctness.

> ## Determining Matches
>
> Which of these files is *not* matched by the expression `glob.glob('data/*as*.csv')`?
>
> 1. `data/gapminder_gdp_africa.csv`
> 2. `data/gapminder_gdp_americas.csv`
> 3. `data/gapminder_gdp_asia.csv`
> 4. 1 and 2 are not matched.
>
> > ## Solution
> >
> > 1 is not matched by the regular expresion.
> {: .solution}
{: .challenge}

> ## Minimum File Size
>
> Modify this program so that it prints the number of records in
> the file that has the fewest records.
>
> ~~~
> import pandas
> fewest = ____
> for filename in glob.glob('data/*.csv'):
>     dataframe = pandas.____(filename)
>     fewest = min(____, dataframe.shape[0]) 
> print('smallest file has', fewest, 'records')
> ~~~
> {: .python}
> Notice that the shape method returns a tuple with 
> the number of rows and columns of the data frame.
>
> > ## Solution
> > ~~~
> > import pandas
> > fewest = 0
> > for filename in glob.glob('data/*.csv'):
> >     dataframe = pandas.read_csv(filename)
> >     fewest = min(fewest , dataframe.shape[0]) 
> > print('smallest file has', fewest, 'records')
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Comparing Data
>
> Write a program that reads in the regional data sets
> and plots the average GDP per capita for each region over time
> in a single chart.
{: .challenge}
