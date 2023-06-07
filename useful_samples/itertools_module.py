'''
    Itertools module : returns iterators on
    - combinations : Associate 2 items of the list
    - permutations : Associate 2 items of the list and their permutations
    - combinations_with_replacement : Associate 2 items of the list and the doubled items
    - product : Associate 2 items of the list, their permutations and the doubled items
'''
from itertools import combinations, permutations, combinations_with_replacement, product

obj_list = [1,2,3,4]
print("\nworks on lists :", obj_list)
print( f"{[i for i in combinations(obj_list, 2)] = }" )
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
print( f"{[i for i in permutations(obj_list, 2)] = }" )
# [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]
print( f"{[i for i in combinations_with_replacement(obj_list,2)] = }" )
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
print( f"{[i for i in product(obj_list, repeat=2)] = }" )
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4)]

obj_list = (1,2,3,4)
print("\nworks on tuples :", obj_list)                      # Same results than list
print( f"{[i for i in combinations(obj_list, 2)] = }" )
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
print( f"{[i for i in permutations(obj_list, 2)] = }" )
# [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]
print( f"{[i for i in combinations_with_replacement(obj_list,2)] = }" )
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
print( f"{[i for i in product(obj_list, repeat=2)] = }" )
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4)]

obj_list = 'ABCD'
print("\nworks on string :", obj_list)
print( f"{[x+y for (x,y) in combinations(obj_list, 2)] = }" )
# ['AB', 'AC', 'AD', 'BC', 'BD', 'CD']
print( f"{[x+y for (x,y) in permutations(obj_list, 2)] = }" )
# ['AB', 'AC', 'AD', 'BA', 'BC', 'BD', 'CA', 'CB', 'CD', 'DA', 'DB', 'DC']
print( f"{[x+y for (x,y) in combinations_with_replacement(obj_list,2)] = }" )
# ['AA', 'AB', 'AC', 'AD', 'BB', 'BC', 'BD', 'CC', 'CD', 'DD']
print( f"{[x+y for (x,y) in product(obj_list, repeat=2)] = }" )
# ['AA', 'AB', 'AC', 'AD', 'BA', 'BB', 'BC', 'BD', 'CA', 'CB', 'CC', 'CD', 'DA', 'DB', 'DC', 'DD']

obj_list = 'TTST'
print("\nand doesn't take care of duplicates :", obj_list)
print( f"{[x+y for (x,y) in combinations(obj_list, 2)] = }" )
# ['AB', 'AC', 'AD', 'BC', 'BD', 'CD']
print( f"{[x+y for (x,y) in permutations(obj_list, 2)] = }" )
# ['AB', 'AC', 'AD', 'BA', 'BC', 'BD', 'CA', 'CB', 'CD', 'DA', 'DB', 'DC']
print( f"{[x+y for (x,y) in combinations_with_replacement(obj_list,2)] = }" )
# ['AA', 'AB', 'AC', 'AD', 'BB', 'BC', 'BD', 'CC', 'CD', 'DD']
print( f"{[x+y for (x,y) in product(obj_list, repeat=2)] = }" )
# ['AA', 'AB', 'AC', 'AD', 'BA', 'BB', 'BC', 'BD', 'CA', 'CB', 'CC', 'CD', 'DA', 'DB', 'DC', 'DD']
