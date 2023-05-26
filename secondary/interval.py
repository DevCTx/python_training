class Interval():
    def __init__(self, hours, minutes, seconds):
        """
        Initiate a timing interval with hours, minutes and seconds
        :param: heures, minutes, secondes
        :return: nothing
        >>> print(Interval(0,0,0))
        00:00:00
        >>> print(Interval(1,1,1))
        01:01:01
        >>> print(Interval(0,0,60))
        00:01:00
        >>> print(Interval(0,60,0))
        01:00:00
        >>> print(Interval(61,61,61))
        62:02:01
        """
        self.h = hours
        self.m = minutes
        self.s = seconds
        if self.s % 60 >= 0:
            self.m += self.s // 60
            self.s = self.s % 60
        if self.m % 60 >= 0:
            self.h += self.m // 60
            self.m = self.m % 60

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

    def __add__(self, other):
        """
        Add an interval to the current if other is Interval \n
        or add seconds to the current if other is int

        :param other: Interval or seconds to add to the current
        :returns: an Interval identical to current but added by other
        :raise TypeError: if other is not Interval or int

        :doctest:
        >>> print(Interval(0,0,0)+Interval(0,0,0))          # 00:00:00 + 00:00:00
        00:00:00
        >>> print(Interval(1,1,1)+Interval(1,1,1))          # 01:01:01 + 01:01:01
        02:02:02
        >>> print(Interval(0,0,60)+Interval(0,0,60))        # 00:01:00 + 00:01:00
        00:02:00
        >>> print(Interval(0,60,0)+Interval(0,60,0))        # 01:00:00 + 01:00:00
        02:00:00
        >>> print(Interval(61,61,61)+Interval(61,61,61))    # 62:02:01 + 62:02:01
        124:04:02
        >>> print(Interval(61,61,61)+(61,61,61))            # 62:02:01 + ?
        Traceback (most recent call last):
        ...
        TypeError: need a type Interval object to add
        >>> print(Interval(61,61,61)+20)                    # 62:02:01 + 00:00:20
        62:02:21
        >>> print(Interval(61,61,61)+80)                    # 62:02:01 + 00:01:20
        62:03:21
        """
        if isinstance(other, Interval):
            other_interval = Interval(other.h, other.m, other.s)
        elif isinstance(other, int):
            other_interval = Interval(0, 0, other)
        else:
            raise TypeError("need a type Interval object to add")

        added_interval = Interval(self.h, self.m, self.s)
        added_interval.s += other_interval.s
        if added_interval.s > 60:
            added_interval.m += 1
            added_interval.s -= 60
        added_interval.m += other_interval.m
        if added_interval.m > 60:
            added_interval.h += 1
            added_interval.m -= 60
        added_interval.h += other_interval.h
        return added_interval

    def __sub__(self, other):
        """
        Subtract an interval to the current
        :param: Interval to subtract to the current
        :return: an Interval identical to current but subtracted by the interval (can not be negative)
        >>> print(Interval(61,61,61)-Interval(0,0,0))   # 62:02:01 - 00:00:00
        62:02:01
        >>> print(Interval(61,61,61)-Interval(0,0,1))   # 62:02:01 - 00:00:01
        62:02:00
        >>> print(Interval(61,61,61)-Interval(0,0,61))  # 62:02:01 - 00:01:01
        62:01:00
        >>> print(Interval(61,61,61)-Interval(0,61,0))  # 62:02:01 - 01:01:00
        61:01:01
        >>> print(Interval(60,0,0)-Interval(0,0,1))     # 60:00:00 - 00:00:01
        59:59:59
        >>> print(Interval(60,0,0)-Interval(60,0,1))    # 60:00:00 - 60:00:01
        00:00:00
        >>> print(Interval(60,0,0)-Interval(60,1,0))    # 60:00:00 - 60:01:00
        00:00:00
        >>> print(Interval(60,0,0)-Interval(61,0,0))    # 60:00:00 - 61:00:00
        00:00:00
        >>> print(Interval(0,0,0)-Interval(0,1,1))      # 00:00:00 - 00:01:01
        00:00:00
        >>> print(Interval(61,61,61)-(61,61,61))        # 62:02:01 - ?
        Traceback (most recent call last):
        ...
        TypeError: need a type Interval object to subtract
        >>> print(Interval(61,61,61)-20)                # 62:02:01 - 00:00:20
        62:01:41
        >>> print(Interval(61,61,61)-80)                # 62:02:01 - 00:01:20
        62:00:41
        """
        if isinstance(other, Interval):
            other_interval = Interval(other.h, other.m, other.s)
        elif isinstance(other, int):
            other_interval = Interval(0, 0, other)
        else:
            raise TypeError("need a type Interval object to subtract")

        sub_interval = Interval(self.h, self.m, self.s)
        if sub_interval.s >= other_interval.s:
            sub_interval.s -= other_interval.s
        else:  # other=2 > sub=1
            sub_interval.m -= (other_interval.s // 60) + 1
            sub_interval.s = (sub_interval.s + 60) - (other_interval.s % 60)

        if sub_interval.m >= other_interval.m:
            sub_interval.m -= other_interval.m
        else:
            sub_interval.h -= (other_interval.m // 60) + 1
            sub_interval.m = (sub_interval.m + 60) - (other_interval.m % 60)

        sub_interval.h -= other_interval.h

        if sub_interval.h < 0:
            sub_interval.h = 0
            sub_interval.m = 0
            sub_interval.s = 0

        return sub_interval
