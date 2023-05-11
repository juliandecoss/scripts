from datetime import date, timedelta

def singularize_time(time:list):
    singular = 0
    for i in time:
        singular += int(i)
    if singular >= 10:
        singular = list(str(singular))
        singular = int(singular[0])+ int(singular[1])
    return singular
PERSONAL_TONIC = 8
for i in range(10):
    today = date.today() + timedelta(days=i)
    today = str(today).split("-")
    print("#####################")
    print(today)
    year = list(today[0])
    month1 = list(today[1])
    day = list(today[2])
    year = singularize_time(year)
    day = singularize_time(day)
    month1 = singularize_time(month1)
    print(f"year: {year} month: {month1} day:{day}")
    one_digit_date = singularize_time([year,day,month1])
    print(f"Tonic of the date: {one_digit_date} + {PERSONAL_TONIC}")
    day_tonic = one_digit_date + PERSONAL_TONIC
    singular_tonic = ""
    if day_tonic >= 10:
        singular_tonic =singularize_time(list(str(day_tonic)))
    print(f"Tonic: {day_tonic} or could be {singular_tonic} ")