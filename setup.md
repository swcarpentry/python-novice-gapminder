---
layout: page
title: "Setup"
permalink: /setup/
---

## Getting the Data

The data we will be using is taken from the [gapminder](gapminder.org) dataset.
To obtain it, download and unzip the file [python-novice-gapminder-data.zip](python-novice-gapminder-data.zip).
In order to follow the presented material, you should create the Jupyter notebook in the "data" directory.

## Starting Python

If you will be using the IPython or Jupyter notebook for the lesson,
you should have already
[installed Anaconda](http://swcarpentry.github.io/workshop-template/#setup)
which includes the notebook.

To start the notebook, open a terminal or git bash and type the command:

~~~
$ jupyter notebook
~~~
{: .source}

To start the Python intrepreter without the notebook, open a terminal or git bash and type the command:

~~~
$ python
~~~
{: .source}

## Installation Using Anaconda

[Python](https://python.org) is a popular language for scientific computing, and great for
general-purpose programming as well. Installing all of its scientific packages
individually can be a bit difficult, so we recommend
[Anaconda](https://www.continuum.io/anaconda), an all-in-one
installer.

Regardless of how you choose to install it, please make sure you install Python
version 3.x (e.g., 3.4 is fine).

We will teach Python using the Jupyter notebook, a programming environment that
runs in a web browser. For this to work you will need a reasonably up-to-date
browser. The current versions of the Chrome, Safari and Firefox browsers are all
supported (some older browsers, including Internet Explorer version 9 and below,
are not).  Enumerated below are setup instructions for Windows, Mac OS X, and
Linux.  Please setup your python environment at least a day in advance of the
workshop.  If you encounter problems with the installation procedure, please ask
your workshop organizers via e-mail for assistance getting set up.

### Windows - [Video tutorial](https://www.youtube.com/watch?v=xxQ0mzZ8UvA)

1. Open [http://continuum.io/downloads](http://continuum.io/downloads) with your web browser.

2. Download the Python 3 installer for Windows.

3. Install Python 3 using all of the defaults for installation except make sure to
   check **Make Anaconda the default Python**.

### Mac OS X - [Video tutorial](https://www.youtube.com/watch?v=TcSAln46u9U)

1. Open [http://continuum.io/downloads](http://continuum.io/downloads) with your web browser.

2. Download the Python 3 installer for OS X.

3. Install Python 3 using all of the defaults for installation.

### Linux

1.  Open [http://continuum.io/downloads](http://continuum.io/downloads) with your web browser.

2.  Download the Python 3 installer for OS X.

3.  Install Python 3 using all of the defaults for installation.  Note that
    installation requires using the shell, if you aren't comfortable doing then
    installation yourself then stop here and request help before the workshop
    begins.

4.  Open a terminal window.

5.  Type

    ~~~
    $ bash Anaconda3-
    ~~~
    {: .source}

    and press tab.  The name of the file you just downloaded should appear.

6.  Press enter.  You will follow the text-only prompts.  When there is a colon
    at the bottom of the screen press the down arrow to move down through the text.
    Type `yes` and press enter to approve the license. Press enter to approve the
    default location for the files. Type `yes` and press enter to prepend Anaconda to
    your `PATH` (this makes the Anaconda distribution the default Python).

## Get Gapminder Data

The data we will be using is taken from the [gapminder](gapminder.org) dataset.
To obtain it, download and unzip the file
[python-novice-gapminder-data.zip]({{ site.github.repository_url }}/python-novice-gapminder-data.zip).
In order to follow the presented material, you should create the Jupyter notebook in the "data" directory.
