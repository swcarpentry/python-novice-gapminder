python-novice-gapminder
=======================

Introduction to Python for non-programmers with a focus on plotting and data analysis.
Please see <https://swcarpentry.github.io/python-novice-gapminder/>
for a rendered version of this material,
[the lesson template documentation][lesson-example]
for instructions on formatting, building, and submitting material,
or run `make` in this directory for a list of helpful commands.

## Run Jekyll and serve lesson content in a Docker container

If you download and install the latest versions of [Docker compose](https://docs.docker.com/compose/install/) and
[Docker engine](https://docs.docker.com/engine/installation/) you can run a Jekyll container that serves this site
with hot-reloading and incremental rebuilds by executing `% docker-compose up` from the command line. On Windows you
should run this via [`PowerShell`](https://docs.docker.com/docker-for-windows/), not a cygwin / bash shell.

The docker-compose file mounts the cloned repository's root directory into the Jekyll container so you should be able to
edit this lesson's Markdown files in place and see those changes when you refresh your browser window.

This should work without issue on up-to-date Linux and Mac OS systems but Windows requires some additional
configuration.

### Windows Docker configuration
[Explicitly mark the hard drive where this git repository was cloned as a shared drive with Docker](https://blogs.msdn.microsoft.com/stevelasker/2016/06/14/configuring-docker-for-windows-volumes/)

The site will be accessible at `localhost:4000` from any browser. 

### Clean up
To clean up and remove the docker containers, run `docker-compose down`.

Maintainer(s):

* [Bennet Fauber][fauber-bennet]
* [Greg Wilson][wilson-greg]

[fauber-bennet]: http://software-carpentry.org/team/#fauber_bennet
[lesson-example]: https://swcarpentry.github.com/lesson-example/
[wilson-greg]: http://software-carpentry.org/team/#wilson_g
