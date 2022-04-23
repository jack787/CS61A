## multiple environment
1. Assignment Statements
2. Def Statements
3. Call Expressions
![](../../images/2022-04-23-15-09-09.png)
![](../../images/2022-04-23-15-27-28.png)
`a new frame will be created in the function`
### Terminology:Frames
1. frame `keeps track of variable-to-value bindings`
2. Global frames `the global frame,is the starting frame.`
3. Parent frames `The parent of a function is the frame in which it was defined`
![](../../images/2022-04-23-15-19-18.png) 
### A nested call expression
![](../../images/2022-04-23-15-29-54.png)
![](../../images/2022-04-23-15-30-29.png)
## Review:Higher-order functions
1. a function that takes a function as an argument value
2. a function that returns a function as a return value
`Functions are values in python`
```py
def apply_twice(f, x):
    return f(f(x))

def square(x):
    return x ** 2

apply_twice(square, 3)
```
![](../../images/2022-04-23-15-32-51.png)
![](../../images/2022-04-23-15-47-18.png)
`Every user-defined function has a parent frame`<br>
`The parent of a function is the frame in which it was defined`
![](../../images/2022-04-23-15-48-34.png)
## How to draw an environment diagram
![](../../images/2022-04-23-15-50-04.png)
`Local names are not visible to non-nested functions`
![](../../images/2022-04-23-15-51-39.png)
### Composer2 expression tree
![](../../images/2022-04-23-15-56-01.png)
## Function currying
![](../../images/2022-04-23-16-00-35.png)