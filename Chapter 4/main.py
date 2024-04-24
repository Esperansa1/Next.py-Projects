
def gen_secs():
    for sec in range(60):
        yield sec

def gen_minutes():
    for minute in range(60):
        yield minute

def gen_hours():
    for hour in range(24):
        yield hour

def gen_years(start=2019):
    while True:
        start += 1
        yield start - 1

def gen_months():
    for i in range(12):
        yield i + 1

def gen_days(month, leap_year=True):
    days_in_month = {
        1: 31,
        2: 28 if not leap_year else 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    for i in range(days_in_month[month]):
        yield i + 1

def gen_date():
    gen_year = gen_years()
    for year in gen_year:
        gen_month = gen_months()
        for month in gen_month:
            gen_day = gen_days(month)
            for day in gen_day:
                for gt in gen_time():
                    year_format = "%02d/%02d/%04d" % (day, month, year) 
                    yield year_format + " " + gt

def gen_time():
    hours = gen_hours()

    for hour in hours:
        minutes = gen_minutes()
        for minute in minutes:
            seconds = gen_secs()
            for second in seconds:
                yield "%02d:%02d:%02d" % (hour, minute, second)


date = gen_date()
for i in range(1000000):
    next(date)
print(next(date))