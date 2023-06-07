'''
    The 'walrus' operator allows you to assign a value to a variable as part of a larger expression.
    It combines the assignment (=) operator with the expression evaluation in a single step.
    The operator is represented by ':=' .
'''
l = [1,2,3]

## Here are 2 different ways to print the length of a list if it is greater than 2
n = len(l)
if n > 2:
    print(n)

if (n := len(l)) > 2:       # and this operator is called 'walrus' ('morse' in French) !!! :)
    print(n)

## These don't work
# if (len(n) as n) > 2:
#     print(n)
#
# if (n = len(l)) > 2:
#     print(n)

