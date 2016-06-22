---
title: "The Call Stack"
teaching: 10
exercises: 15
questions:
- "How do function calls actually work?"
objectives:
- "Identify local and global variables."
- "Identify parameters as local variables."
- "Trace values in non-recursive nested function calls."
keypoints:
- FIXME
---
FIXME: lesson content.

> ## Local and Global Variable Use
>
> Trace the values of all variables in this program as it is executed.
> (Use '---' as the value of variables before and after they exist.)
>
> ~~~
> limit = 100
>
> def clip(value):
>     return min(max(0.0, value), limit)
>
> value = -22.5
> print(clip(value))
> ~~~
> {: .source}
{: .challenge}
