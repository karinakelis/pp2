from datetime import datetime


date1 = datetime(2024, 2, 20)
date2 = datetime(2024, 2, 24)


date_difference = date2 - date1

# Convert the difference to seconds
difference_in_seconds = date_difference.total_seconds()
print(difference_in_seconds)
