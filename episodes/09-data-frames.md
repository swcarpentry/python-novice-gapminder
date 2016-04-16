---
layout: episode
title: Pandas Data Frames
teaching: 10
exercises: 10
questions:
- "How can do statistical analysis of tabular data?"
objectives:
- "Select individual values from a Pandas data frame."
- "Select entire rows or entire columns from a data frame."
- "Select a subset of both rows and columns from a data frame in a single operation."
- "Select a subset of a data frame by a single Boolean criterion."
---
FIXME: lesson content.

> ## Selection
> 
> Assume Pandas has been imported into your notebook
> and the Gapminder GDP data for Europe has been loaded:
> 
> ~~~
> import pandas as pd
> 
> data = pd.read_csv('data/gapminder_gd_europe.csv')
> ~~~
> {: .source}
> 
> Write an expression to select each of the following:
> 
> 1. GDP per capita for all countries in 1982.
> 2. GDP per capita for Denmark for all years.
> 3. GDP per capita for all countries for years *after* 1985.
> 4. GDP per capita for each country in 2007 as a multiple of GDP per capita for that country in 1952.
{: .challenge}

> ## Interpretation
> 
> Poland's borders have been stable since 1945,
> but changed several times in the years before then.
> How would you handle this
> if you were creating a table of GDP per capita for Poland in the Twentieth Century?
{: .challenge}
