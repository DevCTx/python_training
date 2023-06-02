
# 1 ************** faire la somme de liste de liste ***************
# def sum_list(param):
#     return sum(val for line in param for val in line)
#
#
# print(sum_list([[1, 2], [3], [4, 5]]))

# 2 ***** trouver si 2 elements d'une liste sont égaux à une valeur ****
# from itertools import combinations
#
# def val_in_sum_list(N,liste):
#     """
#
#     >>> val_in_sum_list(5,[1,2,3,3,4,6,7])
#     [(1, 4), (2, 3)]
#     >>> val_in_sum_list(17,[1,2,3,3,4,6,7])
#     [(4, 6, 7), (1, 3, 6, 7), (3, 3, 4, 7), (1, 2, 3, 4, 7), (1, 3, 3, 4, 6)]
#     >>> val_in_sum_list(23,[1,2,3,3,4,6,7])
#     [(3, 3, 4, 6, 7), (1, 2, 3, 4, 6, 7)]
#     >>> val_in_sum_list(27,[1,2,3,3,4,6,7])
#     []
#     """
#     k=[]
#     for i in range(2,len(liste)):
#         combi = combinations(liste,i)
#         for c in combi :
#             if sum(c) == N:
#                 if c not in k:
#                     k.append(c)
#     return True if k else False
#
# print(val_in_sum_list(23,[1,2,3,3,4,6,7]))

# 3 ************ afficher toutes les sommes de 2 elements d'une liste, triées par valeurs ***********

# from itertools import combinations
# from collections import defaultdict
#
# L = [ 2, 8, 3, 5, 4, 1 ]
# dd = defaultdict(int)
# for v1,v2 in combinations( sorted(L), 2):
#     dd[f"({v1}, {v2})"] = v1+v2
# for d_item in sorted( dd.items(), key=lambda x: (x[1],min(x[0]))):
#     print( f"{d_item[0]} = {d_item[1]}" )


# 4 ************ increment 2 ***************
# def increment_2(counter):
#     counter += 2
#
#
# result = []
# counter = 0
#
# increment_2(counter)
# result.append(counter)
#
# increment_2(counter)
# result.append(counter)
#
# print(result)

# 5 *********** docstring ******************
# import string
# import random
#
#
# def generate_password(new_password: int = 12) -> str:
#     """ Generate a password base on ascii letters
#
#     :param new_password: length of the password to generate, default value = 12
#     :type new_password: int
#
#     :return: generated password of a new_password length
#     """
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
# print(dir(DirectClass))  # ['BigValue', '__class__', '__delattr__', '__dict__', '__dir__',  ...
# print(dir(InheritedClass))  # ['BigValue', '__class__', '__delattr__', '__dict__', '__dir__',  ...
# print(dir(DirectClass) == dir(InheritedClass))  # True
# print(dir(DirectClass) is dir(InheritedClass))  # False


# 7 ************* recuperer la clé d'une valeur dans un dictionnaire ****************

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(d.get(3))  # None
# print(d.get('c'))  # 3
# print(*(k for k, v in d.items() if v == 3))
#
# d = {'a': 3, 'b': 3, 'c': 3, 'd': 3}
# print(d.get(3))  # None
# print(d.get('c'))  # 3
# print(*(k for k, v in d.items() if v == 3))

# 7bis ************* recuperer la clé de la valeur max d'un dictionnaire ****************
# d = {'a': 2, 'b': 3, 'c': 1, 'd': 0}
# print( [k for (k,v) in d.items() if v==max([v for (k,v) in d.items()])][0] )
# print( [k for (k,v) in d.items() if v==max(d.values())][0] )
# print( [k for k in d.keys() if d[k]==max(d.values())][0] )
# print( *(k for (k,v) in d.items() if v==max(d.values())) )
# print( max(d,key=lambda x : d[x] ) )
# # ou mieux
# print( max(d,key=d.get) )

