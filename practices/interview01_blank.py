def majority_element_indexes(lst):
    '''
    Returns a list of the majority element indexes.
    Majority element is the element that appears more than floor(n/2) times.
    If there is no majority element, return an empty list.

    >>> majority_element_indexes([1,1,2])
    [0, 1]
    >>> majority_element_indexes([1,2])
    []
    >>> majority_element_indexes([])
    []
    >>> majority_element_indexes([1,1,2,1,3,1,3])
    [0, 1, 3, 5]
    >>> majority_element_indexes([1,3,2,3,4,3,3,1,3])
    [1, 3, 5, 6, 8]
    '''
