'''
A generator is created with a iterator object into a tuple
It takes no place in memory but can not be size estimated
'''
list_iterator = [1 if x % 2 == 0 else 0 for x in range(10)]
for v in list_iterator:
        print(v, end=" ")
print()
print( type(list_iterator) )    # <class 'list'>
print( len(list_iterator) )     # 10

tuple_iterator = (1 if x % 2 == 0 else 0 for x in range(10))    # define a generator type
for v in tuple_iterator :
        print(v, end=" ")
print()
print( type(tuple_iterator) )   # <class 'generator'>
print( len(tuple_iterator) )    # TypeError: object of type 'generator' has no len()
