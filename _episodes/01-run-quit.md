---
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
- "Python programs are plain text files."
- "Use the Jupyter Notebook for editing and running Python."
- "The Notebook has Command and Edit modes."
- "Use the keyboard and mouse to select and edit cells."
- "The Notebook will turn Markdown into pretty-printed documentation."
- "Markdown does most of what HTML does."
---
## Python programs are plain text files.

*   They have the `.py` extension to let everyone (including the operating system) 
    know it is a Python program.
    *   This is convention, not a requirement.
*   It's common to write them using a text editor but we are going to use
    the [Jupyter Notebook][jupyter].
*   The bit of extra setup is well worth it because the Notebook provides code completion 
    and other helpful features.
*   Notebook files have the extension `.ipynb` to distinguish them from plain-text Python programs.
    *   Can export as "pure Python" to run from the command line.

## Use the Jupyter Notebook for editing and running Python.

*   The [Anaconda package manager][anaconda] is an automated way to install the Jupyter notebook.
    *   See [the setup instructions]({{ page.root }}/setup/) for Anaconda installation instructions.
*   It also installs all the extra libraries it needs to run.
*   Once you have installed Python and the Jupyter Notebook requirements, open a shell and type:

    ~~~
    $ jupyter notebook
    ~~~

*   This will start a Jupyter Notebook server and open your default web browser. 
*   The server runs locally on your machine only and does not use an internet connection.
*   The server sends messages to your browser.
*   The server does the work and the web browser renders the notebook.
*   You can type code into the browser and see the result when the web page talks to the server.
*   This has several advantages:
    *   You can easily type, edit, and copy and paste blocks of code.
    *   Tab complete allows you to easily access the names of things you are using
        and learn more about them.
    *   It allows you to annotate your code with links, different sized text, bullets, etc.
        to make it more accessible to you and your collaborators.
    *   It allows you to display figures next to the code that produces them
        to tell a complete story of the analysis.

