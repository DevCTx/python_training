'''
    JSONEncode / JSONDecoder : useful to serialize any kind of object
'''
import json


class Vector:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return f'{self.__dict__}'

    class Encoder(json.JSONEncoder):
        def default(self, v):
            if isinstance(v, Vector):
                return v.__dict__
            else:
                return super().default(self, v)

    class Decoder(json.JSONDecoder):
        def __init__(self):
            super().__init__(object_hook=self.decode_vector)

        def decode_vector(self, d):
            return Vector(*d["args"])         # Si on ne passe une liste non définie d'arguments

class Vector2:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'{self.__dict__}'

    class Encoder(json.JSONEncoder):
        def default(self, v):
            if isinstance(v, Vector2):
                return v.__dict__
            else:
                return super().default(self, v)

    class Decoder(json.JSONDecoder):
        def __init__(self):
            super().__init__(object_hook=self.decode_vector)

        def decode_vector(self, d):
            return Vector2(**d)             # Si on ne passe une liste finie d'arguments positionnels

v1 = Vector(4, 2, 6)
print( v1, type(v1) )
json_str = json.dumps(v1, cls=Vector.Encoder)
print( json_str )
v1_back = json.loads(json_str, cls=Vector.Decoder)
print( v1_back, type(v1_back) )
json_str2 = json.dumps(json.loads(json_str, cls=Vector.Decoder), cls=Vector.Encoder)
print( json_str2 )
print()

v2 = Vector2(4, 2, 6)
print( v2, type(v2) )
json_str3 = json.dumps(v2, cls=Vector2.Encoder)
print( json_str3, type(json_str3)  )
v2_back = json.loads(json_str3, cls=Vector2.Decoder)
print( v2_back, type(v2_back) )
json_str4 = json.dumps(json.loads(json_str3, cls=Vector2.Decoder), cls=Vector2.Encoder)
print( json_str4, type(json_str4) )
print()


