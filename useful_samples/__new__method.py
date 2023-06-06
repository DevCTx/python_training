'''
    __new__ allows per example to implement a design pattern called Singleton,
    which ensures that there is only one instance of a class with a given name
'''
class Single_name:
    instances = []

    def __new__(cls, name):
        for instance in cls.instances:
            if instance.name == name :
                return instance
        new_instance = super().__new__(cls)
        new_instance.name = name
        cls.instances.append(new_instance)
        return new_instance


instance1 = Single_name('Alpha')
print(instance1.name)
instance2 = Single_name('Beta')
print(instance2.name)
instance3 = Single_name('Alpha')
print(instance3.name)

print(instance1 is instance2)   # Output: False (The instances are different)
print(instance1 is instance3)   # Output: True (Both instances are the same)
instance1.number = 1
print(instance3.number)         # Automatically added to instance3 as well because it points on the same object