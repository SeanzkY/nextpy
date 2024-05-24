SECONDS_IN_DAY = 60
MINUTES_IN_DAY = 60
HOURS_IN_DAY = 24
MONTHS_IN_YEAR = 12
START_YEAR = 2019
EVERY_TIME_TO_PRINT = 1000000


def gen_secs():
    """
    a generator of seconds
    :return number of seconds 0-59:
    """
    return (x for x in range(SECONDS_IN_DAY))


def gen_minutes():
    """
     a generator of minutes
    :return number of minutes 0-59:
    """
    return (x for x in range(MINUTES_IN_DAY))


def gen_hours():
    """
     a generator of hours
    :return number of hours 0-23:
    """
    return (x for x in range(HOURS_IN_DAY))


def gen_time():
    """
    a generator of times
    :return time in format hours:minutes:seconds
    """
    # loop through hours, to minutes, to seconds in order to return the time
    return ("%02d:%02d:%02d" % (hour, minute, second) for hour in gen_hours() for minute in gen_minutes() for second
            in gen_secs())


def gen_years(start=START_YEAR):
    """
    a generator of years
    :param start: the year in which we start generating (including)
    :type start: int
    :return: year
    """
    while True:
        yield start
        start += 1


def gen_months():
    """
    a generator of month
    :return: the month 1-12
    """
    return (x for x in range(1, MONTHS_IN_YEAR + 1))


def gen_days(month, leap_year=True):
    """
    a generator of days
    :param month: current month
    :type month: int
    :param leap_year: is it a leap year or not
    :type leap_year: bool
    :return: day 1-31
    """
    days_in_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    adder = 1 if (month == 2 and leap_year) else 0
    return (x for x in range(1, days_in_months[month] + adder + 1))


def gen_date():
    """
    generates full date
    :return: the date in format: day/month/year hours:minutes:seconds
    """
    for year in gen_years():
        for month in gen_months():
            for days in gen_days(month, year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
                for time in gen_time():
                    yield "%02d/%02d/%04d %s" % (days, month, year, time)


def main():
    counter = 0
    for x in gen_date():
        if counter % EVERY_TIME_TO_PRINT == 0 and counter != 0:
            print(x)
        counter += 1


if __name__ == '__main__':
    main()
