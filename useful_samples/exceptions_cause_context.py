"""
    Trace the different possibilities to get context, cause and details about more exceptions if it happens
"""

import traceback


class OwnMath(Exception):
    """ Shows that the context and cause are initialised when the except is run only """
    def __init__(self,msg):
        """ print the message given in args and go to the except OwnMath exception handle """
        print("\nOwnMath msg=",msg)                 # OwnMath msg= My bad
        print("OwnMath args=",self.args)            # OwnMath args= ('My bad',)
        print("OwnMath context=",self.__context__)  # OwnMath context= None # because the context is not initialised yet
        print("OwnMath cause=",self.__cause__)      # OwnMath context= None # because the cause is not initialised yet

def calculate_value(numerator , denominator):
    try:
        value = numerator / denominator
        return value
    except ZeroDivisionError as e:
        print("ZeroDivisionError args=", e.args)    # ZeroDivisionError args= ('division by zero',)
        raise OwnMath("My bad") from e
        # ZeroDivisionError: division by zero
        # if 'from e' : The above exception was the direct cause of the following exception
        # else : During handling of the above exception, another exception occurred:
        # OwnMath: My bad
    except Exception:
        print('Traceback', traceback.format_exc())  # Trace the last erroneous line and specify the exception


def calculate_value_detailed(numerator , denominator):
    try:
        value = numerator / denominator
        return value
    except ZeroDivisionError as e:
        print('Traceback', traceback.format_tb(e.__traceback__))        # Trace the erroneous line (.../denominator)
        try:
            print("ZeroDivisionError args=", e.args)    # ZeroDivisionError args= ('division by zero',)
            raise OwnMath("My bad") from e              # Explicit link with 'from e'
        except OwnMath as o:
            print('Traceback', traceback.format_tb(o.__traceback__))     # Trace the erroneous line (raise OwnMath)
            print('\nPrevious error:', e)               # division by zero
            print('last erreur:', o)                    # My bad

            print('\nLast error Context:', o.__context__)               # division by zero
            print('Same as previous Context ?:', o.__context__ is e)    # True

            print('\nLast error Cause:', o.__cause__)                   # division by zero if 'from e' else None
            print('Same as previous Cause ?:', o.__cause__ is e)        # True if 'from e' else False
        except Exception:
            print('Traceback', traceback.format_exc())  # Trace the last erroneous line and specify the exception
    except Exception:
        print('Traceback', traceback.format_exc())  # Trace the last erroneous line and specify the exception

#calculate_value(4,0)
calculate_value_detailed(4,0)

''' Nécessaire de mettre 2 'try' imbriqués sinon affiche :
ZeroDivisionError: division by zero
The above exception was the direct cause of the following exception:
__main__.OwnMath: My bad
'''