import this # that's it
print()
print("A" < "a")    #True
print("0" < "A")    #True
print(" " < "A")    #True
print(" " < "0")    #True
# ' 0Aa'
print(1.0 == 1)     #True
print("1" == 1)     #False
print(True == "1")  #False
print(True == 1)    #True
print(True == 1.0)  #True
print("1" + "1")    #11
print(1 + 1)        #2
try:
    print(1 + "1")      #unsupported operand type(s) for +: 'int' and 'str'
except Exception as e:
    print(e)