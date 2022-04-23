def happy(text):
    return "☻" + text + "☻"


def sad(text):
    return "☹" + text + "☹"


def composer(f, g):
    def composed(x):
        return f(g(x))

    return composed


msg1 = composer(sad, happy)("cs61a!")  #'☹☻cs61a!☻☹'
msg2 = composer(happy, sad)("eecs16a!")  #'☻☹eecs16a!☹☻'
