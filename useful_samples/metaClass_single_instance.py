class SingletonMeta(type):
    """A metaclass that creates singleton classes."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
            print(cls._instances[cls])
        return cls._instances[cls]

class MyClass(metaclass=SingletonMeta):
    """A singleton class created using the SingletonMeta metaclass."""
    def __init__(self, value):
        self.value = value
        print("init value :", value)

# Create two instances of MyClass
x = MyClass(1)
y = MyClass(2)

print(f"x value : {x.value} (id : {id(x)})")
print(f"y value : {y.value} (id : {id(y)})")
del x
print(f"y value : {y.value} (id : {id(y)})")
