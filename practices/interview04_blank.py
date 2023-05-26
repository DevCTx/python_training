def generate_dict():
    """
    Must create a dictionary that returns "Anonymous" if the key is not existing

    >>> datastructure = generate_dict()
    >>> datastructure[3] = "John"
    >>> assert datastructure[3] == "John"
    >>> assert datastructure[9762] == "Anonymous"
    >>> assert datastructure.get(9762) == "Anonymous"
    """

