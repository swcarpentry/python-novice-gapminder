# python-novice-gapminder

Introduction to Python for non-programmers using Pandas with gapminder data.
Please see `index.md` for the current outline.

## Process Used

This lesson is meant to be used in both [Data Carpentry][dc-website] and [Software Carpentry][swc-website] workshops.
It's also meant to serve as a worked example in [instructor training][instructor-training] of how to develop a new lesson.
To that end,
the outline in `index.md` was developed using a slimmed-down variant of the "Understanding by Design" process.
The main sections are:

1.  Assumptions about audience, time, etc.
    (The current draft also includes some conclusions and decisions in this section - that should be refactored.)

2.  Desired results:
    overall goals, summative assessments at half-day granularity, what learners will be able to do, what learners will know.

3.  Learning plan:
    each episode has a heading that summarizes what will be covered,
    then estimates time that will be spent on teaching and on exercises,
    while the exercises are given as bullet points.

While it looks like a waterfall process, in practice I did this:

1.  Draft the assumptions.

2.  Do one bullet point for each of several learning milestones.

3.  Draft the desired results.

4.  Update the learning milestones (still as just one bullet point each, no time estimates or exercises).

5.  Get early feedback from four people.

6.  Do a full pass to flesh out the assumptions and add time estimates and exercises.

7.  Ask for feedback and start iterating (mostly to cut things).

At the start of #7 above, the lesson needed 8.5 hours, versus a budget of 6.5.
NumPy went,
as did everything to do with running scripts from the command line and a bunch of other topics that are useful and important,
but not *as* important as what's there.
This was also the point at which I settled on using the Jupyter Notebook
(I'd decided on the [Gapminder data][gapminder-data] at the outset to be consistent with [Data Carpentry][dc-website]).
It took about six hours of work over several weeks to get to the point where I felt the lesson was ready for general feedback.

[dc-website]: http://datacarpentry.org
[swc-website]: http://software-carpentry.org
[instructor-training]: https://swcarpentry.github.io/instructor-training/
[gapminder-data]: http://www.gapminder.org/data/
