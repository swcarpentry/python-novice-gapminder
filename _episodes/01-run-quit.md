---
title: "Jupyter Notebook Overview"
teaching: 15
exercises: 0
questions:
- "What environment can I use with Python?"
- "How can I create and run Python programs?"
objectives:
- "Launch the Jupyter Notebook, create new notebooks, and exit the Notebook."
- "Create Markdown cells in a notebook."
- "Create and run Python cells in a notebook."
keypoints:
- "Python programs are plain text files."
- "Use the Jupyter Notebook application for editing and running Python."
- "Each Notebook contains cells that can house code, text, or images."
- "Command mode edits the Notebook as a whole, while Edit mode edits individual cells."
- "The Markdown cell option is like HTML, allowing you to create formatted text."
---
## Python programs are plain text files.

Python files typically have `.py` extension to let everyone know it is a Python program. Although you can write Python programs using
a text editor, but we are going to use the [Jupyter Notebook][jupyter] application. Jupyter Notebook provides code completion and other 
helpful features. Notebook files have the extension `.ipynb` to distinguish them from plain-text Python programs. 

## Jupyter Notebook runs and edits Python programs.

Jupyter Notebook is automatically installed with the [Anaconda package manager][anaconda]. See [the setup instructions]({{ page.root }}/setup/) for Anaconda installation instructions.

The application is launched through the command line, by typing

    ~~~
    $ jupyter notebook
    ~~~

in the Mac OS X or Linux Terminal, or 

    ~~~
    jupyter notebook
    ~~~

in the Windows Command Prompt. 

This will start a local Jupyter Notebook server by opening your default web browser. The application uses your web browser to render the 
notebook, not to use your internet connection. Using Jupyter Notebook has several advantages:
    *   You can easily type, edit, and copy and paste blocks of code.
    *   Tab complete allows easy access the names of things you are using and information to learn more about them.
    *   Code annotation makes notebooks more accessible to you and your collaborators.
    *   Displaying graph next to the code that produces them provides a complete story of the analysis.

![Example Jupyter Notebook](../fig/0_jupyter_notebook_example.jpg)  
*Screenshot of a [Jupyter Notebook on quantum mechanics](https://github.com/jrjohansson/qutip-lectures) by Robert Johansson*

> ## How It's Stored
>
> The notebook file is stored in a format called JSON. This format allows Jupyter to mix source code, text, and images, all in one file.
{: .callout}

## Creating a new notebook file.

When Jupyter Notebook launches in your web browser, it opens your local machine directory. To create a new notebook, select the folder
where you would like to house the file, and then click on the 'New' dropdown menu in the top right corner of the Files browser page.
Select 'Python 3' under the heading Notebook, and a new browser windows will open with an Untitled notebook. To rename, click on the 
file name 'Untitled', next to the Jupyter Notebook logo. Jupyter will autosave your changes, but you can also click on the 'Save and 
Checkpoint' icon to manually save.

Right now, our new notebook looks pretty empty, containing a single box with the text 'ln []'. In Jupyter, this box is referred to as a
cell. The 'ln' stands for 'line', and the empty bracket indicates that the cell has not been 'run' by the server. 'Running' the cell 
means that we are telling the server to process whatever is in the cell.
Each notebook contains one or more cells that may contain code, text, or images.

> ## Code vs. Text
>
> We often use the term "code" to mean "the source code of software written in a language such as Python". 
> A "code cell" in a Notebook is a cell that contains software;
> a "text cell" is one that contains ordinary prose written for human beings.
{: .callout}

Cells are automatically designated as code cells. When you click inside the cell, your code cell border will change from blue/gray to 
green. Clicking outside of the cell turns it back to blue/gray. You can also toggle this selection by pressing <kbd>Esc</kbd> and 
<kbd>Return</kbd> alternately.
These are the **Command** (gray) and **Edit** (green) modes of your notebook. Command mode allows you to edit notebook-level features, 
and Edit mode changes the content of cells.

When in Command mode, pressing the <kbd>H</kbd> key will provide a list of all the shortcut keys:
    *   The <kbd>B</kbd> key will make a new cell below the currently selected cell.
    *   The <kbd>A</kbd> key will make one above.
    *   The <kbd>X</kbd> key will delete the current cell.
    *   The <kbd>Z</kbd> key will undo your last cell deletion.
These actions can be also be done using the menus, but keyboard shortcuts can help you complete tasks faster.

> ## Command Vs. Edit
>
> Determine if you are currently in Command or Edit mode.  
> Switch between the modes. 
> Use the shortcuts to generate a new cell. 
> Use the shortcuts to delete a cell
>
> > ## Solution
> >
> > Command mode has a grey boarder and Edit mode has a green border. 
> > Use <kbd>Esc</kbd> and <kbd>Return</kbd> to switch between modes. 
> > You need to be in Command mode (Press <kbd>Esc</kbd> if your cell is green). Type <kbd>B</kbd> or <kbd>A</kbd>.
> > You need to be in Command mode (Press <kbd>Esc</kbd> if your cell is green). Type <kbd>X</kbd>.
> >
> {: .solution}
{: .challenge}

## Editting and running cells.

Clicking within the cell or pressing the <kbd>Return</kbd> key turns the border green and engages Edit mode,
which allows you to type within the cell. Pressing the <kbd>Return</kbd> key when in Edit mode (green) moves the cursor to the next line 
in the cell just like in a text editor.

Pressing <kbd>Shift</kbd>+<kbd>Return</kbd> (<kbd>Shift</kbd>+<kbd>Enter</kbd> for Windows users) together will 'run' the cell, 
executing the contents of the cell. Notice that running the cell changes the empty brackets `[]` to the left of the cell contents to 
`[1]`. Each time the cell is run, this number will increase by one.   

## Using Markdown for documentation.

Notebooks can also render [Markdown][markdown], which allows you to format plain text much like HTML did in an old-fashioned email.
To turn the current cell into a Markdown cell, enter the Command mode (<kbd>Esc</kbd>/gray) and press the <kbd>M</kbd> key. You can also 
select "Markdown" from the dropdown menu with the word "Code". `In [ ]:` will disappear to show it is no longer a code cell and you will 
be able to write in Markdown. To turn the current cell back into a Code cell, enter the Command mode and press the <kbd>Y</kbd> key.

## Markdown basics.

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


[anaconda]: https://docs.continuum.io/anaconda/install
[jupyter]: http://jupyter.org/
[markdown]: https://en.wikipedia.org/wiki/Markdown
