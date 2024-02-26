from datetime import datetime

current_date = datetime.now()

without_microsec  = current_date.replace(microsecond = 0)
print(without_microsec)