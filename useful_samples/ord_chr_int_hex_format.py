'''
    Shows some uses of the ord, chr, int, hex and format functions

    # Conclusion :
    # It's better to use ord to convert string into integer
    # because format is not able to convert string to decimal or hexadecimal
    # chr is to get the character corresponding to a decimal position into ASCII table
    # ord is to get the decimal position corresponding to a character of the ASCII table
'''

# Iterate through ASCII codes 0 to 127
for i in range(128):
    # Convert the ASCII code to a character
    char = chr(i)
    # Get the hexadecimal representation of the ASCII code
    hex_value = hex(i)
    # Get the byte representation of the ASCII code
    byte_value = char.encode('utf-8')
    # Print the ASCII code, character, hexadecimal value, decimal value, and byte value
    print(f"Int: {i}\t\tHex: {hex_value}\t\tChar: {char}\t\tByte: {byte_value}")

print()
print( f"{hex(65)=}", ": convert an integer into a 'hexa value in string'" )    # hex(65)='0x41'
print( f"{int('0x41',base=16)=}", ": convert a 'hexa value in string' into an integer" )    # int('0x41',base=16)=65
print()
print( f"{format(65,'x')=}", ": convert an integer into a 'hexa value in string without 0x'" )  # format(65,'x')='41'
print( f"{format(0x41,'d')=}", ": convert an hexa value into an integer" )  # format(0x41,'d')='65'
print()
print( f"{'{0:#x}'.format(65)=}", ": convert an integer into a 'hexa value in string without 0x'" )  # '{0:#x}'.format(65)='0x41'
print( f"{'{0:#d}'.format(0x41)=}", ": convert an hexa value into an integer" ) # '{0:#d}'.format(0x41)='65'
print()
print( f"{chr(65)=}", ": convert an integer to a character" )   # chr(65)='A'
print( f"{ord('A')=}", ": convert a character to an integer" )  # ord('A')=65
print()
print( f"{format(65,'c')=}", ": convert an integer into a character" )  # format(65,'c')='A'
try :
    print( f"{format('A','d')=}", ": convert a character to an integer" )   # format('A','d') = ValueError
except ValueError as e:
    print("format('A','d') = ValueError :", e)
    print(f"{format(ord('A'),'d')=}", ": convert a character to an integer")    # format(ord('A'),'d')='65'
print()
print( f"{'{:c}'.format(65)=}", ": convert an integer into a character'" )  # '{:c}'.format(65)='A'
try :
    print( f"{'{:d}'.format('A')=}", ": convert a character to an integer" )    # '{:d}'.format('A') = ValueError
except ValueError as e:
    print("'{:d}'.format('A') = ValueError : ", e)  #
    print(f"{'{:d}'.format(ord('A'))=}", ": convert a character to an integer") # '{:d}'.format(ord('A'))='65'


# hex(65)='0x41' : convert an integer into a 'hexa value in string'
# int('0x41',base=16)=65 : convert a 'hexa value in string' into an integer
#
# format(65,'x')='41' : convert an integer into a 'hexa value in string without 0x'
# format(0x41,'d')='65' : convert an hexa value into an integer
#
# '{0:#x}'.format(65)='0x41' : convert an integer into a 'hexa value in string without 0x'
# '{0:#d}'.format(0x41)='65' : convert an hexa value into an integer
#
# chr(65)='A' : convert an integer to a character
# ord('A')=65 : convert a character to an integer
#
# format(65,'c')='A' : convert an integer into a character
# format('A','d') = ValueError : Unknown format code 'd' for object of type 'str'
# format(ord('A'),'d')='65' : convert a character to an integer
#
# '{:c}'.format(65)='A' : convert an integer into a character'
# '{:d}'.format('A') = ValueError :  Unknown format code 'd' for object of type 'str'
# '{:d}'.format(ord('A'))='65' : convert a character to an integer