def val_in_sum_list(N,numlist):
    '''
    Must return all list of numbers from numlist whose sum is equal to N

    >>> val_in_sum_list(5,[1,2,3])
    [(2, 3)]
    >>> val_in_sum_list(5,[1,2,3,3,4,6,7])
    [(1, 4), (2, 3)]
    >>> val_in_sum_list(17,[1,2,3,3,4,6,7])
    [(1, 2, 3, 4, 7), (1, 3, 3, 4, 6), (1, 3, 6, 7), (3, 3, 4, 7), (4, 6, 7)]
    >>> val_in_sum_list(23,[1,2,3,3,4,6,7])
    [(1, 2, 3, 4, 6, 7), (3, 3, 4, 6, 7)]
    >>> val_in_sum_list(27,[1,2,3,3,4,6,7])
    []
    '''

