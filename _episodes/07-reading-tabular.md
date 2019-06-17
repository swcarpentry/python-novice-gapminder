---
title: "Reading Tabular Data into DataFrames"
teaching: 10
exercises: 10
questions:
- "How can I read tabular data?"
objectives:
- "Import the Pandas library."
- "Use Pandas to load a simple CSV data set."
- "Get some basic information about a Pandas DataFrame."
keypoints:
- "Use the Pandas library to get basic statistics out of tabular data."
- "Use `index_col` to specify that a column's values should be used as row headings."
- "Use `DataFrame.info` to find out more about a dataframe."
- "The `DataFrame.columns` variable stores information about the dataframe's columns."
- "Use `DataFrame.T` to transpose a dataframe."
- "Use `DataFrame.describe` to get summary statistics about data."
---
## Use the Pandas library to do statistics on tabular data.

*   Pandas is a widely-used Python library for statistics, particularly on tabular data.
*   Borrows many features from R's dataframes.
    *   A 2-dimensional table whose columns have names
        and potentially have different data types.
*   Load it with `import pandas as pd`. The alias `pd` is commonly used for Pandas.
*   Read a Comma Separated Values (CSV) data file with `pd.read_csv`.
    *   Argument is the name of the file to be read.
    *   Assign result to a variable to store the data that was read.
* In a jupyter notebook, use `display()` not `print()` to view the output of a dataframe.

~~~
import pandas as pd

data = pd.read_csv('data/gapminder_gdp_oceania.csv')
print(data)
~~~
{: .language-python}

~~~
       country  gdpPercap_1952  gdpPercap_1957  gdpPercap_1962  \
0    Australia     10039.59564     10949.64959     12217.22686
1  New Zealand     10556.57566     12247.39532     13175.67800

   gdpPercap_1967  gdpPercap_1972  gdpPercap_1977  gdpPercap_1982  \
0     14526.12465     16788.62948     18334.19751     19477.00928
1     14463.91893     16046.03728     16233.71770     17632.41040

   gdpPercap_1987  gdpPercap_1992  gdpPercap_1997  gdpPercap_2002  \
0     21888.88903     23424.76683     26997.93657     30687.75473
1     19007.19129     18363.32494     21050.41377     23189.80135

   gdpPercap_2007
0     34435.36744
1     25185.00911
~~~
{: .output}

