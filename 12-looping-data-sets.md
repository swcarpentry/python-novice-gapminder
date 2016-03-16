---
layout: lesson
subtitle: Looping Over Data Sets
teaching: 5
exercises: 15
---
> ## Learning Objectives
>
> * Learner will be able to read and write globbing expressions that match sets of files.
> * Learner will use `glob` to create lists of files.
> * Learner will write `for` loops to perform operations on files
>   given their names in a list.
{: .objectives}

FIXME: lesson content - build up to showing how to create one plot per file for multiple files.

## Finding Lots of Files
{: .challenge}

Explain in simple terms what set of files is matched by `glob.glob('*/*.csv')`.

## Determining Matches
{: .challenge}

Which of these files is *not* matched by the expression `glob.glob('data/*as*.csv')`?

1. `data/gapminder_gdp_africa.csv`
2. `data/gapminder_gdp_americas.csv`
3. `data/gapminder_gdp_asia.csv`
4. 1 and 2 are not matched.

## Maximum File Size
{: .challenge}

Modify this program so that it prints the number of records in
the file that has the most records.

~~~
largest = ____
for filename in glob.glob('*.csv'):
    largest = ____
print('largest file has', largest, 'records')
~~~
{: .python}

## Calculating Averages
{: .challenge}

FIXME: show how to calculate average GDP per capita for each region in 2002.
