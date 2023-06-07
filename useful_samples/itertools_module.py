from itertools import combinations, permutations, combinations_with_replacement, product

# Combinations : Associate 2 items of the list
print( f"{[x+y for (x,y) in combinations('ABCD', 2)] = }" )
# ['AB', 'AC', 'AD', 'BC', 'BD', 'CD']

# Permutations : Associate 2 items of the list and their permutations
print( f"{[x+y for (x,y) in permutations('ABCD', 2)] = }" )
# ['AB', 'AC', 'AD', 'BA', 'BC', 'BD', 'CA', 'CB', 'CD', 'DA', 'DB', 'DC']

# Combinations : Associate 2 items of the list and the doubled items
print( f"{[x+y for (x,y) in combinations_with_replacement('ABCD',2)] = }" )
# ['AA', 'AB', 'AC', 'AD', 'BB', 'BC', 'BD', 'CC', 'CD', 'DD']

# Product : Associate 2 items of the list, their permutations and the doubled items
print( f"{[x+y for (x,y) in product('ABCD', repeat=2)] = }" )
# ['AA', 'AB', 'AC', 'AD', 'BA', 'BB', 'BC', 'BD', 'CA', 'CB', 'CC', 'CD', 'DA', 'DB', 'DC', 'DD']



