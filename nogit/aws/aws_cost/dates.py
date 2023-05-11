from calendar import monthrange
from datetime import datetime


first_day = datetime(2023, 2, 1)
_ , day_count = monthrange(2023,2)
last_day = datetime(2023, 2, day_count, 23,59,59)
print(first_day, last_day)
