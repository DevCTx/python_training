from collections import defaultdict
from collections import Counter


def max_count(string):
    '''
    Returns the max of same letter found into the string arguments

    >>> max_count("ALPHABET")
    2
    >>> max_count("ABBA")
    2
    >>> max_count("")
    0
    >>> max_count("ABRACADABRA")
    5
    '''
    dict_s = defaultdict(int, default=0)
    for letter in string:
        dict_s[letter] += 1
    return max(dict_s.values())


def max_count2(s):
    '''
    Returns the max of same letter found into the string arguments

    >>> max_count2("ALPHABET")
    2
    >>> max_count2("ABBA")
    2
    >>> max_count2("")
    0
    >>> max_count2("ABRACADABRA")
    5
    '''
    result = Counter(s)
    return max(result.values()) if result != Counter() else 0