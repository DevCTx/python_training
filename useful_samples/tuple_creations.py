'''
    Kind of tricky ways to build strings, tuples or lists
    Careful to 'AAPL', which is considered as str in a tuple # tuple('AAPL',)    = ('A', 'A', 'P', 'L') <class 'tuple'>
    but considered as tuple alone                            # 'AAPL',           = ('AAPL',)            <class 'tuple'>
'''

# 'AAPL'            = AAPL                 <class 'str'>
# 'AAPL',           = ('AAPL',)            <class 'tuple'>
# ('AAPL')          = AAPL                 <class 'str'>
# ('AAPL',)         = ('AAPL',)            <class 'tuple'>
# ['AAPL']          = ['AAPL']             <class 'list'>
# ['AAPL',]         = ['AAPL']             <class 'list'>
#
# tuple('AAPL')     = ('A', 'A', 'P', 'L') <class 'tuple'>
# tuple('AAPL',)    = ('A', 'A', 'P', 'L') <class 'tuple'>
# tuple(('AAPL'))   = ('A', 'A', 'P', 'L') <class 'tuple'>
# tuple(('AAPL',))  = ('AAPL',)            <class 'tuple'>
# tuple(['AAPL'])   = ('AAPL',)            <class 'tuple'>
# tuple(['AAPL',])  = ('AAPL',)            <class 'tuple'>
#
# list('AAPL')      = ['A', 'A', 'P', 'L'] <class 'list'>
# list('AAPL',)     = ['A', 'A', 'P', 'L'] <class 'list'>
# list(('AAPL'))    = ['A', 'A', 'P', 'L'] <class 'list'>
# list(('AAPL',))   = ['AAPL']             <class 'list'>
# list(['AAPL'])    = ['AAPL']             <class 'list'>
# list(['AAPL',])   = ['AAPL']             <class 'list'>

val_list = [
    "'AAPL'           ",
    "'AAPL',          ",
    "('AAPL')         ",
    "('AAPL',)        ",
    "['AAPL']         ",
    "['AAPL',]        ",
    "tuple('AAPL')    ",
    "tuple('AAPL',)   ",
    "tuple(('AAPL'))  ",
    "tuple(('AAPL',)) ",
    "tuple(['AAPL'])  ",
    "tuple(['AAPL',]) ",
    "list('AAPL')     ",
    "list('AAPL',)    ",
    "list(('AAPL'))   ",
    "list(('AAPL',))  ",
    "list(['AAPL'])   ",
    "list(['AAPL',])  "
]
for idx, val in enumerate(val_list):
    print(f"{val} = {str(eval(val)):20s} {type(eval(val))}", end='\n\n' if idx%6 == 5 else '\n')
