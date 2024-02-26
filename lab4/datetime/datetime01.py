from datetime import datetime, timedelta

# Current date
current_date = datetime.now()

# Subtracting 5 days from the current date
new_date = current_date - timedelta(days=5)

# Formatting the date in YYYY-MM-DD format
formatted_new_date = new_date.strftime('%Y-%m-%d')

print(formatted_new_date)
