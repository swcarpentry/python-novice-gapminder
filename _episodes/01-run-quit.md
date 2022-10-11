---
title: "Running and Quitting"
teaching: 15
exercises: 0
questions:
- "How can I run Python programs?"
objectives:
- "Launch the JupyterLab server." 
- "Create a new Python script." 
- "Create a Jupyter notebook."
- "Shutdown the JupyterLab server."
- "Understand the difference between a Python script and a Jupyter notebook."
- "Create and run Python cells in a notebook."
keypoints:
- "Python scripts are plain text files."
- "Use the Jupyter Notebook for editing and running Python."
- "The Notebook has Command and Edit modes."
- "Use the keyboard and mouse to select and edit cells."
---

Many software developers will often use an integrated development environment (IDE) or a 
text editor to create and edit their Python programs which can be executed through the IDE or command line directly. While this is a common approach, we are going to use the [Jupyter Notebook][jupyter] via [JupyterLab][jupyterlab] for the remainder of this workshop.

This has several advantages:
  *   You can easily type, edit, and copy and paste blocks of code.
  *   Tab complete allows you to easily access the names of things you are using
      and learn more about them.
  *   It allows you to annotate your code with links, different sized text, bullets, etc.
      to make it more accessible to you and your collaborators.
  *   It allows you to display figures next to the code that produces them
      to tell a complete story of the analysis.

Each notebook contains one or more cells that contain code, text, or images.

## Getting Started with JupyterLab

JupyterLab is an application with a web-based user interface from [Project Jupyter][jupyter] that 
enables one to work with documents and activities such as Jupyter notebooks, text editors, terminals,
and even custom components in a flexible, integrated, and extensible manner. JupyterLab requires a
reasonably up-to-date browser (ideally a current version of Chrome, Safari, or Firefox); Internet
Explorer versions 9 and below are *not* supported.

JupyterLab is included as part of the Anaconda Python distribution. If you have not already
installed the Anaconda Python distribution, see [the setup instructions]({{ page.root }}{% link
setup.md %})
for installation instructions.

Even though JupyterLab is a web-based application, JupyterLab runs locally on your machine and 
does not require an internet connection.
*   The JupyterLab server sends messages to your web browser.
*   The JupyterLab server does the work and the web browser renders the result.
*   You will type code into the browser and see the result when the web page talks to the 
    JupyterLab server.

