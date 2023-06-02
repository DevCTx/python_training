
# 1 ************** faire la somme de liste de liste ***************
# print(sum_list([[1, 2], [3], [4, 5]]))

# 2 ***** trouver si 2 elements d'une liste sont égaux à une valeur ****
# print(val_in_sum_list(23,[1,2,3,3,4,6,7]))

# 3 ************ afficher toutes les sommes de 2 elements d'une liste, triées par valeurs ***********
# L = [ 2, 8, 3, 5, 4, 1 ]


# 4 ************ create a function able to increment 2 ***************
# print(result)

# 5 *********** create the docstring of the function ******************
# import string
# import random
#
#
# def generate_password(new_password: int = 12) -> str:
#     New_pwd = ''
#     for i in range(new_password):
#         New_pwd += random.choice(string.ascii_letters)
#     return New_pwd
#
#
# print(help(generate_password))


# 6 ************** dir ************************

# class DirectClass:
#     BigValue = 12
#
#     def __init__(self, value):
#         self.value = value
#
#
# class InheritedClass(DirectClass):
#     pass
#
#
# print(dir(DirectClass) is dir(InheritedClass))  # True or False ?
# print(dir(DirectClass) == dir(InheritedClass))  # True or False ?


# 7 ************* recuperer la clé d'une valeur dans un dictionnaire ****************
# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}



# 7bis ************* recuperer la clé de la valeur max d'un dictionnaire ****************
# d = {'a': 2, 'b': 3, 'c': 1, 'd': 0}



# 8 ******** quel est le plus simple pour demander du texte d'une page HTTP ******
# import requests
# import urllib3


# 9 ************ Le plus grand inférieur à la valeur ******************
# On vous donne une liste triée d'objets obj_list. Trouvez le plus grand qui est inférieur à val ou None s'il n'y en a pas.
# Votre code doit être correctement optimisé. Une limite de 12 comparaisons sera acceptée pour chaque appel de cette méthode.
# La liste obj_list a une longueur inférieure à 2000.
# Exemples :
# largest_one_lt([1,4,7,12], 6) doit renvoyer 4.
# largest_one_lt([1,4,7,12], 12) doit renvoyer 7
# largest_one_lt([1,4,7,12], 23) doit renvoyer 12.
# largest_one_lt([1,4,7,12], 0) doit renvoyer None.

