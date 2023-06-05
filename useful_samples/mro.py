'''
    Methode Resolution Order ...
    - takes the first class and all its parents which are not common to the following classes
      and add every following class and its parents which are not common to the following classes
      then add the common classes
    - Careful : A class CANNOT be a whole part of a following class or a TypeError will be raised
    - mro() is the best built-in function to see it
'''

class A():
    def ident(self): return 'I am A'

class B(A):
    def ident(self): return 'I am B'

class C(B):
    def ident(self): return 'I am C'

class D(A):
    pass

class E(D):
    pass

class F(C):
    pass

def list_parent_classes(cls):
    parent_classes = cls.__bases__
    print(cls.__name__, end='' if cls.__name__ != 'object' else '\n')
    for parent_class in parent_classes:
        print(" <-", end=' ')
        list_parent_classes(parent_class)

list_parent_classes(A)
list_parent_classes(B)
list_parent_classes(C)
list_parent_classes(D)
list_parent_classes(E)
list_parent_classes(F)


# class MRO1(A,B):    # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B
#     pass            # because A is part of B      # A + B<-A = None,B,A  : impossible

class MRO2(B,A):    # B<-A + A = B,A
    pass
mro2 = MRO2()
print( "B,A : ", mro2.ident(), "   ",[ c.__name__ for c in MRO2.mro()] )   # B,A :  I am B

# class MRO3(A,C):    # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, C
#     pass            # because A is part of C      # A + C<-B<-A = None,C,B,A  : impossible

class MRO4(C,A):    # C<-B<-A + A = C,B,A
    pass
mro4 = MRO4()
print( "C,A : ", mro4.ident(), "   ", [ c.__name__ for c in MRO4.mro()  ])   # C,A :  I am C

# class MRO5(B,C):    # TypeError: Cannot create a consistent method resolution order (MRO) for bases B, C
#     pass            # because B is part of C      # B<-A + C<-B<-A = None,C,B,A  : impossible

class MRO6(C,B):    # C<-B<-A + B<-A = C,B,A
    pass
mro6 = MRO6()
print( "C,B : ", mro6.ident(), "   ", [ c.__name__ for c in MRO6.mro()  ])   # C,B :  I am C

# class MRO7(A,D):    # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, D
#     pass            # because A is part of D      # A + D<-A = None,D,A  : impossible

class MRO8(D,A):    # D<-A + A = D,A
    pass
mro8 = MRO8()
print( "D,A : ", mro8.ident(), "   ", [ c.__name__ for c in MRO8.mro()  ] )   # D,A :  I am A

# class MRO9(A,E):    # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, E
#     pass            # because A is part of D      # A + E<-D<-A = None,E,D,A  : impossible

class MRO10(E,A):   # E<-D<-A + A = E,D,A
    pass
mro10 = MRO10()
print( "E,A : ", mro10.ident(), "   ", [ c.__name__ for c in MRO10.mro() ])   # E,A :  I am A

class MRO11(B,D):   # B<-A + D<-A = B,D,A
    pass
mro11 = MRO11()
print( "B,D : ", mro11.ident(), "   ", [ c.__name__ for c in MRO11.mro() ])   # B,D :  I am B

class MRO12(D,B):   # D<-A + B<-A = D,B,A
    pass
mro12 = MRO12()
print( "D,B : ", mro12.ident(), "   ", [ c.__name__ for c in MRO12.mro() ])   # D,B :  I am B

class MRO13(B,E):   # B<-A + E<-D<-A = B,E,D,A
    pass
mro13 = MRO13()
print( "B,E : ", mro13.ident(), "   ", [ c.__name__ for c in MRO13.mro() ])   # B,E :  I am B

class MRO14(E,B):   # E<-D<-A + B<-A = E,D,B,A
    pass
mro14 = MRO14()
print( "E,B : ", mro14.ident(), "   ", [ c.__name__ for c in MRO14.mro() ])   # E,B :  I am B

class MRO15(C,D):   # C<-B<-A + D<-A = C,B,D,A
    pass
mro15 = MRO15()
print( "C,D : ", mro15.ident(), "   ", [ c.__name__ for c in MRO15.mro() ])   # C,D :  I am C

class MRO16(D,C):   #  D<-A + C<-B<-A = D,C,B,A
    pass
mro16 = MRO16()
print( "D,C : ", mro16.ident(), "   ", [ c.__name__ for c in MRO16.mro() ])   # D,C :  I am C

class MRO17(C,E):   # C<-B<-A + E<-D<-A = C,B,E,D,A
    pass
mro17 = MRO17()
print( "C,E : ", mro17.ident(), "   ", [ c.__name__ for c in MRO17.mro() ])   # C,E :  I am C

class MRO18(E,C):   # E<-D<-A + C<-B<-A = E,D,C,B,A
    pass
mro18 = MRO18()
print( "E,C : ", mro18.ident(), "   ", [ c.__name__ for c in MRO18.mro() ])   # E,C :  I am C

