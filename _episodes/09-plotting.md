---
Title: "Plotting"
Teaching: 15
Exercises: 15
Questions:
- "How can I plot my data?"
- "How can I save my plot for publishing?"
Objectives:
- "Create a time series plot showing a single data set."
- "Create a scatter plot showing the relationship between two data sets."
Keypoints:
- "[`Matplotlib`](https://matplotlib.org/) is the most widely used scientific plotting library in Python"
- "Plot data directly from a [`Pandas dataframe`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)."
- "Select and transform data, then plot it."
- "Several plot styles are available: see the [Python Graph Gallery](https://python-graph-gallery.com/matplotlib/) for more options."
- "Can plot many data sets together."
---

## Matplotlib is the most widely used scientific plotting library in Python

* Commonly used Python library called [`matplotlib.pyplot`](https://matplotlib.org/stable/tutorials/introductory/pyplot.html) - here imported as 'plt'.
* The Jupyter Notebook will render plots inline by default.
~~~
import matplotlib.pyplot as plt
~~~
{: .language-python}

* Simple plots are _fairly_ simple to create. 
* For example, using the variables 'time' and 'position' and `plt.plot`.
* We can also add labels to the X and Y axes with `plt.xlabel` and `plt.ylabel`, respectively.
~~~
time = [0, 1, 2, 3]
position = [0, 100, 200, 300]

plt.plot(time, position)
plt.xlabel('Time (hr)')
plt.ylabel('Position (km)')
~~~
{: .language-python}

![Simple Position-Time Plot](../fig/9_simple_position_time_plot.svg)

> ### Display all (open) figures
> 
> * In our Jupyter Notebook example, running the cell will generate the figure directly below the code. 
> * The figure is also included in the Jupyter Notebook document for future viewing.
> * However, other Python environments like an interactive Python session started from a terminal, or a Python script executed via the command line, require an additional command to display the figure.

> To instruct Matplotlib to show a figure directly below the code, run the following command:
> ~~~
> plt.show()
> ~~~
> {: .language-python}
>
> `plt.show()` can also be used in a Jupyter Notebook - for instance, to display multiple figures if several are created by running a single cell.
>
{: .callout}

## Select and plot data directly from a Pandas dataframe

* We can also plot [Pandas dataframes](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) - the Pandas library is here imported as 'pd'.
* Pandas implicitly uses Matplotlib.
~~~
import pandas as pd
~~~
{: .language-python}

But first we need to import our data set. We use the the`index_col` parameter here to make Pandas use the column 'country' as the row labels of our dataframe.
~~~
data = pd.read_csv('data/gapminder_gdp_oceania.csv', index_col='country')
~~~
{: .language-python}

Before plotting, we need to convert the data types of the column headings from strings into integers, since these will represent numerical values.
> ### Data extraction
> For clarity, we need to extract the year from the last four characters of each column name. The current column names are structured as 'gdpPercap_(year)'. 
> 
> * Since we want to plot GDP vs. years, we use `strip()`. This removes the characters stated in the argument - here 'gdpPercap_', from the string .
> 
> * This method works on strings, so we call `str` before `strip()`.
~~~
years = data.columns.str.strip('gdpPercap_')
~~~
{: .language-python}

Now we can convert years values into integers and save the transformed values (i.e., integers rather than strings) back to our dataframe. We do all of this at once with the following command:
~~~
data.columns = years.astype(int)
~~~
{: .language-python}

Finally, we can select subsets of the data by specifying the variable we want to plot. For instance, we can plot data only from Australia by using `data.loc`:
~~~
data.loc['Australia'].plot()
~~~
{: .language-python}

![GDP plot for Australia](../fig/9_gdp_australia.svg)

## Transform data before plotting

* By default, `DataFrame.plot` plots rows in the X axis - here our variable 'years'. 
* We can [transpose](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.transpose.html) the data in order to plot multiple series - here the countries 'Australia' and 'New Zealand'.
* **Note**: The property `T` is an accessor to the method `transpose()`.
~~~
data.T.plot()
plt.ylabel('GDP per capita')
~~~
{: .language-python}

![GDP plot for Australia and New Zealand](../fig/9_gdp_australia_nz.svg)

## Several plot styles are available

* As an exampel, we can create a bar plot with a _fancier_ style, using [`plt.style.use`](https://matplotlib.org/stable/gallery/style_sheets/ggplot.html). 
* Here we use the `ggplot` argument, which adjusts the style to emulate [ggplot](https://r-graph-gallery.com/ggplot2-package.html) - an open-source data visualization package for the statistical programming language R, now known as _ggplot2_.
~~~
plt.style.use('ggplot')
data.T.plot(kind='bar')
plt.ylabel('GDP per capita')
~~~
{: .language-python}

![GDP barplot for Australia](../fig/9_gdp_bar.svg)

## The Matplotlib plot function

* Data can also be plotted by calling the Matplotlib plot function directly with the command `plt.plot(x, y)`.
* The color and format of markers can also be changed using additional optional arguments - e.g., `b-` is a blue line, `g--` is a green dashed line.

As we learned earlier, we can plot a subset of the data (Australia) by using `data.loc`:
~~~
years = data.columns
gdp_australia = data.loc['Australia']
~~~
{: .language-python}

And then create a plot with this subset and `plt.plot`:
~~~
plt.plot(years, gdp_australia, 'g--')
~~~
{: .language-python}

![GDP formatted plot for Australia](../fig/9_gdp_australia_formatted.svg)

## Multiple data sets

* We can plot many sets of data together.
* This is useful to find the relationship between two data sets.

In this example, we will select two countries' worth of data - namely, Australia (data set 'gdp_australia') and New Zealand (data set 'gdp_nz').
~~~
gdp_australia = data.loc['Australia']
gdp_nz = data.loc['New Zealand']
~~~
{: .language-python}

## Color-coded markers and labels

* We can generate a plot with differently-colored markers using the otions `b-` and `g-`. 
* Matplotlib can recognise a wide variety of [colors and formats](https://matplotlib.org/stable/tutorials/colors/colors.html).
* Here we also added labels to each of our data sets with the `label=` argument.
~~~
plt.plot(years, gdp_australia, 'b-', label='Australia')
plt.plot(years, gdp_nz, 'g-', label='New Zealand')
~~~
{: .language-python}

## Legends

* Often when plotting multiple datasets on the same figure it is desirable to have a legend describing the data.
* Once we have labeled each data set that is being plotted (as we did previously), we can create and format a figure legend.

To Instruct Matplotlib to create the legend, we run the `plt.legend()` command. By default Matplotlib will attempt to place the legend in a suitable position, but you can change it with the `loc=` argument:
~~~
plt.legend(loc='upper left')
plt.xlabel('Year')
plt.ylabel('GDP per capita ($)')
~~~
{: .language-python}

![GDP formatted plot for Australia and New Zealand](../fig/9_gdp_australia_nz_formatted.svg)

## Scatter plots

* Scatter plots are useful to show how much one variable is affected by another, and therefore are great to present the relationship between two sets of data (e.g., to visually assess correlation).
* We can create scatter plots using either Matplotlib (with the `plt.scatter` command) or Pandas (with the `DataFrame.plot.scatter` command).

To evaluate the relationship between the GDP of Australia and New Zealand, we can create a scatter plot with our previously selected data sets:
~~~
plt.scatter(gdp_australia, gdp_nz)
~~~
{: .language-python}

![GDP correlation using plt.scatter](../fig/9_gdp_correlation_plt.svg)

We can see the same data frame reflected over its main diagonal by writing rows as columns (i.e., transposing), and also add axes labels with the `x=` and `y=` arguments:
~~~
data.T.plot.scatter(x='Australia', y='New Zealand')
~~~
{: .language-python}

![GDP correlation using data.T.plot.scatter](../fig/9_gdp_correlation_data.svg)

> ## Challenge: minima and maxima
>
> 1. Fill in the blanks below to plot the minimum GDP per capita over time for all European countries.
> 2. Modify it again to plot the maximum GDP per capita over time for all European countries.
> 3. Generate a plot with both the minimum and maximum GDP per capita over time for all European countries.
> ~~~
> data_europe = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
> data_europe.____.plot(label='min')
> data_europe.____
> plt.legend(loc='best')
> plt.xticks(rotation=90)
> ~~~
> {: .language-python}
>
> > ## Solution
> > 
> > 1. **Minimum** GDP per capita over time (Europe).
> > ~~~
> > data_europe = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
> > data_europe.min().plot(label='min')
> > plt.legend(loc='best')
> > plt.xticks(rotation=90)
> > ~~~
> > {: .language-python}
> > 
> > 2. **Maximum** GDP per capita over time (Europe).
> > ~~~
> > data_europe = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
> > data_europe.max().plot(label='max')
> > plt.legend(loc='best')
> > plt.xticks(rotation=90)
> > ~~~
> > {: .language-python}
> > 
> > 3. **Minimum and maximum** GDP per capita over time (Europe).
> > ~~~
> > data_europe = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
> > data_europe.min().plot(label='min')
> > data_europe.max().plot(label='max')
> > plt.legend(loc='best')
> > plt.xticks(rotation=90)
> > ~~~
> > {: .language-python}
> > 
> > ![Minima Maxima Solution](../fig/9_minima_maxima_solution.png)
> >
> {: .solution}
{: .challenge}
>
> ## Challenge: correlations
>
> 1. Modify the example in the notes to create a scatter plot showing the relationship between the minimum and maximum GDP per capita among Asian countries for each year in the data set.
> 2. Is there a relationship between the two variables? If so, which one is it?
>
> > ## Solution
> > 1. **Minimum vs. maximum** GDP per capita over time (Asia).
> > ~~~
> > data_asia = pd.read_csv('data/gapminder_gdp_asia.csv', index_col='country')
> > data_asia.describe().T.plot(kind='scatter', x='min', y='max')
> > ~~~
> > {: .language-python}
> >
> > ![Correlations Solution 1](../fig/9_correlations_solution1.svg)
> >
> > 2. Relationship between variables: no particular correlations can be seen between the minimum and maximum GDP per capita values over time. 
> > It seems the fortunes of asian countries do not rise and fall together!
> >
> {: .solution}
{: .challenge}
>
> You may have noticed that the variability in the maximum variable is much higher than that of the minimum. 
> Let's take a look at the [maximum](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.idxmax.html) and [minimum](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.idxmin.html) indexes - also known as the `idxmax()` and `idxmin()` methods in Pandas:
> 
> ~~~
> data_asia = pd.read_csv('data/gapminder_gdp_asia.csv', index_col='country')
> data_asia.max().plot()
> print(data_asia.idxmax())
> print(data_asia.idxmin())
> ~~~
> {: .language-python}
>
> ![Correlations Solution 2](../fig/9_correlations_solution2.png)
> 
> By using these methods, we now know that the variability in the maximim GPD per capita variable is due to a sharp drop after 1972 (the minimum index), which suggests a potential influence of geopolitics given the dominance of oil producing countries. The Brent crude index would have been an interesting comparison. Notably, whilst Myanmar consistently has the lowest GPD per capita, the country with the highest GPD per capita varies over time.
>
> ## Challenge: more about correlations
>
> The code below creates a plot showing the correlation between GDP and life expectancy in 2007, normalising the marker size by population:
>
> ~~~
> data_all = pd.read_csv('data/gapminder_all.csv', index_col='country')
> 
> data_all.plot(kind='scatter', 
>               x='gdpPercap_2007', 
>               y='lifeExp_2007', 
>               s=data_all['pop_2007']/1e6)
> ~~~
> {: .language-python}
>
> > ![More Correlations Solution](../fig/9_more_correlations_solution.svg)
> 
> Using the `help()` function and other resources, explain what each of the arguments does to `.plot`.
> 
> **Hint**: A good place to start is the documentation for the plot function, which you can see by running `help(data_all.plot)`.
> 
> > ## Solution
> > * `kind=` determines the kind of plot to be created - here a scatter plot.
> >
> > * `x=` and `y=` determine what data will be placed on the X and Y axes of the plot - here the columns 'gdpPercap_2007' and 'gdpPercap_2007'; these could also be column indexes.
> >
> > * `s=` determines the size of the plotted points or markers, with a single number or one value for each data point. 
> > You can see further details in the documentation for the `plt.scatter()` function.
> > 
> {: .solution}
{: .challenge}

## Saving your plot

If you are satisfied with the plot(s) you have created, you may want to save it to a file for later use; perhaps to include it in a publication you are currently working on. The [savefig](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html) function in the Matplotlib.pyplot module accomplishes this:
 
~~~
plt.savefig('my_figure.png')
~~~
{: .language-python}
 
Calling this function will save the current figure to the file `my_figure.png`. 
 
The file format will automatically be deduced from the file name extension - here .png. Other formats like .pdf, .ps, .eps and .svg are also available.

**Notes:** 
* Functions in `plt` refer to a global figure variable and after a figure has been displayed to the screen (e.g., with `plt.show`). 
Matplotlib will make this variable refer to a new empty figure if `plt.savefig()`is called after `plt.show()`, and this can also be problematic when building plots in a Jupyter Notebook (as we are here). 
Therefore, make sure you call `plt.savefig` _before_ the plot is displayed to the screen, otherwise you may find a file with an empty plot.

* When using Pandas dataframes, the data is often generated and plotted to the screen in one line, and `plt.savefig` seems not to be a possible approach.

One possibility to save the figure to a file is then to:
  
i) save a reference to the current figure in a local variable with `plt.gcf`., and

ii) call the `savefig` class method from that variable.
~~~
data.plot(kind='bar')
fig = plt.gcf() # gets the current figure
fig.savefig('my_figure.png') # saves the figure to my_figure.png
~~~
{: .language-python}
{: .callout}

## Tips for making your plots accessible

Whenever you are generating plots for a manuscript or a presentation, there are a few things you can do to ensure that everyone can understand your plots. Here are a few tips to get you started on making _accessible_ plots:

* **Text size:** always make sure that your text is large enough to read. To change your font size, use the `fontsize=` parameter in the `xlabel=`, `ylabel=`, `title=`, and `legend=` arguments. To increase the text size of the numbers on your axes, adjuts the `labelsize` parameter of your [tick_properties]( https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html). 

* **Elements size:** Similarly, you should make your graph elements easy to see. Use `s=` to increase the size of your scatter plot markers and `linewidth=` to increase the sizes of your plot lines.

* **Color:** Using color (and nothing else) to distinguish between different plot elements will make your plots unreadable to anyone who is colorblind, or who happens to have a black-and-white office printer. For lines, the `linestyle=` parameter allows you to use different types of lines. For scatter plots, `marker=` allows you to change the shape of your data points. Moreover, if you are unsure about your colors, you can use [Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/) or [Color Oracle](https://colororacle.org/) to simulate what your plots would look like to those with colorblindness.

{: .callout}
