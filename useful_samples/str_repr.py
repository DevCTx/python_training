'''
    # str() : returns printable/human-readable string representation
    # repr() : returns string representation that's a 'valid' Python expression (meaning can be passed to eval())
'''

class Fraction:
    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    def __str__(self):
        return str(self.__num) + '/' + str(self.__den)

    def __repr__(self):
        return 'Fraction(' + str(self.__num) + ',' + str(self.__den) + ')'

f = Fraction(1,2)
print('I want to represent Fraction as a STRING :', str(f))     # 1/2
print('I want to represent Fraction as an OBJECT :', repr(f))   # Fraction(1,2)
print( "eval( repr(f) ) :", eval( repr(f) ))                    # 1/2
print( "eval( str(f) ) :", eval( str(f) ))                      # 0.5


print("\n# HERE IS ANOTHER GREAT EXAMPLE")

import datetime
today = datetime.datetime.now()
print( str(today) )         # '2012-03-14 09:21:58.130922'
print( today )              # '2012-03-14 09:21:58.130922'      # IDENTIQUE CAR VA CHERCHER LA FONCTION STR
print( repr(today) )        # 'datetime.datetime(2012, 3, 14, 9, 21, 58, 130922)'
print( eval(repr(today)) )  # '2012-03-14 09:21:58.130922'
# print( eval(str(today)) )   # SyntaxError : Not the purpose !
