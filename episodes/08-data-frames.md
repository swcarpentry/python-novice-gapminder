---
title: Pandas DataFrames
teaching: 15
exercises: 15
---

::::::::::::::::::::::::::::::::::::::: objectives

- Select individual values from a Pandas dataframe.
- Select entire rows or entire columns from a dataframe.
- Select a subset of both rows and columns from a dataframe in a single operation.
- Select a subset of a dataframe by a single Boolean criterion.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can I do statistical analysis of tabular data?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Note about Pandas DataFrames/Series

A [DataFrame][pandas-dataframe] is a collection of [Series][pandas-series];
The DataFrame is the way Pandas represents a table, and Series is the data-structure
Pandas use to represent a column.

Pandas is built on top of the [Numpy][numpy] library, which in practice means that
most of the methods defined for Numpy Arrays apply to Pandas Series/DataFrames.

What makes Pandas so attractive is the powerful interface to access individual records
of the table, proper handling of missing values, and relational-databases operations
between DataFrames.

## Selecting values

To access a value at the position `[i,j]` of a DataFrame, we have two options, depending on
what is the meaning of `i` in use.
Remember that a DataFrame provides an *index* as a way to identify the rows of the table;
a row, then, has a *position* inside the table as well as a *label*, which
uniquely identifies its *entry* in the DataFrame.

## Use `DataFrame.iloc[..., ...]` to select values by their (entry) position

- Can specify location by numerical index analogously to 2D version of character selection in strings.

```python
import pandas as pd
data_cancer = pd.read_csv('data-palmers-penguins.csv')
print(data_cancer.iloc[0, 0])
```

```output
Adelie
```

## Use `DataFrame.loc[..., ...]` to select values by their (entry) label.

- Can specify location by row and/or column name.

```python
print(data.loc["Albania", "gdpPercap_1952"])
```

```output
1601.056136
```

## Use `:` on its own to mean all columns or all rows.

- Just like Python's usual slicing notation.

```python
print(data.loc[0, :])
```

```output
species                 Adelie
island               Torgersen
bill_length_mm            39.1
bill_depth_mm             18.7
flipper_length_mm        181.0
body_mass_g             3750.0
sex                       Male
Name: 0, dtype: object
```

## Use comparisons to select data based on value.

- Comparison is applied element by element.
- Returns a similarly-shaped dataframe of `True` and `False`.

```python
# Use a subset of data to keep output readable.
subset = data.loc[:, 'bill_length_mm':'body_mass_g']
print('Subset of data:\n', subset)

# Which values were greater than 10000 ?
print('\nWhere are values large?\n', subset > 100)
```

```output
Where are values large?
      bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g
0             False          False               True         True
1             False          False               True         True
2             False          False               True         True
3             False          False               True         True
4             False          False               True         True
..              ...            ...                ...          ...
328           False          False               True         True
329           False          False               True         True
330           False          False               True         True
331           False          False               True         True
332           False          False               True         True
```

## Select values or NaN using a Boolean mask.

- A frame full of Booleans is sometimes called a *mask* because of how it can be used.

```python
mask = subset > 100
print(subset[mask])
```

```output
     bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g
0               NaN            NaN              181.0       3750.0
1               NaN            NaN              186.0       3800.0
2               NaN            NaN              195.0       3250.0
3               NaN            NaN              193.0       3450.0
4               NaN            NaN              190.0       3650.0
..              ...            ...                ...          ...
328             NaN            NaN              214.0       4925.0
329             NaN            NaN              215.0       4850.0
330             NaN            NaN              222.0       5750.0
331             NaN            NaN              212.0       5200.0
332             NaN            NaN              213.0       5400.0
```

- Get the value where the mask is true, and NaN (Not a Number) where it is false.
- Useful because NaNs are ignored by operations like max, min, average, etc.

```python
print(subset[subset > 100].describe())
```

```output
       bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g
count             0.0            0.0         333.000000   333.000000
mean              NaN            NaN         200.966967  4207.057057
std               NaN            NaN          14.015765   805.215802
min               NaN            NaN         172.000000  2700.000000
25%               NaN            NaN         190.000000  3550.000000
50%               NaN            NaN         197.000000  4050.000000
75%               NaN            NaN         213.000000  4775.000000
max               NaN            NaN         231.000000  6300.000000
```

