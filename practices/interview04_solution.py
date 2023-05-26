from collections import defaultdict

def generate_dict():
    """
    Must create a dictionary which return "Anonymous" if the key is not existing

    >>> datastructure = generate_dict()
    >>> datastructure[3] = "John"
    >>> assert datastructure[3] == "John"
    >>> assert datastructure[9762] == "Anonymous"
    >>> assert datastructure.get(9762) == "Anonymous"
    """
    dic = defaultdict(lambda:"Anonymous")
    return dic

