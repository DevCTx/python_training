import bisect


def closest_lt_or_eq(obj_list, val):
    '''
    Returns the closest value to obj_list that is less than or equal to the number val else None

    >>> print(closest_lt_or_eq([1,2,4,7,12],1))
    1
    >>> print(closest_lt_or_eq([1,2,4,7,12],4))
    4
    >>> print(closest_lt_or_eq([1,2,4,7,12],5))
    4
    >>> print(closest_lt_or_eq([1,2,4,7,12],6))
    4
    >>> print(closest_lt_or_eq([1,2,4,7,12],12))
    12
    >>> print(closest_lt_or_eq([1,2,4,7,12],23))
    None
    >>> print(closest_lt_or_eq([1,2,4,7,12],-1))
    None
    '''
    #
    # if obj_list is None or len(obj_list)==0 or val==None or val<obj_list[0]:
    #     return None
    #
    # min = None
    #
    # for idx,value in enumerate(obj_list):
    #     if value == val:
    #         min = value
    #         break
    #     elif value > val :
    #         min = obj_list[idx - 1]
    #         break
    #
    # return min
    if not obj_list or len(obj_list) == 0 or not val or val < obj_list[0] or val > obj_list[-1]:
        return None
    else:
        return obj_list[ bisect.bisect(obj_list, val) - 1]

def largest_one_lt( obj_list, val ):
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
    # left = 0
    # right = len(obj_list)-1
    #
    # result = None
    # while left <= right and obj_list and val > obj_list[0]:
    #     mid = (left + right)//2
    #     if val <= obj_list[mid]:
    #         right = mid - 1
    #     else:
    #         result = obj_list[mid]
    #         left = mid + 1
    #
    # return result
    if obj_list is None or len(obj_list) == 0 or val is None or val<=obj_list[0]:
        return None
    return obj_list[bisect.bisect_left(obj_list,val) -1 ]


def smallest_one_gt( obj_list, val ):
    '''
    >>> print(smallest_one_gt([1,4,7,12], 1))        # nb pairs, val min
    4
    >>> print(smallest_one_gt([1,4,7,12], 12))       # nb pairs, val max
    None
    >>> print(smallest_one_gt([1,4,7,12], 7))        # nb pairs, val existante
    12
    >>> print(smallest_one_gt([1,4,7,12], 6))        # nb pairs, val inexsitante
    7
    >>> print(smallest_one_gt([1,4,7,12], 23))       # nb pairs, val supérieure
    None
    >>> print(smallest_one_gt([1,4,7,12], 0))        # nb pairs, val inférieure
    1
    >>> print(smallest_one_gt([1,4,5,7,12], 1))      # nb impairs, val min
    4
    >>> print(smallest_one_gt([1,4,5,7,12], 12))     # nb impairs, val max
    None
    >>> print(smallest_one_gt([1,4,5,7,12], 7))      # nb impairs, val existante
    12
    >>> print(smallest_one_gt([1,4,5,7,12], 6))      # nb impairs, val inexistante
    7
    >>> print(smallest_one_gt([1,4,5,7,12], 23))     # nb impairs, val supérieure
    None
    >>> print(smallest_one_gt([1,4,5,7,12], 0))      # nb impairs, val inférieure
    1
    >>> print(smallest_one_gt([4], 4))
    None
    >>> print(smallest_one_gt([], 4))
    None
    >>> print(smallest_one_gt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 1))   # nb impairs, val min
    3
    >>> print(smallest_one_gt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 29))  # nb impairs, val max
    None
    >>> print(smallest_one_gt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 24))  # nb impairs, val existante>12
    26
    >>> print(smallest_one_gt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 21))  # nb impairs, val inexistante>12
    22
    >>> print(smallest_one_gt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 5))  # nb impairs, val existante<12
    7
    >>> print(smallest_one_gt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 2))  # nb impairs, val inexistante<12
    3
    >>> print(smallest_one_gt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 0))  # nb impairs, val inférieure
    1
    >>> print(smallest_one_gt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 30))  # nb impairs, val supérieure
    None
    >>> print(smallest_one_gt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 1))   # nb pairs, val min
    3
    >>> print(smallest_one_gt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 29))  # nb pairs, val max
    None
    >>> print(smallest_one_gt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 24))  # nb pairs, val existante>12
    26
    >>> print(smallest_one_gt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 21))  # nb pairs, val inexistante>12
    22
    >>> print(smallest_one_gt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 5))  # nb pairs, val existante<12
    7
    >>> print(smallest_one_gt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 2))  # nb pairs, val inexistante<12
    3
    >>> print(smallest_one_gt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,23,24,26,27,29], 0))  # nb pairs, val inférieure
    1
    >>> print(smallest_one_gt([1,3,4,5,7,8,9,12,13,14,16,17,18,20,22,24,26,27,29], 30))  # nb impairs, val supérieure
    None
    '''
    # left = 0
    # right = len(obj_list)-1
    #
    # result = None                                       # [1,4,5,7,12]  7
    # while left <= right and obj_list and val < obj_list[-1]:  # 4 <= 3
    #     mid = (left + right)//2                         # (3+3)//2=3
    #     if val < obj_list[mid]:       # First part         # 7 < 7
    #         result = obj_list[mid]                         # 12
    #         right = mid - 1                             # 3
    #     else:                       # Second part       #
    #         left = mid + 1                              # 4
    #
    # return result
    if obj_list is None or len(obj_list) == 0 or val is None or val>=obj_list[-1]:
        return None
    return obj_list[ bisect.bisect_right(obj_list,val) ]


























