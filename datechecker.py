from datetime import datetime, timedelta

n = int(input("Enter the number of days: "))
c=n-1
# Calculate the date n days from today
today = datetime.today()
date_after_n_days = today + timedelta(days=c)
formatted_date = date_after_n_days.strftime("%d-%m-%Y")

print("The date after", n, "days will be:", formatted_date)
