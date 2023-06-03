'''
    Lists the principal patterns for REGEX
'''
import re

# 2 GOOD WEBSITES :  https://pythex.org/ and https://regex101.com/

question = "L0v_ly world! Wonderful world!"
print(question)
print()

print(re.search("world", question))     # <re.Match object; span=(7, 12), match='world'>
print(question[7:12])                   # span shows the index where the pattern is found   # world
match = re.search("world", question)    # search return a Match object but it can be converted into a bool so
if bool(match):                         # it can be tested
    print(match.span())                 # and the span can be displayed     # (7, 12)
print()

print(match.start())                    # start shows the first index of the first occurrence   # 7
print(match.end())                      # end shows the last index of the first occurrence      # 12
print(question[match.start():match.end()])  # shows the first occurrence                        # world
print(match.string)                     # displays the string to be tested      # L0v_ly world! Wonderful world!
print(match.re)                         # shows what is compiled to be searched     # re.compile('world')
print()

print(re.match("world",question))       # Equivalent to a search with a '^' at the begining     # None
print(re.search("^world",question))     # Searches if the question starts with 'world'          # None
print()

# Shortcuts
# '\s' = ' ' : space
# '\d' = '[0-9]' : digit
# '\w' = '[a-zA-Z0-9_]' : lower/upper letter or digit or underscore
# but may need to be used as 'raw' string not to be confused with another escape character
# that's why the string is entered as a 'r-string' with a 'r' before the ""
#
# Search for 5 word-characters
print(re.match("[a-zA-Z0-9_]{6}",question)) # <re.Match object; span=(0, 5), match='L0v_ly'>
print(re.match(r"\w{6}",question))           # <re.Match object; span=(0, 5), match='L0v_ly'>
print()

print("\nA BIT MORE COMPLICATED")
# Search for a word-characters duplicated 0 to multiple times followed by a space duplicated 0 to multiple times
# in a group duplicated 0 to multiple times (meaning looking for words ...)
# and followed by a '!' character in a group duplicated 0 to multiple times (meaning an exclamation sentences ...)
question = "Lovely world! Wonderful world!"
print(question)
print(re.match(r"((\w*\s*)*!)*",question))       # Returns the match with the two sentences
print(re.fullmatch(r"((\w*\s*)*!)*",question))   # Returns also the match with the whole string
print()
question2 = "Lovely world! Wonderful world"     # WITHOUT EXCLAMATION POINT AT THE END
print(question2)
print(re.match(r"((\w*\s*)*!)*",question2))      # Returns the match with the first sentence
# start = time.time()
# print(re.fullmatch("((\w*\s*)*!)*",question2))  # Returns nothing because does not match with the whole string
# print( f"timing : {time.time() - start:.3f} seconds")   # takes a lot of time !!! Suprising for a so short sentence

print("\nGOING FURTHER")
# the character '^' specifies the beginning of the string
# but in a list, it specifies the inverse of characters in this list
question = "Lovely world! Wonderful world! aeiou"
print(question)
# Search for vowels followed by not a vowel but without including the i on the second part
print(re.findall("[aeiou][^aeou]",question))   # returns a list     # ['ov', 'el', 'or', 'on', 'er', 'ul', 'or', 'ei']
question = "Lovely world! Wonderful world! aeiou"
# Search for vowels followed by not a vowel
print(re.findall("[aeiou][^aeiou]",question))   # returns a list    # ['ov', 'el', 'or', 'on', 'er', 'ul', 'or']
print(re.finditer("[aeiou][^aeiou]",question))  # returns an iterator on this list      # <callable_iterator object>
for itr in re.finditer("[aeiou][^aeiou]",question):
    print(question[itr.start():itr.end()], itr.span(), sep='', end=', ')    # ov(1, 3), el(3, 5), or(8, 10), ...
print("\n")
#
print("\nWARNING !!!")                                                      # WARNING !!!
text = "Lovely world! Wonderful world!"
pattern = r"([aeiou][^aeiou])"
print(f"\n1. looking for \"{pattern}\" into \"{text}\" with finditer")
print([ match.group(0) for match in re.finditer(pattern, text) ] )          # ['ov', 'el', 'or', 'on', 'er', 'ul', 'or']
print(f"\n1. looking for \"{pattern}\" into \"{text}\" with findall")
print( re.findall(pattern, text) )                                          # ['ov', 'el', 'or', 'on', 'er', 'ul', 'or']
print(f"\n1. looking for \"{pattern}\" into \"{text}\" with search")
match = re.search(pattern, text)                                            # ('ov',)
print( match.groups() )
# Careful, findall won't always return the same occurrence that finditer
text = "aaaabbbaaaaaaaaabbbbbbb"
pattern = r"(\w)\1*"                                                        # to find all groups of identical letter
print(f"\n2. looking for \"{pattern}\" into \"{text}\" with finditer")
print([ match.group(0) for match in re.finditer(pattern, text) ] )          # ['aaaa', 'bbb', 'aaaaaaaaa', 'bbbbbbb']
print(f"\n2. looking for \"{pattern}\" into \"{text}\" with findall")
print( re.findall(pattern, text) )                                          # ['a', 'b', 'a', 'b']
print(f"\n2. looking for \"{pattern}\" into \"{text}\" with search")
match = re.search(pattern, text)                                            # ('a',)
print( match.groups() )
print()

