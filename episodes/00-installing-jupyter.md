---
title: Installing JupyterLab Desktop
teaching: 15
exercises: 0
---

::::::::::::::::::::::::::::::::::::::: objectives

- Download JupyterLab Desktop.
- Install JuptyterLab Desktop.
- Learn about folders and files on your computer.
- Create a folder for the Jupyter notebooks you will create during this workshop series.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- What steps do I need to take to prepare for this workshop series?
- How do I install JupyterLab Desktop?

::::::::::::::::::::::::::::::::::::::::::::::::::


## Getting Started with JupyterLab Desktop

[JupyterLab Desktop](https://github.com/jupyterlab/jupyterlab-desktop) is a desktop application with an integrated web user interface from [Project Jupyter][jupyter] that
enables one to work with documents and activities such as Jupyter notebooks, text editors, terminals,
and even custom components in a flexible, integrated, and extensible manner. Jupyter notebooks are common in data science and visualization and serve as a convenient common-denominator experience for running Python code interactively where we can easily view and share the results of our Python code.

There are other ways of editing, managing, and running code, but Jupyter notebooks let us execute and view the results of our Python code immediately within the notebook.

## Why Use JupyterLab Notebooks

JupyterLab has many handy features:

- You can easily type, edit, and copy and paste blocks of code.
- Tab complete allows you to easily access the names of things you are using
  and learn more about them.
- It allows you to annotate your code with links, different sized text, bullets, etc.
  to make it more accessible to you and your collaborators.
- It allows you to display figures next to the code that produces them
  to tell a complete story of the analysis.

## Why Run Jupyter Notebooks in JupyterLab Desktop
We use JupyterLab Desktop because it's convenient for our learners:

- It does not require knowledge of the command line to install.
- It is available on MacOS, Windows, and Linux devices.
- It does not require users to install Python separately.

## Installing JupyterLab
How you install JupyterLab Desktop will depend on your operating system.

- If you have a Mac laptop, [click here](#installing-jupyterlab-desktop-macos).
- If you a Windows laptop, [click here](#installing-jupyterlab-desktop-windows).

## Installing JupyterLab Desktop: MacOS

Before installing JupyterLab Desktop on a Mac, you will need to know the type of processor
your computer has. 

Depending on when you bought your laptop, your mac may have an Apple Silicon chip
or an Intel Chip. For JupyterLab Desktop to work correctly, you must install the version of the
program that corresponds to the right chip.

### Finding Your Processor Chip Type

1. Click on the  Apple icon in the top left corner of your screen.
2. Select *About this Mac*.
3. Look at the line labeled *Chip*.
  - If your chip name begins with Apple, it is an Apple Silicon processor.
  - If your chip name begins with Intel, it is an Intel processor.

<p align='center'>   <img alt="Apple Silicon Chip" src="files/apple-silicon-chip.png" width="200"/>
        <img alt="Intel Chip" src="files/apple-silicon-chip.png" width="200"/>
</p>

### Downloading Jupyter Lab
Go to the [JupyterLab Installation](https://github.com/jupyterlab/jupyterlab-desktop?tab=readme-ov-file#installation) page.

<p align='center'>   <img alt="Installation Screen" src="files/installation-os.png" width="700"/>
</p>

From the **Mac (macOS 10.15+)** column, select the download that corresponds to your chip type.
Click to download the file to your computer. 

Once the download has completed, double-click the *.dmg* file.

<p align='center'>   <img alt="MacOS Installation Prompt" src="files/mac-install-apps.png" width="500"/>
</p>

Drag the JupyterLab.app application to the Applications folder on the right.
This will install the JupyterLab app to the Applications folder on your computer.

:::::::::::::::::::::::::::::::::::::::::  callout

## What Are .dmg Files?

- A *.dmg* file is a disk image file, typically used to install software on MacOS. 
- If you do not drag the JupyterLab app icon to your Applications folder, it will run from the *.dmg* file instead.
- By copying the JupyterLab app icon to the Applications folder, you tell your computer that you want the contents
of the *.dmg* copied and installed to your Applications so that you can use the application later.
- You can delete (and eject) the *.dmg* file after you've installed JupyterLab. 
  
::::::::::::::::::::::::::::::::::::::::::::::::::

When the installation has finished, close the installer window.

## Installing JupyterLab Desktop: Windows

Go to the [JupyterLab Installation](https://github.com/jupyterlab/jupyterlab-desktop?tab=readme-ov-file#installation) page.

<p align='center'>   <img alt="Installation Screen" src="files/installation-os.png" width="700"/>
</p>

From the **Windows (10, 11)** column, select the *x64 Installer*.
Click to download the file to your computer. 


## The Notebook has Command and Edit modes.

- If you press <kbd>Esc</kbd> and <kbd>Return</kbd> alternately, the outer border of your code cell will change from gray to blue.
- These are the **Command** (gray) and **Edit** (blue) modes of your notebook.
- Command mode allows you to edit notebook-level features, and Edit mode changes the content of cells.
- When in Command mode (esc/gray),
  - The <kbd>b</kbd> key will make a new cell below the currently selected cell.
  - The <kbd>a</kbd> key will make one above.
  - The <kbd>x</kbd> key will delete the current cell.
  - The <kbd>z</kbd> key will undo your last cell operation (which could be a deletion, creation, etc).
- All actions can be done using the menus, but there are lots of keyboard shortcuts to speed things up.

:::::::::::::::::::::::::::::::::::::::  challenge

## Command Vs. Edit

In the Jupyter notebook page are you currently in Command or Edit mode?  
Switch between the modes.
Use the shortcuts to generate a new cell.
Use the shortcuts to delete a cell.
Use the shortcuts to undo the last cell operation you performed.

:::::::::::::::  solution

## Solution

Command mode has a grey border and Edit mode has a blue border.
Use <kbd>Esc</kbd> and <kbd>Return</kbd> to switch between modes.
You need to be in Command mode (Press <kbd>Esc</kbd> if your cell is blue).  Type <kbd>b</kbd> or <kbd>a</kbd>.
You need to be in Command mode (Press <kbd>Esc</kbd> if your cell is blue).  Type <kbd>x</kbd>.
You need to be in Command mode (Press <kbd>Esc</kbd> if your cell is blue).  Type <kbd>z</kbd>.



:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

### Use the keyboard and mouse to select and edit cells.

- Pressing the <kbd>Return</kbd> key turns the border blue and engages Edit mode, which allows
  you to type within the cell.
- Because we want to be able to write many lines of code in a single cell,
  pressing the <kbd>Return</kbd> key when in Edit mode (blue) moves the cursor to the next line
  in the cell just like in a text editor.
- We need some other way to tell the Notebook we want to run what's in the cell.
- Pressing <kbd>Shift</kbd>\+<kbd>Return</kbd> together will execute the contents of the cell.
- Notice that the <kbd>Return</kbd> and <kbd>Shift</kbd> keys on the right of the keyboard are
  right next to each other.

### The Notebook will turn Markdown into pretty-printed documentation.

- Notebooks can also render [Markdown][markdown].
  - A simple plain-text format for writing lists, links,
    and other things that might go into a web page.
  - Equivalently, a subset of HTML that looks like what you'd send in an old-fashioned email.
- Turn the current cell into a Markdown cell by entering the Command mode (<kbd>Esc</kbd>/gray)
  and press the <kbd>M</kbd> key.
- `In [ ]:` will disappear to show it is no longer a code cell and you will be able to write in
  Markdown.
- Turn the current cell into a Code cell by entering the Command mode (<kbd>Esc</kbd>/gray) and
  press the <kbd>y</kbd> key.

### Markdown does most of what HTML does.

Table: Showing some markdown syntax and its rendered output.

+---------------------------------------+------------------------------------------------+
| Markdown code                         | Rendered output                                |
+=======================================+================================================+
+---------------------------------------+------------------------------------------------+
| ```                                   | <p></p>                                        |
| *   Use asterisks                     | -   Use asterisks                              |
| *   to create                         | -   to create                                  |
| *   bullet lists.                     | -   bullet lists.                              |
| ```                                   |                                                |
+---------------------------------------+------------------------------------------------+
+---------------------------------------+------------------------------------------------+
| ```                                   | <p></p>                                        |
| 1.   Use numbers                      | 1.   Use numbers                               |
| 1.   to create                        | 2.   to create                                 |
| 1.   bullet lists.                    | 3.   numbered lists.                           |
| ```                                   |                                                |
+---------------------------------------+------------------------------------------------+
+---------------------------------------+------------------------------------------------+
| ```                                   | <p></p>                                        |
| *  You can use indents                | - You can use indents                          |
|   *  To create sublists               |   - To create sublists                         |
|   *  of the same type                 |   - of the same type                           |
| *  Or sublists                        | - Or sublists                                  |
|   1. Of different                     |   1. Of different                              |
|   1. types                            |   2. types                                     |
| ```                                   |                                                |
+---------------------------------------+------------------------------------------------+
+---------------------------------------+------------------------------------------------+
| ```                                   | <p></p>                                        |
| # A Level-1 Heading                   | ## A Level-1 Heading                           |
| ```                                   |                                                |
+---------------------------------------+------------------------------------------------+
+---------------------------------------+------------------------------------------------+
| ```                                   | <p></p>                                        |
| ## A Level-2 Heading (etc.)           | ### A Level-2 Heading (etc.)                   |
| ```                                   |                                                |
+---------------------------------------+------------------------------------------------+
+---------------------------------------+------------------------------------------------+
| ```                                   | <p></p>                                        |
| Line breaks                           | Line breaks                                    |
| don't matter.                         | don't matter.                                  |
|                                       |                                                |
| But blank lines                       | But blank lines                                |
| create new paragraphs.                | create new paragraphs.                         |
| ```                                   |                                                |
+---------------------------------------+------------------------------------------------+
+---------------------------------------+------------------------------------------------+
| ```                                   | <p></p>                                        |
| [Links](http://software-carpentry.org)| [Links](https://software-carpentry.org)        |
| are created with `[...](...)`.        | are created with `[...](...)`.                 |
| Or use [named links][data-carp].      | Or use [named links][data_carpentry].          |
|                                       |                                                |
| [data-carp]: http://datacarpentry.org |                                                |
| ```                                   |                                                |
+---------------------------------------+------------------------------------------------+


:::::::::::::::::::::::::::::::::::::::  challenge

## Creating Lists in Markdown

Create a nested list in a Markdown cell in a notebook that looks like this:

1. Get funding.
2. Do work.
  - Design experiment.
  - Collect data.
  - Analyze.
3. Write up.
4. Publish.

:::::::::::::::  solution

## Solution

This challenge integrates both the numbered list and bullet list.
Note that the bullet list is indented 2 spaces so that it is inline with the items of the numbered list.

```
1.  Get funding.
2.  Do work.
    *   Design experiment.
    *   Collect data.
    *   Analyze.
3.  Write up.
4.  Publish.
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## More Math

What is displayed when a Python cell in a notebook
that contains several calculations is executed?
For example, what happens when this cell is executed?

```python
7 * 3
2 + 1
```

:::::::::::::::  solution

## Solution

Python returns the output of the last calculation.

```python
3
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Change an Existing Cell from Code to Markdown

What happens if you write some Python in a code cell
and then you switch it to a Markdown cell?
For example,
put the following in a code cell:

```python
x = 6 * 7 + 12
print(x)
```

And then run it with <kbd>Shift</kbd>\+<kbd>Return</kbd> to be sure that it works as a code cell.
Now go back to the cell and use <kbd>Esc</kbd> then <kbd>m</kbd> to switch the cell to Markdown
and "run" it with <kbd>Shift</kbd>\+<kbd>Return</kbd>.
What happened and how might this be useful?

:::::::::::::::  solution

## Solution

The Python code gets treated like Markdown text.
The lines appear as if they are part of one contiguous paragraph.
This could be useful to temporarily turn on and off cells in notebooks that get used for multiple purposes.

```python
x = 6 * 7 + 12 print(x)
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Equations

Standard Markdown (such as we're using for these notes) won't render equations,
but the Notebook will.
Create a new Markdown cell
and enter the following:

```
$\sum_{i=1}^{N} 2^{-i} \approx 1$
```

(It's probably easier to copy and paste.)
What does it display?
What do you think the underscore, `_`, circumflex, `^`, and dollar sign, `$`, do?

:::::::::::::::  solution

## Solution

The notebook shows the equation as it would be rendered from LaTeX equation syntax.
The dollar sign, `$`, is used to tell Markdown that the text in between is a LaTeX equation.
If you're not familiar with LaTeX,  underscore, `_`, is used for subscripts and circumflex, `^`, is used for superscripts.
A pair of curly braces, `{` and `}`, is used to group text together so that the statement `i=1` becomes the subscript and `N` becomes the superscript.
Similarly, `-i` is in curly braces to make the whole statement the superscript for `2`.
`\sum` and `\approx` are LaTeX commands for "sum over" and "approximate" symbols.



:::::::::::::::::::::::::