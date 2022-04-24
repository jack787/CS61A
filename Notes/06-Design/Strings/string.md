## String interpolation
`string interpolation` is the process of combining string literals with the results of expressions.<br>
Available since Python3.5,`f strings(formatted string literals)` are the best way to do string interpolation.
<br>

just put an `f` in front of the quotes and then put any valid python expression in curly brackets inside:
```py
artist = "Lil Nas X"
song = "Industry Baby"
place = 2

print(f"Debuting at #{place}: '{song}' by {artist}")
#print(f"Debuting at #{place}: '{song}' by {artist}")
```
## Expressions in f strings
`Any valid python expression can go inside the parentheses`,and will be executed in the current environment.
```py
greeting="Ahoy"
noun="Boat"
print(f"{greeting.lower()},{noun.upper()}yMc{noun}Face")
print(f"{greeting*3},{noun[0:3]}yMc{noun[-1]}Face")
```