*   The columns in a dataframe are the observed variables, and the rows are the observations.
*   Pandas uses backslash `\` to show wrapped lines when output is too wide to fit the screen.

note that `print()` does not produce an output that makes it easy to view tabular data.
If you are viewing this in a jupyter notebook, we recommend you use the `display()` function.
~~~
from IPython.display import display
display(data)
~~~
{: .language-python}

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>gdpPercap_1952</th>
      <th>gdpPercap_1957</th>
      <th>gdpPercap_1962</th>
      <th>gdpPercap_1967</th>
      <th>gdpPercap_1972</th>
      <th>gdpPercap_1977</th>
      <th>gdpPercap_1982</th>
      <th>gdpPercap_1987</th>
      <th>gdpPercap_1992</th>
      <th>gdpPercap_1997</th>
      <th>gdpPercap_2002</th>
      <th>gdpPercap_2007</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Australia</td>
      <td>10039.59564</td>
      <td>10949.64959</td>
      <td>12217.22686</td>
      <td>14526.12465</td>
      <td>16788.62948</td>
      <td>18334.19751</td>
      <td>19477.00928</td>
      <td>21888.88903</td>
      <td>23424.76683</td>
      <td>26997.93657</td>
      <td>30687.75473</td>
      <td>34435.36744</td>
    </tr>
    <tr>
      <th>1</th>
      <td>New Zealand</td>
      <td>10556.57566</td>
      <td>12247.39532</td>
      <td>13175.67800</td>
      <td>14463.91893</td>
      <td>16046.03728</td>
      <td>16233.71770</td>
      <td>17632.41040</td>
      <td>19007.19129</td>
      <td>18363.32494</td>
      <td>21050.41377</td>
      <td>23189.80135</td>
      <td>25185.00911</td>
    </tr>
  </tbody>
</table>

> ## File Not Found
>
> Our lessons store their data files in a `data` sub-directory,
> which is why the path to the file is `data/gapminder_gdp_oceania.csv`.
> If you forget to include `data/`,
> or if you include it but your copy of the file is somewhere else,
> you will get a [runtime error]({{ page.root }}/04-built-in/#runtime-error)
> that ends with a line like this:
>
> ~~~
> OSError: File b'gapminder_gdp_oceania.csv' does not exist
> ~~~
> {: .error}
{: .callout}

## Use `index_col` to specify that a column's values should be used as row headings.

*   Row headings are numbers (0 and 1 in this case).
*   Really want to index by country.
*   Pass the name of the column to `read_csv` as its `index_col` parameter to do this.

~~~
data = pd.read_csv('data/gapminder_gdp_oceania.csv', index_col='country')
display(data)
~~~
{: .language-python}
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gdpPercap_1952</th>
      <th>gdpPercap_1957</th>
      <th>gdpPercap_1962</th>
      <th>gdpPercap_1967</th>
      <th>gdpPercap_1972</th>
      <th>gdpPercap_1977</th>
      <th>gdpPercap_1982</th>
      <th>gdpPercap_1987</th>
      <th>gdpPercap_1992</th>
      <th>gdpPercap_1997</th>
      <th>gdpPercap_2002</th>
      <th>gdpPercap_2007</th>
    </tr>
    <tr>
      <th>country</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Australia</th>
      <td>10039.59564</td>
      <td>10949.64959</td>
      <td>12217.22686</td>
      <td>14526.12465</td>
      <td>16788.62948</td>
      <td>18334.19751</td>
      <td>19477.00928</td>
      <td>21888.88903</td>
      <td>23424.76683</td>
      <td>26997.93657</td>
      <td>30687.75473</td>
      <td>34435.36744</td>
    </tr>
    <tr>
      <th>New Zealand</th>
      <td>10556.57566</td>
      <td>12247.39532</td>
      <td>13175.67800</td>
      <td>14463.91893</td>
      <td>16046.03728</td>
      <td>16233.71770</td>
      <td>17632.41040</td>
      <td>19007.19129</td>
      <td>18363.32494</td>
      <td>21050.41377</td>
      <td>23189.80135</td>
      <td>25185.00911</td>
    </tr>
  </tbody>
</table>

## Use `DataFrame.info` to find out more about a dataframe.

~~~
data.info()
~~~
{: .language-python}
~~~
<class 'pandas.core.frame.DataFrame'>
Index: 2 entries, Australia to New Zealand
Data columns (total 12 columns):
gdpPercap_1952    2 non-null float64
gdpPercap_1957    2 non-null float64
gdpPercap_1962    2 non-null float64
gdpPercap_1967    2 non-null float64
gdpPercap_1972    2 non-null float64
gdpPercap_1977    2 non-null float64
gdpPercap_1982    2 non-null float64
gdpPercap_1987    2 non-null float64
gdpPercap_1992    2 non-null float64
gdpPercap_1997    2 non-null float64
gdpPercap_2002    2 non-null float64
gdpPercap_2007    2 non-null float64
dtypes: float64(12)
memory usage: 208.0+ bytes
~~~
{: .output}

*   This is a `DataFrame`
*   Two rows named `'Australia'` and `'New Zealand'`
*   Twelve columns, each of which has two actual 64-bit floating point values.
    *   We will talk later about null values, which are used to represent missing observations.
*   Uses 208 bytes of memory.

## The `DataFrame.columns` variable stores information about the dataframe's columns.

*   Note that this is data, *not* a method.
    *   Like `math.pi`.
    *   So do not use `()` to try to call it.
*   Called a *member variable*, or just *member*.

~~~
display(data.columns)
~~~
{: .language-python}
~~~
Index(['gdpPercap_1952', 'gdpPercap_1957', 'gdpPercap_1962', 'gdpPercap_1967',
       'gdpPercap_1972', 'gdpPercap_1977', 'gdpPercap_1982', 'gdpPercap_1987',
       'gdpPercap_1992', 'gdpPercap_1997', 'gdpPercap_2002', 'gdpPercap_2007'],
      dtype='object')
~~~
{: .output}

## Use `DataFrame.T` to transpose a dataframe.

*   Sometimes want to treat columns as rows and vice versa.
*   Transpose (written `.T`) doesn't copy the data, just changes the program's view of it.
*   Like `columns`, it is a member variable.

~~~
print(data.T)
~~~
{: .language-python}
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>country</th>
      <th>Australia</th>
      <th>New Zealand</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>gdpPercap_1952</th>
      <td>10039.59564</td>
      <td>10556.57566</td>
    </tr>
    <tr>
      <th>gdpPercap_1957</th>
      <td>10949.64959</td>
      <td>12247.39532</td>
    </tr>
    <tr>
      <th>gdpPercap_1962</th>
      <td>12217.22686</td>
      <td>13175.67800</td>
    </tr>
    <tr>
      <th>gdpPercap_1967</th>
      <td>14526.12465</td>
      <td>14463.91893</td>
    </tr>
    <tr>
      <th>gdpPercap_1972</th>
      <td>16788.62948</td>
      <td>16046.03728</td>
    </tr>
    <tr>
      <th>gdpPercap_1977</th>
      <td>18334.19751</td>
      <td>16233.71770</td>
    </tr>
    <tr>
      <th>gdpPercap_1982</th>
      <td>19477.00928</td>
      <td>17632.41040</td>
    </tr>
    <tr>
      <th>gdpPercap_1987</th>
      <td>21888.88903</td>
      <td>19007.19129</td>
    </tr>
    <tr>
      <th>gdpPercap_1992</th>
      <td>23424.76683</td>
      <td>18363.32494</td>
    </tr>
    <tr>
      <th>gdpPercap_1997</th>
      <td>26997.93657</td>
      <td>21050.41377</td>
    </tr>
    <tr>
      <th>gdpPercap_2002</th>
      <td>30687.75473</td>
      <td>23189.80135</td>
    </tr>
    <tr>
      <th>gdpPercap_2007</th>
      <td>34435.36744</td>
      <td>25185.00911</td>
    </tr>
  </tbody>
</table>
{: .output}

## Use `DataFrame.describe` to get summary statistics about data.

DataFrame.describe() gets the summary statistics of only the columns that have numerical data. 
All other columns are ignored, unless you use the argument `include='all'`.
~~~
display(data.describe())
~~~
{: .language-python}

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gdpPercap_1952</th>
      <th>gdpPercap_1957</th>
      <th>gdpPercap_1962</th>
      <th>gdpPercap_1967</th>
      <th>gdpPercap_1972</th>
      <th>gdpPercap_1977</th>
      <th>gdpPercap_1982</th>
      <th>gdpPercap_1987</th>
      <th>gdpPercap_1992</th>
      <th>gdpPercap_1997</th>
      <th>gdpPercap_2002</th>
      <th>gdpPercap_2007</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.00000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>10298.085650</td>
      <td>11598.522455</td>
      <td>12696.452430</td>
      <td>14495.021790</td>
      <td>16417.33338</td>
      <td>17283.957605</td>
      <td>18554.709840</td>
      <td>20448.040160</td>
      <td>20894.045885</td>
      <td>24024.175170</td>
      <td>26938.778040</td>
      <td>29810.188275</td>
    </tr>
    <tr>
      <th>std</th>
      <td>365.560078</td>
      <td>917.644806</td>
      <td>677.727301</td>
      <td>43.986086</td>
      <td>525.09198</td>
      <td>1485.263517</td>
      <td>1304.328377</td>
      <td>2037.668013</td>
      <td>3578.979883</td>
      <td>4205.533703</td>
      <td>5301.853680</td>
      <td>6540.991104</td>
    </tr>
    <tr>
      <th>min</th>
      <td>10039.595640</td>
      <td>10949.649590</td>
      <td>12217.226860</td>
      <td>14463.918930</td>
      <td>16046.03728</td>
      <td>16233.717700</td>
      <td>17632.410400</td>
      <td>19007.191290</td>
      <td>18363.324940</td>
      <td>21050.413770</td>
      <td>23189.801350</td>
      <td>25185.009110</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>10168.840645</td>
      <td>11274.086022</td>
      <td>12456.839645</td>
      <td>14479.470360</td>
      <td>16231.68533</td>
      <td>16758.837652</td>
      <td>18093.560120</td>
      <td>19727.615725</td>
      <td>19628.685413</td>
      <td>22537.294470</td>
      <td>25064.289695</td>
      <td>27497.598692</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>10298.085650</td>
      <td>11598.522455</td>
      <td>12696.452430</td>
      <td>14495.021790</td>
      <td>16417.33338</td>
      <td>17283.957605</td>
      <td>18554.709840</td>
      <td>20448.040160</td>
      <td>20894.045885</td>
      <td>24024.175170</td>
      <td>26938.778040</td>
      <td>29810.188275</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>10427.330655</td>
      <td>11922.958888</td>
      <td>12936.065215</td>
      <td>14510.573220</td>
      <td>16602.98143</td>
      <td>17809.077557</td>
      <td>19015.859560</td>
      <td>21168.464595</td>
      <td>22159.406358</td>
      <td>25511.055870</td>
      <td>28813.266385</td>
      <td>32122.777857</td>
    </tr>
    <tr>
      <th>max</th>
      <td>10556.575660</td>
      <td>12247.395320</td>
      <td>13175.678000</td>
      <td>14526.124650</td>
      <td>16788.62948</td>
      <td>18334.197510</td>
      <td>19477.009280</td>
      <td>21888.889030</td>
      <td>23424.766830</td>
      <td>26997.936570</td>
      <td>30687.754730</td>
      <td>34435.367440</td>
    </tr>
  </tbody>
</table>
{: .output}

*   Not particularly useful with just two records,
    but very helpful when there are thousands.

> ## Reading Other Data
>
> Read the data in `gapminder_gdp_americas.csv`
> (which should be in the same directory as `gapminder_gdp_oceania.csv`)
> into a variable called `americas`
> and display its summary statistics.
>
> > ## Solution
> > To read in a CSV, we use `pd.read_csv` and pass the filename 'data/gapminder_gdp_americas.csv' to it. We also once again pass the
> > column name 'country' to the parameter `index_col` in order to index by country:
> > ~~~
> > americas = pd.read_csv('data/gapminder_gdp_americas.csv', index_col='country')
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}



> ## Inspecting Data
>
> After reading the data for the Americas,
> use `help(americas.head)` and `help(americas.tail)`
> to find out what `DataFrame.head` and `DataFrame.tail` do.
>
> 1.  What method call will display the first three rows of this data?
> 2.  What method call will display the last three columns of this data?
>     (Hint: you may need to change your view of the data.)
>
> > ## Solution
> > 1. We can check out the first five rows of `americas` by executing `americas.head()` (allowing us to view the head
> > of the DataFrame). We can specify the number of rows we wish to see by specifying the parameter `n` in our call
> > to `americas.head()`. To view the first three rows, execute:
> >
> > ~~~
> > americas.head(n=3)
> > ~~~
> > {: .language-python}
> > 
> > The output is then
> > <table border="1" class="dataframe">
> >   <thead>
> >     <tr style="text-align: right;">
> >       <th></th>
> >       <th>continent</th>
> >       <th>gdpPercap_1952</th>
> >       <th>gdpPercap_1957</th>
> >       <th>gdpPercap_1962</th>
> >       <th>gdpPercap_1967</th>
> >       <th>gdpPercap_1972</th>
> >       <th>gdpPercap_1977</th>
> >       <th>gdpPercap_1982</th>
> >       <th>gdpPercap_1987</th>
> >       <th>gdpPercap_1992</th>
> >       <th>gdpPercap_1997</th>
> >       <th>gdpPercap_2002</th>
> >       <th>gdpPercap_2007</th>
> >     </tr>
> >     <tr>
> >       <th>country</th>
> >       <th></th>
> >       <th></th>
> >       <th></th>
> >       <th></th>
> >       <th></th>
> >       <th></th>
> >       <th></th>
> >       <th></th>
> >       <th></th>
> >       <th></th>
> >       <th></th>
> >       <th></th>
> >       <th></th>
> >     </tr>
> >   </thead>
> >   <tbody>
> >     <tr>
> >       <th>Argentina</th>
> >       <td>Americas</td>
> >       <td>5911.315053</td>
> >       <td>6856.856212</td>
> >       <td>7133.166023</td>
> >       <td>8052.953021</td>
> >       <td>9443.038526</td>
> >       <td>10079.026740</td>
> >       <td>8997.897412</td>
> >       <td>9139.671389</td>
> >       <td>9308.418710</td>
> >       <td>10967.281950</td>
> >       <td>8797.640716</td>
> >       <td>12779.379640</td>
> >     </tr>
> >     <tr>
> >       <th>Bolivia</th>
> >       <td>Americas</td>
> >       <td>2677.326347</td>
> >       <td>2127.686326</td>
> >       <td>2180.972546</td>
> >       <td>2586.886053</td>
> >       <td>2980.331339</td>
> >       <td>3548.097832</td>
> >       <td>3156.510452</td>
> >       <td>2753.691490</td>
> >       <td>2961.699694</td>
> >       <td>3326.143191</td>
> >       <td>3413.262690</td>
> >       <td>3822.137084</td>
> >     </tr>
> >     <tr>
> >       <th>Brazil</th>
> >       <td>Americas</td>
> >       <td>2108.944355</td>
> >       <td>2487.365989</td>
> >       <td>3336.585802</td>
> >       <td>3429.864357</td>
> >       <td>4985.711467</td>
> >       <td>6660.118654</td>
> >       <td>7030.835878</td>
> >       <td>7807.095818</td>
> >       <td>6950.283021</td>
> >       <td>7957.980824</td>
> >       <td>8131.212843</td>
> >       <td>9065.800825</td>
> >     </tr>
> >   </tbody>
> > </table>
> >
> > 2. To check out the last three rows of `americas`, we would use the command, `americas.tail(n=3)`,
> > analogous to `head()` used above. However, here we want to look at the last three columns so we need
> > to change our view and then use `tail()`. To do so, we create a new DataFrame in which rows and 
> > columns are switched
> > 
> > ~~~
> > americas_flipped = americas.T
> > ~~~
> > {: .language-python}
> >
> > We can then view the last three columns of `americas` by viewing the last three rows of `americas_flipped`:
> > ~~~
> > americas_flipped.tail(n=3)
> > ~~~
> > {: .language-python}
> > 
> > The output is then
> > <table border="1" class="dataframe">
> >   <thead>
> >     <tr style="text-align: right;">
> >       <th>country</th>
> >       <th>Argentina</th>
> >       <th>Bolivia</th>
> >       <th>Brazil</th>
> >       <th>Canada</th>
> >       <th>Chile</th>
> >       <th>Colombia</th>
> >       <th>Costa Rica</th>
> >       <th>Cuba</th>
> >       <th>Dominican Republic</th>
> >       <th>Ecuador</th>
> >       <th>El Salvador</th>
> >       <th>Guatemala</th>
> >       <th>Haiti</th>
> >       <th>Honduras</th>
> >       <th>Jamaica</th>
> >       <th>Mexico</th>
> >       <th>Nicaragua</th>
> >       <th>Panama</th>
> >       <th>Paraguay</th>
> >       <th>Peru</th>
> >       <th>Puerto Rico</th>
> >       <th>Trinidad and Tobago</th>
> >       <th>United States</th>
> >       <th>Uruguay</th>
> >       <th>Venezuela</th>
> >     </tr>
> >   </thead>
> >   <tbody>
> >     <tr>
> >       <th>gdpPercap_1997</th>
> >       <td>10967.3</td>
> >       <td>3326.14</td>
> >       <td>7957.98</td>
> >       <td>28954.9</td>
> >       <td>10118.1</td>
> >       <td>6117.36</td>
> >       <td>6677.05</td>
> >       <td>5431.99</td>
> >       <td>3614.1</td>
> >       <td>7429.46</td>
> >       <td>5154.83</td>
> >       <td>4684.31</td>
> >       <td>1341.73</td>
> >       <td>3160.45</td>
> >       <td>7121.92</td>
> >       <td>9767.3</td>
> >       <td>2253.02</td>
> >       <td>7113.69</td>
> >       <td>4247.4</td>
> >       <td>5838.35</td>
> >       <td>16999.4</td>
> >       <td>8792.57</td>
> >       <td>35767.4</td>
> >       <td>9230.24</td>
> >       <td>10165.5</td>
> >     </tr>
> >     <tr>
> >       <th>gdpPercap_2002</th>
> >       <td>8797.64</td>
> >       <td>3413.26</td>
> >       <td>8131.21</td>
> >       <td>33329</td>
> >       <td>10778.8</td>
> >       <td>5755.26</td>
> >       <td>7723.45</td>
> >       <td>6340.65</td>
> >       <td>4563.81</td>
> >       <td>5773.04</td>
> >       <td>5351.57</td>
> >       <td>4858.35</td>
> >       <td>1270.36</td>
> >       <td>3099.73</td>
> >       <td>6994.77</td>
> >       <td>10742.4</td>
> >       <td>2474.55</td>
> >       <td>7356.03</td>
> >       <td>3783.67</td>
> >       <td>5909.02</td>
> >       <td>18855.6</td>
> >       <td>11460.6</td>
> >       <td>39097.1</td>
> >       <td>7727</td>
> >       <td>8605.05</td>
> >     </tr>
> >     <tr>
> >       <th>gdpPercap_2007</th>
> >       <td>12779.4</td>
> >       <td>3822.14</td>
> >       <td>9065.8</td>
> >       <td>36319.2</td>
> >       <td>13171.6</td>
> >       <td>7006.58</td>
> >       <td>9645.06</td>
> >       <td>8948.1</td>
> >       <td>6025.37</td>
> >       <td>6873.26</td>
> >       <td>5728.35</td>
> >       <td>5186.05</td>
> >       <td>1201.64</td>
> >       <td>3548.33</td>
> >       <td>7320.88</td>
> >       <td>11977.6</td>
> >       <td>2749.32</td>
> >       <td>9809.19</td>
> >       <td>4172.84</td>
> >       <td>7408.91</td>
> >       <td>19328.7</td>
> >       <td>18008.5</td>
> >       <td>42951.7</td>
> >       <td>10611.5</td>
> >       <td>11415.8</td>
> >     </tr>
> >   </tbody>
> > </table>
> >
> > Note: we could have done the above in a single line of code by
> > [chaining](https://en.wikipedia.org/wiki/Method_chaining) the commands:
> > ~~~
> > americas.T.tail(n=3)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## Reading Files in Other Directories
>
> The data for your current project is stored in a file called `microbes.csv`,
> which is located in a folder called `field_data`.
> You are doing analysis in a notebook called `analysis.ipynb`
> in a sibling folder called `thesis`:
>
> ~~~
> your_home_directory
> +-- field_data/
> |   +-- microbes.csv
> +-- thesis/
>     +-- analysis.ipynb
> ~~~
> {: .output}
>
> What value(s) should you pass to `read_csv` to read `microbes.csv` in `analysis.ipynb`?
> 
> > ## Solution
> > We need to specify the path to the file of interest in the call to `pd.read_csv`. We first need to 'jump' out of
> > the folder `thesis` using '../' and then into the folder `field_data` using 'field_data/'. Then we can specify the filename `microbes.csv.
> > The result is as follows:
> > ~~~
> > data_microbes = pd.read_csv('../field_data/microbes.csv')
> > ~~~
> >{: .language-python}
> {: .solution}
{: .challenge}

> ## Writing Data
> 
> As well as the `read_csv` function for reading data from a file,
> Pandas provides a `to_csv` function to write dataframes to files.
> Applying what you've learned about reading from files,
> write one of your dataframes to a file called `processed.csv`.
> You can use `help` to get information on how to use `to_csv`.
> > ## Solution
> > In order to write the DataFrame `americas` to a file called `processed.csv`, execute the following command:
> > ~~~
> > americas.to_csv('processed.csv')
> > ~~~
> >{: .language-python}
> > For help on `to_csv`, you could execute, for example,
> > ~~~
> > help(americas.to_csv)
> > ~~~
> >{: .language-python}
> > Note that `help(to_csv)` throws an error! This is a subtlety and is due to the fact that `to_csv` is NOT a function in 
> > and of itself and the actual call is `americas.to_csv`. 
> > 
> {: .solution}
{: .challenge}
