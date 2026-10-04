# Using the datetime module

from datetime import datetime, date, timedelta

current_datetime = datetime.now()

print("Current date and time:", current_datetime)
print("Current date:", date.today())

future_date = date.today() + timedelta(days=7)

print("Date after 7 days:", future_date)