# 8 ******** quel est le plus simple pour demander du texte d'une page HTTP ******
# import requests
#
# url = 'https://www.example.com'
# response = requests.get(url)
#
# if response.status_code == 200:
#     html_content = response.text
#     print(html_content)
# else:
#     print('Impossible de récupérer la page web')
#
# ****
#
# import urllib3
#
# http = urllib3.PoolManager()
#
# url = 'https://www.example.com'
# response = http.request('GET', url)
#
# print(response.data)


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
#     if len(liste) <= 0 or val <= liste[0]:
#         return None
#     if val > liste[len(liste) - 1]:
#         return liste[len(liste) - 1]
#     left = 0
#     right = len(liste) - 1
#     while left < right:
#         mid = left + (right - left) // 2 + (right - left) % 2
#         # print(f"left {left} mid {mid} right {right}")
#         if val < liste[mid]:
#             if right == mid:
#                 break
#             else:
#                 right = mid
#         elif val > liste[mid]:
#             left = mid
#         else:
#             break
#     return liste[mid - 1]

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
#     left = 0
#     right = len(liste) -1
#
#     result = None
#     nb_comp = 1
#
#     while left <= right and liste and val > liste[0]:   # 4 <= 3
#         mid = (left + right) // 2                       # (3+3)//2=3
#
#         nb_comp += 1
#         if val <= liste[mid]:                           # 6 <= 7
#             right = mid - 1                             # 4
#         else:
#             result = liste[mid]                         # 5
#             left = mid + 1                              # 3
#
#     return result, nb_comp


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
# print(foo.size,Foo.size)


# 11 **************** Heritage **********************
# écrire Student qui hérite de Person, qui se présente mais fait son devoir au lieu de dormir
# class Person:
#
#     def __init__(self,name):
#         self.name = name
#
#     def introduce_itself(self):
#         return f"Hi my name is {self.name}"
#
#     def do_something(self):
#         return f"{self.name} is sleeping"
#
# class Student(Person):
#
#     def __init__(self, name):
#         super().__init__(name)
#
#     def do_something(self):
#         return f"{self.name} is working"
#
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
# # # Sélectionner les éléments qui ont 3 chiffres consécutifs
# # # ex : Pem345 , Zp309dk , 344k32 seront validés quand el4k4m4 ne le sera pas
# l=['Pem345', 'Zp309dk' , '344k32', 'el4k4m4']
# reg = '\d{3}'
# print([i for i in l if re.search(reg,i)])


# 13 ******************* Relier Nom / Definition *****************
# CPython -- implementation par defaut de python
# Pypy    -- implementation alternative de python (en python)
# venv    -- environnement isolés
# pip     -- installateur de packet par défaut

# 14 ******************* correct str ******************
# print("chaines "imbriquees"")   # SyntaxError
# print("string avec \u3495")     # string avec 㒕
# print(r"string avec \u3495")    # string avec \u3495
# print('char [']')               # SyntaxError

# 15 ******************* f-string **********************
# #A
# firstname="John"; lastname="Doe"; birthday="01/01/2001"
# print("A. Je suis {} {} né le {}".format(firstname,lastname,birthday) )           #OK
# #B
# firstname="John"; lastname="Doe"; birthday="01/01/2001"
# print("B. Je suis {0} {1} né le {2}".format(firstname,lastname,birthday) )        #OK
# #C
# firstname="John"; lastname="Doe"; birthday="01/01/2001"
# print(f"C. Je suis {0} {1} né le {2}".format(firstname,lastname,birthday) )       #NO
# #D
# firstname="John"; lastname="Doe"; birthday="01/01/2001"
# print(f"D. Je suis {firstname} {lastname} né le {birthday}")                      #OK
# #E
# sentence = "E. Je suis {firstname} {lastname} né le {birthday}"
# print(sentence.format(lastname="Doe", firstname="John", birthday="01/01/2001"))   #OK
# #F
# sentence = "F. Je suis {} {} né le {}"
# print(sentence.format("John", "Doe", "01/01/2001"))                               #OK

# 16 ******************* palindrome ******************
# def is_palindrome(param):
#     return param==param[::-1]

# 17 ************* valeur de f-string : r-string est raw non f-strinf **********
# value = 1234
# print(f'decimal={value:010}')
# print(f'binaire={value:012b}')
# print(f'hexa={value:#06x}')
# print(f'octo={value:#2o}')
# print(f'float={value:10.2f}')
# print(f'scientific={value:#2g} <> expo={value:#2e}')
# print(f'system={value:#n}')

#18 ************** Convert a matrix into list of index ***********************
# def graph_matrix_to_list(m):
#     '''
#     >>> graph_matrix_to_list([[False,True],[False,False]])
#     [[1], []]
#     >>> graph_matrix_to_list([[False, True, True],[ True, False, False],[ True, True, False]])
#     [[1, 2], [0], [0, 1]]
#     '''
#     l=[]
#     for ridx,r in enumerate(m):
#         l.append([])
#         for cidx,c in enumerate(r) :
#             if c == True:
#                 l[ridx].append(cidx)
#     return l