import math

def is_prime(n):
    '''
    Calculate the n first prime numbers

    A prime is a whole number greater than 1 that cannot be divided by any whole number other than itself.

    Function optimized by square root not to have to calculate doubles.
    ex : 36 = 2*18 and 18*2 but this one has already been tested so can be avoided
    ex : 36 = 3*12 and 12*3 but this one has already been tested so can be avoided
    ex : 36 = 4*9 and 9*4 but this one has already been tested so can be avoided
    ex : 36 = 6*6 and 6*6 but this one has already been tested so can be avoided and matchs with its square root !
    ex : 19 , we can so test 19/2=9.5, 19/3=6.33... , 19/4=4.75, and that's it because 19/5=3.8 is less than 5
    so it won't be possible to find another whole number over than 5 able to divide 19 and to get a whole number
    '''
    if n < 2 :
        return False
    else:
        for i in range( 2, int(math.sqrt(n))+1 ):
            if (n%i) == 0:
                return False
        return True

print( [ i for i in range(100) if is_prime(i) ]  )
