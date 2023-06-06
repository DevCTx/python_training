'''
    A faster way to find an index into a sorted list
    Can be also used to insert a value into a sorted list at the index to be already sorted
'''
import bisect

def largest_one_lt(obj_list, val):
    '''
    >>> print(largest_one_lt([1,4,7,12], 1))        # nb pairs, val min
    None
    >>> print(largest_one_lt([1,4,7,12], 3))        # nb pairs, val min
    1
    >>> print(largest_one_lt([1,4,7,12], 12))       # nb pairs, val max
    7
    >>> print(largest_one_lt([1,4,7,12], 7))        # nb pairs, val existante
    4
    >>> print(largest_one_lt([1,4,7,12], 6))        # nb pairs, val inexsitante
    4
    >>> print(largest_one_lt([1,4,7,12], 23))       # nb pairs, val supérieure
    12
    >>> print(largest_one_lt([1,4,7,12], 0))        # nb pairs, val inférieure
    None
    >>> print(largest_one_lt([1,4,5,7,12], 1))      # nb impairs, val min
    None
    >>> print(largest_one_lt([1,4,5,7,12], 12))     # nb impairs, val max
    7
    >>> print(largest_one_lt([1,4,5,7,12], 7))      # nb impairs, val existante
    5
    >>> print(largest_one_lt([1,4,5,7,12], 6))      # nb impairs, val inexistante
    5
    >>> print(largest_one_lt([1,4,5,7,12], 23))     # nb impairs, val supérieure
    12
    >>> print(largest_one_lt([1,4,5,7,12], 0))      # nb impairs, val inférieure
    None
    >>> print(largest_one_lt([4], 4))
    None
    >>> print(largest_one_lt([], 4))
    None
    >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 1))   # nb impairs, val min
    None
    >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 29))  # nb impairs, val max
    27
    >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 24))  # nb impairs, val existante>12
    22
    >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 21))  # nb impairs, val inexistante>12
    20
    >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 5))  # nb impairs, val existante<12
    4
    >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 2))  # nb impairs, val inexistante<12
    1
    >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 0))  # nb impairs, val inférieure
    None
    >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 30))  # nb impairs, val supérieure
    29
    >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 1))   # nb pairs, val min
    None
    >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 29))  # nb pairs, val max
    27
    >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 24))  # nb pairs, val existante>12
    23
    >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 21))  # nb pairs, val inexistante>12
    20
    >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 5))  # nb pairs, val existante<12
    4
    >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 2))  # nb pairs, val inexistante<12
    1
    >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 0))  # nb pairs, val inférieure
    None
    >>> print(largest_one_lt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 30))  # nb impairs, val supérieure
    29
    '''
    # if not obj_list or len(obj_list) == 0 or not val or val <= obj_list[0]:
    #     return None
    # if val>obj_list[-1]:
    #     return obj_list[-1]
    #
    # left = 0                                                                # 0
    # right = len(obj_list)-1                                                 # 3
    # while (right-left)>1:                                                       # 0 < 1
    #     mid = (right + left) // 2
    #     if val > obj_list[mid]:
    #         left = mid
    #     else:
    #         right = mid
    # return obj_list[left]
    if not obj_list or len(obj_list) == 0 or not val or val <= obj_list[0]:
        return None
    else:
        return obj_list[ bisect.bisect_left(obj_list, val) - 1 ]
