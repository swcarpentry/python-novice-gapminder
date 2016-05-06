---
layout: episode
title: "Programming Style"
teaching: 10
exercises: 15
questions:
- "How can I make my programs more readable?"
- "How do most programmers format their code?"
objectives:
- "Provide sound justifications for basic rules of coding style."
- "Refactor one-page programs to make them more readable and justify the changes."
- "Use Python community coding standards (PEP-8)."
keypoints:
- FIXME
---
FIXME: lesson content.

> ## Clean Up This Code
> 
> 1. Read this short program and try to predict what it does.
> 2. Run it: how accurate was your prediction?
> 3. Refactor the program to make it more readable.
>    Remember to run it after each change to ensure its behavior hasn't changed.
> 4. Compare your rewrite with your neighbor's.
>    What did you do the same?
>    What did you do differently, and why?
> 
> ~~~
> import sys
> n = int(sys.argv[1])
> s = sys.argv[2]
> print(s)
> i = 0
> while i < n:
>     # print('at', j)
>     new = ''
>     for j in range(len(s)):
>         left = j-1
>         right = (j+1)%len(s)
>         if s[left]==s[right]: new += '-'
>         else: new += '*'
>     s=''.join(new)
>     print(s)
>     i += 1
> ~~~
> {: .source}
{: .challenge}

> ## Finding Neighbors
> 
> This function is supposed to find the minimum value adjacent to (but not in) a specified location in an array.
> For what inputs does it produce the wrong answer?
> How can it be repaired?
> 
> ~~~
> def any_negative_neighbors(array, i, j, use_diagonals):
>     '''
>     Return True if any neighbors of (i,j) are negative, or False if none are.
>     Only check diagonal neighbors if use_diagonals is True.
>     '''
> 
>     width, height = array.shape
> 
>     if i > 0 and array[i-1, j] < 0: return True
>     if i < width and array[i+1, j] < 0: return True
>     if j > 0 and array[i, i-1] < 0: return True
>     if j < width and array[i, j+1] < 0: return True
> 
>     if not use_diagonals: return False
> 
>     if i > 0 and j > 0 and array[i-1, j-1] < 0: return True
>     if i > 0 and j < width and array[i-1, j+1] < 0: return True
>     if i < width and j > 0 and array[i+1, j-1] < 0: return True
>     if i < width and j < height and array[i+1, j+1] < 0: return True
> ~~~
> {: .source}
{: .challenge}
