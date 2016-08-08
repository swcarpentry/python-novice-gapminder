---
title: "Pandas Data Frames"
teaching: 10
exercises: 10
questions:
- "How can I do statistical analysis of tabular data?"
objectives:
- "Select individual values from a Pandas data frame."
- "Select entire rows or entire columns from a data frame."
- "Select a subset of both rows and columns from a data frame in a single operation."
- "Select a subset of a data frame by a single Boolean criterion."
keypoints:
- "Use `DataFrame.ix[..., ...]` to select values by location."
- "Use `:` on its own to mean all columns or all rows."
- "Select multiple columns or rows using `DataFrame.ix` and a named slice."
- "Result of slicing can be used in further operations."
- "Use comparisons to select data based on value."
- "Select values or NaN using a Boolean mask."
---
## Use `DataFrame.ix[..., ...]` to select values by location.

*   Can specify location by name or by numerical index.

~~~
data = pandas.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
print(data.ix["Albania", "gdpPercap_1952"])
print(data.ix[0, 0])
~~~
{: .python}
~~~
1601.056136
1601.056136
~~~
{: .output}

## Use `:` on its own to mean all columns or all rows.

*   Just like Python's usual slicing notation.

~~~
print(data.ix["Albania", :])
~~~
{: .python}
~~~
gdpPercap_1952    1601.056136
gdpPercap_1957    1942.284244
gdpPercap_1962    2312.888958
gdpPercap_1967    2760.196931
gdpPercap_1972    3313.422188
gdpPercap_1977    3533.003910
gdpPercap_1982    3630.880722
gdpPercap_1987    3738.932735
gdpPercap_1992    2497.437901
gdpPercap_1997    3193.054604
gdpPercap_2002    4604.211737
gdpPercap_2007    5937.029526
Name: Albania, dtype: float64
~~~
{: .output}

*   Would get the same result printing `data.ix["Albania"]` (without a second index).

~~~
print(data.ix[:, "gdpPercap_1952"])
~~~
{: .python}
~~~
country
Albania                    1601.056136
Austria                    6137.076492
Belgium                    8343.105127
⋮ ⋮ ⋮
Switzerland               14734.232750
Turkey                     1969.100980
United Kingdom             9979.508487
Name: gdpPercap_1952, dtype: float64
~~~
{: .output}

