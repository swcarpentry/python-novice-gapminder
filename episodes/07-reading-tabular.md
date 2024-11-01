---
title: Reading Tabular Data into DataFrames
teaching: 10
exercises: 10
---

::::::::::::::::::::::::::::::::::::::: objectives

- Import the Pandas library.
- Use Pandas to load a simple CSV data set.
- Get some basic information about a Pandas DataFrame.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can I read tabular data?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Use the Pandas library to do statistics on tabular data.

- [Pandas](https://pandas.pydata.org/) is a widely-used Python library for statistics, particularly on tabular data.
- Borrows many features from R's dataframes.
  - A 2-dimensional table whose columns have names
    and potentially have different data types.
- Load Pandas with `import pandas as pd`. The alias `pd` is commonly used to refer to the Pandas library in code.
- Read a Comma Separated Values (CSV) data file with `pd.read_csv`.
  - Argument is the name of the file to be read.
  - Returns a dataframe that you can assign to a variable

```python
import pandas as pd

data_penguins = pd.read_csv('data/data-palmers-penguins.csv')
print(data_penguins)
```

```output
    species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  \
0    Adelie  Torgersen            39.1           18.7              181.0   
1    Adelie  Torgersen            39.5           17.4              186.0   
2    Adelie  Torgersen            40.3           18.0              195.0   
3    Adelie  Torgersen            36.7           19.3              193.0   
4    Adelie  Torgersen            39.3           20.6              190.0   
..      ...        ...             ...            ...                ...   
328  Gentoo     Biscoe            47.2           13.7              214.0   
329  Gentoo     Biscoe            46.8           14.3              215.0   
330  Gentoo     Biscoe            50.4           15.7              222.0   
331  Gentoo     Biscoe            45.2           14.8              212.0   
332  Gentoo     Biscoe            49.9           16.1              213.0   

     body_mass_g     sex  
0         3750.0    Male  
1         3800.0  Female  
2         3250.0  Female  
3         3450.0  Female  
4         3650.0    Male  
..           ...     ...  
328       4925.0  Female  
329       4850.0  Female  
330       5750.0    Male  
331       5200.0  Female  
332       5400.0    Male 
```

- The columns in a dataframe are the observed variables, and the rows are the observations.
- Pandas uses backslash `\` to show wrapped lines when output is too wide to fit the screen.
- Using descriptive dataframe names helps us distinguish between multiple dataframes so we won't accidentally overwrite a dataframe or read from the wrong one.

:::::::::::::::::::::::::::::::::::::::::  callout

## File Not Found

Our lessons store their data files in a `data` sub-directory,
which is why the path to the file is `data/data-palmers-penguins.csv`.
If you forget to include `data/`,
or if you include it but your copy of the file is somewhere else,
you will get a [runtime error](04-built-in.md)
that ends with a line like this:

```error
FileNotFoundError: [Errno 2] No such file or directory: 'data/data-palmers-penguins.csv'
```

::::::::::::::::::::::::::::::::::::::::::::::::::

## Use `index_col` to specify that a column's values should be used as row headings.

- Row headings are numbers (0 and 1 in this case).
- Really want to index by country.
- Pass the name of the column to `read_csv` as its `index_col` parameter to do this.
- Naming the dataframe `data_penguins_species` tells us what data it includes (`penguins`) and how it is indexed (`species`).

```python
data_penguins_species = pd.read_csv('data/data_penguins_species.csv', index_col='species')
print(data_penguins_species)
```

```output
	island	bill_length_mm	bill_depth_mm	flipper_length_mm	body_mass_g	sex
species						
Adelie	Torgersen	39.1	18.7	181.0	3750.0	Male
Adelie	Torgersen	39.5	17.4	186.0	3800.0	Female
Adelie	Torgersen	40.3	18.0	195.0	3250.0	Female
Adelie	Torgersen	36.7	19.3	193.0	3450.0	Female
Adelie	Torgersen	39.3	20.6	190.0	3650.0	Male
...	...	...	...	...	...	...
Gentoo	Biscoe	47.2	13.7	214.0	4925.0	Female
Gentoo	Biscoe	46.8	14.3	215.0	4850.0	Female
Gentoo	Biscoe	50.4	15.7	222.0	5750.0	Male
Gentoo	Biscoe	45.2	14.8	212.0	5200.0	Female
Gentoo	Biscoe	49.9	16.1	213.0	5400.0	Male

```

## Use the `DataFrame.info()` method to find out more about a dataframe.

```python
data_penguins_species.info()
```

```output
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 333 entries, 0 to 332
Data columns (total 7 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   species            333 non-null    object 
 1   island             333 non-null    object 
 2   bill_length_mm     333 non-null    float64
 3   bill_depth_mm      333 non-null    float64
 4   flipper_length_mm  333 non-null    float64
 5   body_mass_g        333 non-null    float64
 6   sex                333 non-null    object 
dtypes: float64(4), object(3)
memory usage: 18.3+ KB
```

- This is a `DataFrame`.
- Species, island and sex columns with object values.
- Four columns, each of which has two actual 64-bit floating point values.
  - We will talk later about null values, which are used to represent missing observations.
- Uses 18.3+ KB of memory.

## The `DataFrame.columns` variable stores information about the dataframe's columns.

- Note that this is data, *not* a method.  (It doesn't have parentheses.)
  - Like `math.pi`.
  - So do not use `()` to try to call it.
- Called a *member variable*, or just *member*.

```python
print(data_penguins_species.columns)
```

```output
Index(['species', 'island', 'bill_length_mm', 'bill_depth_mm',
       'flipper_length_mm', 'body_mass_g', 'sex'],
      dtype='object')
```


## Use `DataFrame.describe()` to get summary statistics about data.

`DataFrame.describe()` gets the summary statistics of only the columns that have numerical data.
All other columns are ignored, unless you use the argument `include='all'`.

```python
print(data_penguins_species.describe())
```

```output
	bill_length_mm	bill_depth_mm	flipper_length_mm	body_mass_g
count	333.000000	333.000000	333.000000	333.000000
mean	43.992793	17.164865	200.966967	4207.057057
std	5.468668	1.969235	14.015765	805.215802
min	32.100000	13.100000	172.000000	2700.000000
25%	39.500000	15.600000	190.000000	3550.000000
50%	44.500000	17.300000	197.000000	4050.000000
75%	48.600000	18.700000	213.000000	4775.000000
max	59.600000	21.500000	231.000000	6300.000000

```

:::::::::::::::::::::::::::::::::::::::  challenge

## Reading Other Data
Projects/carpentry_python_mods/data-breast-cancer.csv
Read the data in `data-breast-cancer.csv`
(which should be in the same directory as `data-palmers-penguin.csv`)
into a variable called `data_cancer`
and display its summary statistics.

:::::::::::::::  solution

## Solution

To read in a CSV, we use `pd.read_csv` and pass the filename `'data/data-breast-cancer.csv'` to it.
<!-- We also once again pass the column name `'country'` to the parameter `index_col` in order to index by country.
The summary statistics can be displayed with the `DataFrame.describe()` method. -->

```python
data_cancer = pd.read_csv('data/data-breast-cancer.csv')
data_cancer.describe()
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Inspecting Data

After reading the data for the cancer,
use `help(data_cancer.head)` and `help(data_cancer.tail)`
to find out what `DataFrame.head` and `DataFrame.tail` do.

1. What method call will display the first three rows of this data?
2. What method call will display the last three columns of this data?
  (Hint: you may need to change your view of the data.)

:::::::::::::::  solution

## Solution

1. We can check out the first five rows of `data_cancer` by executing `data_cancer.head()`
  which lets us view the beginning of the DataFrame. We can specify the number of rows we wish
  to see by specifying the parameter `n` in our call to `data_cancer.head()`.
  To view the first three rows, execute:
  
  ```python
  data_cancer.head(n=3)
  ```
  
  ```output

diagnosis	radius_mean	texture_mean	perimeter_mean	area_mean	smoothness_mean	compactness_mean	concavity_mean	concave points_mean	symmetry_mean	...	radius_worst	texture_worst	perimeter_worst	area_worst	smoothness_worst	compactness_worst	concavity_worst	concave points_worst	symmetry_worst	fractal_dimension_worst
0	0	17.99	10.38	122.8	1001.0	0.11840	0.27760	0.3001	0.14710	0.2419	...	25.38	17.33	184.6	2019.0	0.1622	0.6656	0.7119	0.2654	0.4601	0.11890
1	0	20.57	17.77	132.9	1326.0	0.08474	0.07864	0.0869	0.07017	0.1812	...	24.99	23.41	158.8	1956.0	0.1238	0.1866	0.2416	0.1860	0.2750	0.08902
2	0	19.69	21.25	130.0	1203.0	0.10960	0.15990	0.1974	0.12790	0.2069	...	23.57	25.53	152.5	1709.0	0.1444	0.4245	0.4504	0.2430	0.3613	0.08758
  ```

2. To check out the last three rows of `data_cancer`, we would use the command,
  `data_cancer.tail(n=3)`, analogous to `head()` used above. However, here we want to look at
  the last three columns so we need to change our view and then use `tail()`. To do so, we
  create a new DataFrame in which rows and columns are switched:
  
  ```python
  cancer_flipped = data_cancer.T
  ```
  
  We can then view the last three columns of `data_cancer` by viewing the last three rows
  of `cancer_flipped`:
  
  ```python
  cancer_flipped.tail(n=3)
  ```

  ```output
0	1	2	3	4	5	6	7	8	9	...	559	560	561	562	563	564	565	566	567	568
concave points_worst	0.2654	0.18600	0.24300	0.2575	0.16250	0.1741	0.19320	0.1556	0.2060	0.2210	...	0.09653	0.10480	0.00000	0.2356	0.25420	0.22160	0.16280	0.1418	0.2650	0.00000
symmetry_worst	0.4601	0.27500	0.36130	0.6638	0.23640	0.3985	0.30630	0.3196	0.4378	0.4366	...	0.21120	0.22500	0.15660	0.4089	0.29290	0.20600	0.25720	0.2218	0.4087	0.28710
fractal_dimension_worst	0.1189	0.08902	0.08758	0.1730	0.07678	0.1244	0.08368	0.1151	0.1072	0.2075	...	0.08732	0.08321	0.05905	0.1409	0.09873	0.07115	0.06637	0.0782	0.1240	0.07039
  ```
  
  This shows the data that we want, but we may prefer to display three columns instead of three rows,
  so we can flip it back:
  
  ```python
  cancer_flipped.tail(n=3).T    
  ```
  
  **Note:** we could have done the above in a single line of code by 'chaining' the commands:
  
  ```python
  data_cancer.T.tail(n=3).T
  ```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Reading Files in Other Directories

The data for your current project is stored in a file called `microbes.csv`,
which is located in a folder called `field_data`.
You are doing analysis in a notebook called `analysis.ipynb`
in a sibling folder called `thesis`:

```output
your_home_directory
+-- field_data/
|   +-- microbes.csv
+-- thesis/
    +-- analysis.ipynb
```

What value(s) should you pass to `read_csv` to read `microbes.csv` in `analysis.ipynb`?

:::::::::::::::  solution

## Solution

We need to specify the path to the file of interest in the call to `pd.read_csv`. We first need to 'jump' out of
the folder `thesis` using '../' and then into the folder `field_data` using 'field\_data/'. Then we can specify the filename \`microbes.csv.
The result is as follows:

```python
data_microbes = pd.read_csv('../field_data/microbes.csv')
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Writing Data

As well as the `read_csv` function for reading data from a file,
Pandas provides a `to_csv` function to write dataframes to files.
Applying what you've learned about reading from files,
write one of your dataframes to a file called `processed.csv`.
You can use `help` to get information on how to use `to_csv`.

:::::::::::::::  solution

## Solution

In order to write the DataFrame `data_cancer` to a file called `processed.csv`, execute the following command:

```python
data_cancer.to_csv('processed.csv')
```

For help on `read_csv` or `to_csv`, you could execute, for example:

```python
help(data_cancer.to_csv)
help(pd.read_csv)
```

Note that `help(to_csv)` or `help(pd.to_csv)` throws an error! This is due to the fact that `to_csv` is not a global Pandas function, but
a member function of DataFrames. This means you can only call it on an instance of a DataFrame
e.g., `data_cancer.to_csv` or `data_penguins.to_csv`



:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Use the Pandas library to get basic statistics out of tabular data.
- Use `index_col` to specify that a column's values should be used as row headings.
- Use `DataFrame.info` to find out more about a dataframe.
- The `DataFrame.columns` variable stores information about the dataframe's columns.
- Use `DataFrame.T` to transpose a dataframe.
- Use `DataFrame.describe` to get summary statistics about data.

::::::::::::::::::::::::::::::::::::::::::::::::::


