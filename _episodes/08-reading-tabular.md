---
layout: episode
title: "Reading Tabular Data"
teaching: 5
exercises: 10
questions:
- "How can I read tabular data?"
objectives:
- "Import the Pandas library."
- "Use Pandas to load a simple CSV data set."
keypoints:
- FIXME
---
FIXME: lesson content.

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
