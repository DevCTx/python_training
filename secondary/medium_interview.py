import builtins


def keypad_string(keys):
    '''
    Given a string consisting of 0-9,
    find the string that is created using
    a standard phone keypad
    | 1        | 2 (abc) | 3 (def)  |
    | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
    | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
    |     *    | 0 ( )   |     #    |
    You can ignore 1, and 0 corresponds to space
    >>> keypad_string("12345")
    'adgj'
    >>> keypad_string("4433555555666")
    'hello'
    >>> keypad_string("2022")
    'a b'
    >>> keypad_string("")
    ''
    >>> keypad_string("111")
    ''
    >>> keypad_string("11112222000333311144440000")
    'ca   fdig    '
    >>> keypad_string("#9277774414446648666166")
    '#washington'
    >>> keypad_string("*#06#")
    '*# m#'
    '''
    k_dict = {
        '1':"",
        '2':"abc",
        '3':"def",
        '4':"ghi",
        '5':"jkl",
        '6':"mno",
        '7':"pqrs",
        '8':"tuv",
        '9':"wxyz",
        '0':" ",
        '*':"*",
        '#':"#",
    }
    k_string = ''
    if keys != None:
        i = -1
        current_k = ''
        for key in keys:
            i = i+1 if key == current_k and i < len(k_dict[key])-1 else 0
            if i > 0:
                k_string = k_string[:-1]
            if len(k_dict[key]) > 0 :
                k_string += k_dict[key][i]
            current_k = key
    return k_string
