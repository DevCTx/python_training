'''
Finds duplicates into set
'''

set_list = [
    {1, 2, 35, 23, 24},
    {0, 3, 6, 18, 34, 65},
    {5, 6, 18, 67},
    {1, 2, 35, 23, 28}
]
set_to_match = {0, 18, 28}

for line in range( len(set_list) ):
    same = set_list[line] & set_to_match                    # a simple & on sets allows to find duplicates
    print(f"[{line}]  same={same}   list={list(same)}")

# Does not work with lists or tuples
'''
list_list = [
    [1, 2, 35, 23, 24],
    [0, 3, 6, 18, 34, 65],
    [5, 6, 18, 67],
    [1, 2, 35, 23, 28]
]
list_to_match = [0, 18, 28]

for line in range( len(list_list) ):
    same = list_list[line] & list_to_match                    # un simple & sur des set permet de retrouver les doublons
    print(f"[{line}]  same={same}   liste={list(same)}")
'''
"""
tuple_tuple = (
    (1, 2, 35, 23, 24),
    (0, 3, 6, 18, 34, 65),
    (5, 6, 18, 67),
    (1, 2, 35, 23, 28)
)
tuple_to_match = (0, 18, 28)

for line in range( len(tuple_tuple) ):
    same = tuple_tuple[line] & tuple_to_match                    # un simple & sur des set permet de retrouver les doublons
    print(f"({line})  same={same}   tuplee={tuple(same)}")
"""