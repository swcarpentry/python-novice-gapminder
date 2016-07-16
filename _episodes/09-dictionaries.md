---
title: "Dictionaries"
teaching: 5
exercises: 10
questions:
- "How can I associate my data with unique identifiers for simple retrieval?"
objectives:
- "Explain why dictionaries are useful and may be more appropriate than lists."
- "Explain the concept of keys and values in a dictionary."
- "Write programs that create dictionaries and retrieve the keys and values contained within."
keypoints:
- FIXME
---
FIXME: lesson content.

## Creating Dictionaries

Dictionaries store information in key:value pairs.  However, unlike lists, this information is stored unsorted.

~~~
character_info = {'first_name':'Charlie', 'last_name':'Brown', 'favorite_sport':'football', 'position':'placekicker'} 
print(character_info)
~~~
{: .source}

~~~
{'first_name': 'Charlie', 'position': 'placekicker', 'favorite_sport': 'football', 'last_name': 'Brown'}
~~~
{: .output}

We can also create an empty dictionary and add to it.

~~~
character_info = {}
character_info['first_name'] = 'Charlie'
character_info['last_name'] = 'Brown'
character_info['favorite_sport'] = 'football'
character_info['position'] = 'placekicker'
print(character_info)
~~~
{: .source}

~~~
{'first_name': 'Charlie', 'position': 'placekicker', 'favorite_sport': 'football', 'last_name': 'Brown'}
~~~
{: .output}

We can access the a certain value by calling its key:

~~~
print(character_info['first_name'])
~~~
{: .source}
~~~
'Charlie'
~~~
{: .output}

> ## Fill in the Blanks
>
> Fill in the blanks so that the program below produces the output shown.
>
> ~~~
> employee = ____
> employee[_____] = 'John Smith'
> employee[_____] = ______
> employee[_____] = 10
> print(employee)
> ~~~
> {: .source}
>
> ~~~
> {'position': 'Manager', 'years employeed': 10, 'name': 'John Smith'}
> ~~~
> {: .output}
{: .challenge}