# def largest_one_lt( liste, val ):
#     '''
#     >>> print(largest_one_lt([1,4,7,12], 1))        # nb pairs, val min
#     (None, 1)
#     >>> print(largest_one_lt([1,4,7,12], 12))       # nb pairs, val max
#     (7, 4)
#     >>> print(largest_one_lt([1,4,7,12], 7))        # nb pairs, val existante
#     (4, 3)
#     >>> print(largest_one_lt([1,4,7,12], 6))        # nb pairs, val inexsitante
#     (4, 3)
#     >>> print(largest_one_lt([1,4,7,12], 23))       # nb pairs, val supérieure
#     (12, 4)
#     >>> print(largest_one_lt([1,4,7,12], 0))        # nb pairs, val inférieure
#     (None, 1)
#     >>> print(largest_one_lt([1,4,5,7,12], 1))      # nb impairs, val min
#     (None, 1)
#     >>> print(largest_one_lt([1,4,5,7,12], 12))     # nb impairs, val max
#     (7, 5)
#     >>> print(largest_one_lt([1,4,5,7,12], 7))      # nb impairs, val existante
#     (5, 4)
#     >>> print(largest_one_lt([1,4,5,7,12], 6))      # nb impairs, val inexistante
#     (5, 4)
#     >>> print(largest_one_lt([1,4,5,7,12], 23))     # nb impairs, val supérieure
#     (12, 5)
#     >>> print(largest_one_lt([1,4,5,7,12], 0))      # nb impairs, val inférieure
#     (None, 1)
#     >>> print(largest_one_lt([4], 4))
#     (None, 1)
#     >>> print(largest_one_lt([], 4))
#     (None, 0)
#     >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 1))   # nb impairs, val min
#     (None, 1)
#     >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 29))  # nb impairs, val max
#     (27, 19)
#     >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 24))  # nb impairs, val existante>12
#     (22, 16)
#     >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 21))  # nb impairs, val inexistante>12
#     (20, 15)
#     >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 5))  # nb impairs, val existante<12
#     (4, 4)
#     >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 2))  # nb impairs, val inexistante<12
#     (1, 2)
#     >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 0))  # nb impairs, val inférieure
#     (None, 1)
#     >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 30))  # nb impairs, val supérieure
#     (29, 19)
#     >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 1))   # nb pairs, val min
#     (None, 1)
#     >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 29))  # nb pairs, val max
#     (27, 20)
#     >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 24))  # nb pairs, val existante>12
#     (23, 17)
#     >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 21))  # nb pairs, val inexistante>12
#     (20, 15)
#     >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 5))  # nb pairs, val existante<12
#     (4, 4)
#     >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 2))  # nb pairs, val inexistante<12
#     (1, 2)
#     >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 0))  # nb pairs, val inférieure
#     (None, 1)
#     >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 30))  # nb impairs, val supérieure
#     (29, 19)
#     '''
#
# def largest_one_lt2( liste, val ):
#     '''
#     >>> print(largest_one_lt2([1,4,7,12], 1))        # nb pairs, val min
#     (None, 1)
#     >>> print(largest_one_lt2([1,4,7,12], 12))       # nb pairs, val max
#     (7, 4)
#     >>> print(largest_one_lt2([1,4,7,12], 7))        # nb pairs, val existante
#     (4, 3)
#     >>> print(largest_one_lt2([1,4,7,12], 6))        # nb pairs, val inexsitante
#     (4, 3)
#     >>> print(largest_one_lt2([1,4,7,12], 23))       # nb pairs, val supérieure
#     (12, 4)
#     >>> print(largest_one_lt2([1,4,7,12], 0))        # nb pairs, val inférieure
#     (None, 1)
#     >>> print(largest_one_lt2([1,4,5,7,12], 1))      # nb impairs, val min
#     (None, 1)
#     >>> print(largest_one_lt2([1,4,5,7,12], 12))     # nb impairs, val max
#     (7, 4)
#     >>> print(largest_one_lt2([1,4,5,7,12], 7))      # nb impairs, val existante
#     (5, 3)
#     >>> print(largest_one_lt2([1,4,5,7,12], 6))      # nb impairs, val inexistante
#     (5, 3)
#     >>> print(largest_one_lt2([1,4,5,7,12], 23))     # nb impairs, val supérieure
#     (12, 4)
#     >>> print(largest_one_lt2([1,4,5,7,12], 0))      # nb impairs, val inférieure
#     (None, 1)
#     >>> print(largest_one_lt2([4], 4))
#     (None, 1)
#     >>> print(largest_one_lt2([], 4))
#     (None, 1)
#     >>> print(largest_one_lt2([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 1))   # nb impairs, val min
#     (None, 1)
#     >>> print(largest_one_lt2([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 29))  # nb impairs, val max
#     (27, 6)
#     >>> print(largest_one_lt2([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 24))  # nb impairs, val existante>12
#     (22, 5)
#     >>> print(largest_one_lt2([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 21))  # nb impairs, val inexistante>12
#     (20, 6)
#     >>> print(largest_one_lt2([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 5))  # nb impairs, val existante<12
#     (4, 6)
#     >>> print(largest_one_lt2([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 2))  # nb impairs, val inexistante<12
#     (1, 5)
#     >>> print(largest_one_lt2([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 0))  # nb impairs, val inférieure
#     (None, 1)
#     >>> print(largest_one_lt2([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 30))  # nb impairs, val supérieure
#     (29, 6)
#     >>> print(largest_one_lt2([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 1))   # nb pairs, val min
#     (None, 1)
#     >>> print(largest_one_lt2([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 29))  # nb pairs, val max
#     (27, 6)
#     >>> print(largest_one_lt2([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 24))  # nb pairs, val existante>12
#     (23, 6)
#     >>> print(largest_one_lt2([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 21))  # nb pairs, val inexistante>12
#     (20, 6)
#     >>> print(largest_one_lt2([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 5))  # nb pairs, val existante<12
#     (4, 6)
#     >>> print(largest_one_lt2([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 2))  # nb pairs, val inexistante<12
#     (1, 5)
#     >>> print(largest_one_lt2([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 0))  # nb pairs, val inférieure
#     (None, 1)
#     >>> print(largest_one_lt2([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 30))  # nb impairs, val supérieure
#     (29, 6)
#     >>> print(largest_one_lt2([1,3,5,7,8,9], 6))  # nb impairs, val supérieure
#     (5, 4)
#     '''


