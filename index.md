---
layout: lesson
---
This lesson is an introduction to programming Python for people with little or no previous programming experience.
It is designed to be used in both [Data Carpentry]({{ site.dc_site }}) and [Software Carpentry]({{ site.swc_site }}) workshops,
and to serve as a worked example of how to develop a new lesson.

> ## Prerequisites
>
> Learners need to understand the concepts of files and directories
> (including the working directory) and how to start a Python
> interpreter before tackling this lesson. This lesson references the Jupyter (IPython)
> Notebook although it can be taught through any Python interpreter.
> The commands in this lesson pertain to **Python 3**.
{: .prereq}

> ## Get gapminder data
> The data we will be using is taken from the [gapminder](gapminder.org) dataset.
> To obtain it, download and unzip the file [python-novice-gapminder-data.zip](python-novice-gapminder-data.zip).
> In order to follow the presented material, you should create the jupyter notebook in the "data" directory.
{: .prereq}

> ## Starting Python
>
> If you will be using the IPython or Jupyter notebook for the lesson,
> you should have already
> [installed Anaconda](http://swcarpentry.github.io/workshop-template/#setup)
> which includes the notebook.
>
> To start the notebook, open a terminal or git bash and type the command:
>
> ~~~
> $ jupyter notebook
> ~~~
>{: .source}
>
> To start the Python intrepreter without the notebook, open a terminal or git bash and type the command:
>
> ~~~
> $ python
> ~~~

> As the first step, we want to load one of the data files using Pandas library. 
>
We first import Pandas library as :
> ~~~
> import pandas
> ~~~
>
> Now that we have the library imported, we can load one of the data files in our directory:
>
> ~~~
> data = pd.read_csv("./gapminder_all.csv", header=0)
> ~~~
>
> Now we have read and stored the content of the "gapminder_all.csv" file in the "data" variable. "header=0" means the first line of the file contains the header info.
> We can look at the contents of the data using "print" command:
> ~~~
> print(data)
> ~~~
>{: .source}
{: .prereq}
