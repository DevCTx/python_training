from random import uniform, randrange

for i in range(100) :
    print( randrange(2, 5)/10, end=', ')     # 0.4, 0.3, 0.3, 0.4, 0.2, 0.2, 0.4, 0.3, 0.4, 0.3, 0.3, 0.4, ...
print()

for i in range(100) :
    print( uniform(.2, .5), end=',')         # 0.3500276907377062,0.36675711833929836,0.4380057870768961, ...
print()



