SECONDS_IN_DAY = 60
MINUTES_IN_DAY = 60
HOURS_IN_DAY = 24


def gen_secs():
    return (x for x in range(SECONDS_IN_DAY))


def gen_minutes():
    return (x for x in range(MINUTES_IN_DAY))


def gen_hours():
    return (x for x in range(HOURS_IN_DAY))


def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                date_format = "%02d:%02d:%02d" % (hour, minute, second)
                yield date_format


def main():
    for gt in gen_time():
        print(gt)


if __name__ == '__main__':
    main()