## Group By: split-apply-combine

::::::::::::::::::::::::::::::::::::: instructor
Learners often struggle here, many may not work with financial data and concepts so they
find the example concepts difficult to get their head around. The biggest problem
though is the line generating the wealth_score, this step needs to be talked through
throughly:
* It uses implicit conversion between boolean and float values which 
has not been covered in the course so far. 
* The axis=1 argument needs to be explained clearly.
:::::::::::::::::::::::::::::::::::::::::::::::::

Pandas vectorizing methods and grouping operations are features that provide users
much flexibility to analyse their data.

```python
data.groupby('species')['body_mass_g'].mean()
```

:::::::::::::::::::::::::::::::::::::::  challenge

## Looking at unique values

Look at pandas documentation and see what method can be used to get unique values. 

:::::::::::::::  solution

## Solution

To get the count of unique values you can use value_counts method:

```python
data.value_counts()
```

The output is

```output
species  island     bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g  sex   
Adelie   Biscoe     34.5            18.1           187.0              2900.0       Female    1
Gentoo   Biscoe     44.0            13.6           208.0              4350.0       Female    1
                    43.6            13.9           217.0              4900.0       Female    1
                    43.5            15.2           213.0              4650.0       Female    1
                                    14.2           220.0              4700.0       Female    1
                                                                                            ..
Adelie   Torgersen  36.6            17.8           185.0              3700.0       Female    1
                    36.2            17.2           187.0              3150.0       Female    1
                                    16.1           187.0              3550.0       Female    1
                    35.9            16.6           190.0              3050.0       Female    1
Gentoo   Biscoe     59.6            17.0           230.0              6050.0       Male      1
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Filtering

1. How can you filter the DataFrame data to get all rows where the species is 'Adelie' and the island is 'Torgersen'?
2. What code would you use to filter the DataFrame data to find all entries where the body mass is greater than 4000 grams and the flipper length is greater than 200 mm?

:::::::::::::::  solution

## Solution

```python
data[(data['species'] == 'Adelie') & (data['island'] == 'Torgersen')]
```
```python
data[(data['body_mass_g'] > 4000) & (data['flipper_length_mm'] > 200)]
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Many Ways of Access

There are at least two ways of accessing a value or slice of a DataFrame: by name or index.
However, there are many others. For example, a single column or row can be accessed either as a `DataFrame`
or a `Series` object.

Suggest different ways of doing the following operations on a DataFrame:

1. Access a single column
2. Access a single row
3. Access an individual DataFrame element
4. Access several columns
5. Access several rows
6. Access a subset of specific rows and columns
7. Access a subset of row and column ranges

:::::::::::::::  solution

## Solution

1\. Access a single column:

```python
# by name
data["col_name"]   # as a Series
data[["col_name"]] # as a DataFrame

# by name using .loc
data.T.loc["col_name"]  # as a Series
data.T.loc[["col_name"]].T  # as a DataFrame

# Dot notation (Series)
data.col_name

# by index (iloc)
data.iloc[:, col_index]   # as a Series
data.iloc[:, [col_index]] # as a DataFrame

# using a mask
data.T[data.T.index == "col_name"].T
```

2\. Access a single row:

```python
# by name using .loc
data.loc["row_name"] # as a Series
data.loc[["row_name"]] # as a DataFrame

# by name
data.T["row_name"] # as a Series
data.T[["row_name"]].T # as a DataFrame

# by index
data.iloc[row_index]   # as a Series
data.iloc[[row_index]]   # as a DataFrame

# using mask
data[data.index == "row_name"]
```

3\. Access an individual DataFrame element:

