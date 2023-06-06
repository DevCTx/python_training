'''
    Shows the differences between 'strptime' and 'strftime' from 'datetime' and 'time' modules
'''
import datetime
import time

dateA = datetime.datetime.now()
print(type(dateA), dateA)

# Convert datetime to str  - Return a string representing the date, controlled by an explicit format string.
dateB = dateA.strftime('%m/%d/%Y')
print(type(dateB), dateB)

# Convert str to datetime  - Return a datetime corresponding to date_string, parsed according to format.
dateC = datetime.datetime.strptime(dateB,'%m/%d/%Y')
print(type(dateC), dateC)

# Convert str to struct_time  - Parse a string to a time tuple according to a format specification.
dateD = time.strptime(dateB,'%m/%d/%Y')
print(type(dateD), dateD)

# Convert struct_time to str  - Convert a time tuple to a string according to a format specification.
dateE = time.strftime('%m/%d/%Y')
print(type(dateE), dateE)
