from decorators import do_twice, do_twice1, do_twice2


@do_twice1
def greet(name):
    print(f"Hello {name}")


# greet("曾文杰")
@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


t = return_greeting("Adam")
# Creating greeting
# Creating greeting
print(t)
# None
