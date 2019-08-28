---
layout: page
title: "Setup"
permalink: /setup/
root: ..
---

## Installing Python

[Python][python] is a popular language for scientific computing, and great for general-purpose 
programming as well. Installing all of its scientific packages individually can be a bit 
difficult, however, so we recommend using [Miniconda Python Distribution][miniconda] from 
[Anaconda][anaconda] for your OS. Miniconda is mini version of the 
[Anaconda Python Distribution][anaconda-distribution] that includes Python as well as the Conda 
environment and package management tool (and its core dependencies). If, however, you would prefer 
to install the full Anaconda Python Distribution, instructions are also provided below.

> ## Prefer Miniconda to Anaconda
>
> I suggest installing Miniconda which combines Conda with Python 3 (and a small number of core 
> systems packages) instead of the full Anaconda distribution. Installing only Miniconda will 
> encourage you to create separate environments for each project (and to install only those packages 
> that you actually need for each project!). Project specific environments enhance portability and 
> reproducibility of your research and workflows. 
> 
> Besides, if you *really* want the full Anaconda distribution you can always create an new conda 
> environment and install it using the following command.
>
> ~~~
> $ conda create --name my-anaconda-env anaconda=5.3
> ~~~
> {: .language-bash}
>
> We will discuss the above command in great depth in this lesson.
{: .callout}

Regardless of how you choose to install it, please make sure you install Python 3 version of the 
installer. Also, please set up your python environment at least a day in advance of the workshop. 
If you encounter problems with the installation procedure, ask your workshop organizers via e-mail 
for assistance so you are ready to go as soon as the workshop begins.

### Installing Python Using Miniconda

First check whether Conda has already been installed on your local machine by running the 
following command in a terminal if you are running macOS or Linux.

~~~
$ which conda
/Users/$USERNAME/miniconda3/bin/conda
~~~
{: .language-bash}

If Conda has already been installed on your machine, then this command should return the 
absolute path to the `conda` executable.

Windows users will need to search for the "Anaconda Powershell Prompt". If this program is already 
installed, then Conda has also already been installed on your machine.

If Conda has not been installed on your machine, then install the Python 3 version of 
[Miniconda][miniconda] from Anaconda for your OS. Miniconda is a mini version of the 
[Anaconda Python distribution](https://www.anaconda.com/distribution/) that includes only Conda 
and its dependencies.

### Installing Python Using Anaconda

The exact procedure for installing the full Anaconda Python Distibution differs slightly depending 
on your OS.

#### Windows - [Video tutorial][video-windows]

1. Open [https://www.anaconda.com/download][anaconda-windows]
   with your web browser.

2. Download the Python 3 installer for Windows.

3. Double-click the executable and install Python 3 using _MOST_ of the default settings. The only 
   exception is to check the **Make Anaconda the default Python** option.

#### Mac OS X - [Video tutorial][video-mac]

1. Open [https://www.anaconda.com/download][anaconda-mac]
   with your web browser.

2. Download the Python 3 installer for OS X.

3. Install Python 3 using all of the defaults for installation.

#### Linux

Note that the following installation steps require you to work from the shell. 
If you run into any difficulties, please request help before the workshop begins.

1.  Open [https://www.anaconda.com/download][anaconda-linux] with your web browser.

2.  Download the Python 3 installer for Linux.

3.  Install Python 3 using all of the defaults for installation.

    a.  Open a terminal window.

    b.  Navigate to the folder where you downloaded the installer

    c.  Type

    ~~~
    $ bash Anaconda3-
    ~~~
    {: .bash}

    and press tab.  The name of the file you just downloaded should appear.

    d.  Press enter.

    e.  Follow the text-only prompts.  When the license agreement appears (a colon
        will be present at the bottom of the screen) hold the down arrow until the 
        bottom of the text. Type `yes` and press enter to approve the license. Press 
        enter again to approve the default location for the files. Type `yes` and 
        press enter to prepend Anaconda to your `PATH` (this makes the Anaconda 
        distribution the default Python).

## Getting the Data

The data we will be using is taken from the [gapminder][gapminder] dataset.
To obtain it, download and unzip the file 
[python-novice-gapminder-data.zip]({{page.root}}/files/python-novice-gapminder-data.zip).
In order to follow the presented material, you should launch the JupyterLab 
server in the root directory (see [Starting JupyterLab]({{ page.root }}/01-run-quit/#starting-jupyterlab)).


[anaconda]: https://www.anaconda.com/
[anaconda-mac]: https://www.anaconda.com/download/#macos
[anaconda-linux]: https://www.anaconda.com/download/#linux
[anaconda-windows]: https://www.anaconda.com/download/#windows
[gapminder]: https://en.wikipedia.org/wiki/Gapminder_Foundation
[jupyter]: http://jupyter.org/
[python]: https://python.org
[video-mac]: https://www.youtube.com/watch?v=TcSAln46u9U
[video-windows]: https://www.youtube.com/watch?v=xxQ0mzZ8UvA