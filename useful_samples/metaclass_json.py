import json

class Json_Object_Meta(type):
    """ Metaclass responsible for adding the Encoder and Decoder methods to the class that uses it """

    def __new__(cls, name, bases, attrs):
        # # Check if the class already has an __init__ method defined
        # if '__init__' in attrs:
        #     # Wrap the existing __init__ method to add JSON serialization/deserialization
        #     original_init = attrs['__init__']
        #
        #     def wrapped_init(self, *args, **kwargs):
        #         original_init(self, *args, **kwargs)
        #
        #     attrs['__init__'] = wrapped_init

        # Add the Encoder method to the class
        def to_json(self):
            return json.dumps(self.__dict__)

        attrs['to_json'] = to_json

        # Add the Decoder method to the class
        @classmethod
        def from_json(cls, json_string):
            obj = cls.__new__(cls)
            obj.__dict__ = json.loads(json_string)
            return obj

        attrs['from_json'] = from_json

        return super().__new__(cls, name, bases, attrs)

# Example usage of the metaclass
class MyClass(metaclass=Json_Object_Meta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of MyClass
obj = MyClass("John", 30)


# Convert the instance to a JSON string
json_string = obj.to_json()
print(json_string)  # Output: '{"name": "John", "age": 30}'

# Create a new instance from the JSON string
new_obj = MyClass.from_json(json_string)
print(new_obj.name)  # Output: 'John'
print(new_obj.age)   # Output: 30
