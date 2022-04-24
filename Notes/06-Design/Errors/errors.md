## Types of errors
1. Logic errors
2. Syntax errors
3. Runtime errors
### Logic errors(逻辑错误)
指a program doesn't behave as expected.
### Syntax errors(语法错误)
#### syntaxerror
![](../../../images/2022-04-24-19-29-50.png)
#### indentationerror/taberror(对齐error)
![](../../../images/2022-04-24-19-31-22.png)
### Runtime errors
![](../../../images/2022-04-24-19-32-05.png)
#### NoneType
![](../../../images/2022-04-24-19-32-45.png)
### UnboundLocalError
![](../../../images/2022-04-24-19-34-56.png)
```py
sum = 0
def sum_nums(x, y):
    sum += x + y
    return sum
sum_nums(4, 5)
```

### traceback
![](../../../images/2022-04-24-19-37-42.png)
![](../../../images/2022-04-24-19-37-57.png)
![](../../../images/2022-04-24-19-38-11.png)