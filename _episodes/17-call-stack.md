---
title: The Call Stack
teaching: 10
exercises: 15
questions:
- "How do function calls actually work?"
objectives:
- "Learner will correctly distinguish local and global variables."
- "Learner will correctly identify parameters as local variables."
- "Learner will correctly trace values in non-recursive nested function calls."
---
FIXME: lesson content.

## Local and Global Variable Use
{: .challenge}

Trace the values of all variables in this program as it is executed.
(Use '---' as the value of variables before and after they exist.)

~~~
limit = 100

def clip(value):
    return min(max(0.0, value), limit)

value = -22.5
print(clip(value))
~~~
{: .python}
