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

There are other ways of editing, managing, and running code, but Jupyter notebooks 
let us execute and view the results of our Python code immediately within the notebook.

## Why Run Jupyter Notebooks in JupyterLab Desktop
We use JupyterLab Desktop because it's convenient for our learners:

- It does not require knowledge of the command line to install.
- It is available on MacOS, Windows, and Linux devices.
- It does not require users to install Python separately.

## Installing JupyterLab Desktop
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

<p align='center'>   <img alt="Apple Silicon Chip" src="files/apple-silicon-chip.png" width="400"/>
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

- A *.dmg file is a disk image file, typically used to install software on MacOS. 
- If you do not drag the JupyterLab app icon to your Applications folder, it will run from the *.dmg* file instead.
- By copying the JupyterLab app icon to the Applications folder, you tell your computer that you want the contents
of the *.dmg* copied and installed to your Applications so that you can use the application later.
- You can delete (and eject) the *.dmg* file after you've installed JupyterLab. 
  
::::::::::::::::::::::::::::::::::::::::::::::::::

When the installation has finished, close the installer window.

## Installing JupyterLab Desktop: Windows


### Downloading JupyterLab Desktop for Windows
Go to the [JupyterLab Installation](https://github.com/jupyterlab/jupyterlab-desktop?tab=readme-ov-file#installation) page.

<p align='center'>   <img alt="Installation Screen" src="files/installation-os.png" width="700"/>
</p>

From the **Windows (10, 11)** column, select the *x64 Installer*.
Click to download the file to your computer.  

Locate the downloaded file (it will often go to your Downloads folder by default) 
to start the installation process. Double-click it.

### Installing JupyterLab Desktop
<p align='center'>   <img alt="JupyterLab download" src="files/windows-setup.PNG" width="500"/>
</p>

You will see a launcher like this open.

<p align='center'>   <img alt="JupyterLab setup" src="files/windows-install-prompt.PNG" width="500"/>
</p>

When the application has finished installing, click *Finish*
to complete the installation and open JupyterLab Desktop.

<p align='center'>   <img alt="JupyterLab launch" src="files/windows-launch.PNG" width="500"/>
</p>