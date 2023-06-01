'''
    Identifies different kind of int literals
'''
strings = (
    1257823489853,              # is int given as long
    0xABCDEF,                   # is int given as hexa
    0B110101,                   # is int given as binary
    #4,321,678,                 # formats 3 differents numbers
    1_234_567,                  # is another way to write 1234567
    0,                          # is int
    '123',                      # is string
    #0L9223372036854775807,     # long does not more exist since Python 3
    1.234,                      # is float
    #0x1A3C5D7G,                # G is not an hexa character
)

for s in strings:
    try :
        assert type(s) is int
    except :
        print(f"{s} is type {type(s)} ")