print("\nGROUPS AND CONTENTS")
content = "I count like this: one, two, three"
match = re.search(r"(\w+), (\w+), (\w+)", content)
print('\n',match)           # <re.Match object; span=(19, 34), match='one, two, three'>
print(match.groups())       # ('one', 'two', 'three')
print(match.group(1))       # displays the first group              # one
print(match.group(2))       # displays the second group (idem)      # two
print(match.group(0))       # displays ALL GROUPS !!!               # one, two, three
print(match[1])             # also displays the first group         # one
print(match[0])             # also displays ALL GROUPS !!!          # one, two, three

match = re.search(r"(?P<first>\w+), (?P<second>\w+), (?P<third>\w+)", content)
print('\n',match)           # <re.Match object; span=(19, 34), match='one, two, three'>
print(match.groups())       # ('one', 'two', 'three')
print(match.group(1))       # displays the first group (idem)       # one
print(match.group(0))       # displays ALL GROUPS !!! (idem)        # one, two, three
print(match[1])             # also displays the first group (idem)  # one
print(match[0])             # also displays ALL GROUPS !!! (idem)   # one, two, three
# But This also defines a dictionary with the name of indicated groups
print(match.groupdict())    # {'first': 'one', 'second': 'two', 'third': 'three'}
print(match['first'])       # displays the 'first' group (idem)     # one
print(match['second'])      # displays the 'second' group (idem)    # two

match = re.search(r"(?P<first>\w+), (?:\w+), (?P<third>\w+)", content)
print('\n',match)           # <re.Match object; span=(19, 34), match='one, two, three'>     # Match Idem
print(match.groups())       # ('one', 'three')                          # But does not registered the group with '?:'
print(match.group(1))       # displays the first registered group       # one
print(match.group(2))       # displays the second registered group      # three
print(match.group(0))       # displays ALL groups (only two)            # one, three
print(match[2])             # also displays the second registered group # three
print(match[0])             # also displays ALL groups (only two)       # one, three
# But This also defines a dictionary with the name of indicated groups
print(match.groupdict())
print(match['first'])       # displays the 'first' group (idem)         # one
print(match['third'])       # displays the 'third' group (idem)         # three
print()


print("\nSUBSTITUTIONS AND MODIFICATIONS")
content = "My favorite numbers are 13 and 42"
print( re.sub(r"\d+", "#", content) )                   # My favorite numbers are # and #
print( re.sub(r"\d+", "#", content, count=1) )          # My favorite numbers are # and 42
#
# The following line will use the last completed match (one, who, three) and not the current
print( re.sub(r"\d+", match.group(0)[::-1], content) )  # My favorite numbers are eerht ,owt ,eno ...
# But a callback function can be entered to do it
def reverse(match):
    return match.group(0)[::-1]
print( re.sub(r"\d+", reverse, content) )               # My favorite numbers are 31 and 24
#
CONTENT = "My favorite numbers are 13 and 42"
PATTERN = r"(\d+)(.*?)(\d+)"                # identifies 2 groups of digits with any kind of characters between them
REVERSE = r"\3 \2 \1"
print( re.sub(PATTERN, REVERSE, CONTENT))               # My favorite numbers are 42 and 13
#
print( re.sub(r"(\d+)", r"\g<1>0", "Is this a 2 ?"))    # Add 0 to the first digit found      # Is this a 20 ?


print("\nSPLITTING")
print( "one,two,three".split(',') )             # ['one', 'two', 'three']
print( re.split( r"(\w+)", "one,two,three") )   # ['', 'one', ',', 'two', ',', 'three', '']
print( re.findall( r"(\w+)", "one,two,three") ) # ['one', 'two', 'three']


print("\nESCAPING")
print( re.findall( "2^4", "Even more than 2^2 is 2^4") )    # []
print( re.findall( "2\^4", "Even more than 2^2 is 2^4") )   # ['2^4']
regex = re.escape("2^4")                                    # can be useful if the argument come from another source
print( regex, re.findall( re.escape("2^4"), "Even more than 2^2 is 2^4") )
print()