![Example Jupyter Notebook](../fig/0_jupyter_notebook_example.jpg)  
*Screenshot of a [Jupyter Notebook on quantum mechanics](https://github.com/jrjohansson/qutip-lectures) by Robert Johansson*

> ## How It's Stored
>
> *   The notebook file is stored in a format called JSON.
> *   Just like a webpage, what's saved looks different from what you see in your browser.
> *   But this format allows Jupyter to mix source code, text, and images, all in one file.
{: .callout}

> ## Code vs. Text
>
> Jupyter mixes code and text in different types of blocks, called cells. We often use the term
> "code" to mean "the source code of software written in a language such as Python".
> A "code cell" in a Notebook is a cell that contains software;
> a "text cell" is one that contains ordinary prose written for human beings.
{: .callout}

## The Notebook has Command and Edit modes.

*   Open a new notebook from the dropdown menu (that says 'New') in the top right corner of the file browser page.
*   Each notebook contains one or more cells that contain code, text, or images.
*   If you press <kbd>Esc</kbd> and <kbd>Return</kbd> alternately,
    the outer border of your code cell will change from gray/blue to green.
    *   The difference in color is subtle.
*   These are the **Command** (gray) and **Edit** (green) modes of your notebook.
*   In Command mode, pressing the <kbd>H</kbd> key will provide 
    a list of all the shortcut keys.
*   Command mode allows you to edit notebook-level features, and Edit mode changes the content of cells.
*   When in Command mode (esc/gray),
    *   The <kbd>B</kbd> key will make a new cell below the currently selected cell.
    *   The <kbd>A</kbd> key will make one above.
    *   The <kbd>X</kbd> key will delete the current cell.
    *   The <kbd>Z</kbd> key will undo your last cell deletion.
*   All actions can be done using the menus,
    but there are lots of keyboard shortcuts to speed things up.
*   If you remember the <kbd>Esc</kbd> and <kbd>H</kbd> shortcut, you will be able to find out all the rest.

> ## Command Vs. Edit
>
> In the Jupyter notebook page are you currently in Command or Edit mode?  
> Switch between the modes. 
> Use the shortcuts to generate a new cell. 
> Use the shortcuts to delete a cell
>
> > ## Solution
> >
> > Command mode has a grey boarder and Edit mode has a green border. 
> > Use <kbd>Esc</kbd> and <kbd>Return</kbd> to switch between modes. 
> > You need to be in Command mode (Press <kbd>Esc</kbd> if your cell is green).  Type <kbd>B</kbd> or <kbd>A</kbd>.
> > You need to be in Command mode (Press <kbd>Esc</kbd> if your cell is green).  Type <kbd>X</kbd>.
> >
> {: .solution}
{: .challenge}

## Use the keyboard and mouse to select and edit cells.

*   Pressing the <kbd>Return</kbd> key turns the border green and engages Edit mode,
    which allows you to type within the cell.
*   Because we want to be able to write many lines of code in a single cell,
    pressing the <kbd>Return</kbd> key when in Edit mode (green) moves the cursor to the next line in the cell just like in a text editor.
*   We need some other way to tell the Notebook we want to run what's in the cell.
*   Pressing <kbd>Shift</kbd>+<kbd>Return</kbd> together will execute the contents of the cell.
*   Notice that the <kbd>Return</kbd> and <kbd>Shift</kbd> keys on the 
    right of the keyboard are right next to each other.

## The Notebook will turn Markdown into pretty-printed documentation.

*   Notebooks can also render [Markdown][markdown].
    *   A simple plain-text format for writing lists, links, 
        and other things that might go into a web page.
    *   Equivalently, a subset of HTML that looks like what you'd send in an old-fashioned email.
*   Turn the current cell into a Markdown cell by entering 
    the Command mode (<kbd>Esc</kbd>/gray) and press the <kbd>M</kbd> key.
*   `In [ ]:` will disappear to show it is no longer a code cell
    and you will be able to write in Markdown.
*   Turn the current cell into a Code cell
    by entering the Command mode (<kbd>Esc</kbd>/gray) and press the <kbd>Y</kbd> key.

## Markdown does most of what HTML does.

<div class="row">
  <div class="col-md-6" markdown="1">
~~~
*   Use asterisks
*   to create
*   bullet lists.
~~~
  </div>
  <div class="col-md-6" markdown="1">
*   Use asterisks
*   to create
*   bullet lists.
  </div>
</div>

<div class="row">
  <div class="col-md-6" markdown="1">
~~~
1.  Use numbers
1.  to create
1.  numbered lists.
~~~
  </div>
  <div class="col-md-6" markdown="1">
1.  Use numbers
1.  to create
1.  numbered lists.
  </div>
</div>

<div class="row">
  <div class="col-md-6" markdown="1">
~~~
*  You can use indents
	*  To create sublists 
	*  of the same type
*  Or sublists
	1. Of different
	1. types
~~~
  </div>
  <div class="col-md-6" markdown="1">
*  You can use indents
	*  To create sublists
	*  of the same type
*  Or sublists
	1. Of different
	1. types
  </div>
</div>

<div class="row">
  <div class="col-md-6" markdown="1">
~~~
# A Level-1 Heading
~~~
  </div>
  <div class="col-md-6" markdown="1">
# A Level-1 Heading
  </div>
</div>

<div class="row">
  <div class="col-md-6" markdown="1">
~~~
## A Level-2 Heading (etc.)
~~~
  </div>
  <div class="col-md-6" markdown="1">
## A Level-2 Heading (etc.)
  </div>
</div>

<div class="row">
  <div class="col-md-6" markdown="1">
~~~
Line breaks
don't matter.

But blank lines
create new paragraphs.
~~~
  </div>
  <div class="col-md-6" markdown="1">
Line breaks
don't matter.

But blank lines
create new paragraphs.
  </div>
</div>

<div class="row">
  <div class="col-md-6" markdown="1">
~~~
[Create links](http://software-carpentry.org) with `[...](...)`.
Or use [named links][data_carpentry].

[data_carpentry]: http://datacarpentry.org
~~~
  </div>
  <div class="col-md-6" markdown="1">
[Create links](http://software-carpentry.org) with `[...](...)`.
Or use [named links][data_carpentry].

[data_carpentry]: http://datacarpentry.org
  </div>
</div>

> ## Creating Lists in Markdown
>
> Create a nested list in a Markdown cell in a notebook that looks like this:
>
> 1.  Get funding.
> 2.  Do work.
>     *   Design experiment.
>     *   Collect data.
>     *   Analyze.
> 3.  Write up.
> 4.  Publish.
> 
> > ## Solution
> >
> > This challenge integrates both the numbered list and bullet list. 
> > Note that the bullet list is indented 2 spaces so that it is inline with the items of the numbered list.
> > ~~~
> > 1.  Get funding.
> > 2.  Do work.
> >     *   Design experiment.
> >     *   Collect data.
> >     *   Analyze.
> > 3.  Write up.
> > 4.  Publish.
> > ~~~
> {: .solution}
{: .challenge}

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

> ## Change an Existing Cell from Code to Markdown
>
> What happens if you write some Python in a code cell
> and then you switch it to a Markdown cell?
> For example,
> put the following in a code cell:
>
> ~~~
> x = 6 * 7 + 12
> print(x)
> ~~~
> {: .language-python}
>
> And then run it with <kbd>Shift</kbd>+<kbd>Return</kbd> to be sure that it works as a code cell.
> Now go back to the cell and use <kbd>Esc</kbd> then <kbd>M</kbd> to switch the cell to Markdown
> and "run" it with <kbd>Shift</kbd>+<kbd>Return</kbd>.
> What happened and how might this be useful?
> 
> > ## Solution
> >
> > The Python code gets treated like Markdown text.
> > The lines appear as if they are part of one contiguous paragraph.
> > This could be useful to temporarily turn on and off cells in notebooks that get used for multiple purposes. 
> > ~~~
> > x = 6 * 7 + 12 print(x)
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

> ## Equations
>
> Standard Markdown (such as we're using for these notes) won't render equations,
> but the Notebook will.
> Create a new Markdown cell
> and enter the following:
>
> ~~~
> $\sum_{i=1}^{N} 2^{-i} \approx 1$
> ~~~
>
> (It's probably easier to copy and paste.)
> What does it display?
> What do you think the underscore, `_`, circumflex, `^`, and dollar sign, `$`, do?
> 
> > ## Solution
> >
> > The notebook shows the equation as it would be rendered from LaTeX equation syntax.
> > The dollar sign, `$`, is used to tell Markdown that the text in between is a LaTeX equation.
> > If you're not familiar with LaTeX,  underscore, `_`, is used for subscripts and circumflex, `^`, is used for superscripts.
> > A pair of curly braces, `{` and `}`, is used to group text together so that the statement `i=1` becomes the the subscript and `N` becomes the superscript.
> > Similarly, `-i` is in curly braces to make the whole statement the superscript for `2`.
> > `\sum` and `\approx` are LaTeX commands for "sum over" and "approximate" symbols. 
> {: .solution}
{: .challenge}

[anaconda]: https://docs.continuum.io/anaconda/install
[jupyter]: http://jupyter.org/
[markdown]: https://en.wikipedia.org/wiki/Markdown
