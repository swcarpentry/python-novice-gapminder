> ## Exercise: For 16-writing-functions.md 
>
> The Gapminder files have GDP per capita data
> for two years out of every decade from the 1950s to the 2000s. We
> can read a specific continent file into a dataframe with the
> index set to be the country names, and extract GDP data for a
> specific country as shown in the example code below (we will
> assume that pandas has been imported with
> abbreviation `pd` and that we are in the directory `data`):
>
> ~~~ 
> df = pd.read_csv('gapminder_gdp_asia.csv',delimiter=',',index_col=0)
> nippon = df.ix["Japan"]
> ~~~
> {: .source}
>
> 1. Complete the statements below to obtain the average GDP for
>   Japan across the two reported 1980s years in the data.
>
> ~~~ 
>
> year = 1983
> gdp_decade = 'gdpPercap_'+str(year // ____)
> avg = (nippon.ix[gdp_decade + ___]+nippon.ix[gdp_decade + ___])/2
> 
> ~~~
> {: .source}
>
> 2. Now *abstract* the code above into a single function (assume
>   that `pandas` is imported as `pd`) 
>
> ~~~
>
> def avg_gdp_in_decade(country, continent, year):
>     """Returns the average GDP per capita
>
>     Compute the average reported GDP per capita for the country in the
>     given continent for the decade to which the year belongs.
>
>     country, continent: strings (e.g. 'japan' and 'asia' respectively)
>     year: integer between 1950 and 2009 inclusive (e.g. 1983)
>     """
>     df = pd.read_csv('gapminder_gdp_'+___+'.csv',delimiter=',',index_col=0)
>     ___
>     ___
>     ___
>     return avg
>
> ~~~
> {: .source}
>
> 3. How would you generalize this function's code if you did not
>    know beforehand which specific years occurred as columns in the data? For
>    instance, what if we also had data from years ending in 1 and
>    9 for each decade? (*Hint: * Use the columns to filter out
>    the ones that correspond to the decade, instead of
>    enumerating them in the code.) 
>
> > ## Solution
> >
> > >Note: While the exercise is eventually about encapsulating a
> > >sequence of useful parametrized statements into a function, it
> > >also engages the learners in thinking about and practicing numeric
> > >operations (integer versus float division), string
> > >operations (concatenation; conversion from types; prefix
> > >matching), and pandas dataframe/series indexing. Part 3 is
> > >bit more advanced because a solution requires using loops (or
> > >list comprehension or `filter` for the more seasoned
> > >programmers) to accumulate the relevant data and compute its average.
> >
> > 1. 
> > ~~~ 
> >
> > year = 1983
> > gdp_decade = 'gdpPercap_'+str(year // 10)
> > avg = (nippon.ix[gdp_decade + '2']+nippon.ix[gdp_decade + '7'])/2
> > 
> > ~~~
> > {: .source}
> >
> > 2. Function docstring omitted in the solution for brevity.
> > ~~~
> >
> > def avg_gdp_in_decade(country, continent, year):
> >     df = pd.read_csv('gapminder_gdp_'+continent+'.csv',delimiter=',',index_col=0)
> >     c = df.ix[country]
> >     gdp_decade = 'gdpPercap_'+str(year // 10)
> >     avg = (c.ix[gdp_decade + '2'] + c.ix[gdp_decade + '7'])/2
> >     return avg
> >
> > ~~~
> > {: .source}
> >
> > 3. We need to loop over the reported years to obtain the 
> >    average over the relevant ones in the data.
> > ~~~
> >
> > def avg_gdp_in_decade(country, continent, year):
> >     df = pd.read_csv('gapminder_gdp_'+continent+'.csv',delimiter=',',index_col=0)
> >     c = df.ix[country] 
> >     gdp_decade = 'gdpPercap_'+str(year // 10)
> >     total = 0.0
> >     num_years = 0
> >     for yr_header in c.index: # c's index contains reported years
> >         if yr_header.startswith(gdp_decade):
> >             total = total + c.ix[yr_header] # or can use +=
> >             num_years = num_years+1  # or can use +=
> >     return total/num_years
> >
> > ~~~
> > {: .source}
> > {: .solution}
> {: .challenge}
