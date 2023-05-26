""" Decorator Function Samples and order of called in a stack of decorator """

""" Decorator Function Samples """
import time

def timing1(decorated_function):
    def inverse_args(*args_of_decorated_function):
        return f"{time.ctime()} : {decorated_function(*args_of_decorated_function[::-1])}"
    return inverse_args


def timing2(param_decorator):
    def function_decorator(decorated_function):
        def inverse_args(*args_of_decorated_function):
            return f"{param_decorator} : {decorated_function(*args_of_decorated_function[::-1])}"
        return inverse_args
    return function_decorator


@timing1
def division(a, b):
    return f"{a} / {b} = {a / b}\n"

@timing2(time.ctime())
def soustraction(a, b):
    return f"{a} - {b} = {a - b}\n"


@timing2(time.ctime())
@timing1
def multiplication(a, b):
    return f"{a} * {b} = {a * b}"


print(division(20, 10))         # Thu May 18 13:21:57 2023 : 10 / 20 = 0.5
print(soustraction(20, 10))     # Thu May 18 13:21:57 2023 : 10 - 20 = -10
print(multiplication(20, 10))   # Thu May 18 13:21:57 2023 : Thu May 18 13:21:57 2023 : 20 * 10 = 200
print()


""" order of called in a stack of decorator """

def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1 before function call")
        result = func(*args, **kwargs)
        print("Decorator 1 after function call")
        return result
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2 before function call")
        result = func(*args, **kwargs)
        print("Decorator 2 after function call")
        return result
    return wrapper

def decorator3(func):
    def wrapper(*args, **kwargs):
        print("Decorator 3 before function call")
        result = func(*args, **kwargs)
        print("Decorator 3 after function call")
        return result
    return wrapper

@decorator1
@decorator2
@decorator3
def my_function():
    print("My Function")

my_function()

# Decorator 1 before function call
# Decorator 2 before function call
# Decorator 3 before function call
# My Function
# Decorator 3 after function call
# Decorator 2 after function call
# Decorator 1 after function call
