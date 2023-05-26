'''
    Functions which shows how to add time to a datetime
'''
import json
import datetime



# This format is automatically applied into print
# def format_timedelta(duration):
#     days, remainder = divmod(duration.total_seconds(), 86400)
#     hours, remainder = divmod(remainder, 3600)
#     minutes, seconds = divmod(remainder, 60)
#     return "{} day(s) {:02}:{:02}:{:02}".format(int(days), int(hours), int(minutes), int(seconds))


def arrival_date(json_string):
    '''
    >>> arrival_date( json.dumps({'departure_date': '2021-12-30', 'travelling_time': 1}) )
    '2021-12-31'
    >>> arrival_date( json.dumps({'departure_date': '2021-12-30', 'travelling_time': 10}) )
    '2022-01-09'
    '''
    package_info = json.loads(json_string)
    departure_date = package_info["departure_date"]
    travelling_time = package_info["travelling_time"]

    # datetime.datetime object = YYYY-mm-dd HH:MM:SS
    departure_date_obj = datetime.datetime.strptime(departure_date, "%Y-%m-%d")

    # datetime.datetime object = YYYY-mm-dd HH:MM:SS
    # + datetime.timedelta object = 10 days , 0:00:00
    # = datetime.datetime object
    arrival_date_obj = departure_date_obj + datetime.timedelta(days=travelling_time)
    #print(datetime.timedelta(days=travelling_time))

    return arrival_date_obj.isoformat()[:10]


def arrival_date_2(json_string):
    '''
    >>> arrival_date_2( json.dumps({'departure_date': '2021-12-30', 'travelling_time': 1}) )
    '2021-12-31'
    >>> arrival_date_2( json.dumps({'departure_date': '2021-12-30', 'travelling_time': 10}) )
    '2022-01-09'
    '''
    package_info = json.loads(json_string)
    departure_date = package_info["departure_date"]
    travelling_time = package_info["travelling_time"]

    # datetime.datetime object = YYYY-mm-dd HH:MM:SS
    departure_date_obj = datetime.datetime.strptime(departure_date, "%Y-%m-%d")

    # departure_timestamp in seconds
    departure_timestamp = departure_date_obj.timestamp()

    # adds travelling_time in seconds
    arrival_timestamp = departure_timestamp + travelling_time * 24 * 60 * 60

    # returns a datetime.datetime object = YYYY-mm-dd HH:MM:SS
    arrival_date_obj = datetime.datetime.fromtimestamp(arrival_timestamp)

    return arrival_date_obj.isoformat()[:10]

