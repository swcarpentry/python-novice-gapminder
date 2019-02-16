---
title: "Variable Scope"
teaching: 10
exercises: 10
questions:
- "What is a variable’s scope?"
- "What are the different types of variable scope?"
- "What is the difference between a variable’s lifetime and it’s visibility?"
objectives:
- "Identify local and global variables."
- "Identify parameters as local variables."
- "Identify when a variable’s lifetime ends and it can no longer be used to reference previous values."
- "Identify when a variable is visible to a section of source code."
keypoints:
- "Understanding variable scope by its lifetime and visibility."
---
## The lifetime and visibility of a variable is its scope.

A variable is a location in memory where a value can be stored. Variables have a finite lifetime within the execution of a program, during which it can be written to store a value, and read to retrieve the last value stored. This lifetime is referred to as the scope of the variable and it specifies the portion of the software source code that references to a variable is considered valid. 
Assigning scope, or limited lifetime, to variables is a useful programming trait as it facilitates compartmentalization. In other words, you do not have to be concerned with the variable names used by a function you are invoking, neither do you need to be concerned about the variable names that may be used by software source code that is invoking your function.  
Python 3 has both global and local variables, which are indicators of the variable’s scope. A global variable exists for the entire duration of the program’s execution (lifetime) and it can be referenced at any point of the program’s source code (visibility). A local variable more restricted in both these regards. When created within a function, a variable can only be referenced in this function and no longer exists when the function ends.  
Understanding the scope of variables in Python is particularly important as errors from referencing a variable out of scope can lead to subtle and difficult to resolve runtime semantic anomalies.  

~~~
pressure = 103.9  # global var

def no_adjust():
    print("1. Initial global pressure:", pressure)

def local_adjust():
    pressure = 99.9  # local var
    print("2. Changing local pressure:", pressure)

def global_adjust():
    global pressure
    pressure = 22.2  # , changing global var
~~~
{: .python}

*   `pressure` is a  used both as a *global* and *local* variable*  

    *   It is first created as a global variable - outside any particular function - and is visible everywhere.  

    *   It is then created as a local variable inside the local_adjust function and can only be used there.  

    *   To update the global variable pressure in a function we use the global qualifier as a prefix as in the global_adjust function.  

    *   Remember: a function parameter is a variable that is automatically assigned a value when the function is called.​  

~~~
no_adjust()
local_adjust()
print("3. Unchanged global pressure:", pressure)  # no change to global
global_adjust()
print("4. Changed global pressure:", pressure)
~~~
{: .output}
~~~
1. Initial global pressure: 103.9
2. Changing local pressure: 99.9
3. Unchanged global pressure: 103.9
4. Changed global pressure: 22.2
~~~

{: .challenge}