print("\nCOMPILE REGEX")                        # Registered regex to facilitate the reuse later
content = "My favorite numbers are 13 and 42"
print(content)
print( re.search("(\d+)", content))             # <re.Match object; span=(24, 26), match='13'>
digit_re = re.compile("(\d+)")                  # Memorise a regex and return a re.Pattern object
print( digit_re.search(content) )               # <re.Match object; span=(24, 26), match='13'>
DIGIT_RE = "(\d+)"                              # Another way to do the same thing
print( re.search(DIGIT_RE, content))            # <re.Match object; span=(24, 26), match='13'>
print()


print("\nFLAGS")                                # FLAGS : Active or inactive options on any functions
#
# re.I OR re.IGNORECASE : Makes matching of alphabetic characters case-insensitive
print( re.search("a+", "AAA") )                          # None
print( re.search("a+", "AAA", re.IGNORECASE) )           # <re.Match object; span=(0, 3), match='AAA'>
print()
# re.M OR re.MULTILINE  : Causes ^ and $ anchors to match embedded newlines
print( re.search(r"(^N)", "Yes you did\nNo I didn't") )                   # None
print( re.search(r"(^N)", "Yes you did\nNo I didn't", re.MULTILINE) )     # <re.Match object; span=(12, 13), match='N'>
print( re.search(r"(\AN)", "Yes you did\nNo I didn't", re.MULTILINE) )    # None (Only look the first line)
print()
# re.S OR re.DOTALL     : Causes dot meta-character to match a newline
print( re.search("1.2", "First 1\n2 Next") )           # None (The dot does not consider '\n' as a character by default)
print( re.search("1.2", "First 1\n2 Next", re.DOTALL) )     # <re.Match object; span=(6, 9), match='1\n2'>
print()
# re.X OR re.VERBOSE    : Allows to insert WHITESPACES and COMMENTS within regex
PHONE_REGEX1 = r"(1\s)?\(\d\d\d\)\s\d\d\d-\d\d\d\d"
PHONE_REGEX2 = r"""
    (1\s)?      # optional leading 1
    \(\d\d\d\)  # area code
    \s          # space
    \d\d\d-     # prefix
    \d\d\d\d    # line number
"""
phone1 = re.compile(PHONE_REGEX1)                   # Can match with REGEX 1 ONLY (not easily readable)
print("PHONE REGEX 1 : ", PHONE_REGEX1)
print( phone1.match('1 (406) 967-1111') )           # <re.Match object; span=(0, 16), match='1 (406) 967-1111'>
print()
phone2 = re.compile(PHONE_REGEX2,re.VERBOSE)        # Can match with both and the code is more readable with comments
print("PHONE REGEX 2 with VERBOSE : ", PHONE_REGEX2)
print( phone2.match('1 (406) 967-1111') )           # <re.Match object; span=(0, 16), match='1 (406) 967-1111'>
print()
#
# Careful the reciprocal is true as well
print( re.search("bacon, eggs", "bacon, eggs, and potatoes") )  # <re.Match object; span=(0, 11), match='bacon, eggs'>
# The following will response None because it searches 'bacon,eggs' without space !
print( re.search("bacon, eggs", "bacon, eggs, and potatoes", re.VERBOSE) )      # None
# The following will response because it searches 'bacon,eggs' without space !
print( re.search("bacon, eggs", "bacon,eggs, and potatoes", re.VERBOSE) )  # <re.Match object; match='bacon,eggs'>
print()
#
#         re.DEBUG      : Debug information is printed to console       # AND GOOD LUCK !!!
# re.A OR re.ASCII      : Uses ASCII encoding for character classification
# re.U OR re.UNICODE    : Uses UNICODE encoding for character classification (default in Python 3)
# re.L OR re.LOCALE     : Uses current locale to determine encoding for character classification


print("\nCONDITIONALS, LOOK BACKWARD OR FORWARD, AND COMMENTS");
content = "12145 12245[A] 123456 1244[B] 125[C] 126 1274 12[D] [E]"
print(content)
# get [] with a character inside
print( re.findall(r"\[\w\]", content) )                  # ['[A]', '[B]', '[C]', '[D]', '[E]']

# get 4 digits followed by [] with a character inside
print( re.findall(r"\d{4}\[\w\]", content) )             # ['2245[A]', '1244[B]']

# get [] with a character inside only if preceded by 4 digits but without this digits
print( re.findall(r"(?<=\d{4})\[\w\]", content) )        # ['[A]', '[B]']

# get 4 digits provided they are followed by [] with a character inside
print( re.findall(r"\d{4}(?=\[\w\])", content) )         # ['2245', '1244']

# get 4 digits provided they are NOT followed by [] with a character inside
print( re.findall(r"\d{4}(?!\[\w\])", content) )         # ['1214', '1224', '1234', '1274']
#
# And finally, here is how to enter a comment into a regex directly
print( re.findall(r"(?#2 digits)\d{2}(?#space)\s(?#2 digits)\d{2}", content) )  # ['45 12', '56 12', '26 12', '74 12']
#