*   Would get the same result printing `data["gdpPercap_1952"]`
*   Also get the same result printing `data.gdpPercap_1952` (since it's a column name)

## Select multiple columns or rows using `DataFrame.ix` and a named slice.

~~~
print(data.ix['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972'])
~~~
{: .python}
~~~
             gdpPercap_1962  gdpPercap_1967  gdpPercap_1972
country
Italy           8243.582340    10022.401310    12269.273780
Montenegro      4649.593785     5907.850937     7778.414017
Netherlands    12790.849560    15363.251360    18794.745670
Norway         13450.401510    16361.876470    18965.055510
Poland          5338.752143     6557.152776     8006.506993
~~~
{: .output}

In the above code, we discover that **slicing using indexes is inclusive at both
ends**, which differs from typical python behavior, where slicing indicates
everything up to but not including the final index.  However, if we use integers
when our DataFrame is indexed by something else, slicing follows typical
pythonic behavior.

## Result of slicing can be used in further operations.

*   Usually don't just print a slice.
*   All the statistical operators that work on entire data frames
    work the same way on slices.

~~~
print(data.ix['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972'].max())
~~~
{: .python}
~~~
gdpPercap_1962    13450.40151
gdpPercap_1967    16361.87647
gdpPercap_1972    18965.05551
dtype: float64
~~~
{: .output}

~~~
print(data.ix['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972'].min())
~~~
{: .python}
~~~
gdpPercap_1962    4649.593785
gdpPercap_1967    5907.850937
gdpPercap_1972    7778.414017
dtype: float64
~~~
{: .output}

## Use comparisons to select data based on value.

*   Comparison is applied element by element.
*   Returns a similarly-shaped data frame of `True` and `False`.

~~~
# Use a subset of data to keep output readable.
subset = data.ix['Italy':'Poland', 'gdpPercap_1962':'gdpPercap_1972']
print('Subset of data:\n', subset)

# Which values were greater than 10000 ?
print('\nWhere are values large?\n', subset > 10000)
~~~
{: .python}
~~~
Subset of data:
             gdpPercap_1962  gdpPercap_1967  gdpPercap_1972
country
Italy           8243.582340    10022.401310    12269.273780
Montenegro      4649.593785     5907.850937     7778.414017
Netherlands    12790.849560    15363.251360    18794.745670
Norway         13450.401510    16361.876470    18965.055510
Poland          5338.752143     6557.152776     8006.506993

Where are values large?
            gdpPercap_1962 gdpPercap_1967 gdpPercap_1972
country
Italy                False           True           True
Montenegro           False          False          False
Netherlands           True           True           True
Norway                True           True           True
Poland               False          False          False
~~~
{: .output}

## Select values or NaN using a Boolean mask.

*   A frame full of Booleans is sometimes called a *mask* because of how it can be used.

~~~
mask = subset > 10000
print(subset[mask])
~~~
{: .python}
~~~
             gdpPercap_1962  gdpPercap_1967  gdpPercap_1972
country
Italy                   NaN     10022.40131     12269.27378
Montenegro              NaN             NaN             NaN
Netherlands     12790.84956     15363.25136     18794.74567
Norway          13450.40151     16361.87647     18965.05551
Poland                  NaN             NaN             NaN
~~~
{: .output}

*   Get the value where the mask is true, and NaN (Not a Number) where it is false.
*   Useful because NaNs are ignored by operations like max, min, average, etc.

~~~
print(subset[subset > 10000].describe())
~~~
{: .python}
~~~
       gdpPercap_1962  gdpPercap_1967  gdpPercap_1972
count        2.000000        3.000000        3.000000
mean     13120.625535    13915.843047    16676.358320
std        466.373656     3408.589070     3817.597015
min      12790.849560    10022.401310    12269.273780
25%      12955.737547    12692.826335    15532.009725
50%      13120.625535    15363.251360    18794.745670
75%      13285.513523    15862.563915    18879.900590
max      13450.401510    16361.876470    18965.055510
~~~
{: .output}

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

> ## Extent of Slicing
>
> 1.  Do the two statements below produce the same output?
> 2.  Based on this,
>     what rule governs what is included (or not) in numerical slices and named slices in Pandas?
>
> ~~~
> print(data.ix[0:2, 0:2])
> print(data.ix['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])
> ~~~
> {: .python}
{: .challenge}

> ## Reconstructing Data
>
> Explain what each line in the following short program does:
> what is in `first`, `second`, etc.?
>
> ~~~
> first = pandas.read_csv('data/gapminder_gdp_all.csv', index_col='country')
> second = df[df['continent'] == 'Americas']
> third = second.drop('Puerto Rico')
> fourth = third.drop('continent', axis = 1)
> fourth.to_csv('result.csv')
> ~~~
> {: .python}
{: .challenge}

> ## Selecting Indices
>
> Explain in simple terms what `idxmin` and `idxmax` do in the short program below.
> When would you use these methods?
>
> ~~~
> data = pandas.load_csv('data/gapminder_gdp_europe.csv', index_col='country')
> print(data.idxmin())
> print(data.idxmax())
> ~~~
> {: .python}
{: .challenge}

> ## Practice with Selection.
>
> Assume Pandas has been imported and the Gapminder GDP data for Europe has been loaded.
> Write an expression to select each of the following:
>
> 1.  GDP per capita for all countries in 1982.
> 2.  GDP per capita for Denmark for all years.
> 3.  GDP per capita for all countries for years *after* 1985.
> 4.  GDP per capita for each country in 2007 as a multiple of 
>     GDP per capita for that country in 1952.
{: .challenge}

> ## Interpretation
>
> Poland's borders have been stable since 1945,
> but changed several times in the years before then.
> How would you handle this if you were creating a table of GDP per capita for Poland
> for the entire Twentieth Century?
{: .challenge}
