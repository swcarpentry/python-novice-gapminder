[![Create a Slack Account with us](https://img.shields.io/badge/Create_Slack_Account-The_Carpentries-071159.svg)](https://swc-slack-invite.herokuapp.com/) 
[![Slack Status](https://img.shields.io/badge/Slack_Channel-swc--py--gapminder-E01563.svg)](https://swcarpentry.slack.com/messages/C9X4W03KL) 

python-novice-gapminder
=======================

This is a [mybinder](https://gke.mybinder.org/) branch designed to accompany the 
[Python Novice Gapminder lesson](https://swcarpentry.github.io/python-novice-gapminder/). 

Maintainer(s):

* [Allen Lee][lee-allen]
* [Nathan Moore][moore-nathan]
* [David R. Pugh][david-pugh]
* [Sourav Singh][singh-sourav]
* [Olav Vahtras][olav-vahtras]

[lee-allen]: https://software-carpentry.org/team/#lee-allen
[moore-nathan]: https://software-carpentry.org/team/#moore_nathan
[singh-sourav]: https://software-carpentry.org/team/#singh-sourav
[olav-vahtras]: https://software-carpentry.org/team/#vahtras_olav
[david-pugh]: https://github.com/davidrpugh

## Running locally

### Install Conda

### Creating the Conda environment

After cloning the repo you can use the following commands to build the environment on your local machine.

```bash
$ cd /python-novice-gapminder
$ git checkout -b binder
$ conda env create --file environment.yml --prefix ./env
```

### Running JupyterLab

Once the environment has been created, then you can activate it and lauch the JupyterLab server.

```bash
$ source activate ./env
$ jupyter lab
``` 

