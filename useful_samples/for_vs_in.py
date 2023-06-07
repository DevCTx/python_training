'''
    for_vs_in : shows the differences of complexity to solve a single problem by 4 different ways
    better to use 'in' than to make a test on for iteration
'''
import random
import time

n=1000
list_1 = [random.randint(0,1000) for _ in range(n) ]
list_2 = [random.randint(0,1000) for _ in range(n) ]
set_1 = set(list_1)
set_2 = set(list_2)

start = time.time()
nb = 0
for i in list_1:
    for j in list_2:
        if i+j == 1000 :
            nb += 1
print( time.time()-start, nb)

start = time.time()
nb = 0
for i in list_1:
    j = 1000 - i
    if j in list_2 :
        nb += 1
print( time.time()-start, nb)

start = time.time()
nb = 0
for i in set_1:
    for j in set_2:
        if i+j == 1000 :
            nb += 1
print( time.time()-start, nb)

start = time.time()
nb = 0
for i in set_1:
    j = 1000 - i
    if j in set_2 :
        nb += 1
print( time.time()-start, nb)

