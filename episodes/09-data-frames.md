---
layout: episode
title: "Pandas Data Frames"
teaching: 10
exercises: 10
questions:
- "How can do statistical analysis of tabular data?"
objectives:
- "Select individual values from a Pandas data frame."
- "Select entire rows or entire columns from a data frame."
- "Select a subset of both rows and columns from a data frame in a single operation."
- "Select a subset of a data frame by a single Boolean criterion."
keypoints:
- FIXME
---
- Selecting individual values
- label-based vs. index based

~~~
data_frame = pandas.read_csv('data/gapminder_gdp_europe.csv', index_col="country")

data_frame.ix["Albania", "gdpPercap_1952"]
data_frame.ix[0, 0]
~~~
{: .source}

> ## Selection of Individual Values
> 
> Assume Pandas has been imported into your notebook
> and the Gapminder GDP data for Europe has been loaded:
> 
> ~~~
> import pandas
> 
> df = pandas.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
> ~~~
> {: .source}
> 
> Write an expression to find the Per Capita GDP of Serbia in 2007.
{: .challenge}

- Selecting a row
- Colon by itself means "all of", i. e. "all columns" or "all rows"

~~~
data_frame.ix["Albania", :]
data_frame.ix["Albania"]
~~~
{: .source}

- Selecting a column

~~~
data_frame.ix[:, "gdpPercap_1952"]
data_frame["gdpPercap_1952"]
data_frame.gdpPercap_1952
~~~
{: .source}

I can get multiple columns or rows using DataFrame.ix and the colon to indicate
slicing.

~~~
# rows
data_frame.ix["Italy":"Poland"]

# columns
data_frame.ix[:, "gdpPercap_1962":"gdpPercap_1972"]

# slicing both ways
data_frame.ix["Italy":"Poland", "gdpPercap_1962":"gdpPercap_1972"]
~~~
{: .source}

Will the two snippets below produce the same output?  Why or why not?  How many
data entries will be in the result?

~~~ 
data_frame.ix[0:2, 0:2]
data_frame.ix["Albania":"Belgium", "gdpPercap_1952":"gdpPercap_1962"]
~~~ 
{: .source}

In the above code, we discover that **slicing using indexes is inclusive at both
ends**, which differs from typical python behavior, where slicing indicates
everything up to but not including the final index.  However, if we use integers
when our DataFrame is indexed by something else, slicing follows typical
pythonic behavior.

- Subsets using boolean criteria
- All values greater than 10000, everything else is NaN

~~~ 
df[df > 10000]
~~~ 
{: .source}

- All rows corresponding to 1952 GDP > 10000

~~~ 
df[df["gdpPercap_1952"] > 10000]
~~~
{: .source}

> ## Make Americas.csv great again
> Note that the Americas data is incorrect.  Take a look:
> 
> ~~~ 
> df = pandas.load_csv("gapminder_gdp_americas.csv", index_col="country")
> ~~~
> {: .source}
> 
> Fix it!
> Use the following code to save a dataframe to csv
> DataFrame.to_csv(filename)
>
> ~~~ 
> df = pandas.load_csv("gapminder_gdp_all.csv", index_col="country")
> americas = df[df["continent"] == "Americas"]
> americas = americas.drop("Puerto Rico")
> americas = americas.drop("continent", axis = 1)
> americas.to_csv("gapminder_gdp_americas_fixed.csv")
> ~~~
> {: .source}
{: .challenge}

## More operations

- Minima

~~~
df = pandas.load_csv("gapminder_gdp_europe.csv", index_col="country")
df.min()
df.idxmin()
~~~
{: .source}

- Maxima

~~~
df = pandas.load_csv("gapminder_gdp_europe.csv", index_col="country")
df.max()
df.idxmax()
~~~
{: .source}

> ## Selection of Rows
> 
> Assume Pandas has been imported into your notebook and the Gapminder GDP data
> for Europe has been loaded:
> 
> ~~~ 
> import pandas data = pandas.read_csv('data/gapminder_gdp_europe.csv') 
> ~~~
> {: .source}
> 
> Write an expression to select each of the following:
> 
> 1. GDP per capita for all countries in 1982.  2. GDP per capita for Denmark
> for all years.  3. GDP per capita for all countries for years *after* 1985.
> 4. GDP per capita for each country in 2007 as a multiple of GDP per capita for
> that country in 1952.
{: .challenge}

> ## Interpretation
> 
> Poland's borders have been stable since 1945, but changed several times in the
> years before then.  How would you handle this if you were creating a table of
> GDP per capita for Poland in the Twentieth Century?
{: .challenge}
