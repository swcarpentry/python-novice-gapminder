---
title: "Setup"
---

## Installing Python Using Anaconda

[Python][python] is a popular language for scientific computing, and great for
general-purpose programming as well. Installing all of its scientific packages
individually can be a bit difficult, however, so we recommend the all-in-one
installer [Anaconda][anaconda].

Regardless of how you choose to install it, please make sure you install Python
version 3.x (e.g., 3.4 is fine). Also, please set up your python environment at
least a day in advance of the workshop.  If you encounter problems with the
installation procedure, ask your workshop organizers via e-mail for assistance so
you are ready to go as soon as the workshop begins.

### Windows - [Video tutorial][video-windows]

1. Open [https://www.anaconda.com/distribution/][anaconda-windows] with your web browser.

2. Download the Python 3 installer for Windows.

3. Double-click the executable and install Python 3 using the recommended settings. Make sure that **Register Anaconda as my default Python 3.x** option is checked - it should be in the latest version of Anaconda

### Mac OS X - [Video tutorial][video-mac]

1. Visit [https://www.anaconda.com/distribution/][anaconda-mac] with your web browser.

2. Download the Python 3 installer for OS X. These instructions assume that you use the graphical installer `.pkg` file.

3. Follow the Python 3 installation instructions. Make sure that the install location is set to "Install only for me" so Anaconda will install its files locally, relative to your home directory. Installing the software for all users tends to create problems in the long run and should be avoided.


### Linux

Note that the following installation steps require you to work from the shell.
If you run into any difficulties, please request help before the workshop begins.

1.  Open [https://www.anaconda.com/distribution/][anaconda-linux] with your web browser.

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
        will be present at the bottom of the screen) press the space bar until you see the
        bottom of the text. Type `yes` and press enter to approve the license. Press
        enter again to approve the default location for the files. Type `yes` and
        press enter to prepend Anaconda to your `PATH` (this makes the Anaconda
        distribution your user's default Python).

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
