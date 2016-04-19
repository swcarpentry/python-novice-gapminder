---
layout: lesson_page
title: Setup
permalink: /setup/
---
For the SQL lessons, 
we will use the [SQLite](https://www.sqlite.org/) relational database management system, 
which comes pre-installed on most operating systems. 
While these instructions are specific to SQLite,
most other database management systems
(e.g. MySQL, Oracle, PostGreSQL)
have similar functions for loading data and performing basic operations.

First, download and install SQLite if it is not already installed on your operating system:

* Windows: Download the [SQLite program](http://www.sqlite.org/download.html).
* Mac OS X: `sqlite3` comes pre-installed on Mac OS X.
* Linux: `sqlite3` comes pre-installed on Linux.

Create a directory where you will carry out the exercises for this lesson, and
change to it using the `cd` command. Download the file [survey.db](http://files.software-carpentry.org/survey.db) into this
directory.

~~~
$ mkdir swc_sql 
$ cd swc_sql
$ wget http://files.software-carpentry.org/survey.db
~~~
{: .source}

First, load the example database into SQLite. 
On the shell command line, type

~~~
sqlite3 survey.db
~~~
{: .source}

This command instructs SQLite to load the database in the `survey.db` file.

You should see something like the following.

~~~
SQLite version 3.8.8 2015-01-16 12:08:06
Enter ".help" for usage hints.
sqlite>
~~~
{: .source}

For a list of useful system commands, enter `.help`.

All SQLite-specific commands are prefixed with a . to distinguish them from SQL commands. 
Type `.tables` to list the tables in the database. 

~~~
sqlite> .tables
Person   Site     Survey   Visited
~~~
{: .source}

Type the following SQL `SELECT` command. 
This `SELECT` statement selects all (*) rows from the Site table.

~~~
select * from Site;
~~~
{: .source}

Complete your SQL statement with a semicolon.

~~~
sqlite> select * from Site;
DR-1|-49.85|-128.57
DR-3|-47.15|-126.72
MSK-4|-48.87|-123.4
~~~
{: .source}
