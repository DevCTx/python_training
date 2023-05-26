""" Defaultdict samples """

""" Define the 'Anonymous' string as default value for any requested key on a dictionary if non-existent """

from collections import defaultdict

def generate_defaultdict():
    ''' PS : use python -m doctest ./defaultdict.py to run it

    :return:

    >>> datastructure = generate_defaultdict()
    >>> datastructure[3] = "John"
    >>> print(datastructure[3])
    John
    >>> print(datastructure[9762])
    Anonymous
    >>> print(datastructure["pistache"])
    Anonymous

    '''
    obj = defaultdict(lambda:"Anonymous")
    return obj


""" Might also be done with a simple dict and a class """

class My_Dict(dict):

    def __getitem__(self, key):
        return self.get(key, "Anonymous")


def generate_my_dict():
    ''' PS : use python -m doctest ./defaultdict.py to run it

    :return:

    >>> datastructure = generate_my_dict()
    >>> datastructure[3] = "John"
    >>> print(datastructure[3])
    John
    >>> print(datastructure[9762])
    Anonymous
    >>> print(datastructure["pistache"])
    Anonymous

    '''
    obj = My_Dict()
    return obj


""" Counts the number of employees in each department """

from collections import defaultdict

dep = [
    ('Sales', 'John'),
    ('Sales', 'Martin'),
    ('Accounting', 'Jane'),
    ('Marketing', 'Elizabeth'),
    ('Marketing', 'Adam')
]
dd = defaultdict(int)
for department, _ in dep:
    dd[department] += 1

print(dd)
