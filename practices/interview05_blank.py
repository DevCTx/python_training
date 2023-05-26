def mix_colors_numbers(color_number_list):
    """
    Return a dictionary of color-numbers pairs from the color_number_list

    :param color_list: list of tuples with a color associated to a number
    :return: a dictionary of color-numbers pairs sorted by colors and numbers

    >>> mix_colors_numbers([('yellow', 5), ('blue', 2), ('yellow', 3), ('blue', 7), ('red', 1)])
    {'blue': [2, 7], 'red': [1], 'yellow': [3, 5]}
    >>> mix_colors_numbers([('yellow', 1), ('blue', 2), ('yellow', 1), ('blue', 7), ('red', 1)])
    {'blue': [2, 7], 'red': [1], 'yellow': [1]}
    >>> mix_colors_numbers([('yellow', 1), ('blue', 2), ('blue', 7), ('red', 1), ('blue', 2)])
    {'blue': [2, 7], 'red': [1], 'yellow': [1]}
    """
