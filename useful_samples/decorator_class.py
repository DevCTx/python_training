""" Decorator Class Sample """

import time

class Timing():

    def __init__(self, param_decorator=time.ctime()):
        self.param_class = param_decorator

    def __call__(self, decorated_function):
        """ Called by the system each time we call the decorated_function """
        def add_timing(*args_decorated_function,**kwargs_decorated_function):
            return f"{self.param_class} : {decorated_function(*args_decorated_function)}"
        return add_timing

@Timing()
def addition(a, b):
    return f"{a} + {b} = {a + b}"

@Timing(time.ctime())
@Timing("Pacific Standard Time")
def soustraction(a, b):
    return f"{a} - {b} = {a - b}"

@Timing(time.ctime())
def multiplication(a, b):
    return f"{a} * {b} = {a * b}"


print(addition(20, 10))         # Thu May 18 13:18:47 2023 : 20 + 10 = 30
print(soustraction(20, 10))     # Thu May 18 13:18:47 2023 : Pacific Standard Time : 20 - 10 = 10
print(multiplication(20, 10))   # Thu May 18 13:18:47 2023 : 20 * 10 = 200