# 10 ***************** variable de classe *********************
# class Foo:
#     size=0
#
#     @classmethod
#     def add(cls,value):
#         cls.size+=value
#
# foo = Foo()
# foo.size=42
# foo.add(10)
#
# print(foo.size,Foo.size) ?


# 11 **************** Heritage **********************
# écrire Student qui hérite de Person, qui se présente mais fait son devoir au lieu de dormir

# eric = Person("Eric")
# print( eric.introduce_itself() )
# print( eric.do_something() )
#
# betty = Student("Betty")
# print( betty.introduce_itself() )
# print( betty.do_something() )


# 12 ******************** Regex *************************
# import re
#
# # Sélectionner les éléments qui ont 3 chiffres consécutifs
# # ex : Pem345 , Zp309dk , 344k32 seront validés quand el4k4m4 ne le sera pas
# reg = ''
#
# #print( ... ) ???


# 13 ******************* Relier Nom / Definition *****************
# venv
# CPython
# Pypy
# pip

# implementation par defaut de python
# implementation alternative de python (en python)
# environnement isolés
# installateur de packet par défaut


# 14 ******************* correct str ******************
# print("chaines "imbriquees"")   # Correct or What Error ?
# print("string avec \u3495")     # Correct or What Error ?
# print(r"string avec \u3495")    # Correct or What Error ?
# print('char [']')               # Correct or What Error ?

# 15 ******************* f-string **********************
# #A    # Correct or What Error ?
# firstname="John"; lastname="Doe"; birthday="01/01/2001"
# print("A. Je suis {} {} né le {}".format(firstname,lastname,birthday) )
# #B    # Correct or What Error ?
# firstname="John"; lastname="Doe"; birthday="01/01/2001"
# print("B. Je suis {0} {1} né le {2}".format(firstname,lastname,birthday) )
# #C    # Correct or What Error ?
# firstname="John"; lastname="Doe"; birthday="01/01/2001"
# print(f"C. Je suis {0} {1} né le {2}".format(firstname,lastname,birthday) )
# #D    # Correct or What Error ?
# firstname="John"; lastname="Doe"; birthday="01/01/2001"
# print(f"D. Je suis {firstname} {lastname} né le {birthday}")
# #E    # Correct or What Error ?
# sentence = "E. Je suis {firstname} {lastname} né le {birthday}"
# print(sentence.format(lastname="Doe", firstname="John", birthday="01/01/2001"))
# #F    # Correct or What Error ?
# sentence = "F. Je suis {} {} né le {}"
# print(sentence.format("John", "Doe", "01/01/2001"))

# 16 ******************* palindrome ******************
# def is_palindrome(param):

# 17 ************* valeur de f-string : r-string est raw non f-strinf **********
# print(f'decimal={value:06} : binaire={value:012b} : hexa={value:#06x} : octo={value:#2o} : float={value:2.2f} ')
# value = 123456.789
# print(f'scientific={value:#2g} <> expo={value:#2e} : system={value:#n}')

#18 ************** Convert a matrix into list of index ***********************
# def graph_matrix_to_list(m):
#     '''
#     >>> graph_matrix_to_list([[False,True],[False,False]])
#     [[1], []]
#     >>> graph_matrix_to_list([[False, True, True],[ True, False, False],[ True, True, False]])
#     [[1, 2], [0], [0, 1]]
#     '''
