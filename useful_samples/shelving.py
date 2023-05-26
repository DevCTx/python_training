'''
Creates files similar to dictionary but on a disk and not in memory
Equivalent to a very simplified BDD
'''
import os
import shelve

original_list = [1, 2, "hello", {"a": 1, "b": 2}]
another_list = [3, 4, "world"]

with shelve.open("shelve_example") as shelf:
    if 'persistent_list' in shelf :
        print(f"Persistent list existe : {shelf['persistent_list']},\n" 
              f" copie de another list : {another_list}")
        shelf["persistent_list"] = another_list
    else:
        print(f"Persistent list n'existe pas, \n copie de original list : {original_list}")
        shelf["persistent_list"] = original_list


# Delete the created files
os.remove("../shelve_example.bak")
os.remove("../shelve_example.dir")
os.remove("../shelve_example.dat")