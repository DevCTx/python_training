import re

def count_dates_into_string(string):
    '''
    Counts the number of dates into the string

    Accepted formats : 'YYYY-MM-DD' , 'YYYY/MM/DD' , 'YYYY.MM.DD' only but not a mixed of them like 'YYYY.MM/DD'
    No verification on real dates needed : 2034-14-32 is ok, only accepted date formats must be counted

    >>> count_dates_into_string('2021-06-23')
    1
    >>> count_dates_into_string('mWv pKO+')
    0
    >>> count_dates_into_string('1999-033-1')
    0
    >>> count_dates_into_string("2021/05/21lo14-~D%~2000.05.27F+0")
    2
    >>> count_dates_into_string("2021.05/21 2021/05/22 2021/05.23 2021.05.24")
    2
    >>> count_dates_into_string("2O23/O4/O4") # 0 replaced by the letter O
    0
    '''
    pattern = r"(?#YYYY-MM-DD)\d{4}-\d{2}-\d{2}|(?#YYYY/MM/DD)\d{4}/\d{2}/\d{2}|(?#YYYY.MM.DD)\d{4}\.\d{2}\.\d{2}"
    return len(re.findall( pattern, string))
