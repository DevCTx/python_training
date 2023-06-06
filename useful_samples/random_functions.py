from random import uniform, randrange, choice, choices

for i in range(100) :
    # Choose a random item from range(stop) or range(start, stop[, step]).
    print(randrange(2, 5)/10, end=', ')     # 0.4, 0.3, 0.3, 0.4, 0.2, 0.2, 0.4, 0.3, 0.4, 0.3, 0.3, 0.4, ...
print()

for i in range(100) :
    # Get a random number in the range [a, b) or [a, b] depending on rounding.
    print(uniform(.2, .5), end=',')         # 0.3500276907377062,0.36675711833929836,0.4380057870768961, ...
print()

for i in range(100) :
    # Choose a random element from a non-empty sequence
    print(choice([2,5]), end=', ')          # 5, 2, 5, 2, 5, 5, 2, 5, 5, 2, 5, 5, 2, 2, 2, 2, 2, ...
print()

for i in range(100) :
    # Return a k sized list of population elements chosen with replacement. A weight of probability can be added.
    print(choices([2,5]), end=', ')         # [2], [5], [5], [2], [5], [5], [5], [2], [2], [2], [5], ...
print()