# class MRO19(D,E):   # TypeError: Cannot create a consistent method resolution order (MRO) for bases D, E
#     pass            # because D is part of E      # D<-A + E<-D<-A = None,D,A  : impossible

class MRO20(E,D):   # E<-D<-A + D<-A = E,D,A
    pass
mro20 = MRO20()
print( "E,D : ", mro20.ident(), "   ", [ c.__name__ for c in MRO20.mro() ])   # E,D :  I am A

# class MRO21(A,F):   # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, F
#     pass            # because A is part of F      # A + F<-C<-B<-A = None,F,C,B,A  : impossible

class MRO22(F,A):   # F<-C<-B<-A + A = F,C,B,A
    pass
mro22 = MRO22()
print( "F,A : ", mro22.ident(), "   ", [ c.__name__ for c in MRO22.mro() ])   # F,A :  I am C

# class MRO23(B,F):   # TypeError: Cannot create a consistent method resolution order (MRO) for bases B, F
#     pass            # because B is part of F      # B<-A + F<-C<-B<-A = None,F,C,B,A  : impossible
class MRO24(F,B):   # F<-C<-B<-A + B<-A = F,C,B,A
    pass
mro24 = MRO24()
print( "F,B : ", mro24.ident(), "   ", [ c.__name__ for c in MRO24.mro() ])   # F,B :  I am C

# class MRO25(C,F):   # TypeError: Cannot create a consistent method resolution order (MRO) for bases C, F
#     pass            # because C is part of F      # C<-B<-A + F<-C<-B<-A = None,F,C,B,A : impossible

class MRO26(F,C):   # F<-C<-B<-A + C<-B<-A = F,C,B,A
    pass
mro26 = MRO26()
print( "F,C : ", mro26.ident(), "   ", [ c.__name__ for c in MRO26.mro() ])   # F,C :  I am C

class MRO27(D,F):   # D<-A + F<-C<-B<-A = D,F,C,B,A
    pass
mro27 = MRO27()
print( "D,F : ", mro27.ident(), "   ", [ c.__name__ for c in MRO27.mro() ])   # D,F :  I am C

class MRO28(F,D):   # F<-C<-B<-A + D<-A = F,C,B,D,A
    pass
mro28 = MRO28()
print( "F,D : ", mro28.ident(), "   ", [ c.__name__ for c in MRO28.mro() ])   # F,D :  I am C

class MRO29(E,F):   # E<-D<-A + F<-C<-B<-A = E,D,F,C,B,A
    pass
mro29 = MRO29()
print( "E,F : ", mro29.ident(), "   ", [ c.__name__ for c in MRO29.mro() ])   # E,F :  I am C

class MRO30(F,E):   # F<-C<-B<-A + E<-D<-A = F,C,B,E,D,A
    pass
mro30 = MRO30()
print( "F,E : ", mro30.ident(), "   ", [ c.__name__ for c in MRO30.mro() ])   # F,E :  I am C


### Conlcusion : Always add the class which inherits first

# A <- object
# B <- A <- object
# C <- B <- A <- object
# D <- A <- object
# E <- D <- A <- object
# F <- C <- B <- A <- object
# B,A :  I am B     ['MRO2', 'B', 'A', 'object']
# C,A :  I am C     ['MRO4', 'C', 'B', 'A', 'object']
# C,B :  I am C     ['MRO6', 'C', 'B', 'A', 'object']
# D,A :  I am A     ['MRO8', 'D', 'A', 'object']
# E,A :  I am A     ['MRO10', 'E', 'D', 'A', 'object']
# B,D :  I am B     ['MRO11', 'B', 'D', 'A', 'object']
# D,B :  I am B     ['MRO12', 'D', 'B', 'A', 'object']
# B,E :  I am B     ['MRO13', 'B', 'E', 'D', 'A', 'object']
# E,B :  I am B     ['MRO14', 'E', 'D', 'B', 'A', 'object']
# C,D :  I am C     ['MRO15', 'C', 'B', 'D', 'A', 'object']
# D,C :  I am C     ['MRO16', 'D', 'C', 'B', 'A', 'object']
# C,E :  I am C     ['MRO17', 'C', 'B', 'E', 'D', 'A', 'object']
# E,C :  I am C     ['MRO18', 'E', 'D', 'C', 'B', 'A', 'object']
# E,D :  I am A     ['MRO20', 'E', 'D', 'A', 'object']
# F,A :  I am C     ['MRO22', 'F', 'C', 'B', 'A', 'object']
# F,B :  I am C     ['MRO24', 'F', 'C', 'B', 'A', 'object']
# F,C :  I am C     ['MRO26', 'F', 'C', 'B', 'A', 'object']
# D,F :  I am C     ['MRO27', 'D', 'F', 'C', 'B', 'A', 'object']
# F,D :  I am C     ['MRO28', 'F', 'C', 'B', 'D', 'A', 'object']
# E,F :  I am C     ['MRO29', 'E', 'D', 'F', 'C', 'B', 'A', 'object']
# F,E :  I am C     ['MRO30', 'F', 'C', 'B', 'E', 'D', 'A', 'object']
