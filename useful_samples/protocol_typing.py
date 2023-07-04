# protocol.py : use sample of Protocol from typing tools
# Even if this does not raise a runtime error,
# Mypy or any other type checker will raise an error if the type is not suitable when calling 'greet'.
# A way to pass it without inheriting from a common class is to use Protocol

from typing import Protocol


class Named(Protocol):
    name: str


class Dog:
    name = 'Good Dog'


class Cat:
    name = 'Sweet Cat'


def greet_Named(obj : Named) -> None:
    print(f"Hi {obj.name}")

def greet_Dog(obj : Dog) -> None:
    print(f"Hi {obj.name}")


x = Dog()
greet_Named(x)
greet_Dog(x)

y = Cat()
greet_Named(y)
greet_Dog(y)


# The last line will raise an error when the previous won't
# > mypy .\protocol_typing.py
# protocol_typing.py:34: error: Argument 1 to "greet_Dog" has incompatible type "Cat"; expected "Dog"  [arg-type]
# Found 1 error in 1 file (checked 1 source file)