'''
    Pickle use Sample to serialize in bytes any kind of object
'''

import pickle

class class_sample:
    number_sample = 35
    string_sample = "hey"
    list_sample = [1, 2, 3]
    dict_sample = {"first": "a", "second": 2, "third": [1, 2, 3]}
    tuple_sample = (22, 23)

    def method_sample(self):
        return f"I am a '{self.__class__.__name__}' object"

my_object = class_sample()

print(f"This is my object: {my_object}")
print(f"and its method : {my_object.method_sample()}\n")
my_pickled_object = pickle.dumps(my_object)  # Pickling the object
print(f"This is my pickled object:\n{my_pickled_object}\n")

print(f"This is my object.dict_sample:\n{my_object.dict_sample}\n")
my_object.dict_sample = None
print(f"This is my object.dict_sample after erasing:\n{my_object.dict_sample} \n")

my_unpickled_object = pickle.loads(my_pickled_object)  # Unpickling the object
print(f"This is my unpickled object: {my_unpickled_object}\n")
print(f"This is dict_sample from my unpickled object:\n{my_unpickled_object.dict_sample}")
print(f"and its method : {my_unpickled_object.method_sample()}\n")