```python
# by column/row names
data["column_name"]["row_name"]         # as a Series

data[["col_name"]].loc["row_name"]  # as a Series
data[["col_name"]].loc[["row_name"]]  # as a DataFrame

data.loc["row_name"]["col_name"]  # as a value
data.loc[["row_name"]]["col_name"]  # as a Series
data.loc[["row_name"]][["col_name"]]  # as a DataFrame

data.loc["row_name", "col_name"]  # as a value
data.loc[["row_name"], "col_name"]  # as a Series. Preserves index. Column name is moved to `.name`.
data.loc["row_name", ["col_name"]]  # as a Series. Index is moved to `.name.` Sets index to column name.
data.loc[["row_name"], ["col_name"]]  # as a DataFrame (preserves original index and column name)

# by column/row names: Dot notation
data.col_name.row_name

# by column/row indices
data.iloc[row_index, col_index] # as a value
data.iloc[[row_index], col_index] # as a Series. Preserves index. Column name is moved to `.name`
data.iloc[row_index, [col_index]] # as a Series. Index is moved to `.name.` Sets index to column name.
data.iloc[[row_index], [col_index]] # as a DataFrame (preserves original index and column name)

# column name + row index
data["col_name"][row_index]
data.col_name[row_index]
data["col_name"].iloc[row_index]

# column index + row name
data.iloc[:, [col_index]].loc["row_name"]  # as a Series
data.iloc[:, [col_index]].loc[["row_name"]]  # as a DataFrame

# using masks
data[data.index == "row_name"].T[data.T.index == "col_name"].T
```

4\. Access several columns:

```python
# by name
data[["col1", "col2", "col3"]]
data.loc[:, ["col1", "col2", "col3"]]

# by index
data.iloc[:, [col1_index, col2_index, col3_index]]
```

5\. Access several rows

```python
# by name
data.loc[["row1", "row2", "row3"]]

# by index
data.iloc[[row1_index, row2_index, row3_index]]
```

6\. Access a subset of specific rows and columns

```python
# by names
data.loc[["row1", "row2", "row3"], ["col1", "col2", "col3"]]

# by indices
data.iloc[[row1_index, row2_index, row3_index], [col1_index, col2_index, col3_index]]

# column names + row indices
data[["col1", "col2", "col3"]].iloc[[row1_index, row2_index, row3_index]]

# column indices + row names
data.iloc[:, [col1_index, col2_index, col3_index]].loc[["row1", "row2", "row3"]]
```

7\. Access a subset of row and column ranges

```python
# by name
data.loc["row1":"row2", "col1":"col2"]

# by index
data.iloc[row1_index:row2_index, col1_index:col2_index]

# column names + row indices
data.loc[:, "col1_name":"col2_name"].iloc[row1_index:row2_index]

# column indices + row names
data.iloc[:, col1_index:col2_index].loc["row1":"row2"]
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Exploring available methods using the `dir()` function

Python includes a `dir()` function that can be used to display all of the available methods (functions) that are built into a data object.  In Episode 4, we used some methods with a string. But we can see many more are available by using `dir()`:

```python
my_string = 'Hello world!'   # creation of a string object 
dir(my_string)
```

This command returns:

```python
['__add__',
...
'__subclasshook__',
'capitalize',
'casefold',
'center',
...
'upper',
'zfill']
```

You can use `help()` or <kbd>Shift</kbd>\+<kbd>Tab</kbd> to get more information about what these methods do.

Assume Pandas has been imported and the Gapminder GDP data for Europe has been loaded as `data`.  Then, use `dir()`
to find the function that prints out the median per-capita GDP across all European countries for each year that information is available.

:::::::::::::::  solution

## Solution

Among many choices, `dir()` lists the `median()` function as a possibility.  Thus,

```python
data.median()
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Interpretation

Poland's borders have been stable since 1945,
but changed several times in the years before then.
How would you handle this if you were creating a table of GDP per capita for Poland
for the entire twentieth century?


::::::::::::::::::::::::::::::::::::::::::::::::::

[pandas-dataframe]: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
[pandas-series]: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html
[numpy]: https://www.numpy.org/


:::::::::::::::::::::::::::::::::::::::: keypoints

- Use `DataFrame.iloc[..., ...]` to select values by integer location.
- Use `:` on its own to mean all columns or all rows.
- Select multiple columns or rows using `DataFrame.loc` and a named slice.
- Result of slicing can be used in further operations.
- Use comparisons to select data based on value.
- Select values or NaN using a Boolean mask.

::::::::::::::::::::::::::::::::::::::::::::::::::


