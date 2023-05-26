class A:
    _Var = 10
    __Var = 20
    def __init__(self, var):
        self._prop = var
        self.__propp = var

class B(A):
    pass

class C(B):
    pass

a = A(1)
c = C(3)
print(isinstance(c,A))      # True

try : print(a._Var)         # 10
except : print("nope")
try : print(A._Var)         # 10
except : print("nope")
try : print(c._Var)         # 10
except : print("nope")
try : print(C._Var)         # 10
except : print("nope")
try : print(a._A_Var)       # nope
except : print("nope")
try : print(A._A_Var)       # nope
except : print("nope")
try : print(c._A_Var)       # nope
except : print("nope")
try : print(C._A_Var)       # nope
except : print("nope")
print()
try : print(a.__Var)        # nope
except : print("nope")
try : print(A.__Var)        # nope
except : print("nope")
try : print(c.__Var)        # nope
except : print("nope")
try : print(C.__Var)        # nope
except : print("nope")
try : print(a._A__Var)      # 20
except : print("nope")
try : print(A._A__Var)      # 20
except : print("nope")
try : print(c._A__Var)      # 20
except : print("nope")
try : print(C._A__Var)      # 20
except : print("nope")
print()
try : print(a._prop)        # 1
except : print("nope")
try : print(A._prop)        # nope
except : print("nope")
try : print(c._prop)        # 3
except : print("nope")
try : print(C._prop)        # nope
except : print("nope")
try : print(a._A_prop)      # nope
except : print("nope")
try : print(A._A_prop)      # nope
except : print("nope")
try : print(c._A_prop)      # nope
except : print("nope")
try : print(C._A_prop)      # nope
except : print("nope")
print()
try : print(a.__propp)      # nope
except : print("nope")
try : print(A.__propp)      # nope
except : print("nope")
try : print(c.__propp)      # nope
except : print("nope")
try : print(C.__propp)      # nope
except : print("nope")
try : print(a._A__propp)    # 1
except : print("nope")
try : print(A._A__propp)    # nope
except : print("nope")
try : print(c._A__propp)    # 3
except : print("nope")
try : print(C._A__propp)    # nope
except : print("nope")
print()