> ## JupyterLab? What about Jupyter notebooks?
> 
> JupyterLab is the [next stage in the evolution of the Jupyter Notebook](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html#overview).
> If you have prior experience working with Jupyter notebooks, then you will have a good idea of what to expect from JupyterLab. 
> 
> Experienced users of Jupyter notebooks interested in a more detailed discussion of the similarities and differences
> between the JupyterLab and Jupyter notebook user interfaces can find more information in the 
> [JupyterLab user interface documentation][jupyterlab-ui].
{: .callout}

## Starting JupyterLab

You can start the JupyterLab server through the command line or through an application called 
`Anaconda Navigator`. Anaconda Navigator is included as part of the Anaconda Python distribution.

### macOS - Command Line
To start the JupyterLab server you will need to access the command line through the Terminal. 
There are two ways to open Terminal on Mac.

1. In your Applications folder, open Utilities and double-click on Terminal
2. Press <kbd>Command</kbd> + <kbd>spacebar</kbd> to launch Spotlight. Type `Terminal` and then 
double-click the search result or hit <kbd>Enter</kbd>

After you have launched Terminal, type the command to launch the JupyterLab server.

~~~
$ jupyter lab
~~~
{: .bash}

### Windows Users - Command Line
To start the JupyterLab server you will need to access the Anaconda Prompt.

Press <kbd>Windows Logo Key</kbd> and search for `Anaconda Prompt`, click the result or press enter.

After you have launched the Anaconda Prompt, type the command:

~~~
$ jupyter lab
~~~
{: .bash}

###  Anaconda Navigator

To start a JupyterLab server from Anaconda Navigator you must first [start Anaconda Navigator (click for detailed instructions on macOS, Windows, and Linux)](https://docs.anaconda.com/anaconda/navigator/getting-started/#starting-navigator). You can search for Anaconda Navigator via Spotlight on macOS (<kbd>Command</kbd> + <kbd>spacebar</kbd>), the Windows search function (<kbd>Windows Logo Key</kbd>) or opening a terminal shell and executing the `anaconda-navigator` executable from the command line.

After you have launched Anaconda Navigator, click the `Launch` button under JupyterLab. You may need
to scroll down to find it.

Here is a screenshot of an Anaconda Navigator page similar to the one that should open on either macOS
or Windows.

<p align='center'>
  <img alt="Anaconda Navigator landing page" src="../fig/0_anaconda_navigator_landing_page.png" width="750"/>
</p>

And here is a screenshot of a JupyterLab landing page that should be similar to the one that opens in your 
default web browser after starting the JupyterLab server on either macOS or Windows.

<p align='center'>
  <img alt="JupyterLab landing page" src="../fig/0_jupyterlab_landing_page.png" width="750"/>
</p>

## The JupyterLab Interface

JupyterLab has many features found in traditional integrated development environments (IDEs) but 
is focused on providing flexible building blocks for interactive, exploratory computing.

The [JupyterLab Interface](https://jupyterlab.readthedocs.io/en/stable/user/interface.html) 
consists of the Menu Bar, a collapsable Left Side Bar, and the Main Work Area which contains tabs 
of documents and activities.

### Menu Bar

The Menu Bar at the top of JupyterLab has the top-level menus that expose various actions 
available in JupyterLab along with their keyboard shortcuts (where applicable). The following 
menus are included by default.

*   **File:** Actions related to files and directories such as *New*, *Open*, *Close*, *Save*, etc. The *File* menu also includes the *Shut Down* action used to shutdown the JupyterLab server.
*   **Edit:** Actions related to editing documents and other activities such as *Undo*, *Cut*, *Copy*, *Paste*, etc.
*   **View:** Actions that alter the appearance of JupyterLab.
*   **Run:** Actions for running code in different activities such as notebooks and code consoles (discussed below).
*   **Kernel:** Actions for managing kernels. Kernels in Jupyter will be explained in more detail below.
*   **Tabs:** A list of the open documents and activities in the main work area.
*   **Settings:** Common JupyterLab settings can be configured using this menu. There is also an *Advanced Settings Editor* option in the dropdown menu that provides more fine-grained control of JupyterLab settings and configuration options.
*   **Help:** A list of JupyterLab and kernel help links.

> ## Kernels
> The JupyterLab [docs](https://jupyterlab.readthedocs.io/en/stable/user/documents_kernels.html) 
> define kernels as "separate processes started by the server that run your code in different programming languages and environments."
> When we open a Jupyter Notebook, that starts a kernel - a process - that is going to run the code. 
> In this lesson, we'll be using the Jupyter ipython kernel which lets us run Python 3 code interactively.
> 
> Using other Jupyter [kernels for other programming languages](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) would let us 
> write and execute code in other programming languages in the same JupyterLab interface, like R, Java, Julia, Ruby, JavaScript, Fortran, 
> etc.
> 
{: .callout}

A screenshot of the default Menu Bar is provided below.

<p align='center'>
    <img alt="JupyterLab Menu Bar" src="../fig/0_jupyterlab_menu_bar.png" width="750"/>
</p>

### Left Sidebar

The left sidebar contains a number of commonly used tabs, such as a file browser (showing the 
contents of the directory where the JupyterLab server was launched), a list of running kernels 
and terminals, the command palette, and a list of open tabs in the main work area. A screenshot of 
the default Left Side Bar is provided below.

<p align='center'>
    <img alt="JupyterLab Left Side Bar" src="../fig/0_jupyterlab_left_side_bar.png" width="250"/>
</p>

The left sidebar can be collapsed or expanded by selecting “Show Left Sidebar” in the View menu or 
by clicking on the active sidebar tab.

### Main Work Area

The main work area in JupyterLab enables you to arrange documents (notebooks, text files, etc.) 
and other activities (terminals, code consoles, etc.) into panels of tabs that can be resized or 
subdivided. A screenshot of the default Main Work Area is provided below.

<p align='center'>
    <img alt="JupyterLab Main Work Area" src="../fig/0_jupyterlab_main_work_area.png" width="750"/>
</p>

Drag a tab to the center of a tab panel to move the tab to the panel. Subdivide a tab panel by 
dragging a tab to the left, right, top, or bottom of the panel. The work area has a single current 
activity. The tab for the current activity is marked with a colored top border (blue by default).

## Creating a Python script

*   To start writing a new Python program click the Text File icon under the *Other* header in the Launcher tab of the Main Work Area.
    *   You can also create a new plain text file by selecting the *New -> Text File* from the *File* menu in the Menu Bar.
*   To convert this plain text file to a Python program, select the *Save File As* action from the *File* menu in the Menu Bar and give your new text file a name that ends with the `.py` extension.
    *   The `.py` extension lets everyone (including the operating system) know that this text file is a Python program.
    *   This is convention, not a requirement.

## Creating a Jupyter Notebook

To open a new notebook click the Python 3 icon under the *Notebook* header in the Launcher tab in 
the main work area. You can also create a new notebook by selecting *New -> Notebook* from the *File* menu in the Menu Bar.

Additional notes on Jupyter notebooks.

  *   Notebook files have the extension `.ipynb` to distinguish them from plain-text Python programs.
  *   Notebooks can be exported as Python scripts that can be run from the command line.

Below is a screenshot of a Jupyter notebook running inside JupyterLab. If you are interested in 
more details, then see the [official notebook documentation][jupyterlab-notebook-docs].

<p align='center'>
    <img alt="Example Jupyter Notebook" src="../fig/0_jupyterlab_notebook_screenshot.png" width="750"/>
</p>

> ## How It's Stored
>
> *   The notebook file is stored in a format called JSON.
> *   Just like a webpage, what's saved looks different from what you see in your browser.
> *   But this format allows Jupyter to mix source code, text, and images, all in one file.
{: .callout}

> ## Arranging Documents into Panels of Tabs
>
> In the JupyterLab Main Work Area you can arrange documents into panels of tabs. Here is an 
> example from the [official documentation][jupyterlab].
> 
> <p align='center'>
>    <img alt="Multi-panel JupyterLab" src="../fig/0_multipanel_jupyterlab_screenshot.png" width="750"/>
> </p>
>
> First, create a text file, Python console, and terminal window and arrange them into three 
> panels in the main work area. Next, create a notebook, terminal window, and text file and 
> arrange them into three panels in the main work area. Finally, create your own combination of 
> panels and tabs. What combination of panels and tabs do you think will be most useful for your 
> workflow?
>
> > ## Solution
> >
> > After creating the necessary tabs, you can drag one of the tabs to the center of a panel to 
> > move the tab to the panel; next you can subdivide a tab panel by dragging a tab to the left, 
> > right, top, or bottom of the panel.
> {: .solution}
{: .challenge}

> ## Code vs. Text
>
> Jupyter mixes code and text in different types of blocks, called cells. We often use the term
> "code" to mean "the source code of software written in a language such as Python".
> A "code cell" in a Notebook is a cell that contains software;
> a "text cell" is one that contains ordinary prose written for human beings.
{: .callout}

## The Notebook has Command and Edit modes.

*   If you press <kbd>Esc</kbd> and <kbd>Return</kbd> alternately, the outer border of your code cell will change from gray to blue.
*   These are the **Command** (gray) and **Edit** (blue) modes of your notebook.
*   Command mode allows you to edit notebook-level features, and Edit mode changes the content of cells.
*   When in Command mode (esc/gray),
    *   The <kbd>b</kbd> key will make a new cell below the currently selected cell.
    *   The <kbd>a</kbd> key will make one above.
    *   The <kbd>x</kbd> key will delete the current cell.
    *   The <kbd>z</kbd> key will undo your last cell operation (which could be a deletion, creation, etc).
*   All actions can be done using the menus, but there are lots of keyboard shortcuts to speed things up.

> ## Command Vs. Edit
>
> In the Jupyter notebook page are you currently in Command or Edit mode?  
> Switch between the modes. 
> Use the shortcuts to generate a new cell. 
> Use the shortcuts to delete a cell.
> Use the shortcuts to undo the last cell operation you performed.
>
> > ## Solution
> >
> > Command mode has a grey border and Edit mode has a blue border. 
> > Use <kbd>Esc</kbd> and <kbd>Return</kbd> to switch between modes. 
> > You need to be in Command mode (Press <kbd>Esc</kbd> if your cell is blue).  Type <kbd>b</kbd> or <kbd>a</kbd>.
> > You need to be in Command mode (Press <kbd>Esc</kbd> if your cell is blue).  Type <kbd>x</kbd>.
> > You need to be in Command mode (Press <kbd>Esc</kbd> if your cell is blue).  Type <kbd>z</kbd>.
> {: .solution}
{: .challenge}

### Use the keyboard and mouse to select and edit cells.

*   Pressing the <kbd>Return</kbd> key turns the border blue and engages Edit mode, which allows 
    you to type within the cell.
*   Because we want to be able to write many lines of code in a single cell,
    pressing the <kbd>Return</kbd> key when in Edit mode (blue) moves the cursor to the next line 
    in the cell just like in a text editor.
*   We need some other way to tell the Notebook we want to run what's in the cell.
*   Pressing <kbd>Shift</kbd>+<kbd>Return</kbd> together will execute the contents of the cell.
*   Notice that the <kbd>Return</kbd> and <kbd>Shift</kbd> keys on the right of the keyboard are 
    right next to each other.


> ## More Math
>
> What is displayed when a Python cell in a notebook
> that contains several calculations is executed?
> For example, what happens when this cell is executed?
>
> ~~~
> 7 * 3
> 2 + 1
> ~~~
> {: .language-python}
> 
> > ## Solution
> >
> > Python returns the output of the last calculation.
> > ~~~
> > 3
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

## Closing JupyterLab

*   From the Menu Bar select the "File" menu and then choose "Shut Down" at the bottom of the dropdown menu. You will be prompted to confirm that you wish to shutdown the JupyterLab server (don't forget to save your work!). Click "Shut Down" to shutdown the JupyterLab server.
*   To restart the JupyterLab server you will need to re-run the following command from a shell.

~~~
$ jupyter lab
~~~

> ## Closing JupyterLab
>
> Practice closing and restarting the JupyterLab server.
{: .challenge}

[anaconda]: https://docs.continuum.io/anaconda/install
[jupyterlab]: https://jupyterlab.readthedocs.io/en/stable/
[jupyterlab-ui]: https://jupyterlab.readthedocs.io/en/stable/user/interface.html
[jupyterlab-notebook-docs]: https://jupyterlab.readthedocs.io/en/stable/user/notebook.html

{% include links.md %}
