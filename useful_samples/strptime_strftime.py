import datetime
import time

dateA = datetime.datetime.now()
print(type(dateA), dateA)

# Convert a datetime to str
dateB = dateA.strftime('%m/%d/%Y')
print(type(dateB), dateB)

# Convert str to datetime
dateC = datetime.datetime.strptime(dateB,'%m/%d/%Y')
print(type(dateC), dateC)

# Convert str to struct_time
dateD = time.strptime(dateB,'%m/%d/%Y')
print(type(dateD), dateD)

# Convert struct_time to str
dateE = time.strftime('%m/%d/%Y')
print(type(dateE), dateE)
