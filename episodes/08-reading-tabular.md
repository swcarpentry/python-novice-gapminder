---
layout: episode
title: "Reading Tabular Data into Data Frames"
teaching: 5
exercises: 10
questions:
- "How can I read tabular data?"
objectives:
- "Import the Pandas library."
- "Use Pandas to load a simple CSV data set."
- "Get some basic information about a Pandas Data frame."
keypoints:
- FIXME
---
- import pandas

~~~
import pandas
~~~
{: .source}

- using pandas.read_csv
- ensure reading from correct location
- store it as a variable

~~~
data_frame = pandas.read_csv("gapminder_gdp_oceania.csv")
~~~
{: .source}

- Note that row headings, or **indexes** are numbers, automatically generated
- specify row headings from a chosen column using index_col

~~~
data_frame = pandas.read_csv("gapminder_gdp_oceania.csv", index_col="country")
~~~
{: .source}

- look at info about data frame

~~~
data_frame.info()
~~~
{: .source}

- look at columns

~~~
data_frame.columns
~~~
{: .source}

- Transpose

~~~
data_frame.T
~~~
{: .source}

- Viewing top or bottom cells

~~~
df = pandas.read_csv("gapminder_gdp_europe.csv", index_col="country")

df.head()
df.tail()

df.head(10)
~~~
{: .source}

- Summary statistics by column

~~~
data_frame.describe()
~~~
{: .source}

> ## Reading Other Data
> 
> 1.  Create a new notebook called `test_loading`.
> 2.  Create a single Python cell in that notebook that contains
>     all the instructions needed to load and display the data in
>     `data/gapminder_gdp_oceania.csv'.
{: .challenge}

> ## Error Messages
> 
> The data for your current project is stored in a file called `microbes.csv`,
> which is located in a folder called `field_data`.
> You are doing analysis in a notebook called `analysis.ipynb`
> in a sibling folder called `thesis`:
> 
> ~~~
> your_home_directory
> |-- field_data/
> |   \-- microbes.csv
> |-- thesis/
> |   \-- analysis.ipynb
> ~~~
> 
> What value(s) should you pass to `read_csv` to read `microbes.csv` in `analysis.ipynb`?
{: .challenge}
