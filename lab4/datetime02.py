from datetime import datetime, timedelta

current_date = datetime.now()
yesterday = current_date - timedelta(days = 1)
tomorrow = current_date + timedelta(days = 1)
formating = current_date.strftime('%Y-%m-%d')
formating1 = yesterday.strftime('%Y-%m-%d')
formating2 = tomorrow.strftime('%Y-%m-%d')
print(formating1,formating,formating2)
