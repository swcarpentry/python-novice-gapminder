---
layout: lesson
subtitle: Programming Style
teaching: 10
exercises: 10
---
> ## Learning Objectives
>
> * Learner will provide sound justifications for basic rules of coding style.
> * Learner will refactor simple programs to make them more readable
>   and justify the changes.
{: .objectives}

FIXME: lesson content.

## Clean Up This Code
{: .challenge}

1. Read this short program and try to predict what it does.
2. Run it: how accurate was your prediction?
3. Refactor the program to make it more readable.
   Remember to run it after each change to ensure its behavior hasn't changed.
4. Compare your rewrite with your neighbor's.
   What did you do the same?
   What did you do differently, and why?

~~~
import sys
n = int(sys.argv[1])
s = sys.argv[2]
print(s)
i = 0
while i < n:
    # print('at', j)
    new = ''
    for j in range(len(s)):
        left = j-1
        right = (j+1)%len(s)
        if s[left]==s[right]: new += '-'
        else: new += '*'
    s=''.join(new)
    print(s)
    i += 1
~~~
{: .python}
