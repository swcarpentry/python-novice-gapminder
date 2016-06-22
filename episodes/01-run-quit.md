---
layout: episode
title: "Running and Quitting"
teaching: 15
exercises: 0
questions:
- "How can I run Python programs?"
objectives:
- "Launch the Jupyter Notebook, create new notebooks, and exit the Notebook."
- "Create Markdown cells in a notebook."
- "Create and run Python cells in a notebook."
keypoints:
- FIXME
---
### Python Programs are plain text files.

*   They have the ".py" extension to let everyone know (including the operating system) it is a Python program.
*   It's common to write them using a text editor but we are going to use the Jupyter notebook.
*   The bit of extra setup is well worth it because the notebook provides code completion and other helpful features.
*   The notebooks have the extension ".ipynb" to distinguish them from plain text python programs.

### The Jupyter Notebook

*   The [Anaconda package manager][anaconda] is an automated way to install the Jupyter notebook.
*   It also installs all the extra libraries it needs to run.
*   Once you have installed Python and the Jupyter Notebook requirements, open a bash shell and type:

~~~
$ jupyter notebook .
~~~
{: .source}

*   This will start a Jupyter Notebook server and open your default web browser.
*   The server sends messages to your browser.
*   The server does the work and the web browser renders the notebook.
*   You can type code into the browser and see the result when the web page talks to the server.
*   FIXME: what advantages are there to this arrangement?
*   The notebook is stored as JSON.
*   Just like a webpage, the saved notebook looks different to what you see when it gets rendered by your browser.

### Control and Edit modes

*   Open a new notebook from the dropdown menu in the top right corner of the file browser page.
*   If you press "esc" and "return" alternately, you will see the surround of your code cell change from blue to green.
*   The difference in colour is subtle.
*   These are the control and edit modes of your notebook.
*   If you use the "esc" and "return" keys to make the surround blue and then press the "H" key, a list of all the shortcut keys will appear.

*   When in control mode (esc/Blue),
    *   The "B" key will make a new cell below the currently selected cell.
    *   The "A" key will make one above.
    *   The "X" key will delete the current cell.
*   There are lots of shortcuts you can try out and most actions can done with the menus at the top of the page if you forget the shortcuts.
*   *If you first remember the "esc" and "H" shortcut, you will be able to find out all the rest.*

*   Pressing the "return" key turns the surround green to signify edit mode and you can type code into the cell.
*   Because we want to be able to write many lines of code in a single cell, the "return" key will do what it normally does.
*   It moves the cursor to the next line just like in a text editor.
*   We need some other way to tell the Notebook we want to execute the code in the cell.
*   Pressing the "return" key and the "shift" key together will execute the code in the cell.
*   Notice that the "return" and "shift" keys on the right of the keyboard are right next to each other.

### Markdown

*   Notebooks can also render Markdown.
*   Turn the current cell into a Markdown cell by entering the control mode (esc/blue) and press the "M" key.
*   The `In [ ]:` will disappear to show it is no longer a code cell and you will be able to write in Markdown.
*   FIXME: how do you turn a Markdown cell back into a code cell?

> ## Creating Lists
>
> Create a numbered list in a Markdown cell in a notebook
> that looks like this:
>
> 1.  Get funding.
> 2.  Design experiment.
> 3.  Collect data.
> 4.  Analyze.
> 5.  Write up.
> 6.  Publish.
{: .challenge}

> ## More Math
>
> What is displayed when a Python cell in a notebook
> that contains several calculations
> is executed?
> For example,
> what happens when this cell is executed?
>
> ~~~
> 7 * 3
> 2 + 1
> ~~~
> {: .source}
{: .challenge}

> ## Change an Existing Cell from Code to Markdown
> What if you already wrote some code in into your *code cell* and then you switch it to a *markdown cell*?
> Give it a try; type the following into a cell in *Edit Mode*:
> 
> ~~~
> x = 6 * 7 + 12
> print(x)
> ~~~ 
> {: .python}
> 
> Now run the cell to be sure that it works as a code cell (shift + return). 
> 
> Now go back to the cell, press escape to make sure you're in *Control Mode*, and press the "M" key. Now try running the cell (shift + return). 
>
> What happened and how might this be useful? 
> 
> As an added challenge, try changing back to a code cell by pressing the "Y" key from the *Control Mode*. 
{: .challenge}

[anaconda]: https://docs.continuum.io/anaconda/install
