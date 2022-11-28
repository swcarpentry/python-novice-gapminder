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

We can see the same data frame reflected over its main diagonal by writing rows as columns (i.e., transposing), and also add axes labels with the `x=` and `y=`  arguments:
~~~
data.T.plot.scatter(x='Australia', y='New Zealand')
~~~
{: .language-python}

![GDP correlation using data.T.plot.scatter](../fig/9_gdp_correlation_data.svg)










#########################################################START HERE!!!!

> ## Minima and Maxima
>
> Fill in the blanks below to plot the minimum GDP per capita over time
> for all the countries in Europe.
> Modify it again to plot the maximum GDP per capita over time for Europe.
>
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
> > ~~~
> > data_europe = pd.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
> > data_europe.min().plot(label='min')
> > data_europe.max().plot(label='max')
> > plt.legend(loc='best')
> > plt.xticks(rotation=90)
> > ~~~
> > {: .language-python}
> > ![Minima Maxima Solution](../fig/9_minima_maxima_solution.png)
> {: .solution}
{: .challenge}

> ## Correlations
>
> Modify the example in the notes to create a scatter plot showing
> the relationship between the minimum and maximum GDP per capita
> among the countries in Asia for each year in the data set.
> What relationship do you see (if any)?
>
>
> > ## Solution
> > ~~~
> > data_asia = pd.read_csv('data/gapminder_gdp_asia.csv', index_col='country')
> > data_asia.describe().T.plot(kind='scatter', x='min', y='max')
> > ~~~
> > {: .language-python}
> >
> > ![Correlations Solution 1](../fig/9_correlations_solution1.svg)
> >
> > No particular correlations can be seen between the minimum and maximum gdp values
> > year on year. It seems the fortunes of asian countries do not rise and fall together.
> {: .solution}
>
> You might note that the variability in the maximum is much higher than
> that of the minimum.  Take a look at the maximum and the max indexes:
>
> ~~~
> data_asia = pd.read_csv('data/gapminder_gdp_asia.csv', index_col='country')
> data_asia.max().plot()
> print(data_asia.idxmax())
> print(data_asia.idxmin())
> ~~~
> {: .language-python}
> > ## Solution
> > ![Correlations Solution 2](../fig/9_correlations_solution2.png)
> >
> > Seems the variability in this value is due to a sharp drop after 1972.
> > Some geopolitics at play perhaps? Given the dominance of oil producing countries,
> > maybe the Brent crude index would make an interesting comparison?
> > Whilst Myanmar consistently has the lowest gdp, the highest gdb nation has varied
> > more notably.
> {: .solution}
{: .challenge}

> ## More Correlations
>
> This short program creates a plot showing
> the correlation between GDP and life expectancy for 2007,
> normalizing marker size by population:
>
> ~~~
> data_all = pd.read_csv('data/gapminder_all.csv', index_col='country')
> data_all.plot(kind='scatter', x='gdpPercap_2007', y='lifeExp_2007',
>               s=data_all['pop_2007']/1e6)
> ~~~
> {: .language-python}
>
> Using online help and other resources,
> explain what each argument to `plot` does.
>
> > ## Solution
> > ![More Correlations Solution](../fig/9_more_correlations_solution.svg)
> >
> > A good place to look is the documentation for the plot function -
> > help(data_all.plot).
> >
> > kind - As seen already this determines the kind of plot to be drawn.
> >
> > x and y - A column name or index that determines what data will be
> > placed on the x and y axes of the plot
> >
> > s - Details for this can be found in the documentation of plt.scatter.
> > A single number or one value for each data point. Determines the size
> > of the plotted points.
> {: .solution}
{: .challenge}

> ## Saving your plot to a file
> 
> If you are satisfied with the plot you see you may want to save it to a file,
> perhaps to include it in a publication. There is a function in the
> matplotlib.pyplot module that accomplishes this:
> [savefig](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html).
> Calling this function, e.g. with
> ~~~
> plt.savefig('my_figure.png')
> ~~~
> {: .language-python}
> 
> will save the current figure to the file `my_figure.png`. The file format
> will automatically be deduced from the file name extension (other formats
> are pdf, ps, eps and svg).
>
> Note that functions in `plt` refer to a global figure variable
> and after a figure has been displayed to the screen (e.g. with `plt.show`) 
> matplotlib will make this  variable refer to a new empty figure.
> Therefore, make sure you call `plt.savefig` before the plot is displayed to
> the screen, otherwise you may find a file with an empty plot.
>
> When using dataframes, data is often generated and plotted to screen in one line,
> and `plt.savefig` seems not to be a possible approach.
> One possibility to save the figure to file is then to
>
> * save a reference to the current figure in a local variable (with `plt.gcf`) 
> * call the `savefig` class method from that variable.
>
> ~~~
> data.plot(kind='bar')
> fig = plt.gcf() # get current figure
> fig.savefig('my_figure.png')
> ~~~
> {: .language-python}
{: .callout}

> ## Making your plots accessible
>
> Whenever you are generating plots to go into a paper or a presentation, there are a few things you can do to make sure that everyone can understand your plots.
> * Always make sure your text is large enough to read. Use the `fontsize` parameter in `xlabel`, `ylabel`, `title`, and `legend`, and [`tick_params` with `labelsize`](https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.tick_params.html) to increase the text size of the numbers on your axes.
> * Similarly, you should make your graph elements easy to see. Use `s` to increase the size of your scatterplot markers and `linewidth` to increase the sizes of your plot lines.
> * Using color (and nothing else) to distinguish between different plot elements will make your plots unreadable to anyone who is colorblind, or who happens to have a black-and-white office printer. For lines, the `linestyle` parameter lets you use different types of lines. For scatterplots, `marker` lets you change the shape of your points. If you're unsure about your colors, you can use [Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/) or [Color Oracle](https://colororacle.org/) to simulate what your plots would look like to those with colorblindness.
{: .callout}
