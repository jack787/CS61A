## Decorators on classes
`2 different ways to use decorators on classes`:
### `decorate the methods of a class`

<!-- 1. decorate methods  -->
```py
#decorators.py
import functools,time
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args,**kwargs):
        start_time=time.perf_counter()
        t=func(*args,**kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finish {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer
# TimeWaster.py
from decorators import timer
class TimeWaster:
    def __init__(self, max_num) -> None:
        self.max_num = max_num
    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
```
![](../../images/2022-04-26-10-49-10.png)
### `decorate the whole class`
1. Use the `dataclasses.dataclass`
```py
from dataclasses import dataclass
@dataclass
class PlayingCard:
    rank:str
    suit:str
```
![](../../images/2022-04-26-10-57-34.png)
2. Use your decorator
```py
from decorators import timer

@timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
```
Decorating a class does not decorate its methods. Recall that `@timer is just shorthand` for `TimeWaster = timer(TimeWaster).`
![](../../images/2022-04-26-11-00-08.png)
## Several decorators on one function/Nesting Decorators
`apply several decorators` to a function by stacking them on top of each other
This will call `do_twice`,and then call`timer`,shorthand is `timer(do_twice(greet()))`
```py
from decorators import do_twice, timer
@timer
@do_twice
def greet(name):
    print(f"Hello {name}")
```
If we change the position of `timer` and `do_twice`:<br>
```py
@do_twice
@timer
def greet(name):
    print(f"Hello {name}")
```
![](../../images/2022-04-26-11-18-16.png)
## Decorators with arguments
It's useful to `pass arguments to your decorators.`<br>
For instance,`@do_twice` coud be extended to a `@repeat(num_times)` decorator. `The number of times to execute the decorated function could then be given as an argument`
```py
@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")
```
![](../../images/2022-04-26-11-21-52.png)
`to realize repeat(num_times=4)`,we can use follow template:<br>
![](../../images/2022-04-26-11-25-39.png)
```py
#decorators.py
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value

        return wrapper_repeat

    return decorator_repeat
### decorators_with_args.py
from decorators import repeat


@repeat(num_times=4)
def greet(name):
    print(f"My name is {name}")
```
![](../../images/2022-04-26-11-28-39.png)
![](../../images/2022-04-26-11-31-15.png)
## Decorators that can optionally take arguments
## Stateful decorators
## Classes as decorators
