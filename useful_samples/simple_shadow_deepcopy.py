"""
Simple, Shadow and Deep copies samples
"""

import copy
import time

a_list = [(1,2,3) for x in range(1_000_000)]

print('Single reference copy : b_list = a_list')
time_start = time.time()
b_list = a_list
print('Execution time:', round(time.time() - time_start, 3))
print('id(a_list), id(b_list):', id(a_list), id(b_list))
print('a_list is b_list?', a_list is b_list)
print('a_list[0] is b_list[0]', a_list[0] is b_list[0])
print('id(a_list[0]), id(b_list[0]):', id(a_list[0]), id(b_list[0]))
print()

print('Shallow copy : b_list = a_list[:]')
time_start = time.time()
b_list = a_list[:]
print('Execution time:', round(time.time() - time_start, 3))
print('id(a_list), id(b_list):', id(a_list), id(b_list))
print('a_list is b_list?', a_list is b_list)
print('a_list[0] is b_list[0]', a_list[0] is b_list[0])
print('id(a_list[0]), id(b_list[0]):', id(a_list[0]), id(b_list[0]))
print()

print('Deep copy : b_list = copy.deepcopy(a_list)')
time_start = time.time()
b_list = copy.deepcopy(a_list)
print('Execution time:', round(time.time() - time_start, 3))
print('id(a_list), id(b_list):', id(a_list), id(b_list))
print('a_list is b_list?', a_list is b_list)
print('a_list[0] is b_list[0]', a_list[0] is b_list[0])
print('id(a_list[0]), id(b_list[0]):', id(a_list[0]), id(b_list[0]))
