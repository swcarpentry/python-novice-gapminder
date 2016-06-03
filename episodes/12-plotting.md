---
layout: episode
title: "Plotting"
teaching: 10
exercises: 10
questions:
- "How can I plot my data?"
objectives:
- "Create a time series plot showing a single data set."
- "Create a scatter plot showing relationship between two data sets."
keypoints:
- FIXME
---
- Set up matplotlib inline functionality in jupyter notebook

~~~
%matplotlib inline
~~~
{: .source}

- Plot Australia data using dataframe plot method
- Access row, Series.plot plots with columns as x variable
- Note that dataframe is implicitly using matplotlib

~~~
df = pandas.read_csv("gapminder_gdp_oceania.csv", index_col="country")
df.ix["Australia"].plot()
plt.xticks(rotation=90)
~~~
{: .source}

- Plot both series
- By default, DataFrame.plot plots with the indexes (or rows) as the x axis
- We can transpose to get what we need in order to plot multiple series

~~~
plt.plot(df.T)
plt.ylabel("GDP per capita")
plt.xticks(rotation=90)
~~~
{: .source}

- Do a bar plot, use fancier style

~~~
plt.style.use("ggplot")
plt.plot(df.T)
plt.xticks(rotation=90)
plt.ylabel("GDP per capita")
~~~
{: .source}

- Use pyplot.plot explicitly
- Get years using list comprehension
- convert dataframe data to list

~~~
years = [col[-4:] for col in df.columns.tolist()]
gdp_australia = df.ix["Australia"].tolist()
plt.plot(years, gdp_australia, 'b-')
~~~
{: .source}

- Plot two series with labels

~~~
years = [col[-4:] for col in df.columns.tolist()]
gdp_australia = df.ix["Australia"].tolist()
gdp_nz = df.ix["New Zealand"].tolist()
plt.plot(years, gdp_australia, 'b-', label="Australia")
plt.plot(years, gdp_nz, 'g-', label="New Zealand")
plt.legend(loc="upper left")
plt.xlabel("Year")
plt.ylabel("GDP per capita ($)")
~~~
{: .source}

- Plot a scatter plot correlating the GDP of Australia and New Zealand
- Using plt.scatter and DataFrame.plot.scatter
- Note that you could also use plt.plot
- Transpose the data frame again to make the "dates" the indices

~~~
plt.scatter(gdp_australia, gdp_nz)
df.T.plot.scatter(x = "Australia", y = "New Zealand")
~~~
{: .source}

> ## Minima and Maxima
> 
> Modify the example in the notes to plot the minimum GDP per capita over time
> for all the countries in Asia.
> Modify it again to plot the maximum GDP per capita over time for Asia.
> 
> ~~~
> df_europe = pandas.read_csv("gapminder_gdp_europe.csv")
> df_europe.min().plot(label='min')
> df_europe.max().plot(label='max')
> plt.legend(loc='best')
> ~~~
> {: .source}
{: .challenge}

> ## Correlations
> 
> Modify the example in the notes to create a scatter plot showing
> the relationship between the minimum and maximum GDP per capita
> among the countries in Asia
> for each year in the data set.
> What relationship do you see (if any)?
>
> ~~~
> df_asia = pandas.read_csv("gapminder_gdp_asia.csv")
> df_asia.describe().T.plot(kind='scatter', x = 'min', y = 'max')
> ~~~
> {: .source}
> 
> You might note that the variability in the maximum is much higher than
> that of the minimum.  Take a look at the maximum and the max indexes:
>
> ~~~
> df_asia = pandas.read_csv("gapminder_gdp_asia.csv")
> df_asia.max().plot()
> df_asia.idxmax()
> df_asia.idxmin()
> ~~~
> {: .source}

> ## More correlations
> 
> As a final exercise, make a fancy plot that shows the correlation between
> GDP and life expectancy for 2007, normalizing marker size by population.
>
> ~~~
> df_all = pandas.read_csv("gapminder_all.csv")
> df_all.plot(kind='scatter', x = 'gdpPercap_2007', y='lifeExp_2007', 
>             s = df_all['pop_2007']/1e6)
> ~~~
> {: .source}

{: .challenge}
