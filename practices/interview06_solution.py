
def unested(nested):
    """
    Unested the current nested lists and return a list with each elem of the nested lists

    :param nested: list of lists to unest
    :return: the list of each element of the nested list

    >>> unested([[['META', 'TSLA'], 'MSFT', 'AMZN'],'MSFT', ['AAPL', 'TSLA', 'NVDA']])
    ['AAPL', 'AMZN', 'META', 'MSFT', 'NVDA', 'TSLA']
    """
    ret = []
    for part in nested:
        if type(part) == list :
            ret.extend( unested(part) )
        else:
            ret.extend( [part] )
    return sorted(set(ret))

