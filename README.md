python-novice-gapminder
=======================

Introduction to Python for non-programmers with a focus on plotting and data analysis.
Please see <https://swcarpentry.github.io/python-novice-gapminder/>
for a rendered version of this material,
[the lesson template documentation][lesson-example]
for instructions on formatting, building, and submitting material,
or run `make` in this directory for a list of helpful commands.

## Run Jekyll in a Docker container

If you download and install the latest versions of [Docker compose](https://docs.docker.com/compose/install/) and
[Docker engine](https://docs.docker.com/engine/installation/) you can build a Jekyll container to serve this site with
hot-reloading and incremental rebuilds by running `docker-compose up` and visiting `localhost:4000` in a browser. 

The docker-compose file mounts this root directory into the Jekyll container so you can edit the lesson's Markdown files
in place and see those changes when you refresh your browser window.

To clean up and remove the docker containers, run `docker-compose down -v` or `docker system prune`.

Maintainer(s):

* [Bennet Fauber][fauber-bennet]
* [Greg Wilson][wilson-greg]

[fauber-bennet]: http://software-carpentry.org/team/#fauber_bennet
[lesson-example]: https://swcarpentry.github.com/lesson-example/
[wilson-greg]: http://software-carpentry.org/team/#wilson_g
