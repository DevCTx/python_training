import pytz
import datetime

vancouver_tz = pytz.timezone('America/Vancouver')
now = datetime.datetime.now(vancouver_tz)
print(f"{now}    is Now in America/Vancouver time zone", end='\n\n')

time_to_convert = input("Time to convert (2022-07-20T14:40:27Z) : ")
t = datetime.datetime.fromisoformat(time_to_convert).astimezone(vancouver_tz)
print(t, end='\n\n')
