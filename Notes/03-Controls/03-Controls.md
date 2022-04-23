## Conditional statements
`if-elif-else` syntax:
truthy value(`True`,a non zero integer,etc)<br>
falsy value(`False`,`0`,`None`,`""`,`[]`,etc)
## Boolean Operators
`and,or,not`
1. `not` returns the opposite boolean value of the following expression, and will always return either True or False.
2. `and` evaluates expressions in order and stops evaluating (short-circuits) once it `reaches the first falsy value`, and then `returns it`. If all values `evaluate to a truthy value, the last value is returned`.
3. `or` evalutes expressions in order and short-circuits `at the first truthy value and returns it`. `If all values evaluate to a falsy value, the last value is returned`.
```py
>>> not None
True
>>> not True
False
>>> -1 and 0 and 1
0
>>> False or 9999 or 1/0
9999
```